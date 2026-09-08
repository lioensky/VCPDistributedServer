# SPDX-FileCopyrightText: 2026 Blender Authors
#
# SPDX-License-Identifier: GPL-3.0-or-later

"""
End-to-end integration test for the chat client pipeline.

Verifies: user input -> chat client -> LLM -> MCP server -> Blender addon -> Blender.

The LLM may be from:
- ``USE_ANTHROPIC``: you must have an API key.
- ``USE_LLAMA_CXX``: you must setup a local modal and have LLAMA.C++ installed.

``BLENDER_BIN`` env var provides the Blender binary (test skips if unset).

Run with::

    BLENDER_BIN=/path/to/blender \
        python -m unittest tests.integration.test_blender_mcp_with_llm -v
"""

__all__ = ()

import glob
import http.server
import inspect
import json
from typing import Any, Self
import os
import shlex
import signal
import socket
import subprocess
import sys
import tempfile
import textwrap
import threading
import time
import unittest

from collections.abc import Callable

# Root of the repository.
_REPO_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# Ensure the repository root is on the path so `tests` resolves as a package.
if _REPO_DIR not in sys.path:
    sys.path.insert(0, _REPO_DIR)

# Fixed ports (avoid existing 9876-9878).
_PORT_BLENDER = 9879
_PORT_MOCK_LLM = 9880
_PORT_LLAMA_SERVER = 9881

# Scale all timeouts (e.g. `GLOBAL_TIMEOUT_SCALE=2` doubles every limit).
_TIMEOUT_SCALE = float(os.environ.get("GLOBAL_TIMEOUT_SCALE", "1"))

# Maximum time to wait for servers to start (seconds).
# For llama-server, loading large models can take a while.
_TIMEOUT_STARTUP = int(60 * _TIMEOUT_SCALE)

# Maximum time to wait for a local process to respond or exit (seconds).
_TIMEOUT_LOCAL_PROC = int(10 * _TIMEOUT_SCALE)

# Maximum time for a single HTTP health-check request (seconds).
_TIMEOUT_HTTP_REQUEST = 2.0 * _TIMEOUT_SCALE

# Maximum time to wait for the chat client to finish (seconds).
_TIMEOUT_CHAT_CLIENT = int(120 * _TIMEOUT_SCALE)


def _env_nonzero(var: str) -> bool:
    return os.environ.get(var, "").lstrip("0") != ""


if _env_nonzero("USE_LLAMA_CXX"):
    if _env_nonzero("USE_ANTHROPIC"):
        raise RuntimeError("USE_LLAMA_CXX and USE_ANTHROPIC cannot both be set")
    if not os.environ.get("LLAMA_SERVER_BIN"):
        raise RuntimeError("USE_LLAMA_CXX requires LLAMA_SERVER_BIN")
    if not os.environ.get("LLAMA_SERVER_ARGS"):
        raise RuntimeError("USE_LLAMA_CXX requires LLAMA_SERVER_ARGS")


def use_llm_check() -> bool:
    """True when a real LLM is available (``USE_ANTHROPIC=1`` or ``USE_LLAMA_CXX=1``)."""
    return _env_nonzero("USE_ANTHROPIC") or _env_nonzero("USE_LLAMA_CXX")


use_llm_text = "This test requires a real LLM (USE_ANTHROPIC or USE_LLAMA_CXX)"


def use_screenshot_check() -> bool:
    """True when screenshots are enabled (``USE_SCREENSHOT=1``)."""
    return _env_nonzero("USE_SCREENSHOT")


# ---------------------------------------------------------------------------
# Helpers (duplicated from test_blender_mcp_with_blender.py, same pattern).

def _blender_env(tmpdir: str) -> dict[str, str]:
    """
    Return an environment dict for Blender sub-processes.

    Sets ``HOME`` to *tmpdir* so that Blender reads and writes its
    configuration there instead of touching the real user directory.
    Disables ASAN leak checking so debug builds exit cleanly.
    """
    env = os.environ.copy()
    env["HOME"] = tmpdir
    env["ASAN_OPTIONS"] = ":".join(filter(None, [
        env.get("ASAN_OPTIONS", ""),
        "alloc_dealloc_mismatch=0",
        "leak_check_at_exit=0",
    ]))
    return env


def _run_blender(args: list[str], env: dict[str, str]) -> None:
    """
    Run a Blender command and raise on failure, including stderr in the message.
    """
    result = subprocess.run(args, capture_output=True, env=env)
    if result.returncode != 0:
        raise RuntimeError(
            "Command failed (exit {:d}):\n  {:s}\n{:s}".format(
                result.returncode,
                " ".join(args),
                result.stderr.decode("utf-8", errors="replace"),
            )
        )


def _drain_stdout(proc: "subprocess.Popen[bytes]") -> None:
    """
    Read and discard *proc* stdout in a daemon thread.

    This prevents the pipe buffer from filling up and blocking the child.
    """
    def _reader() -> None:
        assert proc.stdout is not None
        for _line in proc.stdout:
            pass

    threading.Thread(target=_reader, daemon=True).start()


def _start_headless_display(
    env: dict[str, str],
) -> tuple["subprocess.Popen[bytes]", str]:
    """
    Start a headless Wayland display server and add ``WAYLAND_DISPLAY`` to *env*.

    Returns ``(weston_process, ini_path)``. The caller must call
    ``_stop_headless_display`` when done.
    """
    from src.tests.utils.blender_headless import backend_wayland

    weston_socket = "wl-blmcp-{:d}".format(os.getpid())
    weston_bin = os.environ.get("WESTON_BIN", "weston")
    weston_env, weston_ini = backend_wayland._weston_env_and_ini()

    ini_fd, ini_path = tempfile.mkstemp(prefix="weston_", suffix=".ini")
    with os.fdopen(ini_fd, "w", encoding="utf-8") as fh:
        fh.write(weston_ini)

    cmd = [
        weston_bin,
        "--socket={:s}".format(weston_socket),
        "--backend=headless",
        "--width=800",
        "--height=600",
        "--config={:s}".format(ini_path),
    ]

    proc: subprocess.Popen[bytes] = subprocess.Popen(
        cmd,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        env=weston_env,
    )

    if not backend_wayland._wait_for_wayland_server(
        socket=weston_socket, timeout=_TIMEOUT_LOCAL_PROC,
    ):
        proc.send_signal(signal.SIGINT)
        proc.communicate()
        os.remove(ini_path)
        raise RuntimeError("Failed to start headless Wayland display server")

    env["WAYLAND_DISPLAY"] = weston_socket
    return proc, ini_path


def _stop_headless_display(proc: "subprocess.Popen[bytes]", ini_path: str) -> None:
    """
    Stop the headless Wayland display server started by ``_start_headless_display``.
    """
    proc.send_signal(signal.SIGINT)
    proc.communicate(timeout=_TIMEOUT_LOCAL_PROC)
    if os.path.exists(ini_path):
        os.remove(ini_path)


def _wait_for_port(port: int, timeout: int, proc: "subprocess.Popen[bytes]") -> None:
    """
    Block until a TCP connection to *port* on localhost succeeds.

    Checks *proc* on each iteration so an early crash is reported
    immediately instead of waiting for the full timeout.
    Raises ``RuntimeError`` if *timeout* seconds elapse or *proc* exits.
    """
    deadline = time.monotonic() + timeout
    while time.monotonic() < deadline:
        rc = proc.poll()
        if rc is not None:
            raise RuntimeError(
                "Blender exited with code {:d} before the server became reachable".format(rc)
            )
        try:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
                sock.settimeout(1)
                sock.connect(("localhost", port))
                return
        except (ConnectionRefusedError, OSError):
            time.sleep(0.2)
    raise RuntimeError(
        "Port {:d} not reachable within {:d}s".format(port, timeout)
    )


def _wait_for_health(
    port: int, timeout: int, proc: "subprocess.Popen[bytes]",
) -> None:
    """
    Block until ``http://localhost:{port}/health`` returns 200.

    Used for llama-server which opens the port before the model is loaded
    (returning 503 until ready).
    """
    import urllib.error
    import urllib.request

    url = "http://localhost:{:d}/health".format(port)
    deadline = time.monotonic() + timeout
    while time.monotonic() < deadline:
        rc = proc.poll()
        if rc is not None:
            raise RuntimeError(
                "llama-server exited with code {:d} before becoming healthy".format(rc)
            )
        try:
            with urllib.request.urlopen(url, timeout=_TIMEOUT_HTTP_REQUEST) as resp:
                if resp.status == 200:
                    return
        except urllib.error.HTTPError as ex:
            ex.close()
        except (urllib.error.URLError, OSError):
            pass
        time.sleep(1)
    raise RuntimeError(
        "llama-server health check not passing within {:d}s".format(timeout)
    )


# ---------------------------------------------------------------------------
# Blender TCP helpers.

def _blender_exec_for_internal_use_only(
    port: int, code: str, timeout: float = _TIMEOUT_LOCAL_PROC,
) -> dict[str, Any]:
    """
    Execute *code* in Blender via the addon's TCP socket server.

    Sends a null-byte-delimited JSON request and returns the parsed response.
    """
    request = json.dumps({
        "type": "execute",
        "code": code,
        "strict_json": True,
    }).encode("utf-8") + b"\0"
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        sock.settimeout(timeout)
        sock.connect(("localhost", port))
        sock.sendall(request)
        buf = bytearray()
        while b"\0" not in buf:
            chunk = sock.recv(4096)
            if not chunk:
                break
            buf.extend(chunk)
    result: dict[str, Any] = json.loads(bytes(buf.rstrip(b"\0")))
    return result


def _blender_exec_for_internal_use_only_ok_or_exception(
    port: int, code: str, timeout: float = _TIMEOUT_LOCAL_PROC,
) -> dict[str, Any]:
    """
    Like ``_blender_exec_for_internal_use_only`` but raises ``RuntimeError``
    when the response status is not ``ok``.
    """
    result = _blender_exec_for_internal_use_only(port, code, timeout)
    if result.get("status") != "ok":
        raise RuntimeError(
            "Blender exec failed: {:s}".format(
                str(result.get("message", result))
            )
        )
    return result


def _python_fn_body_as_string(fn: "Callable[[], None]") -> str:
    """
    Return the body of *fn* as a dedented string.

    Strips the ``def`` line and dedents the remaining lines.
    """
    source = inspect.getsource(fn)
    lines = source.splitlines()
    body_lines = lines[1:]
    code = textwrap.dedent("\n".join(body_lines))
    assert code.strip(), "Function body is empty"
    return code


def _blend_file_save(port: int, filepath: str) -> None:
    """
    Save the current Blender file to *filepath* for debugging tests.
    """
    _blender_exec_for_internal_use_only_ok_or_exception(
        port,
        "import bpy; bpy.ops.wm.save_as_mainfile(filepath={!r})".format(filepath),
    )


def _save_screenshot(port: int, filepath: str) -> None:
    """
    Save a screenshot of the Blender window to *filepath*.
    """
    def code() -> None:
        import bpy  # pylint: disable=import-error
        bpy.ops.screen.screenshot(filepath=filepath)  # noqa: F821

    _blender_exec_for_internal_use_only_ok_or_exception(
        port, "filepath = {!r}\n{:s}".format(
            filepath, _python_fn_body_as_string(code),
        ),
    )


def _blender_reset(port: int) -> None:
    """
    Reset Blender's scene via File -> New (``read_homefile``).

    Uses the addon's TCP server directly because routing this through
    the LLM/chat pipeline would be unreliable and slow. This is a
    simpler alternative to restarting Blender between tests.
    """
    _blender_exec_for_internal_use_only_ok_or_exception(
        port,
        "import bpy; bpy.ops.wm.read_homefile(use_empty=True)",
    )


# ---------------------------------------------------------------------------
# New helpers.

class _StatusReport:
    """
    Context manager that prints a setup step label on entry and a
    status tag on exit. Raises ``RuntimeError`` if the block exits
    without calling :meth:`status`.
    """

    def __init__(self, label: str) -> None:
        self._label = label
        self._status: str | None = None

    def status(self, text: str) -> None:
        self._status = text

    def __enter__(self) -> Self:
        print("  {:s} ...".format(self._label), end="", flush=True)
        return self

    def __exit__(self, *_args: object) -> None:
        if self._status is None:
            print(" [???]", flush=True)
            raise RuntimeError(
                "No status set for step: {:s}".format(self._label)
            )
        print(" [{:s}]".format(self._status), flush=True)


def _create_venv() -> str:
    """
    Create a virtual environment and install the project into it.

    The venv is cached at ``<repo>/.test_venv`` and reused on subsequent
    runs. Delete the directory manually to force a rebuild.

    Returns the path to the venv python binary.
    """
    venv_dir = os.path.join(_REPO_DIR, ".test_venv")
    venv_python = os.path.join(venv_dir, "bin", "python")

    if os.path.isfile(venv_python):
        return venv_python

    subprocess.run(
        [sys.executable, "-m", "venv", venv_dir],
        check=True,
    )
    result = subprocess.run(
        [venv_python, "-m", "pip", "install", os.path.join(_REPO_DIR, "mcp")],
        capture_output=True,
    )
    if result.returncode != 0:
        raise RuntimeError(
            "pip install failed (exit {:d}):\n{:s}".format(
                result.returncode,
                result.stderr.decode("utf-8", errors="replace"),
            )
        )
    return venv_python


def _start_llama_server(
    port: int,
    env: dict[str, str],
) -> "subprocess.Popen[bytes]":
    """
    Start ``llama-server`` from ``LLAMA_SERVER_BIN`` on *port*.

    Extra flags come from ``LLAMA_SERVER_ARGS`` (shell-quoted).
    The port is always provided by the test harness via ``--port``;
    do not include ``--port`` in ``LLAMA_SERVER_ARGS``.

    Returns the process handle. The caller must terminate it.
    """
    llama_bin = os.environ["LLAMA_SERVER_BIN"]
    extra_args = shlex.split(os.environ["LLAMA_SERVER_ARGS"])
    cmd = [llama_bin, "--port", str(port)] + extra_args
    print("\n    command: {:s}".format(shlex.join(cmd)), flush=True)

    verbose = _env_nonzero("LLAMA_SERVER_VERBOSE")
    if verbose:
        proc: subprocess.Popen[bytes] = subprocess.Popen(cmd, env=env)
    else:
        proc = subprocess.Popen(
            cmd,
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
            env=env,
        )
        _drain_stdout(proc)
    return proc


def _stop_llama_server(proc: "subprocess.Popen[bytes]") -> None:
    """Terminate a llama-server process."""
    proc.terminate()
    proc.wait(timeout=_TIMEOUT_LOCAL_PROC)
    if proc.stdout is not None:
        proc.stdout.close()


def _start_mock_llm(port: int) -> http.server.HTTPServer:
    """
    Start a mock OpenAI-compatible HTTP server on a daemon thread.

    Returns the server (call ``shutdown()`` to stop).
    """

    class _Handler(http.server.BaseHTTPRequestHandler):
        _counter = 0
        _lock = threading.Lock()

        def do_POST(self) -> None:
            content_length = int(self.headers.get("Content-Length", 0))
            _body = self.rfile.read(content_length)

            with _Handler._lock:
                request_num = _Handler._counter
                _Handler._counter += 1

            if request_num == 0:
                # First request: tell the LLM to call get_object_detail_summary.
                response = {
                    "choices": [{
                        "message": {
                            "role": "assistant",
                            "content": None,
                            "tool_calls": [{
                                "id": "call_001",
                                "type": "function",
                                "function": {
                                    "name": "get_object_detail_summary",
                                    "arguments": json.dumps({"name": "Cube"}),
                                },
                            }],
                        },
                        "finish_reason": "tool_calls",
                    }],
                }
            else:
                # Second (and any subsequent) request: plain text reply.
                response = {
                    "choices": [{
                        "message": {
                            "role": "assistant",
                            "content": "The active object is Cube.",
                        },
                        "finish_reason": "stop",
                    }],
                }

            payload = json.dumps(response).encode()
            self.send_response(200)
            self.send_header("Content-Type", "application/json")
            self.send_header("Content-Length", str(len(payload)))
            self.end_headers()
            self.wfile.write(payload)

        def log_message(self, format: str, *args: object) -> None:
            # Suppress stderr noise.
            pass

    server = http.server.HTTPServer(("localhost", port), _Handler)
    thread = threading.Thread(target=server.serve_forever, daemon=True)
    thread.start()
    return server


# ---------------------------------------------------------------------------
# Test class.

@unittest.skipUnless(
    os.environ.get("BLENDER_BIN"),
    "BLENDER_BIN environment variable must be set",
)
class TestChatClient(unittest.TestCase):
    """
    End-to-end test: chat client -> mock LLM -> MCP server -> Blender.
    """

    _tmpdir: tempfile.TemporaryDirectory[str]
    _venv_python: str
    _blender_proc: subprocess.Popen[bytes]
    _mock_server: http.server.HTTPServer
    _llama_server_proc: subprocess.Popen[bytes] | None
    _blender_mcp_cmd: str
    _blender_bin: str
    _env: dict[str, str]

    @classmethod
    def setUpClass(cls) -> None:
        print()
        blender_bin = os.environ["BLENDER_BIN"]

        cls._tmpdir = tempfile.TemporaryDirectory()
        tmpdir = cls._tmpdir.name
        cls.addClassCleanup(cls._tmpdir.cleanup)

        env = _blender_env(tmpdir)

        # ----
        # Venv
        with _StatusReport("Creating venv and installing blender-mcp") as st:
            cls._venv_python = _create_venv()
            venv_bin_dir = os.path.dirname(cls._venv_python)
            st.status("OK")

        # -----------
        # Build addon
        with _StatusReport("Building addon") as st:
            addon_src = os.path.join(_REPO_DIR, "addon", "blender_mcp_addon")
            _run_blender(
                [
                    blender_bin, "--command", "extension", "build",
                    "--source-dir=" + addon_src,
                    "--output-dir=" + tmpdir,
                ],
                env=env,
            )
            zips = glob.glob(os.path.join(tmpdir, "mcp-*.zip"))
            if not zips:
                raise RuntimeError("Extension build did not produce a zip")
            st.status("OK")

        # -------------
        # Install addon
        with _StatusReport("Installing addon") as st:
            _run_blender(
                [
                    blender_bin, "--background", "--factory-startup", "--online-mode",
                    "--command", "extension", "install-file",
                    zips[0], "--repo", "user_default", "--enable",
                ],
                env=env,
            )
            st.status("OK")

        # -----------------------------------
        # Save preferences (interactive mode)
        with _StatusReport("Saving preferences (port {:d})".format(_PORT_BLENDER)) as st:
            _run_blender(
                [
                    blender_bin, "--background", "--online-mode",
                    "--python-expr",
                    (
                        "import bpy; "
                        "prefs = bpy.context.preferences.addons"
                        "['bl_ext.user_default.mcp'].preferences; "
                        "prefs.port = {:d}; "
                        "prefs.autostart_delay = 0.0; "
                        "bpy.ops.wm.save_userpref()"
                    ).format(_PORT_BLENDER),
                ],
                env=env,
            )
            st.status("OK")

        # ----------------
        # Headless display
        if not _env_nonzero("BLENDER_MCP_FOREGROUND"):
            with _StatusReport("Starting headless display") as st:
                weston_proc, weston_ini = _start_headless_display(env)
                cls.addClassCleanup(_stop_headless_display, weston_proc, weston_ini)
                st.status("OK")

        # ------------------------------------------
        # Start Blender (graphical, no --background)
        with _StatusReport("Starting Blender") as st:
            cls._blender_proc = subprocess.Popen(
                [blender_bin, "--online-mode", "--gpu-backend", "vulkan"],
                stdout=subprocess.PIPE,
                stderr=subprocess.STDOUT,
                env=env,
            )
            cls.addClassCleanup(cls._cleanup_blender)
            _drain_stdout(cls._blender_proc)
            _wait_for_port(_PORT_BLENDER, _TIMEOUT_STARTUP, cls._blender_proc)
            st.status("OK")

        # --------
        # Mock LLM
        with _StatusReport("Starting mock LLM (port {:d})".format(_PORT_MOCK_LLM)) as st:
            cls._mock_server = _start_mock_llm(_PORT_MOCK_LLM)
            cls.addClassCleanup(cls._mock_server.shutdown)
            st.status("OK")

        # -----------------------
        # llama-server (optional)
        cls._llama_server_proc = None
        if _env_nonzero("USE_LLAMA_CXX"):
            with _StatusReport("Starting llama-server (port {:d})".format(_PORT_LLAMA_SERVER)) as st:
                cls._llama_server_proc = _start_llama_server(_PORT_LLAMA_SERVER, env)
                cls.addClassCleanup(_stop_llama_server, cls._llama_server_proc)
                st.status("OK")
            with _StatusReport("Waiting for llama-server to load model") as st:
                _wait_for_health(_PORT_LLAMA_SERVER, _TIMEOUT_STARTUP, cls._llama_server_proc)
                st.status("OK")

        # ----------------------------
        # Store paths for test methods
        cls._blender_mcp_cmd = os.path.join(venv_bin_dir, "blender-mcp")
        cls._blender_bin = blender_bin
        cls._env = env

    @classmethod
    def _cleanup_blender(cls) -> None:
        """
        Terminate Blender and close its stdout pipe.
        """
        cls._blender_proc.terminate()
        cls._blender_proc.wait(timeout=_TIMEOUT_LOCAL_PROC)
        if cls._blender_proc.stdout is not None:
            cls._blender_proc.stdout.close()

    def tearDown(self) -> None:
        if use_screenshot_check():
            filepath = os.path.join(
                os.getcwd(),
                "{:s}.{:s}.png".format(type(self).__name__, self._testMethodName),
            )
            _save_screenshot(_PORT_BLENDER, filepath)

    def test_chat_client_tool_call(self) -> None:
        """
        Verify tool call round-trip through mock LLM, MCP server and Blender.
        """
        stdout_text, _stderr_text = self._run_chat_client(
            "Describe the default cube",
            ["openai", "--api-url", "http://localhost:{:d}".format(_PORT_MOCK_LLM)],
        )
        self.assertIn("Cube", stdout_text, "Expected 'Cube' in output.\n" + self._last_output_info)
        self.assertIn(
            "get_object_detail_summary", stdout_text,
            "Expected tool call name in output.\n" + self._last_output_info,
        )

    @unittest.skipUnless(use_llm_check(), use_llm_text)
    def test_chat_client_llm_backed(self) -> None:
        """
        Query the default object name via a real LLM.
        """
        stdout_text, _stderr_text = self._run_chat_client(
            "What is the name of the default object in the scene?",
            self._llm_provider_args(),
        )
        self.assertIn("Cube", stdout_text, "Expected 'Cube' in output.\n" + self._last_output_info)
        # Verify a tool was actually called (not just answered from training data).
        self.assertTrue(
            "get_object_detail_summary" in stdout_text or "execute_blender_code" in stdout_text,
            "Expected a tool call in output.\n" + self._last_output_info,
        )

    @unittest.skipUnless(_env_nonzero("USE_LLAMA_CXX"), "USE_LLAMA_CXX must be set")
    def test_chat_client_for_primitive_llm(self) -> None:
        """
        Basic tool call via llama-server with an explicit tool name in the prompt.

        The prompt names the tool directly so this can run on weak models
        that struggle to select tools on their own. Good for testing if
        an LLM/MCP is properly hooked up.
        """
        stdout_text, _stderr_text = self._run_chat_client(
            "Use get_object_detail_summary to describe the object named 'Cube'.",
            ["openai", "--api-url", "http://localhost:{:d}".format(_PORT_LLAMA_SERVER)],
        )
        self.assertIn("Cube", stdout_text, "Expected 'Cube' in output.\n" + self._last_output_info)
        self.assertTrue(
            "get_object_detail_summary" in stdout_text
            or "get_objects_summary" in stdout_text
            or "execute_blender_code" in stdout_text,
            "Expected a tool call in output.\n" + self._last_output_info,
        )

    @unittest.skipUnless(use_llm_check(), use_llm_text)
    def test_chat_client_rotate_cube(self) -> None:
        """
        Rotate the default cube via LLM and verify the transform.
        """
        provider = self._llm_provider_args()

        # Step 1: ask the LLM to rotate the cube.
        stdout_text, _stderr_text = self._run_chat_client(
            "Rotate the default Cube by 45 degrees on the X axis.", provider,
        )
        self.assertIn(
            "execute_blender_code", stdout_text,
            "Expected a code execution tool call.\n" + self._last_output_info,
        )

        # Step 2: ask the LLM to report the rotation.
        stdout_text, _stderr_text = self._run_chat_client(
            "What is the X rotation of the Cube in degrees?", provider,
        )
        self.assertIn("45", stdout_text, "Expected '45' in output.\n" + self._last_output_info)

        # Reset so this test does not leak state.
        _blender_reset(_PORT_BLENDER)

    # --------------------------
    # Helpers for use-case tests

    def _setup_scene(self, fn: Callable[[], None]) -> None:
        """
        Reset Blender to factory defaults, then run *fn* to prepare the scene.

        The source of *fn* is extracted with :mod:`inspect` and sent to
        Blender via the addon's TCP server. *fn* is never called locally.
        """
        _blender_reset(_PORT_BLENDER)
        _blender_exec_for_internal_use_only_ok_or_exception(
            _PORT_BLENDER, _python_fn_body_as_string(fn),
        )

    def _run_in_blender(self, fn: Callable[[], object]) -> object:
        """
        Run *fn* in Blender via the addon's TCP server and return its result.

        The source of *fn* is sent as a function definition followed by
        ``result = {"value": fn()}``. *fn* is never called locally.
        """
        source = textwrap.dedent(inspect.getsource(fn))
        code = "{:s}\nresult = {{\"value\": {:s}()}}\n".format(source, fn.__name__)
        response = _blender_exec_for_internal_use_only_ok_or_exception(_PORT_BLENDER, code)
        return response.get("result", {}).get("value")

    def _run_chat_client(
        self, prompt: str, provider_args: list[str], *, timeout: int = _TIMEOUT_CHAT_CLIENT,
    ) -> tuple[str, str]:
        """
        Run the chat client with *prompt* and return ``(stdout, stderr)`` text.

        *provider_args* are appended after the common flags (e.g.
        ``["openai", "--api-url", url]`` or ``["claude", "--model", m]``).

        Stores full stdout+stderr in ``self._last_output_info`` for use
        in assertion messages.
        """
        env = self._env.copy()
        env["BLENDER_MCP_PORT"] = str(_PORT_BLENDER)
        env["BLENDER_PATH"] = self._blender_bin
        api_key = os.environ.get("ANTHROPIC_API_KEY")
        if api_key:
            env["ANTHROPIC_API_KEY"] = api_key

        chat_client = os.path.join(_REPO_DIR, "chat_client", "chat_client.py")
        proc = subprocess.Popen(
            [
                self._venv_python, chat_client,
                "--server-command", self._blender_mcp_cmd,
                "--non-interactive",
                "--prompt", prompt,
            ] + provider_args,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            env=env,
        )

        stdout, stderr = proc.communicate(timeout=timeout)
        stdout_text = stdout.decode("utf-8", errors="replace")
        stderr_text = stderr.decode("utf-8", errors="replace")
        self._last_output_info = (
            "stdout:\n{:s}\nstderr:\n{:s}".format(stdout_text, stderr_text)
        )
        print("", flush=True)
        print("  prompt: {:s}".format(prompt), flush=True)
        print("  response: {:s}".format(stdout_text.strip()), flush=True)
        return stdout_text, stderr_text

    def _llm_provider_args(self) -> list[str]:
        """Return provider arguments for the real LLM (Claude or llama-server)."""
        if _env_nonzero("USE_LLAMA_CXX"):
            return ["openai", "--api-url", "http://localhost:{:d}".format(_PORT_LLAMA_SERVER)]
        model = os.environ.get("ANTHROPIC_MODEL", "claude-sonnet-4-20250514")
        return ["claude", "--model", model]

    def _run_prompt(self, prompt: str) -> str:
        """
        Send *prompt* to the LLM via the chat client and return stdout text.

        Stores full stdout+stderr in ``self._last_output_info`` for use
        in assertion messages.
        """
        stdout_text, _stderr_text = self._run_chat_client(
            prompt, self._llm_provider_args(),
        )
        return stdout_text

    # --------------
    # Use-case tests
    #
    # One test per bullet point in `use_cases.txt` (Use Cases).
    # Each is gated on use_llm_check().

    @unittest.skipUnless(use_llm_check(), use_llm_text)
    def test_usecase_datablock_rename_typos(self) -> None:
        """
        Three misspelled object names are corrected by the LLM.
        """
        def setup() -> None:
            """Three objects with misspelled names."""
            import bpy
            bpy.ops.mesh.primitive_cube_add()
            ob = bpy.context.object
            ob.name = ob.data.name = 'Cuube'
            bpy.ops.object.camera_add()
            ob = bpy.context.object
            ob.name = ob.data.name = 'Cmera'
            bpy.ops.object.light_add(type='POINT')
            ob = bpy.context.object
            ob.name = ob.data.name = 'Lihgt'

        self._setup_scene(setup)
        self._run_prompt(
            "There are three objects in the scene whose names contain "
            "spelling mistakes. Fix the spelling of all object names. "
            "Do it immediately."
        )
        result = _blender_exec_for_internal_use_only_ok_or_exception(
            _PORT_BLENDER,
            "import bpy; result = {'names': sorted(ob.name for ob in bpy.data.objects)}",
        )
        names = result.get("result", {}).get("names")
        self.assertEqual(
            names, ["Camera", "Cube", "Light"],
            "Expected corrected names.\n" + self._last_output_info,
        )

    @unittest.skipUnless(use_llm_check(), use_llm_text)
    def test_usecase_query_material_usage(self) -> None:
        """
        Query which objects use a given material.
        """
        def setup() -> None:
            """Create a 'Cube' and 'Sphere' both sharing a material 'Red'."""
            import bpy
            mat = bpy.data.materials.new('Red')
            bpy.ops.mesh.primitive_cube_add()
            bpy.context.object.name = 'Cube'
            bpy.context.object.data.materials.append(mat)
            bpy.ops.mesh.primitive_uv_sphere_add()
            bpy.context.object.name = 'Sphere'
            bpy.context.object.data.materials.append(mat)

        self._setup_scene(setup)
        self._run_prompt(
            "Select all objects that use the material named 'Red'. "
            "Do it immediately."
        )

        def validate() -> list[str]:
            import bpy
            return sorted(ob.name for ob in bpy.context.selected_objects)

        selected = self._run_in_blender(validate)
        self.assertEqual(
            selected, ["Cube", "Sphere"],
            "Expected only objects using the 'Red' material to be selected.\n"
            + self._last_output_info,
        )

    @unittest.skipUnless(use_llm_check(), use_llm_text)
    def test_usecase_scene_highest_polycount(self) -> None:
        """
        Select the object with the highest polygon count.
        """
        def setup() -> None:
            """Add a high-poly UV sphere ('HighPolySphere') and a default cube ('LowPolyCube')."""
            import bpy
            bpy.ops.mesh.primitive_uv_sphere_add(segments=64, ring_count=32)
            bpy.context.object.name = 'HighPolySphere'
            bpy.ops.mesh.primitive_cube_add()
            bpy.context.object.name = 'LowPolyCube'

        self._setup_scene(setup)
        self._run_prompt(
            "Select the object with the highest polycount in this file. "
            "Do it immediately."
        )

        def validate() -> list[str]:
            import bpy
            return sorted(ob.name for ob in bpy.context.selected_objects)

        selected = self._run_in_blender(validate)
        self.assertEqual(
            selected, ["HighPolySphere"],
            "Expected only the high-poly object to be selected.\n"
            + self._last_output_info,
        )

    @unittest.skipUnless(use_llm_check(), use_llm_text)
    def test_usecase_mesh_not_deformed_by_armature(self) -> None:
        """
        Fix a mesh that is not deformed by its armature.
        """
        def setup() -> None:
            """Create a mesh 'Body' and an armature 'Rig' but do NOT parent them or add an Armature modifier."""
            import bpy
            bpy.ops.mesh.primitive_cube_add()
            ob = bpy.context.object
            ob.name = 'Body'
            vg = ob.vertex_groups.new(name='Bone')
            vg.add(range(len(ob.data.vertices)), 1.0, 'REPLACE')
            bpy.ops.object.armature_add()
            bpy.context.object.name = 'Rig'

        self._setup_scene(setup)
        _stdout = self._run_prompt(
            "My mesh 'Body' is not being deformed by my armature 'Rig', "
            "how can I fix that?"
        )

        def validate() -> bool:
            import bpy
            from mathutils import Vector  # type: ignore[import-not-found]  # Blender-only module.
            dg = bpy.context.evaluated_depsgraph_get()
            body = bpy.data.objects['Body']
            rig = bpy.data.objects['Rig']
            rest_cos = [v.co.copy() for v in body.evaluated_get(dg).data.vertices]
            rig.pose.bones['Bone'].location = Vector((0, 0, 2))
            rig.update_tag()
            dg.update()
            posed_cos = [v.co.copy() for v in body.evaluated_get(dg).data.vertices]
            return any((a - b).length > 0.01 for a, b in zip(rest_cos, posed_cos))

        _blend_file_save(_PORT_BLENDER, "/tmp/my_test.blend")
        self.assertTrue(
            self._run_in_blender(validate),
            "Mesh 'Body' was not deformed by armature 'Rig' after posing.\n"
            + self._last_output_info,
        )

    @unittest.skipUnless(use_llm_check(), use_llm_text)
    def test_usecase_verify_checklist(self) -> None:
        """
        Select only objects that fail a quality checklist.
        """
        # Defect: non-manifold (face deleted).
        # Defect: no material assigned.
        # Defect: material uses an absolute image path.
        objects_bad = ["Barrel", "Lantern", "Wagon"]
        objects_good = ["Chimney", "Crate", "Fence"]

        def setup() -> None:
            """
            Six objects with neutral names, three with problems and three without.

            Problems:
            * ``Barrel`` -- non-manifold (face deleted).
            * ``Lantern`` -- no material assigned.
            * ``Wagon`` -- material uses an absolute image path.

            Clean:
            * ``Crate`` -- manifold, has material, no absolute paths.
            * ``Fence`` -- manifold, has material, no absolute paths.
            * ``Chimney`` -- manifold, has material, no absolute paths.
            """
            import bmesh  # type: ignore[import-not-found]  # Blender-only module.
            import bpy

            mat = bpy.data.materials.new('Default')

            # ---------------------
            # Objects with problems

            # Barrel: non-manifold (face deleted).
            bpy.ops.mesh.primitive_cube_add(location=(0, 0, 0))
            ob = bpy.context.object
            ob.name = 'Barrel'
            ob.data.materials.append(mat)
            bpy.ops.object.mode_set(mode='EDIT')
            bm = bmesh.from_edit_mesh(ob.data)
            bm.faces.ensure_lookup_table()
            bmesh.ops.delete(bm, geom=[bm.faces[0]], context='FACES')
            bmesh.update_edit_mesh(ob.data)
            bpy.ops.object.mode_set(mode='OBJECT')

            # Lantern: no material assigned.
            bpy.ops.mesh.primitive_cube_add(location=(3, 0, 0))
            ob = bpy.context.object
            ob.name = 'Lantern'
            ob.data.materials.clear()

            # Wagon: material uses an absolute image path.
            bpy.ops.mesh.primitive_cube_add(location=(6, 0, 0))
            ob = bpy.context.object
            ob.name = 'Wagon'
            abs_mat = bpy.data.materials.new('AbsPathMat')
            abs_mat.use_nodes = True
            tex = abs_mat.node_tree.nodes.new('ShaderNodeTexImage')
            img = bpy.data.images.new('WoodTex', 1, 1)
            img.filepath = '/home/user/textures/wood.png'
            tex.image = img
            ob.data.materials.append(abs_mat)

            # --------------------------
            # Clean objects (no defects)

            bpy.ops.mesh.primitive_cube_add(location=(0, 3, 0))
            ob = bpy.context.object
            ob.name = 'Crate'
            ob.data.materials.append(mat)

            bpy.ops.mesh.primitive_uv_sphere_add(location=(3, 3, 0))
            ob = bpy.context.object
            ob.name = 'Fence'
            ob.data.materials.append(mat)

            bpy.ops.mesh.primitive_cylinder_add(location=(6, 3, 0))
            ob = bpy.context.object
            ob.name = 'Chimney'
            ob.data.materials.append(mat)

        self._setup_scene(setup)
        _stdout = self._run_prompt(
            "Verify this checklist against every object in the scene:\n"
            "- Meshes must be manifold, all objects must have materials.\n"
            # The clarification about nodes is needed - perhaps it shouldn't be needed (ideally).
            "- No absolute file paths in image textures (via materials, nodes etc).\n"
            "\n"
            "Select only the objects that fail.\n"
            # Ideally this wouldn't be needed, if not added it tries to "plan" at times.
            "Do it immediately."
        )

        def validate() -> list[str]:
            import bpy
            return sorted(ob.name for ob in bpy.context.selected_objects)

        selected = self._run_in_blender(validate)
        self.assertEqual(
            selected, sorted(objects_bad),
            "Expected only objects with problems to be selected.\n"
            + self._last_output_info,
        )


if __name__ == "__main__":
    unittest.main()
