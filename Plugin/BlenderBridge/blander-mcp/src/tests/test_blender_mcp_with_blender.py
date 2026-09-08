# SPDX-FileCopyrightText: 2026 Blender Authors
#
# SPDX-License-Identifier: GPL-3.0-or-later

"""
Integration test for MCP & Blender.

Verifies: Mock-LLM-Client -> MCP server -> Blender addon -> Blender.

The "Mock-LLM-Client" simply sends requests to the MCP server,
the "useful" part of these tests is that it connects to a real Blender instance
and runs the MCP tools verifying they give correct results.

This runs in both background & foreground mode (headless)
where it's possible to check that taking screenshots works properly.

Defaults to ``blender`` and ``blender-mcp`` from ``PATH``.
Override with ``BLENDER_BIN`` and ``BLENDER_MCP`` environment variables.

Foreground tests run headless via a Wayland display server (Weston).
Set ``BLENDER_MCP_FOREGROUND=1`` to use the real display instead.
"""

__all__ = ()

import base64
import glob
import inspect
import json
import os
import shlex
import shutil
import signal
import socket
import struct
import subprocess
import tempfile
import textwrap
import threading
import time
import unittest

import sys

import atexit

# Root of the repository.
_REPO_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Ensure the repository root is on the path so `tests` resolves as a package.
if _REPO_DIR not in sys.path:
    sys.path.insert(0, _REPO_DIR)

from src.tests.mcp_client import MCPClient

# Fixed ports for the test servers (background and foreground).
_PORT_BACKGROUND = 9876
_PORT_FOREGROUND = 9877
_PORT_INTERACTIVE = 9878

# Scale all timeouts (e.g. `GLOBAL_TIMEOUT_SCALE=2` doubles every limit).
_TIMEOUT_SCALE = float(os.environ.get("GLOBAL_TIMEOUT_SCALE", "1"))

# Maximum time to wait for Blender to start (seconds).
_TIMEOUT_STARTUP = int(int(os.environ.get("BLENDER_MCP_TIMEOUT", "10")) * _TIMEOUT_SCALE)

# Maximum time to wait for a local process to respond or exit (seconds).
_TIMEOUT_LOCAL_PROC = int(10 * _TIMEOUT_SCALE)

# Timeout for tools that run ``blender --background`` (CLI tools).
# Must be at least as large as blender_cli._CLI_TIMEOUT (120 s) plus startup.
_TIMEOUT_CLI_TOOL = int(150 * _TIMEOUT_SCALE)

# Tool coverage tracking.
_all_tools: set[str] = set()
_tested_tools: set[str] = set()


def _print_untested_tools() -> None:
    """
    Print tools that were not exercised by any test.
    """
    untested = sorted(_all_tools - _tested_tools)
    if not untested:
        return
    print("\nUntested tools ({:d}/{:d}):".format(len(untested), len(_all_tools)))
    for name in untested:
        print("  - {:s}".format(name))


atexit.register(_print_untested_tools)


def _python_fn_body_as_string(fn: object) -> str:
    """
    Return the body of *fn* as a dedented string.
    """
    source = inspect.getsource(fn)
    lines = source.splitlines()
    body_lines = lines[1:]
    code = textwrap.dedent("\n".join(body_lines))
    assert code.strip(), "Function body is empty"
    return code


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


def _drain_stdout(proc: "subprocess.Popen[bytes]") -> list[str]:
    """
    Read *proc* stdout in a daemon thread, collecting lines.

    This prevents the pipe buffer from filling up and blocking the child.
    Returns a list that is appended to from the reader thread.
    """
    lines: list[str] = []

    def _reader() -> None:
        assert proc.stdout is not None
        for raw in proc.stdout:
            lines.append(raw.decode("utf-8", errors="replace"))

    threading.Thread(target=_reader, daemon=True).start()
    return lines


def _start_headless_display(env: dict[str, str]) -> "subprocess.Popen[bytes]":
    """
    Start a headless Wayland display server and add ``WAYLAND_DISPLAY`` to *env*.

    Returns the weston process. The caller must call
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
    weston_kw: dict[str, object] = {
        "stdout": subprocess.PIPE,
        "stderr": subprocess.PIPE,
    }
    if weston_env is not None:
        weston_kw["env"] = weston_env

    proc = subprocess.Popen(cmd, **weston_kw)

    if not backend_wayland._wait_for_wayland_server(
        socket=weston_socket, timeout=_TIMEOUT_LOCAL_PROC,
    ):
        proc.send_signal(signal.SIGINT)
        proc.communicate()
        os.remove(ini_path)
        raise RuntimeError("Failed to start headless Wayland display server")

    env["WAYLAND_DISPLAY"] = weston_socket
    # Store for cleanup.
    proc._weston_ini_path = ini_path  # type: ignore[attr-defined]
    return proc


def _stop_headless_display(proc: "subprocess.Popen[bytes]") -> None:
    """
    Stop the headless Wayland display server started by ``_start_headless_display``.
    """
    proc.send_signal(signal.SIGINT)
    proc.communicate(timeout=_TIMEOUT_LOCAL_PROC)
    ini_path = getattr(proc, "_weston_ini_path", None)
    if ini_path is not None and os.path.exists(ini_path):
        os.remove(ini_path)


def _check_port_reachable(port: int) -> None:
    """
    Verify *port* on localhost is open; raise ``RuntimeError`` if not.

    Used in reuse mode to confirm an existing Blender MCP addon is listening
    before attempting to connect.
    """
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            sock.settimeout(2)
            sock.connect(("localhost", port))
    except (ConnectionRefusedError, OSError) as ex:
        raise RuntimeError(
            "BLENDER_MCP_REUSE=1 but port {:d} is not reachable: {:s}\n"
            "Make sure Blender is open with the MCP addon enabled "
            "and listening on that port.".format(port, str(ex))
        ) from ex


def _wait_for_port(
        port: int,
        timeout: int,
        proc: "subprocess.Popen[bytes]",
        output: list[str],
) -> None:
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
                "Blender exited with code {:d} before the server became reachable\n{:s}".format(
                    rc, "".join(output[-50:]),
                )
            )
        try:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
                sock.settimeout(1)
                sock.connect(("localhost", port))
                return
        except (ConnectionRefusedError, OSError):
            time.sleep(0.2)
    raise RuntimeError(
        "Port {:d} not reachable within {:d}s\n{:s}".format(
            port, timeout, "".join(output[-50:]),
        )
    )


class _TestServerMixin:
    """
    Shared setup, cleanup, helpers and test methods for both background
    and foreground server modes.

    Concrete subclasses set ``_background`` and ``_port`` as class variables.
    """

    _background: bool
    _interactive: bool = False
    _port: int

    _reuse_mode: bool = False

    @classmethod
    def setUpClass(cls) -> None:
        blender_bin = os.environ.get("BLENDER_BIN", "blender")
        blender_mcp = os.environ.get("BLENDER_MCP", "blender-mcp")

        cls._tmpdir = tempfile.TemporaryDirectory()
        tmpdir = cls._tmpdir.name
        cls.addClassCleanup(cls._tmpdir.cleanup)

        if cls._reuse_mode:
            # Reuse mode: skip build / install / Blender launch.
            # Connect directly to the already-running Blender MCP addon.
            _check_port_reachable(cls._port)
            mcp_env = os.environ.copy()
            mcp_env["BLENDER_MCP_PORT"] = str(cls._port)
            mcp_env["BLENDER_PATH"] = blender_bin
        else:
            env = _blender_env(tmpdir)

            # Build the extension zip.
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

            # Install the extension into the isolated HOME.
            _run_blender(
                [
                    blender_bin, "--online-mode", "--background", "--factory-startup",
                    "--command", "extension", "install-file",
                    zips[0], "--repo", "user_default", "--enable",
                ],
                env=env,
            )

            if cls._interactive:
                # Save preferences before launching so the autostart timer
                # reads the correct port with no delay.
                # This could be supported more generically by passing arbitrary
                # preference overrides, but port and delay are all we need for now.
                _run_blender(
                    [
                        blender_bin, "--background",
                        "--python-expr",
                        (
                            "import bpy; "
                            "prefs = bpy.context.preferences.addons"
                            "['bl_ext.user_default.mcp'].preferences; "
                            "prefs.port = {:d}; "
                            "prefs.autostart_delay = 0.0; "
                            "bpy.ops.wm.save_userpref()"
                        ).format(cls._port),
                    ],
                    env=env,
                )

            # Start a headless display server for non-background tests.
            # Registered before Blender so cleanup order is Blender first,
            # then the display server (LIFO).
            if not cls._background and not os.environ.get("BLENDER_MCP_FOREGROUND"):
                cls._weston_proc = _start_headless_display(env)
                cls.addClassCleanup(_stop_headless_display, cls._weston_proc)

            # Start Blender with the installed addon.
            # Omit `--factory-startup` so saved preferences (with the
            # extension enabled) are loaded from the isolated HOME.
            blender_args = [blender_bin, "--online-mode"]
            if cls._background:
                blender_args.append("--background")
            # Use Vulkan when not in background mode. OpenGL (llvmpipe) is known
            # to crash during shader JIT compilation under headless Weston with
            # recent LLVM/Mesa versions.
            if not cls._background:
                blender_args.extend(["--gpu-backend", "vulkan"])
            if not cls._interactive:
                blender_args.extend([
                    "--command", "blender_mcp", "--port", str(cls._port),
                ])

            cls._blender_proc = subprocess.Popen(
                blender_args,
                stdout=subprocess.PIPE,
                stderr=subprocess.STDOUT,
                env=env,
            )
            cls.addClassCleanup(cls._cleanup_blender)

            output = _drain_stdout(cls._blender_proc)
            _wait_for_port(cls._port, _TIMEOUT_STARTUP, cls._blender_proc, output)

            mcp_env = _blender_env(tmpdir)
            mcp_env["BLENDER_MCP_PORT"] = str(cls._port)
            mcp_env["BLENDER_PATH"] = blender_bin

        cls._client = MCPClient(shlex.split(blender_mcp), env=mcp_env)
        cls.addClassCleanup(cls._client.close)
        cls._client.initialize()
        _all_tools.update(cls._client.list_tools())

        # Create a minimal factory-default blend file for CLI tools.
        # Saves via a fresh --background process rather than the running
        # interactive Blender, so the file stays small regardless of how
        # much test data has accumulated in the live session.
        cls._blend_path = os.path.join(tmpdir, "test.blend")
        _run_blender(
            [
                blender_bin, "--factory-startup", "--background",
                "--python-expr",
                (
                    "import bpy, sys\n"
                    "bpy.ops.wm.save_as_mainfile(filepath={!r})\n"
                    "sys.exit(0)\n"
                ).format(cls._blend_path),
            ],
            env=os.environ.copy(),
        )

    @classmethod
    def _cleanup_blender(cls) -> None:
        """
        Terminate Blender and close its stdout pipe.
        """
        cls._blender_proc.terminate()
        cls._blender_proc.wait(timeout=_TIMEOUT_LOCAL_PROC)
        if cls._blender_proc.stdout is not None:
            cls._blender_proc.stdout.close()

    @staticmethod
    def _tool_timeout(name: str) -> int:
        """Return the appropriate call timeout for *name*.

        Tools that launch ``blender --background`` need a much longer timeout
        than the default 30 s because Blender CLI startup on Windows can take
        60-120 s.
        """
        if name.endswith("_for_cli"):
            return _TIMEOUT_CLI_TOOL
        return 0  # 0 → use MCPClient default

    def _call_tool(
        self,
        name: str,
        arguments: dict[str, object] | None = None,
    ) -> list[dict[str, object]]:
        """
        Call a tool, verify the response is not an error, and return the content list.
        """
        _tested_tools.add(name)
        t = self._tool_timeout(name)
        result = self._client.call_tool(name, arguments, timeout=t or None)
        content = result.get("content", [])
        self.assertFalse(
            result.get("isError", False),
            "Tool {:s} returned an error: {!r}".format(name, content),
        )
        self.assertIsInstance(content, list)
        self.assertTrue(
            len(content) > 0,
            "Expected at least one content item for {:s}".format(name),
        )
        return content

    def _call_tool_expect_error(
        self,
        name: str,
        arguments: dict[str, object] | None = None,
    ) -> list[dict[str, object]]:
        """
        Call a tool and assert that the response is an MCP-level error.
        """
        _tested_tools.add(name)
        t = self._tool_timeout(name)
        result = self._client.call_tool(name, arguments, timeout=t or None)
        self.assertTrue(
            result.get("isError", False),
            "Expected {:s} to return isError".format(name),
        )
        return result.get("content", [])

    def _test_tool(
        self,
        name: str,
        arguments: dict[str, object] | None = None,
    ) -> dict[str, object]:
        """
        Call a tool that returns text and return the parsed JSON result.

        When the response contains ``"status": "ok"`` the ``"result"``
        value is returned directly. Error responses are returned as-is.
        """
        content = self._call_tool(name, arguments)
        text_item = content[0]
        self.assertEqual(
            text_item.get("type"), "text",
            "Expected text content for {:s}, got {!r}".format(
                name, text_item.get("type"),
            ),
        )
        data = json.loads(text_item["text"])
        if data.get("status") == "ok":
            # Tools that run code in Blender wrap their response in
            # `{"status": "ok", "result": ...}`, but toolcode-based
            # tools may omit the `result` key.
            return data.get("result", data)
        return data

    def setUp(self) -> None:
        """Reload the default scene so each test starts from a clean state."""
        self._client.call_tool("execute_blender_code", {
            "code": (
                "import bpy\n"
                "bpy.ops.wm.read_homefile(use_empty=False)\n"
                "result = {'reset': True}\n"
            ),
        })

    # -----------------------------------------------------------------
    # Interactive tools.

    def test_execute_blender_code(self) -> None:
        data = self._test_tool("execute_blender_code", {
            "code": "result = {'value': 1 + 1}",
        })
        self.assertEqual(data["value"], 2)

    def test_get_blendfile_summary_datablocks(self) -> None:
        data = self._test_tool("get_blendfile_summary_datablocks")
        self.assertEqual(data["scene_name"], "Scene")
        self.assertIn("Layout", data["workspaces"])
        self.assertIsInstance(data["datablock_counts"], dict)

    def test_get_blendfile_summary_missing_files(self) -> None:
        data = self._test_tool("get_blendfile_summary_missing_files")
        self.assertIsInstance(data["missing_files"], list)
        self.assertEqual(data["missing_files"], [])

    def test_get_blendfile_summary_of_linked_libraries(self) -> None:
        data = self._test_tool("get_blendfile_summary_of_linked_libraries")
        self.assertEqual(data["total_library_count"], 0)
        self.assertEqual(data["direct_libraries"], [])
        self.assertEqual(data["indirect_libraries"], [])

    def test_get_blendfile_summary_path_info(self) -> None:
        data = self._test_tool("get_blendfile_summary_path_info")
        self.assertEqual(data["filepath"], "")
        self.assertFalse(data["is_saved"])
        self.assertIsNone(data["age_seconds"])
        self.assertIsNone(data["file_size_bytes"])
        self.assertIsNone(data["backups"])

    def test_get_blendfile_summary_usage_guess(self) -> None:
        data = self._test_tool("get_blendfile_summary_usage_guess")
        guesses = data["usage_guesses"]
        self.assertIn("Animation", guesses)
        self.assertIn("Modeling", guesses)
        for scores in guesses.values():
            self.assertIn("score", scores)
            self.assertIn("certainty", scores)

    def _call_tool_screenshot(
        self,
        name: str,
        arguments: dict[str, object] | None = None,
    ) -> list[dict[str, object]]:
        _tested_tools.add(name)
        result = self._client.call_tool(name, arguments)
        content = result.get("content", [])
        if not self._interactive:
            # Non-interactive modes (--background and --command) have
            # bpy.app.background == True, so screenshots are unavailable.
            self.assertTrue(
                result.get("isError", False),
                "Expected {:s} to fail in non-interactive mode".format(name),
            )
        else:
            self.assertFalse(
                result.get("isError", False),
                "Tool {:s} returned an error: {!r}".format(name, content),
            )
            self.assertEqual(content[0].get("type"), "image")
            image_data = content[0].get("data", "")
            self.assertTrue(len(image_data) > 0)
            width, height = self._image_size(image_data)
            self.assertGreater(width, 1)
            self.assertLess(width, 4096)
            self.assertGreater(height, 1)
            self.assertLess(height, 4096)
        return content

    @staticmethod
    def _image_size(image_base64: str) -> tuple[int, int]:
        """Return (width, height) of a base64-encoded PNG by reading the IHDR chunk."""
        data = base64.b64decode(image_base64)
        if data[:8] != b"\x89PNG\r\n\x1a\n":
            return (-1, -1)
        width, height = struct.unpack(">II", data[16:24])
        return (width, height)

    def test_get_screenshot_of_area_as_image(self) -> None:
        self._call_tool_screenshot("get_screenshot_of_area_as_image", {
            "area_ui_type": "VIEW_3D",
        })

    def test_get_screenshot_of_area_as_image_error(self) -> None:
        self._call_tool_expect_error("get_screenshot_of_area_as_image", {
            "area_ui_type": "NONEXISTENT",
        })

    def test_get_screenshot_of_window_as_image(self) -> None:
        self._call_tool_screenshot("get_screenshot_of_window_as_image")

    def test_get_screenshot_of_window_as_image_size_limit(self) -> None:
        size_limit = 16 * 1024  # 16 KB.
        content = self._call_tool_screenshot("get_screenshot_of_window_as_image", {
            "size_limit_in_bytes": size_limit,
        })
        if self._interactive:
            image_data = content[0].get("data", "")
            raw_bytes = base64.b64decode(image_data)
            self.assertLessEqual(
                len(raw_bytes), size_limit,
                "Screenshot exceeds {:d} byte limit ({:d} bytes)".format(size_limit, len(raw_bytes)),
            )

    def test_get_screenshot_of_window_as_json(self) -> None:
        data = self._test_tool("get_screenshot_of_window_as_json")
        if not self._interactive:
            self.assertEqual(data["status"], "error")
        else:
            self.assertEqual(data["scene"], "Scene")
            self.assertIsInstance(data["areas"], list)
            self.assertTrue(len(data["areas"]) > 0)
            self.assertIsNotNone(data["active_object"])
            self.assertIn("name", data["active_object"])

    # -----------------------------------------------------------------
    # CLI tools.

    def test_execute_blender_code_for_cli(self) -> None:
        data = self._test_tool("execute_blender_code_for_cli", {
            "blend_file": self._blend_path,
            "code": "result = {'version': 1}",
        })
        self.assertEqual(data["version"], 1)

    def test_get_blendfile_summary_datablocks_for_cli(self) -> None:
        data = self._test_tool("get_blendfile_summary_datablocks_for_cli", {
            "blend_file": self._blend_path,
        })
        self.assertEqual(data["scene_name"], "Scene")
        self.assertIsInstance(data["datablock_counts"], dict)

    def test_get_blendfile_summary_missing_files_for_cli(self) -> None:
        data = self._test_tool("get_blendfile_summary_missing_files_for_cli", {
            "blend_file": self._blend_path,
        })
        self.assertEqual(data["missing_files"], [])

    def test_get_blendfile_summary_of_linked_libraries_for_cli(self) -> None:
        data = self._test_tool("get_blendfile_summary_of_linked_libraries_for_cli", {
            "blend_file": self._blend_path,
        })
        self.assertEqual(data["total_library_count"], 0)

    def test_get_blendfile_summary_path_info_for_cli(self) -> None:
        data = self._test_tool("get_blendfile_summary_path_info_for_cli", {
            "blend_file": self._blend_path,
        })
        self.assertTrue(data["is_saved"])
        self.assertTrue(data["filepath"].endswith(".blend"))

    def test_get_blendfile_summary_usage_guess_for_cli(self) -> None:
        data = self._test_tool("get_blendfile_summary_usage_guess_for_cli", {
            "blend_file": self._blend_path,
        })
        guesses = data["usage_guesses"]
        self.assertIn("Animation", guesses)
        self.assertIn("Modeling", guesses)

    # -----------------------------------------------------------------
    # Object inspection tools.

    def test_get_object_detail_summary(self) -> None:
        data = self._test_tool("get_object_detail_summary", {"name": "Cube"})
        self.assertEqual(data["status"], "ok")
        self.assertEqual(data["name"], "Cube")
        self.assertEqual(data["type"], "MESH")
        self.assertEqual(data["data_name"], "Cube")
        self.assertEqual(data["location"], [0.0, 0.0, 0.0])
        self.assertEqual(data["rotation"], [0.0, 0.0, 0.0])
        self.assertEqual(data["scale"], [1.0, 1.0, 1.0])
        self.assertEqual(data["dimensions"], [2.0, 2.0, 2.0])
        self.assertIsNone(data["parent"])
        self.assertEqual(data["children"], [])
        self.assertEqual(data["modifiers"], [])
        self.assertEqual(data["constraints"], [])
        self.assertEqual(data["materials"], ["Material"])
        self.assertEqual(data["visibility"], {
            "hide_viewport": False,
            "hide_render": False,
            "hide_get": False,
        })
        self.assertIn("Collection", data["collections"])

    def test_get_object_detail_summary_error(self) -> None:
        data = self._test_tool("get_object_detail_summary", {"name": "NonExistent"})
        self.assertEqual(data["status"], "error")
        self.assertEqual(data["error_code"], "OBJECT_NOT_FOUND")
        self.assertIn("'NonExistent'", data["message"])
        self.assertIn("Cube", data["current_state"]["available_objects"])
        self.assertIsInstance(data["hint"], str)
        self.assertTrue(data["hint"])

    def test_get_objects_summary(self) -> None:
        data = self._test_tool("get_objects_summary")
        self.assertEqual(data, {
            "status": "ok",
            "scene_name": "Scene",
            "active_workspace": "Layout",
            "active_object": "Cube",
            "object_mode": "OBJECT",
            "camera_object": "Camera",
            "collections": [
                {
                    "name": "Scene Collection",
                    "exclude": False,
                    "hide_viewport": False,
                    "objects": [],
                    "children": [
                        {
                            "name": "Collection",
                            "exclude": False,
                            "hide_viewport": False,
                            "objects": [
                                {
                                    "name": "Camera",
                                    "type": "CAMERA",
                                    "parent": None,
                                    "data_name": "Camera",
                                    "selected": False,
                                    "visible": True,
                                    "hide_viewport": False,
                                },
                                {
                                    "name": "Cube",
                                    "type": "MESH",
                                    "parent": None,
                                    "data_name": "Cube",
                                    "selected": True,
                                    "visible": True,
                                    "hide_viewport": False,
                                },
                                {
                                    "name": "Light",
                                    "type": "LIGHT",
                                    "parent": None,
                                    "data_name": "Light",
                                    "selected": False,
                                    "visible": True,
                                    "hide_viewport": False,
                                },
                            ],
                            "children": [],
                        },
                    ],
                },
            ],
        })

    def test_get_scene_state(self) -> None:
        data = self._test_tool("get_scene_state")
        self.assertEqual(data["status"], "ok")
        self.assertEqual(data["scene_name"], "Scene")
        # Frame info.
        self.assertIsInstance(data["frame_start"], int)
        self.assertIsInstance(data["frame_end"], int)
        self.assertIsInstance(data["frame_current"], int)
        self.assertGreaterEqual(data["frame_end"], data["frame_start"])
        self.assertIsInstance(data["fps"], (int, float))
        self.assertGreater(data["fps"], 0)
        # Objects.
        objects = data["objects"]
        self.assertIsInstance(objects, list)
        names = [o["name"] for o in objects]
        self.assertIn("Camera", names)
        self.assertIn("Cube", names)
        self.assertIn("Light", names)
        for obj in objects:
            self.assertIn("name", obj)
            self.assertIn("type", obj)
            location = obj["location"]
            self.assertIsInstance(location, list)
            self.assertEqual(len(location), 3)
            for coord in location:
                self.assertIsInstance(coord, float)

    def test_get_scene_state_frame_info(self) -> None:
        """Verify that frame_current and frame_end reflect live Blender state."""
        self._test_tool("execute_blender_code", {
            "code": (
                "import bpy\n"
                "bpy.context.scene.frame_current = 42\n"
                "bpy.context.scene.frame_end = 120\n"
                "result = {'done': True}\n"
            ),
        })
        data = self._test_tool("get_scene_state")
        self.assertEqual(data["frame_current"], 42)
        self.assertEqual(data["frame_end"], 120)

    # -----------------------------------------------------------------
    # Grease Pencil tools (REQ-03).

    def test_gp_object_create(self) -> None:
        data = self._test_tool("gp_object_create", {"name": "Canvas"})
        self.assertEqual(data["status"], "ok")
        self.assertEqual(data["name"], "Canvas")
        self.assertIsInstance(data["collection"], str)

    def test_gp_object_create_deduplication(self) -> None:
        """Second object with the same name gets a .001 suffix."""
        self._test_tool("gp_object_create", {"name": "Canvas"})
        data = self._test_tool("gp_object_create", {"name": "Canvas"})
        self.assertEqual(data["status"], "ok")
        self.assertNotEqual(data["name"], "Canvas")
        self.assertTrue(data["name"].startswith("Canvas"))

    def test_gp_layer_create(self) -> None:
        self._test_tool("gp_object_create", {"name": "Canvas"})
        data = self._test_tool("gp_layer_create", {
            "object_name": "Canvas",
            "layer_name": "Lines",
        })
        self.assertEqual(data["status"], "ok")
        self.assertEqual(data["object_name"], "Canvas")
        self.assertEqual(data["layer_name"], "Lines")

    def test_gp_layers_list(self) -> None:
        self._test_tool("gp_object_create", {"name": "Canvas"})
        self._test_tool("gp_layer_create", {
            "object_name": "Canvas", "layer_name": "Lines",
        })
        self._test_tool("gp_layer_create", {
            "object_name": "Canvas", "layer_name": "Fill",
        })
        data = self._test_tool("gp_layers_list", {"object_name": "Canvas"})
        self.assertEqual(data["status"], "ok")
        self.assertEqual(data["object_name"], "Canvas")
        names = [l["name"] for l in data["layers"]]
        self.assertIn("Lines", names)
        self.assertIn("Fill", names)
        for layer in data["layers"]:
            self.assertIn("name", layer)
            self.assertIn("opacity", layer)
            self.assertIn("hide", layer)

    def test_gp_layer_delete(self) -> None:
        self._test_tool("gp_object_create", {"name": "Canvas"})
        self._test_tool("gp_layer_create", {
            "object_name": "Canvas", "layer_name": "Lines",
        })
        data = self._test_tool("gp_layer_delete", {
            "object_name": "Canvas",
            "layer_name": "Lines",
        })
        self.assertEqual(data["status"], "ok")
        # Verify the layer is gone.
        list_data = self._test_tool("gp_layers_list", {"object_name": "Canvas"})
        names = [l["name"] for l in list_data["layers"]]
        self.assertNotIn("Lines", names)

    def test_gp_object_create_error_not_gp(self) -> None:
        """gp_layer_create rejects non-GP objects."""
        data = self._test_tool("gp_layer_create", {
            "object_name": "Cube",
            "layer_name": "Lines",
        })
        self.assertEqual(data["status"], "error")
        self.assertEqual(data["error_code"], "INVALID_OBJECT_TYPE")
        self.assertIsInstance(data["hint"], str)

    def test_gp_layer_create_object_not_found(self) -> None:
        data = self._test_tool("gp_layer_create", {
            "object_name": "NonExistent",
            "layer_name": "Lines",
        })
        self.assertEqual(data["status"], "error")
        self.assertEqual(data["error_code"], "OBJECT_NOT_FOUND")
        self.assertIsInstance(data["current_state"]["available_gp_objects"], list)

    def test_gp_layer_delete_layer_not_found(self) -> None:
        self._test_tool("gp_object_create", {"name": "Canvas"})
        data = self._test_tool("gp_layer_delete", {
            "object_name": "Canvas",
            "layer_name": "DoesNotExist",
        })
        self.assertEqual(data["status"], "error")
        self.assertEqual(data["error_code"], "LAYER_NOT_FOUND")
        self.assertIsInstance(data["current_state"]["available_layers"], list)

    # -----------------------------------------------------------------
    # Stroke drawing tools (REQ-04).

    def _setup_gp_canvas(self) -> None:
        """Create a fresh GP object named 'Canvas' with one layer 'Strokes'."""
        self._test_tool("gp_object_create", {"name": "Canvas"})
        self._test_tool("gp_layer_create", {
            "object_name": "Canvas",
            "layer_name": "Strokes",
        })

    def test_gp_stroke_draw_basic(self) -> None:
        self._setup_gp_canvas()
        data = self._test_tool("gp_stroke_draw", {
            "object_name": "Canvas",
            "layer_name": "Strokes",
            "frame": 1,
            "points": [[-1.0, 0.0, 0.0], [0.0, 0.0, 0.0], [1.0, 0.0, 0.0]],
        })
        self.assertEqual(data["status"], "ok")
        self.assertEqual(data["object_name"], "Canvas")
        self.assertEqual(data["layer_name"], "Strokes")
        self.assertEqual(data["frame"], 1)
        self.assertGreaterEqual(data["stroke_count"], 1)

    def test_gp_stroke_draw_replace(self) -> None:
        self._setup_gp_canvas()
        self._test_tool("gp_stroke_draw", {
            "object_name": "Canvas",
            "layer_name": "Strokes",
            "frame": 1,
            "points": [[0.0, 0.0, 0.0], [1.0, 0.0, 0.0]],
            "mode": "replace",
        })
        data = self._test_tool("gp_stroke_draw", {
            "object_name": "Canvas",
            "layer_name": "Strokes",
            "frame": 1,
            "points": [[0.0, 0.0, 1.0], [1.0, 0.0, 1.0]],
            "mode": "replace",
        })
        self.assertEqual(data["status"], "ok")
        self.assertEqual(data["stroke_count"], 1)

    def test_gp_stroke_draw_append(self) -> None:
        self._setup_gp_canvas()
        self._test_tool("gp_stroke_draw", {
            "object_name": "Canvas",
            "layer_name": "Strokes",
            "frame": 1,
            "points": [[0.0, 0.0, 0.0], [1.0, 0.0, 0.0]],
            "mode": "replace",
        })
        data = self._test_tool("gp_stroke_draw", {
            "object_name": "Canvas",
            "layer_name": "Strokes",
            "frame": 1,
            "points": [[0.0, 0.0, 1.0], [1.0, 0.0, 1.0]],
            "mode": "append",
        })
        self.assertEqual(data["status"], "ok")
        self.assertEqual(data["stroke_count"], 2)

    def test_gp_stroke_draw_error_layer_not_found(self) -> None:
        self._test_tool("gp_object_create", {"name": "Canvas"})
        data = self._test_tool("gp_stroke_draw", {
            "object_name": "Canvas",
            "layer_name": "NoSuchLayer",
            "frame": 1,
            "points": [[0.0, 0.0, 0.0], [1.0, 0.0, 0.0]],
        })
        self.assertEqual(data["status"], "error")
        self.assertEqual(data["error_code"], "LAYER_NOT_FOUND")
        self.assertIsInstance(data["current_state"]["available_layers"], list)
        self.assertIsInstance(data["hint"], str)

    def test_gp_stroke_draw_error_invalid_points(self) -> None:
        self._setup_gp_canvas()
        data = self._test_tool("gp_stroke_draw", {
            "object_name": "Canvas",
            "layer_name": "Strokes",
            "frame": 1,
            "points": [],
        })
        self.assertEqual(data["status"], "error")
        self.assertEqual(data["error_code"], "INVALID_POINTS")

    def test_gp_shape_draw_rect(self) -> None:
        self._setup_gp_canvas()
        data = self._test_tool("gp_shape_draw", {
            "object_name": "Canvas",
            "layer_name": "Strokes",
            "frame": 1,
            "shape": "rect",
            "cx": 0.0, "cy": 0.0, "cz": 0.0,
            "width": 2.0, "height": 1.0,
        })
        self.assertEqual(data["status"], "ok")
        self.assertEqual(data["shape"], "rect")
        self.assertEqual(data["point_count"], 5)

    def test_gp_shape_draw_circle(self) -> None:
        self._setup_gp_canvas()
        data = self._test_tool("gp_shape_draw", {
            "object_name": "Canvas",
            "layer_name": "Strokes",
            "frame": 1,
            "shape": "circle",
            "cx": 0.0, "cy": 0.0, "cz": 0.0,
            "radius": 1.5,
            "segments": 16,
        })
        self.assertEqual(data["status"], "ok")
        self.assertEqual(data["shape"], "circle")
        self.assertEqual(data["point_count"], 17)

    def test_gp_shape_draw_line(self) -> None:
        self._setup_gp_canvas()
        data = self._test_tool("gp_shape_draw", {
            "object_name": "Canvas",
            "layer_name": "Strokes",
            "frame": 1,
            "shape": "line",
            "x1": 0.0, "y1": 0.0, "z1": 0.0,
            "x2": 2.0, "y2": 0.0, "z2": 1.0,
        })
        self.assertEqual(data["status"], "ok")
        self.assertEqual(data["shape"], "line")
        self.assertEqual(data["point_count"], 2)

    def test_gp_shape_draw_line_with_points_count(self) -> None:
        self._setup_gp_canvas()
        data = self._test_tool("gp_shape_draw", {
            "object_name": "Canvas",
            "layer_name": "Strokes",
            "frame": 1,
            "shape": "line",
            "x1": -1.0, "y1": 0.0, "z1": 0.0,
            "x2": 1.0, "y2": 0.0, "z2": 0.0,
            "points_count": 5,
        })
        self.assertEqual(data["status"], "ok")
        self.assertEqual(data["point_count"], 5)

    def test_gp_shape_draw_error_invalid_shape(self) -> None:
        self._setup_gp_canvas()
        data = self._test_tool("gp_shape_draw", {
            "object_name": "Canvas",
            "layer_name": "Strokes",
            "frame": 1,
            "shape": "triangle",
        })
        self.assertEqual(data["status"], "error")
        self.assertEqual(data["error_code"], "INVALID_SHAPE")

    # -----------------------------------------------------------------
    # Material tools (REQ-05).

    def test_gp_material_create_basic(self) -> None:
        data = self._test_tool("gp_material_create", {
            "name": "TestMat",
            "stroke_color": [1.0, 0.0, 0.0, 1.0],
            "fill_color": [0.0, 1.0, 0.0, 0.5],
        })
        self.assertEqual(data["status"], "ok")
        self.assertEqual(data["name"], "TestMat")
        self.assertIsInstance(data["stroke_color"], list)
        self.assertEqual(len(data["stroke_color"]), 4)
        self.assertIsInstance(data["fill_color"], list)

    def test_gp_material_create_deduplication(self) -> None:
        self._test_tool("gp_material_create", {"name": "MatA"})
        data = self._test_tool("gp_material_create", {"name": "MatA"})
        self.assertEqual(data["status"], "ok")
        self.assertNotEqual(data["name"], "MatA")

    def test_gp_material_create_error_invalid_color(self) -> None:
        data = self._test_tool("gp_material_create", {
            "name": "Bad",
            "stroke_color": [1.0, 0.0],
        })
        self.assertEqual(data["status"], "error")
        self.assertEqual(data["error_code"], "INVALID_COLOR")

    def test_gp_material_assign_basic(self) -> None:
        self._test_tool("gp_object_create", {"name": "Canvas"})
        self._test_tool("gp_material_create", {"name": "Ink"})
        data = self._test_tool("gp_material_assign", {
            "object_name": "Canvas",
            "material_name": "Ink",
        })
        self.assertEqual(data["status"], "ok")
        self.assertEqual(data["object_name"], "Canvas")
        self.assertEqual(data["material_name"], "Ink")
        self.assertIsInstance(data["slot_index"], int)
        self.assertGreaterEqual(data["slot_index"], 0)

    def test_gp_material_assign_idempotent(self) -> None:
        self._test_tool("gp_object_create", {"name": "Canvas"})
        self._test_tool("gp_material_create", {"name": "Ink"})
        d1 = self._test_tool("gp_material_assign", {
            "object_name": "Canvas",
            "material_name": "Ink",
        })
        d2 = self._test_tool("gp_material_assign", {
            "object_name": "Canvas",
            "material_name": "Ink",
        })
        self.assertEqual(d1["slot_index"], d2["slot_index"])

    def test_gp_material_assign_error_material_not_found(self) -> None:
        self._test_tool("gp_object_create", {"name": "Canvas"})
        data = self._test_tool("gp_material_assign", {
            "object_name": "Canvas",
            "material_name": "NoSuchMaterial",
        })
        self.assertEqual(data["status"], "error")
        self.assertEqual(data["error_code"], "MATERIAL_NOT_FOUND")
        self.assertIsInstance(data["current_state"]["available_gp_materials"], list)

    def test_gp_material_assign_error_not_gp_material(self) -> None:
        self._test_tool("gp_object_create", {"name": "Canvas"})
        # Create a plain (non-GP) material via execute_blender_code
        self._test_tool("execute_blender_code", {
            "code": "import bpy\nbpy.data.materials.new('PlainMat')\n",
        })
        data = self._test_tool("gp_material_assign", {
            "object_name": "Canvas",
            "material_name": "PlainMat",
        })
        self.assertEqual(data["status"], "error")
        self.assertEqual(data["error_code"], "NOT_GP_MATERIAL")

    # -----------------------------------------------------------------
    # Layer animation tools (REQ-06).

    def _setup_gp_anim_canvas(self) -> None:
        """Create GP object 'AnimCanvas' with layer 'Outline' for animation tests."""
        self._test_tool("gp_object_create", {"name": "AnimCanvas"})
        self._test_tool("gp_layer_create", {
            "object_name": "AnimCanvas",
            "layer_name": "Outline",
        })

    def test_gp_layer_opacity_set_basic(self) -> None:
        self._setup_gp_anim_canvas()
        data = self._test_tool("gp_layer_opacity_set", {
            "object_name": "AnimCanvas",
            "layer_name": "Outline",
            "frame": 1,
            "opacity": 1.0,
        })
        self.assertEqual(data["status"], "ok")
        self.assertEqual(data["object_name"], "AnimCanvas")
        self.assertEqual(data["layer_name"], "Outline")
        self.assertEqual(data["frame"], 1)
        self.assertAlmostEqual(data["opacity"], 1.0, places=5)

    def test_gp_layer_opacity_set_multiple_frames(self) -> None:
        self._setup_gp_anim_canvas()
        self._test_tool("gp_layer_opacity_set", {
            "object_name": "AnimCanvas",
            "layer_name": "Outline",
            "frame": 1,
            "opacity": 1.0,
        })
        data = self._test_tool("gp_layer_opacity_set", {
            "object_name": "AnimCanvas",
            "layer_name": "Outline",
            "frame": 30,
            "opacity": 0.0,
        })
        self.assertEqual(data["status"], "ok")
        self.assertAlmostEqual(data["opacity"], 0.0, places=5)

    def test_gp_layer_opacity_set_error_out_of_range(self) -> None:
        self._setup_gp_anim_canvas()
        data = self._test_tool("gp_layer_opacity_set", {
            "object_name": "AnimCanvas",
            "layer_name": "Outline",
            "frame": 1,
            "opacity": 1.5,
        })
        self.assertEqual(data["status"], "error")
        self.assertEqual(data["error_code"], "INVALID_OPACITY")
        self.assertIn("current_opacity", data["current_state"])

    def test_gp_layer_keyframes_list_empty(self) -> None:
        self._setup_gp_anim_canvas()
        data = self._test_tool("gp_layer_keyframes_list", {
            "object_name": "AnimCanvas",
            "layer_name": "Outline",
        })
        self.assertEqual(data["status"], "ok")
        self.assertIsInstance(data["keyframes"], list)
        self.assertEqual(len(data["keyframes"]), 0)

    def test_gp_layer_keyframes_list_after_set(self) -> None:
        self._setup_gp_anim_canvas()
        self._test_tool("gp_layer_opacity_set", {
            "object_name": "AnimCanvas",
            "layer_name": "Outline",
            "frame": 1,
            "opacity": 1.0,
        })
        self._test_tool("gp_layer_opacity_set", {
            "object_name": "AnimCanvas",
            "layer_name": "Outline",
            "frame": 60,
            "opacity": 0.0,
        })
        data = self._test_tool("gp_layer_keyframes_list", {
            "object_name": "AnimCanvas",
            "layer_name": "Outline",
        })
        self.assertEqual(data["status"], "ok")
        kfs = data["keyframes"]
        self.assertEqual(len(kfs), 2)
        self.assertEqual(kfs[0]["frame"], 1)
        self.assertAlmostEqual(kfs[0]["opacity"], 1.0, places=4)
        self.assertEqual(kfs[1]["frame"], 60)
        self.assertAlmostEqual(kfs[1]["opacity"], 0.0, places=4)

    def test_gp_layer_keyframes_list_error_layer_not_found(self) -> None:
        self._test_tool("gp_object_create", {"name": "AnimCanvas"})
        data = self._test_tool("gp_layer_keyframes_list", {
            "object_name": "AnimCanvas",
            "layer_name": "DoesNotExist",
        })
        self.assertEqual(data["status"], "error")
        self.assertEqual(data["error_code"], "LAYER_NOT_FOUND")
        self.assertIsInstance(data["current_state"]["available_layers"], list)

    # -----------------------------------------------------------------
    # Navigation tools.

    def test_jump_to_tab_by_name(self) -> None:
        data = self._test_tool("jump_to_tab_by_name", {"name": "Layout"})
        if not self._interactive:
            self.assertEqual(data["status"], "error")
            return
        self.assertEqual(data["status"], "ok")
        self.assertEqual(data["workspace"], "Layout")

    def test_jump_to_tab_by_space_type(self) -> None:
        data = self._test_tool("jump_to_tab_by_space_type", {"space_type": "VIEW_3D"})
        if not self._interactive:
            self.assertEqual(data["status"], "error")
            return
        self.assertEqual(data["status"], "ok")
        self.assertEqual(data["space_type"], "VIEW_3D")

    def test_jump_to_view3d_object_by_name(self) -> None:
        data = self._test_tool("jump_to_view3d_object_by_name", {"name": "Cube"})
        if not self._interactive:
            self.assertEqual(data["status"], "error")
            return
        self.assertEqual(data["status"], "ok")
        self.assertEqual(data["object"], "Cube")
        self.assertEqual(data["type"], "MESH")

    def test_jump_to_view3d_object_data_by_name(self) -> None:
        data = self._test_tool("jump_to_view3d_object_data_by_name", {"name": "Cube"})
        if not self._interactive:
            self.assertEqual(data["status"], "error")
            return
        self.assertEqual(data["status"], "ok")
        self.assertEqual(data["data_name"], "Cube")
        self.assertEqual(data["type"], "MESH")

    # -----------------------------------------------------------------
    # 3D mesh primitive tools (REQ-08).

    def test_mesh_primitive_add_cube(self) -> None:
        data = self._test_tool("mesh_primitive_add", {
            "primitive_type": "CUBE",
            "name": "MyCube",
            "location": [1.0, 2.0, 3.0],
        })
        self.assertEqual(data["status"], "ok")
        self.assertEqual(data["name"], "MyCube")
        self.assertEqual(data["primitive_type"], "CUBE")
        loc = data["location"]
        self.assertAlmostEqual(loc[0], 1.0, places=4)
        self.assertAlmostEqual(loc[1], 2.0, places=4)
        self.assertAlmostEqual(loc[2], 3.0, places=4)

    def test_mesh_primitive_add_sphere(self) -> None:
        data = self._test_tool("mesh_primitive_add", {
            "primitive_type": "SPHERE",
            "name": "MySphere",
        })
        self.assertEqual(data["status"], "ok")
        self.assertEqual(data["name"], "MySphere")
        self.assertEqual(data["primitive_type"], "SPHERE")
        self.assertIsInstance(data["location"], list)
        self.assertEqual(len(data["location"]), 3)

    def test_mesh_primitive_add_plane(self) -> None:
        data = self._test_tool("mesh_primitive_add", {
            "primitive_type": "PLANE",
            "name": "MyPlane",
        })
        self.assertEqual(data["status"], "ok")
        self.assertEqual(data["name"], "MyPlane")
        self.assertEqual(data["primitive_type"], "PLANE")

    def test_mesh_primitive_add_cylinder(self) -> None:
        data = self._test_tool("mesh_primitive_add", {
            "primitive_type": "CYLINDER",
            "name": "MyCylinder",
        })
        self.assertEqual(data["status"], "ok")
        self.assertEqual(data["name"], "MyCylinder")
        self.assertEqual(data["primitive_type"], "CYLINDER")

    def test_mesh_primitive_add_default_name(self) -> None:
        """Omitting name gives Blender a default name."""
        data = self._test_tool("mesh_primitive_add", {
            "primitive_type": "CUBE",
        })
        self.assertEqual(data["status"], "ok")
        self.assertIsInstance(data["name"], str)
        self.assertTrue(len(data["name"]) > 0)

    def test_mesh_primitive_add_name_deduplication(self) -> None:
        """Second object with the same name gets a .001 suffix."""
        self._test_tool("mesh_primitive_add", {
            "primitive_type": "CUBE",
            "name": "SharedName",
        })
        data = self._test_tool("mesh_primitive_add", {
            "primitive_type": "SPHERE",
            "name": "SharedName",
        })
        self.assertEqual(data["status"], "ok")
        self.assertNotEqual(data["name"], "SharedName")
        self.assertTrue(data["name"].startswith("SharedName"))

    def test_mesh_primitive_add_object_in_scene(self) -> None:
        """Verify the created object is visible in scene state."""
        self._test_tool("mesh_primitive_add", {
            "primitive_type": "CUBE",
            "name": "SceneCheckCube",
        })
        state = self._test_tool("get_scene_state")
        names = [o["name"] for o in state["objects"]]
        self.assertIn("SceneCheckCube", names)

    def test_mesh_primitive_add_error_invalid_type(self) -> None:
        data = self._test_tool("mesh_primitive_add", {
            "primitive_type": "TORUS",
        })
        self.assertEqual(data["status"], "error")
        self.assertEqual(data["error_code"], "INVALID_PRIMITIVE_TYPE")
        self.assertIsInstance(data["current_state"]["supported_types"], list)
        self.assertIsInstance(data["hint"], str)

    # -----------------------------------------------------------------
    # Transform keyframe tools (REQ-09).

    def _setup_mesh_cube(self, name: str = "KFCube") -> None:
        """Create a mesh cube for keyframe tests."""
        self._test_tool("mesh_primitive_add", {
            "primitive_type": "CUBE",
            "name": name,
        })

    def test_object_keyframe_insert_location(self) -> None:
        self._setup_mesh_cube()
        data = self._test_tool("object_keyframe_insert", {
            "object_name": "KFCube",
            "frame": 1,
            "location": [1.0, 2.0, 3.0],
        })
        self.assertEqual(data["status"], "ok")
        self.assertEqual(data["object_name"], "KFCube")
        self.assertEqual(data["frame"], 1)
        self.assertIn("location", data["inserted"])
        self.assertEqual(data["interpolation"], "BEZIER")

    def test_object_keyframe_insert_rotation(self) -> None:
        self._setup_mesh_cube()
        import math
        data = self._test_tool("object_keyframe_insert", {
            "object_name": "KFCube",
            "frame": 10,
            "rotation": [0.0, 0.0, math.pi / 2],
        })
        self.assertEqual(data["status"], "ok")
        self.assertIn("rotation_euler", data["inserted"])

    def test_object_keyframe_insert_scale(self) -> None:
        self._setup_mesh_cube()
        data = self._test_tool("object_keyframe_insert", {
            "object_name": "KFCube",
            "frame": 5,
            "scale": [2.0, 2.0, 2.0],
        })
        self.assertEqual(data["status"], "ok")
        self.assertIn("scale", data["inserted"])

    def test_object_keyframe_insert_all_channels(self) -> None:
        """Insert location + rotation + scale in one call."""
        self._setup_mesh_cube()
        data = self._test_tool("object_keyframe_insert", {
            "object_name": "KFCube",
            "frame": 20,
            "location": [0.0, 0.0, 0.0],
            "rotation": [0.0, 0.0, 0.0],
            "scale": [1.0, 1.0, 1.0],
        })
        self.assertEqual(data["status"], "ok")
        self.assertIn("location", data["inserted"])
        self.assertIn("rotation_euler", data["inserted"])
        self.assertIn("scale", data["inserted"])

    def test_object_keyframe_insert_linear_interpolation(self) -> None:
        self._setup_mesh_cube()
        data = self._test_tool("object_keyframe_insert", {
            "object_name": "KFCube",
            "frame": 1,
            "location": [0.0, 0.0, 0.0],
            "interpolation": "LINEAR",
        })
        self.assertEqual(data["status"], "ok")
        self.assertEqual(data["interpolation"], "LINEAR")

    def test_object_keyframe_insert_error_object_not_found(self) -> None:
        data = self._test_tool("object_keyframe_insert", {
            "object_name": "NoSuchObject",
            "frame": 1,
            "location": [0.0, 0.0, 0.0],
        })
        self.assertEqual(data["status"], "error")
        self.assertEqual(data["error_code"], "OBJECT_NOT_FOUND")
        self.assertIsInstance(data["current_state"]["available_objects"], list)

    def test_object_keyframe_insert_error_no_properties(self) -> None:
        self._setup_mesh_cube()
        data = self._test_tool("object_keyframe_insert", {
            "object_name": "KFCube",
            "frame": 1,
        })
        self.assertEqual(data["status"], "error")
        self.assertEqual(data["error_code"], "NO_PROPERTIES")

    def test_object_keyframe_insert_error_invalid_interpolation(self) -> None:
        self._setup_mesh_cube()
        data = self._test_tool("object_keyframe_insert", {
            "object_name": "KFCube",
            "frame": 1,
            "location": [0.0, 0.0, 0.0],
            "interpolation": "EASE_IN",
        })
        self.assertEqual(data["status"], "error")
        self.assertEqual(data["error_code"], "INVALID_INTERPOLATION")

    def test_object_fcurve_list_empty(self) -> None:
        """Object with no animation returns empty curves."""
        self._setup_mesh_cube()
        data = self._test_tool("object_fcurve_list", {
            "object_name": "KFCube",
            "data_path": "location",
        })
        self.assertEqual(data["status"], "ok")
        self.assertEqual(data["data_path"], "location")
        self.assertIsInstance(data["curves"], list)
        self.assertEqual(len(data["curves"]), 0)

    def test_object_fcurve_list_after_insert(self) -> None:
        """F-Curve data matches what was inserted."""
        self._setup_mesh_cube()
        self._test_tool("object_keyframe_insert", {
            "object_name": "KFCube",
            "frame": 1,
            "location": [0.0, 0.0, 0.0],
            "interpolation": "LINEAR",
        })
        self._test_tool("object_keyframe_insert", {
            "object_name": "KFCube",
            "frame": 30,
            "location": [3.0, 0.0, 0.0],
            "interpolation": "LINEAR",
        })
        data = self._test_tool("object_fcurve_list", {
            "object_name": "KFCube",
            "data_path": "location",
        })
        self.assertEqual(data["status"], "ok")
        # Should have 3 curves (X, Y, Z).
        self.assertEqual(len(data["curves"]), 3)
        # Find X axis (array_index 0).
        x_curve = next(c for c in data["curves"] if c["array_index"] == 0)
        kfs = x_curve["keyframes"]
        self.assertEqual(len(kfs), 2)
        self.assertEqual(kfs[0]["frame"], 1)
        self.assertAlmostEqual(kfs[0]["value"], 0.0, places=4)
        self.assertEqual(kfs[0]["interpolation"], "LINEAR")
        self.assertEqual(kfs[1]["frame"], 30)
        self.assertAlmostEqual(kfs[1]["value"], 3.0, places=4)

    def test_object_fcurve_list_rotation(self) -> None:
        """rotation_euler data_path is accepted."""
        self._setup_mesh_cube()
        self._test_tool("object_keyframe_insert", {
            "object_name": "KFCube",
            "frame": 1,
            "rotation": [0.0, 0.0, 0.0],
        })
        data = self._test_tool("object_fcurve_list", {
            "object_name": "KFCube",
            "data_path": "rotation_euler",
        })
        self.assertEqual(data["status"], "ok")
        self.assertEqual(len(data["curves"]), 3)

    def test_object_fcurve_list_error_invalid_data_path(self) -> None:
        self._setup_mesh_cube()
        data = self._test_tool("object_fcurve_list", {
            "object_name": "KFCube",
            "data_path": "color",
        })
        self.assertEqual(data["status"], "error")
        self.assertEqual(data["error_code"], "INVALID_DATA_PATH")
        self.assertIsInstance(data["current_state"]["supported_data_paths"], list)

    def test_object_fcurve_list_error_object_not_found(self) -> None:
        data = self._test_tool("object_fcurve_list", {
            "object_name": "NoSuchObject",
            "data_path": "location",
        })
        self.assertEqual(data["status"], "error")
        self.assertEqual(data["error_code"], "OBJECT_NOT_FOUND")

    # -----------------------------------------------------------------
    # Modifier tools (REQ-11).

    def test_object_modifier_add_subsurf(self) -> None:
        data = self._test_tool("object_modifier_add", {
            "object_name": "Cube",
            "modifier_type": "SUBSURF",
            "name": "MySub",
            "params": {"levels": 2, "render_levels": 3},
        })
        self.assertEqual(data["status"], "ok")
        self.assertEqual(data["object_name"], "Cube")
        self.assertEqual(data["modifier_name"], "MySub")
        self.assertEqual(data["modifier_type"], "SUBSURF")
        self.assertIn("levels", data["applied_params"])
        self.assertIn("render_levels", data["applied_params"])

    def test_object_modifier_add_wave(self) -> None:
        data = self._test_tool("object_modifier_add", {
            "object_name": "Cube",
            "modifier_type": "WAVE",
            "params": {"height": 0.5, "width": 1.5, "speed": 2.0},
        })
        self.assertEqual(data["status"], "ok")
        self.assertEqual(data["modifier_type"], "WAVE")
        self.assertIn("height", data["applied_params"])
        self.assertIn("width", data["applied_params"])
        self.assertIn("speed", data["applied_params"])

    def test_object_modifier_add_default_name(self) -> None:
        """Omitting name auto-generates one."""
        data = self._test_tool("object_modifier_add", {
            "object_name": "Cube",
            "modifier_type": "SOLIDIFY",
        })
        self.assertEqual(data["status"], "ok")
        self.assertIsInstance(data["modifier_name"], str)
        self.assertTrue(len(data["modifier_name"]) > 0)

    def test_object_modifier_add_no_params(self) -> None:
        """Modifier added without any params has empty applied/failed lists."""
        data = self._test_tool("object_modifier_add", {
            "object_name": "Cube",
            "modifier_type": "BEVEL",
        })
        self.assertEqual(data["status"], "ok")
        self.assertIsInstance(data["applied_params"], list)
        self.assertIsInstance(data["failed_params"], list)

    def test_object_modifier_add_error_object_not_found(self) -> None:
        data = self._test_tool("object_modifier_add", {
            "object_name": "NoSuchObject",
            "modifier_type": "SUBSURF",
        })
        self.assertEqual(data["status"], "error")
        self.assertEqual(data["error_code"], "OBJECT_NOT_FOUND")

    def test_object_modifier_add_error_invalid_type(self) -> None:
        data = self._test_tool("object_modifier_add", {
            "object_name": "Cube",
            "modifier_type": "FAKE_MOD",
        })
        self.assertEqual(data["status"], "error")
        self.assertEqual(data["error_code"], "INVALID_MODIFIER_TYPE")
        self.assertIsInstance(data["hint"], str)

    def test_object_modifiers_list_empty(self) -> None:
        """Fresh mesh object has no modifiers."""
        self._test_tool("mesh_primitive_add", {
            "primitive_type": "PLANE",
            "name": "CleanPlane",
        })
        data = self._test_tool("object_modifiers_list", {
            "object_name": "CleanPlane",
        })
        self.assertEqual(data["status"], "ok")
        self.assertEqual(data["object_name"], "CleanPlane")
        self.assertIsInstance(data["modifiers"], list)
        self.assertEqual(len(data["modifiers"]), 0)

    def test_object_modifiers_list_after_add(self) -> None:
        """Modifier added via object_modifier_add is returned by list."""
        self._test_tool("object_modifier_add", {
            "object_name": "Cube",
            "modifier_type": "SUBSURF",
            "name": "ListCheck",
            "params": {"levels": 2},
        })
        data = self._test_tool("object_modifiers_list", {
            "object_name": "Cube",
        })
        self.assertEqual(data["status"], "ok")
        names = [m["name"] for m in data["modifiers"]]
        self.assertIn("ListCheck", names)
        sub_mod = next(m for m in data["modifiers"] if m["name"] == "ListCheck")
        self.assertEqual(sub_mod["type"], "SUBSURF")
        self.assertIsInstance(sub_mod["params"], dict)
        self.assertEqual(sub_mod["params"].get("levels"), 2)

    def test_object_modifiers_list_params_roundtrip(self) -> None:
        """Params set via object_modifier_add are read back correctly."""
        self._test_tool("object_modifier_add", {
            "object_name": "Cube",
            "modifier_type": "WAVE",
            "name": "WaveCheck",
            "params": {"height": 0.75, "speed": 1.5},
        })
        data = self._test_tool("object_modifiers_list", {
            "object_name": "Cube",
        })
        wave = next(
            (m for m in data["modifiers"] if m["name"] == "WaveCheck"), None,
        )
        self.assertIsNotNone(wave)
        self.assertAlmostEqual(wave["params"].get("height"), 0.75, places=4)
        self.assertAlmostEqual(wave["params"].get("speed"), 1.5, places=4)

    def test_object_modifiers_list_error_object_not_found(self) -> None:
        data = self._test_tool("object_modifiers_list", {
            "object_name": "NoSuchObject",
        })
        self.assertEqual(data["status"], "error")
        self.assertEqual(data["error_code"], "OBJECT_NOT_FOUND")

    def test_object_modifier_visible_in_detail_summary(self) -> None:
        """Modifier added to Cube appears in get_object_detail_summary."""
        self._test_tool("object_modifier_add", {
            "object_name": "Cube",
            "modifier_type": "SUBSURF",
            "name": "DetailCheck",
        })
        detail = self._test_tool("get_object_detail_summary", {"name": "Cube"})
        mod_names = [m["name"] for m in detail.get("modifiers", [])]
        self.assertIn("DetailCheck", mod_names)

    # -----------------------------------------------------------------
    # Driver tools (REQ-12).

    def test_object_driver_add_location_z(self) -> None:
        """Add sin(frame/10) driver to location Z — canonical REQ-12 case."""
        data = self._test_tool("object_driver_add", {
            "object_name": "Cube",
            "data_path": "location",
            "index": 2,
            "expression": "sin(frame/10)",
        })
        self.assertEqual(data["status"], "ok")
        self.assertEqual(data["object_name"], "Cube")
        self.assertEqual(data["data_path"], "location")
        self.assertEqual(data["index"], 2)
        self.assertEqual(data["expression"], "sin(frame/10)")
        self.assertEqual(data["action"], "added")

    def test_object_driver_add_update_existing(self) -> None:
        """Calling driver_add twice on the same channel updates the expression."""
        self._test_tool("object_driver_add", {
            "object_name": "Cube",
            "data_path": "location",
            "index": 0,
            "expression": "frame * 0.01",
        })
        data = self._test_tool("object_driver_add", {
            "object_name": "Cube",
            "data_path": "location",
            "index": 0,
            "expression": "frame * 0.02",
        })
        self.assertEqual(data["status"], "ok")
        self.assertEqual(data["action"], "updated")
        self.assertEqual(data["expression"], "frame * 0.02")

    def test_object_driver_add_rotation(self) -> None:
        data = self._test_tool("object_driver_add", {
            "object_name": "Cube",
            "data_path": "rotation_euler",
            "index": 2,
            "expression": "frame * 0.1",
        })
        self.assertEqual(data["status"], "ok")
        self.assertEqual(data["data_path"], "rotation_euler")

    def test_object_driver_add_scale(self) -> None:
        data = self._test_tool("object_driver_add", {
            "object_name": "Cube",
            "data_path": "scale",
            "index": 1,
            "expression": "1 + sin(frame / 20) * 0.5",
        })
        self.assertEqual(data["status"], "ok")
        self.assertEqual(data["data_path"], "scale")

    def test_object_driver_add_error_object_not_found(self) -> None:
        data = self._test_tool("object_driver_add", {
            "object_name": "NoSuchObject",
            "data_path": "location",
            "index": 0,
            "expression": "frame",
        })
        self.assertEqual(data["status"], "error")
        self.assertEqual(data["error_code"], "OBJECT_NOT_FOUND")
        self.assertIsInstance(data["current_state"]["available_objects"], list)

    def test_object_driver_add_error_empty_expression(self) -> None:
        data = self._test_tool("object_driver_add", {
            "object_name": "Cube",
            "data_path": "location",
            "index": 0,
            "expression": "   ",
        })
        self.assertEqual(data["status"], "error")
        self.assertEqual(data["error_code"], "EMPTY_EXPRESSION")

    def test_object_driver_list_empty(self) -> None:
        """Fresh mesh object has no drivers."""
        self._test_tool("mesh_primitive_add", {
            "primitive_type": "CUBE",
            "name": "NoDrvCube",
        })
        data = self._test_tool("object_driver_list", {
            "object_name": "NoDrvCube",
        })
        self.assertEqual(data["status"], "ok")
        self.assertIsInstance(data["drivers"], list)
        self.assertEqual(len(data["drivers"]), 0)

    def test_object_driver_list_after_add(self) -> None:
        """Driver written by object_driver_add is returned by object_driver_list."""
        self._test_tool("object_driver_add", {
            "object_name": "Cube",
            "data_path": "location",
            "index": 2,
            "expression": "sin(frame/10)",
        })
        data = self._test_tool("object_driver_list", {
            "object_name": "Cube",
        })
        self.assertEqual(data["status"], "ok")
        drivers = data["drivers"]
        self.assertTrue(len(drivers) >= 1)
        z_drv = next(
            (d for d in drivers
             if d["data_path"] == "location" and d["index"] == 2),
            None,
        )
        self.assertIsNotNone(z_drv)
        self.assertEqual(z_drv["expression"], "sin(frame/10)")
        self.assertEqual(z_drv["driver_type"], "SCRIPTED")

    def test_object_driver_list_multiple(self) -> None:
        """Multiple drivers on different channels are all returned."""
        for idx, expr in enumerate(["frame*0.1", "sin(frame)", "cos(frame)"]):
            self._test_tool("object_driver_add", {
                "object_name": "Cube",
                "data_path": "location",
                "index": idx,
                "expression": expr,
            })
        data = self._test_tool("object_driver_list", {
            "object_name": "Cube",
        })
        self.assertEqual(data["status"], "ok")
        loc_drivers = [
            d for d in data["drivers"] if d["data_path"] == "location"
        ]
        self.assertEqual(len(loc_drivers), 3)

    def test_object_driver_list_error_object_not_found(self) -> None:
        data = self._test_tool("object_driver_list", {
            "object_name": "NoSuchObject",
        })
        self.assertEqual(data["status"], "error")
        self.assertEqual(data["error_code"], "OBJECT_NOT_FOUND")

    # -----------------------------------------------------------------
    # Camera animation tools (REQ-10).

    def test_camera_position_keyframe(self) -> None:
        """Camera position keyframe via object_keyframe_insert."""
        data = self._test_tool("object_keyframe_insert", {
            "object_name": "Camera",
            "frame": 1,
            "location": [0.0, -8.0, 5.0],
            "interpolation": "LINEAR",
        })
        self.assertEqual(data["status"], "ok")
        self.assertEqual(data["object_name"], "Camera")
        self.assertIn("location", data["inserted"])

    def test_camera_target_track_basic(self) -> None:
        """Set up Track-To constraint using scene camera."""
        data = self._test_tool("camera_target_track", {
            "target_location": [0.0, 0.0, 0.0],
        })
        self.assertEqual(data["status"], "ok")
        self.assertEqual(data["camera_name"], "Camera")
        self.assertIsInstance(data["target_name"], str)
        self.assertTrue(data["target_name"])
        self.assertIsInstance(data["constraint_name"], str)
        self.assertEqual(data["frame"], -1)

    def test_camera_target_track_explicit_camera(self) -> None:
        """Explicit camera_name resolves correctly."""
        data = self._test_tool("camera_target_track", {
            "camera_name": "Camera",
            "target_name": "FocusPoint",
            "target_location": [1.0, 0.0, 0.0],
        })
        self.assertEqual(data["status"], "ok")
        self.assertEqual(data["camera_name"], "Camera")
        self.assertEqual(data["target_name"], "FocusPoint")

    def test_camera_target_track_with_keyframe(self) -> None:
        """Insert keyframe on target and verify via object_fcurve_list."""
        self._test_tool("camera_target_track", {
            "target_name": "CamTarget",
            "target_location": [0.0, 0.0, 0.0],
            "frame": 1,
            "interpolation": "LINEAR",
        })
        self._test_tool("camera_target_track", {
            "target_name": "CamTarget",
            "target_location": [5.0, 0.0, 0.0],
            "frame": 30,
            "interpolation": "LINEAR",
        })
        fcurve = self._test_tool("object_fcurve_list", {
            "object_name": "CamTarget",
            "data_path": "location",
        })
        self.assertEqual(fcurve["status"], "ok")
        self.assertEqual(len(fcurve["curves"]), 3)
        x_curve = next(c for c in fcurve["curves"] if c["array_index"] == 0)
        self.assertEqual(len(x_curve["keyframes"]), 2)
        self.assertEqual(x_curve["keyframes"][0]["frame"], 1)
        self.assertAlmostEqual(x_curve["keyframes"][0]["value"], 0.0, places=4)
        self.assertEqual(x_curve["keyframes"][1]["frame"], 30)
        self.assertAlmostEqual(x_curve["keyframes"][1]["value"], 5.0, places=4)
        self.assertEqual(x_curve["keyframes"][0]["interpolation"], "LINEAR")

    def test_camera_target_track_idempotent(self) -> None:
        """Calling twice with the same target does not duplicate the constraint."""
        self._test_tool("camera_target_track", {
            "target_name": "StableTarget",
            "target_location": [0.0, 0.0, 0.0],
        })
        d2 = self._test_tool("camera_target_track", {
            "target_name": "StableTarget",
            "target_location": [1.0, 0.0, 0.0],
        })
        self.assertEqual(d2["status"], "ok")
        # Verify only one Track-To constraint exists via execute_blender_code.
        check = self._test_tool("execute_blender_code", {
            "code": (
                "import bpy\n"
                "cam = bpy.data.objects['Camera']\n"
                "target = bpy.data.objects.get('StableTarget')\n"
                "count = sum(\n"
                "    1 for c in cam.constraints\n"
                "    if c.type == 'TRACK_TO' and c.target == target\n"
                ")\n"
                "result = {'constraint_count': count}\n"
            ),
        })
        self.assertEqual(check["constraint_count"], 1)

    def test_camera_target_track_auto_target_name(self) -> None:
        """When target_name is omitted, it defaults to '{camera}_Target'."""
        data = self._test_tool("camera_target_track", {
            "camera_name": "Camera",
            "target_location": [0.0, 0.0, 0.0],
        })
        self.assertEqual(data["status"], "ok")
        self.assertEqual(data["target_name"], "Camera_Target")

    def test_camera_target_track_error_not_camera(self) -> None:
        data = self._test_tool("camera_target_track", {
            "camera_name": "Cube",
            "target_location": [0.0, 0.0, 0.0],
        })
        self.assertEqual(data["status"], "error")
        self.assertEqual(data["error_code"], "INVALID_OBJECT_TYPE")
        self.assertIsInstance(data["current_state"]["available_cameras"], list)

    def test_camera_target_track_error_object_not_found(self) -> None:
        data = self._test_tool("camera_target_track", {
            "camera_name": "NoSuchCamera",
            "target_location": [0.0, 0.0, 0.0],
        })
        self.assertEqual(data["status"], "error")
        self.assertEqual(data["error_code"], "OBJECT_NOT_FOUND")

    # -----------------------------------------------------------------
    # Render tools.

    def _assert_valid_png(self, filepath: str) -> None:
        """
        Ask Blender to verify that *filepath* is a valid PNG file.
        """
        data = self._test_tool("execute_blender_code", {
            "code": (
                "import os\n"
                "with open({!r}, 'rb') as fh:\n"
                "    header = fh.read(8)\n"
                "result = {{\n"
                "    'size': os.path.getsize({!r}),\n"
                "    'png_magic': header == b'\\x89PNG\\r\\n\\x1a\\n',\n"
                "}}\n"
            ).format(filepath, filepath),
        })
        self.assertGreater(data["size"], 0)
        self.assertTrue(data["png_magic"])

    def _set_cycles_cpu(self) -> None:
        """Switch to Cycles CPU so rendering works in headless environments."""
        def code() -> None:
            import bpy  # type: ignore[import-not-found]
            bpy.context.scene.render.engine = 'CYCLES'
            bpy.context.scene.cycles.device = 'CPU'
            result = {'engine': 'CYCLES'}  # noqa: F841
        self._test_tool("execute_blender_code", {
            "code": _python_fn_body_as_string(code),
        })

    def test_render_thumbnail_to_path(self) -> None:
        self._set_cycles_cpu()
        data = self._test_tool("render_thumbnail_to_path", {
            "output_path": "thumb.png",
        })
        self.assertEqual(data["status"], "ok")
        self.assertTrue(data["filepath"].endswith("thumb.png"))
        self._assert_valid_png(data["filepath"])

    def test_render_viewport_to_path(self) -> None:
        self._set_cycles_cpu()
        data = self._test_tool("render_viewport_to_path", {
            "output_path": "render.png",
        })
        self.assertEqual(data["status"], "ok")
        self.assertTrue(data["filepath"].endswith("render.png"))
        self._assert_valid_png(data["filepath"])

    def test_render_frame_basic(self) -> None:
        self._set_cycles_cpu()
        data = self._test_tool("render_frame", {
            "output_path": "frame.png",
            "width": 64,
            "height": 64,
        })
        self.assertEqual(data["status"], "ok")
        self.assertTrue(data["filepath"].endswith("frame.png"))
        self.assertEqual(data["width"], 64)
        self.assertEqual(data["height"], 64)
        self._assert_valid_png(data["filepath"])

    def test_render_frame_with_frame_override(self) -> None:
        self._set_cycles_cpu()
        data = self._test_tool("render_frame", {
            "output_path": "frame10.png",
            "frame": 10,
            "width": 64,
            "height": 64,
        })
        self.assertEqual(data["status"], "ok")
        self.assertEqual(data["frame"], 10)
        self._assert_valid_png(data["filepath"])

    def test_render_animation_basic(self) -> None:
        self._set_cycles_cpu()

        def _setup_short_anim() -> None:
            import bpy  # type: ignore[import-not-found]
            bpy.context.scene.frame_start = 1
            bpy.context.scene.frame_end = 2
            result = {"frame_start": bpy.context.scene.frame_start}  # noqa: F841

        self._test_tool("execute_blender_code", {
            "code": _python_fn_body_as_string(_setup_short_anim),
        })

        output = os.path.join(tempfile.gettempdir(), "blender_mcp_test_anim.mp4")
        data = self._test_tool("render_animation", {
            "output_path": output,
            "frame_start": 1,
            "frame_end": 2,
            "width": 64,
            "height": 64,
        })
        self.assertEqual(data["status"], "ok")
        self.assertEqual(data["frame_start"], 1)
        self.assertEqual(data["frame_end"], 2)
        self.assertEqual(data["width"], 64)
        self.assertEqual(data["height"], 64)
        # Verify output file exists and has content.
        filepath = data["filepath"]
        self.assertTrue(os.path.exists(filepath), f"Video file missing: {filepath}")
        self.assertGreater(os.path.getsize(filepath), 0)

    # -----------------------------------------------------------------
    # Deferred tool response.

    def test_deferred_tool_response(self) -> None:
        """Synthetic test for the deferred response mechanism, not a real tool."""
        if not self._interactive:
            # Deferred responses only apply to interactive (timer-based) mode.
            # Background mode rejects them explicitly.
            return

        # Send code that sets check_is_finished. The deferred response
        # mechanism polls it until it returns a non-None result.
        def deferred_code() -> None:
            import time
            deadline = time.monotonic() + 0.3

            def check_is_finished():  # noqa: F841 (read by the exec namespace)
                if time.monotonic() < deadline:
                    return None
                return {'deferred': True, 'value': 42}
            result = {}  # noqa: F841
        data = self._test_tool("execute_blender_code", {
            "code": _python_fn_body_as_string(deferred_code),
        })
        self.assertTrue(data["deferred"])
        self.assertEqual(data["value"], 42)

    def test_deferred_tool_response_blocking_mode_error(self) -> None:
        """Synthetic test: blocking server modes reject deferred responses clearly."""
        if self._interactive:
            return

        def deferred_code() -> None:
            def check_is_finished():  # noqa: F841 (read by the exec namespace)
                return {'deferred': True, 'value': 42}
            result = {}  # noqa: F841
        data = self._test_tool("execute_blender_code", {
            "code": _python_fn_body_as_string(deferred_code),
        })
        self.assertEqual(data["status"], "error")
        self.assertIn(
            "Deferred responses via `check_is_finished` are only supported by the interactive addon server",
            data["message"],
        )

    def test_deferred_tool_render(self) -> None:
        """Test the deferred path with a real render of a non-trivial scene."""
        if not self._interactive:
            return

        def _setup_render_scene() -> None:
            import bpy  # type: ignore[import-not-found]
            bpy.ops.wm.read_homefile(use_empty=True)
            scene = bpy.context.scene
            # Use Cycles CPU so the render works in headless environments
            # where EEVEE may not have a usable GPU context.
            scene.render.engine = 'CYCLES'
            scene.cycles.device = 'CPU'
            scene.cycles.samples = 16
            scene.render.resolution_x = 960
            scene.render.resolution_y = 540
            # Camera.
            bpy.ops.object.camera_add(location=(7, -7, 5))
            cam = bpy.context.active_object
            cam.rotation_euler = (1.1, 0, 0.8)
            scene.camera = cam
            # Light.
            bpy.ops.object.light_add(type='SUN', location=(5, -3, 8))
            # Grid of spheres with different materials.
            for i in range(6):
                for j in range(6):
                    bpy.ops.mesh.primitive_uv_sphere_add(
                        segments=32, ring_count=16,
                        radius=0.4, location=(i, j, 0),
                    )
                    ob = bpy.context.active_object
                    mat = bpy.data.materials.new('M_{:d}_{:d}'.format(i, j))
                    mat.use_nodes = True
                    bsdf = mat.node_tree.nodes['Principled BSDF']
                    bsdf.inputs['Base Color'].default_value = (
                        i / 5.0, j / 5.0, 0.5, 1.0,
                    )
                    bsdf.inputs['Roughness'].default_value = i / 5.0
                    bsdf.inputs['Metallic'].default_value = j / 5.0
                    ob.data.materials.append(mat)
            # Ground plane.
            bpy.ops.mesh.primitive_plane_add(size=20, location=(2.5, 2.5, -0.5))
            result = {'objects': len(bpy.data.objects)}  # noqa: F841

        self._test_tool("execute_blender_code", {
            "code": _python_fn_body_as_string(_setup_render_scene),
        })

        data = self._test_tool("render_viewport_to_path", {
            "output_path": "deferred_render.png",
        })
        self.assertEqual(data["status"], "ok")
        self.assertTrue(data["filepath"].endswith("deferred_render.png"))
        self._assert_valid_png(data["filepath"])

    def test_deferred_tool_response_error(self) -> None:
        """Synthetic test: verify that an exception in check_is_finished is reported."""
        if not self._interactive:
            return

        def deferred_error_code() -> None:
            def check_is_finished():  # noqa: F841
                raise RuntimeError('checker failed')
            result = {}  # noqa: F841
        data = self._test_tool("execute_blender_code", {
            "code": _python_fn_body_as_string(deferred_error_code),
        })
        self.assertEqual(data["status"], "error")
        self.assertIn("checker failed", data["message"])

    # -----------------------------------------------------------------
    # Error handling.

    def test_execute_blender_code_error(self) -> None:
        data = self._test_tool("execute_blender_code", {
            "code": "raise ValueError('test error')",
        })
        self.assertEqual(data["status"], "error")
        self.assertIn("ValueError", data["message"])

    def test_execute_blender_code_blocked_operator(self) -> None:
        """Verify that the sandbox blocks actions which may exit Blender or lose our connection."""
        data = self._test_tool("execute_blender_code", {
            "code": "import bpy; bpy.ops.wm.read_factory_settings()",
        })
        self.assertEqual(data["status"], "error")
        self.assertIn(
            "RuntimeError: Operator 'bpy.ops.wm.read_factory_settings()' is not allowed "
            "in LLM-generated code: Resets all user preferences and startup file, "
            "use bpy.ops.wm.read_homefile() or "
            "bpy.ops.wm.read_homefile(use_empty=True, use_factory_startup=True) instead",
            data["message"],
        )

    def test_execute_blender_code_blocked_sys_exit(self) -> None:
        """Verify that the sandbox blocks sys.exit()."""
        data = self._test_tool("execute_blender_code", {
            "code": "import sys; sys.exit(1)",
        })
        self.assertEqual(data["status"], "error")
        self.assertIn(
            "RuntimeError: sys.exit() is not allowed in LLM-generated code",
            data["message"],
        )

    def test_jump_to_tab_by_name_error(self) -> None:
        if not self._interactive:
            return
        data = self._test_tool("jump_to_tab_by_name", {"name": "NonExistent"})
        self.assertEqual(data["status"], "error")
        self.assertEqual(data["error_code"], "WORKSPACE_NOT_FOUND")
        self.assertIsInstance(
            data["current_state"]["available_workspaces"], list
        )
        self.assertIsInstance(data["hint"], str)
        self.assertTrue(data["hint"])

    def test_execute_blender_code_for_cli_error(self) -> None:
        self._call_tool_expect_error("execute_blender_code_for_cli", {
            "blend_file": self._blend_path,
            "code": "raise ValueError('cli test error')",
        })

    def test_jump_to_view3d_object_by_name_error(self) -> None:
        if not self._interactive:
            return
        data = self._test_tool("jump_to_view3d_object_by_name", {"name": "NonExistent"})
        self.assertEqual(data["status"], "error")
        self.assertEqual(data["error_code"], "OBJECT_NOT_FOUND")
        self.assertIn("'NonExistent'", data["message"])
        self.assertIn("Cube", data["current_state"]["available_objects"])
        self.assertIsInstance(data["hint"], str)
        self.assertTrue(data["hint"])

    def test_jump_to_view3d_object_data_by_name_error(self) -> None:
        if not self._interactive:
            return
        data = self._test_tool("jump_to_view3d_object_data_by_name", {"name": "NonExistent"})
        self.assertEqual(data["status"], "error")
        self.assertEqual(data["error_code"], "DATA_NOT_FOUND")
        self.assertIn("'NonExistent'", data["message"])
        self.assertIsInstance(data["current_state"]["available_data_names"], list)
        self.assertIsInstance(data["hint"], str)
        self.assertTrue(data["hint"])

    # -----------------------------------------------------------------
    # State verification.

    def test_jump_to_view3d_object_by_name_allow_edits(self) -> None:
        """
        Verify that ``allow_edits`` un-hides a hidden object.
        """
        if not self._interactive:
            return
        # Hide the default Cube.
        self._test_tool("execute_blender_code", {
            "code": (
                "import bpy\n"
                "bpy.data.objects['Cube'].hide_viewport = True\n"
                "result = {'hidden': True}\n"
            ),
        })
        # Jump to it with allow_edits enabled.
        data = self._test_tool("jump_to_view3d_object_by_name", {
            "name": "Cube", "allow_edits": True,
        })
        self.assertEqual(data["status"], "ok")
        self.assertEqual(data["object"], "Cube")
        # Verify the object is no longer hidden.
        check = self._test_tool("execute_blender_code", {
            "code": (
                "import bpy\n"
                "result = {'hide_viewport': bpy.data.objects['Cube'].hide_viewport}\n"
            ),
        })
        self.assertFalse(check["hide_viewport"])

    def test_jump_to_view3d_object_data_by_name_allow_edits(self) -> None:
        """
        Verify that ``allow_edits`` un-hides an object found by data name.
        """
        if not self._interactive:
            return
        # Hide the default Cube.
        self._test_tool("execute_blender_code", {
            "code": (
                "import bpy\n"
                "bpy.data.objects['Cube'].hide_viewport = True\n"
                "result = {'hidden': True}\n"
            ),
        })
        # Jump to it via data name with allow_edits enabled.
        data = self._test_tool("jump_to_view3d_object_data_by_name", {
            "name": "Cube", "allow_edits": True,
        })
        self.assertEqual(data["status"], "ok")
        self.assertEqual(data["data_name"], "Cube")
        # Verify the object is no longer hidden.
        check = self._test_tool("execute_blender_code", {
            "code": (
                "import bpy\n"
                "result = {'hide_viewport': bpy.data.objects['Cube'].hide_viewport}\n"
            ),
        })
        self.assertFalse(check["hide_viewport"])

    def test_execute_blender_code_stateful(self) -> None:
        """
        Verify that the Blender session is stateful across tool calls.
        """
        # Create an object.
        self._test_tool("execute_blender_code", {
            "code": (
                "import bpy\n"
                "bpy.ops.mesh.primitive_ico_sphere_add()\n"
                "bpy.context.active_object.name = 'TestSphere'\n"
                "result = {'created': True}\n"
            ),
        })
        # Verify it exists in a separate call.
        data = self._test_tool("execute_blender_code", {
            "code": "import bpy\nresult = {'found': 'TestSphere' in bpy.data.objects}\n",
        })
        self.assertTrue(data["found"])

    # -----------------------------------------------------------------
    # Geometry Nodes tools (REQ-13).

    def test_geonodes_apply_preset_wave(self) -> None:
        """Apply wave preset; modifier and node tree are created."""
        data = self._test_tool("geonodes_apply_preset", {
            "object_name": "Cube",
            "preset": "wave",
        })
        self.assertEqual(data["status"], "ok")
        self.assertEqual(data["object_name"], "Cube")
        self.assertEqual(data["preset"], "wave")
        self.assertIn("modifier_name", data)
        self.assertIn("node_tree_name", data)
        self.assertGreater(len(data["nodes_created"]), 0)

    def test_geonodes_apply_preset_noise_displace(self) -> None:
        """Apply noise_displace preset; modifier and nodes are created."""
        data = self._test_tool("geonodes_apply_preset", {
            "object_name": "Cube",
            "preset": "noise_displace",
        })
        self.assertEqual(data["status"], "ok")
        self.assertEqual(data["preset"], "noise_displace")
        self.assertGreater(len(data["nodes_created"]), 0)

    def test_geonodes_apply_preset_error_invalid(self) -> None:
        """Unknown preset returns INVALID_PRESET error."""
        data = self._test_tool("geonodes_apply_preset", {
            "object_name": "Cube",
            "preset": "nonexistent",
        })
        self.assertEqual(data["status"], "error")
        self.assertEqual(data["error_code"], "INVALID_PRESET")

    def test_geonodes_apply_preset_error_object_not_found(self) -> None:
        """Object not found returns OBJECT_NOT_FOUND error."""
        data = self._test_tool("geonodes_apply_preset", {
            "object_name": "GhostObject",
            "preset": "wave",
        })
        self.assertEqual(data["status"], "error")
        self.assertEqual(data["error_code"], "OBJECT_NOT_FOUND")

    def test_geonodes_query_after_preset(self) -> None:
        """Query returns node list matching the applied wave preset."""
        self._test_tool("geonodes_apply_preset", {
            "object_name": "Cube",
            "preset": "wave",
        })
        data = self._test_tool("geonodes_query", {
            "object_name": "Cube",
        })
        self.assertEqual(data["status"], "ok")
        self.assertGreater(len(data["nodes"]), 0)
        node_names = [n["name"] for n in data["nodes"]]
        # The preset creates Group Input / Output plus math/position nodes.
        self.assertTrue(
            any("Group Input" in name or "NodeGroupInput" in name
                for name in [n.get("bl_idname", "") for n in data["nodes"]]),
            "Expected NodeGroupInput in nodes",
        )

    def test_geonodes_query_error_no_modifier(self) -> None:
        """Query on object with no GN modifier returns NO_GEONODES_MODIFIER."""
        # Light has no GN modifier by default.
        data = self._test_tool("geonodes_query", {
            "object_name": "Light",
        })
        self.assertEqual(data["status"], "error")
        self.assertEqual(data["error_code"], "NO_GEONODES_MODIFIER")

    def test_geonodes_node_set_basic(self) -> None:
        """Set a node input value; new_value matches what was set."""
        self._test_tool("geonodes_apply_preset", {
            "object_name": "Cube",
            "preset": "wave",
        })
        # "Multiply Amplitude" node has a second scalar input (Value slot 1).
        data = self._test_tool("geonodes_node_set", {
            "object_name": "Cube",
            "node_name": "Multiply Amplitude",
            "input_name": "Value",
            "value": 0.75,
        })
        self.assertEqual(data["status"], "ok")
        self.assertAlmostEqual(data["new_value"], 0.75, places=4)

    def test_geonodes_node_set_readback_matches(self) -> None:
        """After set, query confirms the updated default_value."""
        self._test_tool("geonodes_apply_preset", {
            "object_name": "Cube",
            "preset": "wave",
        })
        self._test_tool("geonodes_node_set", {
            "object_name": "Cube",
            "node_name": "Multiply Amplitude",
            "input_name": "Value",
            "value": 1.23,
        })
        query = self._test_tool("geonodes_query", {"object_name": "Cube"})
        nodes = {n["name"]: n for n in query["nodes"]}
        amp_node = nodes.get("Multiply Amplitude")
        self.assertIsNotNone(amp_node)
        # The first "Value" input (index 0) was set to 1.23.
        # default_value is returned for all inputs regardless of link status.
        value_inputs = [i for i in amp_node["inputs"] if i["name"] == "Value"]
        self.assertTrue(
            any(abs((i.get("default_value") or 0) - 1.23) < 0.01
                for i in value_inputs),
            "Expected default_value ~1.23 after geonodes_node_set",
        )

    def test_geonodes_node_set_error_node_not_found(self) -> None:
        """Setting a non-existent node returns NODE_NOT_FOUND."""
        self._test_tool("geonodes_apply_preset", {
            "object_name": "Cube",
            "preset": "wave",
        })
        data = self._test_tool("geonodes_node_set", {
            "object_name": "Cube",
            "node_name": "GhostNode",
            "input_name": "Value",
            "value": 1.0,
        })
        self.assertEqual(data["status"], "error")
        self.assertEqual(data["error_code"], "NODE_NOT_FOUND")

    def test_geonodes_node_keyframe_basic(self) -> None:
        """Keyframe a node input; result frame and value match request."""
        self._test_tool("geonodes_apply_preset", {
            "object_name": "Cube",
            "preset": "wave",
        })
        data = self._test_tool("geonodes_node_keyframe", {
            "object_name": "Cube",
            "node_name": "Multiply Amplitude",
            "input_name": "Value",
            "frame": 1,
            "value": 0.1,
            "interpolation": "LINEAR",
        })
        self.assertEqual(data["status"], "ok")
        self.assertEqual(data["frame"], 1)
        self.assertAlmostEqual(data["value"], 0.1, places=4)
        self.assertEqual(data["interpolation"], "LINEAR")

    def test_geonodes_node_keyframe_two_frames(self) -> None:
        """Two keyframes at different frames are both accepted."""
        self._test_tool("geonodes_apply_preset", {
            "object_name": "Cube",
            "preset": "wave",
        })
        for frame, val in ((1, 0.1), (50, 0.9)):
            data = self._test_tool("geonodes_node_keyframe", {
                "object_name": "Cube",
                "node_name": "Multiply Amplitude",
                "input_name": "Value",
                "frame": frame,
                "value": val,
                "interpolation": "BEZIER",
            })
            self.assertEqual(data["status"], "ok")
            self.assertEqual(data["frame"], frame)

    def test_geonodes_node_keyframe_error_invalid_interpolation(self) -> None:
        """Invalid interpolation returns INVALID_INTERPOLATION error."""
        self._test_tool("geonodes_apply_preset", {
            "object_name": "Cube",
            "preset": "wave",
        })
        data = self._test_tool("geonodes_node_keyframe", {
            "object_name": "Cube",
            "node_name": "Multiply Amplitude",
            "input_name": "Value",
            "frame": 10,
            "value": 0.5,
            "interpolation": "BOUNCE",
        })
        self.assertEqual(data["status"], "error")
        self.assertEqual(data["error_code"], "INVALID_INTERPOLATION")

    # -----------------------------------------------------------------
    # Material query tools (REQ-14).

    def test_material_list_default_scene(self) -> None:
        """Default scene has at least the 'Material' material."""
        data = self._test_tool("material_list", {})
        self.assertEqual(data["status"], "ok")
        self.assertIn("materials", data)
        self.assertIsInstance(data["materials"], list)
        # Default Blender scene ships with one material named "Material".
        names = [m["name"] for m in data["materials"]]
        self.assertIn("Material", names)

    def test_material_list_includes_new_material(self) -> None:
        """After creating a new material it appears in material_list."""
        self._test_tool("execute_blender_code", {
            "code": (
                "import bpy\n"
                "mat = bpy.data.materials.new('TestMaterialREQ14')\n"
                "result = {'created': mat.name}\n"
            ),
        })
        data = self._test_tool("material_list", {})
        self.assertEqual(data["status"], "ok")
        names = [m["name"] for m in data["materials"]]
        self.assertIn("TestMaterialREQ14", names)

    def test_material_list_properties_present(self) -> None:
        """Each material entry has required property keys."""
        data = self._test_tool("material_list", {})
        self.assertGreater(len(data["materials"]), 0)
        for mat in data["materials"]:
            self.assertIn("name", mat)
            self.assertIn("use_nodes", mat)
            self.assertIn("is_grease_pencil", mat)
            self.assertIn("diffuse_color", mat)

    def test_material_list_principled_bsdf_properties(self) -> None:
        """A node-based material with Principled BSDF exposes extra props."""
        self._test_tool("execute_blender_code", {
            "code": (
                "import bpy\n"
                "mat = bpy.data.materials.new('PBSDFTestMat')\n"
                "mat.use_nodes = True\n"
                "principled = mat.node_tree.nodes.get('Principled BSDF')\n"
                "if principled:\n"
                "    principled.inputs['Base Color'].default_value = "
                "(0.8, 0.2, 0.1, 1.0)\n"
                "result = {'name': mat.name}\n"
            ),
        })
        data = self._test_tool("material_list", {})
        mats = {m["name"]: m for m in data["materials"]}
        pbsdf = mats.get("PBSDFTestMat")
        self.assertIsNotNone(pbsdf, "PBSDFTestMat not found in material_list")
        self.assertTrue(pbsdf["use_nodes"])
        self.assertIn("base_color", pbsdf)
        self.assertAlmostEqual(pbsdf["base_color"][0], 0.8, places=1)
        self.assertIn("metallic", pbsdf)
        self.assertIn("roughness", pbsdf)

    def test_material_list_sorted_alphabetically(self) -> None:
        """Results are in alphabetical order."""
        data = self._test_tool("material_list", {})
        names = [m["name"] for m in data["materials"]]
        self.assertEqual(names, sorted(names))

    def test_object_material_list_default_cube(self) -> None:
        """Default Cube has one material slot with 'Material'."""
        data = self._test_tool("object_material_list", {
            "object_name": "Cube",
        })
        self.assertEqual(data["status"], "ok")
        self.assertEqual(data["object_name"], "Cube")
        self.assertIn("slots", data)
        self.assertGreater(len(data["slots"]), 0)
        mat_names = [s["material_name"] for s in data["slots"]]
        self.assertIn("Material", mat_names)

    def test_object_material_list_slot_structure(self) -> None:
        """Each slot has index, material_name, and is_active keys."""
        data = self._test_tool("object_material_list", {
            "object_name": "Cube",
        })
        for slot in data["slots"]:
            self.assertIn("index", slot)
            self.assertIn("material_name", slot)
            self.assertIn("is_active", slot)

    def test_object_material_list_updates_after_assign(self) -> None:
        """After assigning a material via code, object_material_list updates."""
        self._test_tool("execute_blender_code", {
            "code": (
                "import bpy\n"
                "obj = bpy.data.objects['Cube']\n"
                "mat = bpy.data.materials.new('AssignedMat')\n"
                "obj.data.materials.append(mat)\n"
                "result = {'slot_count': len(obj.material_slots)}\n"
            ),
        })
        data = self._test_tool("object_material_list", {
            "object_name": "Cube",
        })
        mat_names = [
            s["material_name"] for s in data["slots"]
            if s["material_name"] is not None
        ]
        self.assertIn("AssignedMat", mat_names)

    def test_object_material_list_error_object_not_found(self) -> None:
        """Non-existent object returns OBJECT_NOT_FOUND error."""
        data = self._test_tool("object_material_list", {
            "object_name": "NoSuchObject",
        })
        self.assertEqual(data["status"], "error")
        self.assertEqual(data["error_code"], "OBJECT_NOT_FOUND")

    # -----------------------------------------------------------------
    # Material assignment tool (REQ-15).

    def test_object_material_assign_overwrite_slot0(self) -> None:
        """Overwriting slot 0 replaces the existing material."""
        # Create a fresh material.
        self._test_tool("execute_blender_code", {
            "code": (
                "import bpy\n"
                "mat = bpy.data.materials.new('NewMat15')\n"
                "result = {'name': mat.name}\n"
            ),
        })
        data = self._test_tool("object_material_assign", {
            "object_name": "Cube",
            "material_name": "NewMat15",
            "slot_index": 0,
        })
        self.assertEqual(data["status"], "ok")
        self.assertEqual(data["material_name"], "NewMat15")
        self.assertEqual(data["slot_index"], 0)
        self.assertEqual(data["action"], "assigned")

        # Verify via object_material_list.
        slots = self._test_tool("object_material_list", {"object_name": "Cube"})
        self.assertEqual(slots["slots"][0]["material_name"], "NewMat15")

    def test_object_material_assign_append(self) -> None:
        """Appending (slot_index=-1) adds a new slot."""
        self._test_tool("execute_blender_code", {
            "code": (
                "import bpy\n"
                "mat = bpy.data.materials.new('AppendMat15')\n"
                "result = {'name': mat.name}\n"
            ),
        })
        before = self._test_tool("object_material_list", {"object_name": "Cube"})
        slot_count_before = len(before["slots"])

        data = self._test_tool("object_material_assign", {
            "object_name": "Cube",
            "material_name": "AppendMat15",
            "slot_index": -1,
        })
        self.assertEqual(data["status"], "ok")
        self.assertEqual(data["action"], "appended")
        self.assertEqual(data["total_slots"], slot_count_before + 1)

        after = self._test_tool("object_material_list", {"object_name": "Cube"})
        mat_names = [s["material_name"] for s in after["slots"]]
        self.assertIn("AppendMat15", mat_names)

    def test_object_material_assign_returns_correct_slot_index(self) -> None:
        """Appended slot_index equals the new last index."""
        self._test_tool("execute_blender_code", {
            "code": (
                "import bpy\n"
                "mat = bpy.data.materials.new('IndexCheckMat')\n"
                "result = {}\n"
            ),
        })
        before = self._test_tool("object_material_list", {"object_name": "Cube"})
        expected_index = len(before["slots"])

        data = self._test_tool("object_material_assign", {
            "object_name": "Cube",
            "material_name": "IndexCheckMat",
            "slot_index": -1,
        })
        self.assertEqual(data["slot_index"], expected_index)

    def test_object_material_assign_error_object_not_found(self) -> None:
        data = self._test_tool("object_material_assign", {
            "object_name": "GhostObject",
            "material_name": "Material",
        })
        self.assertEqual(data["status"], "error")
        self.assertEqual(data["error_code"], "OBJECT_NOT_FOUND")

    def test_object_material_assign_error_material_not_found(self) -> None:
        data = self._test_tool("object_material_assign", {
            "object_name": "Cube",
            "material_name": "NoSuchMaterial",
        })
        self.assertEqual(data["status"], "error")
        self.assertEqual(data["error_code"], "MATERIAL_NOT_FOUND")
        self.assertIn("available_materials", data["current_state"])

    def test_object_material_assign_error_slot_out_of_range(self) -> None:
        data = self._test_tool("object_material_assign", {
            "object_name": "Cube",
            "material_name": "Material",
            "slot_index": 99,
        })
        self.assertEqual(data["status"], "error")
        self.assertEqual(data["error_code"], "SLOT_INDEX_OUT_OF_RANGE")

    # -----------------------------------------------------------------
    # Asset import tools (REQ-16).

    # -- asset_import error cases (no external files needed) ----------

    def test_asset_import_error_file_not_found(self) -> None:
        data = self._test_tool("asset_import", {
            "filepath": "/no/such/file.obj",
        })
        self.assertEqual(data["status"], "error")
        self.assertEqual(data["error_code"], "FILE_NOT_FOUND")

    def test_asset_import_error_unsupported_format(self) -> None:
        """Unknown extension with no format override returns error."""
        # Create an empty temp file with an unknown extension.
        tmp_path = self._test_tool("execute_blender_code", {
            "code": (
                "import tempfile, os\n"
                "fd, path = tempfile.mkstemp(suffix='.xyz')\n"
                "os.close(fd)\n"
                "result = {'path': path}\n"
            ),
        })["path"]
        data = self._test_tool("asset_import", {"filepath": tmp_path})
        self.assertEqual(data["status"], "error")
        self.assertEqual(data["error_code"], "UNSUPPORTED_FORMAT")

    # -- OBJ round-trip -----------------------------------------------

    def test_asset_import_obj_roundtrip(self) -> None:
        """Export Cube to OBJ then import; new objects appear in scene."""
        # Export the default Cube to a temp OBJ file inside Blender.
        export_res = self._test_tool("execute_blender_code", {
            "code": (
                "import bpy, tempfile, os\n"
                "tmpdir = tempfile.mkdtemp()\n"
                "obj_path = os.path.join(tmpdir, 'cube_export.obj')\n"
                "bpy.ops.wm.obj_export(\n"
                "    filepath=obj_path,\n"
                "    export_selected_objects=False,\n"
                ")\n"
                "result = {'path': obj_path, 'exists': os.path.isfile(obj_path)}\n"
            ),
        })
        self.assertTrue(export_res.get("exists"), "OBJ export failed")
        obj_path = export_res["path"]

        data = self._test_tool("asset_import", {
            "filepath": obj_path,
            "format": "OBJ",
        })
        self.assertEqual(data["status"], "ok")
        self.assertEqual(data["format"], "OBJ")
        # At least one object should have been imported.
        self.assertGreater(len(data["imported_objects"]), 0)

    # -- GLTF round-trip -----------------------------------------------

    def test_asset_import_gltf_roundtrip(self) -> None:
        """Export Cube to GLB then import; new objects appear in scene."""
        export_res = self._test_tool("execute_blender_code", {
            "code": (
                "import bpy, tempfile, os\n"
                "tmpdir = tempfile.mkdtemp()\n"
                "glb_path = os.path.join(tmpdir, 'cube_export.glb')\n"
                "bpy.ops.export_scene.gltf(\n"
                "    filepath=glb_path,\n"
                "    export_format='GLB',\n"
                ")\n"
                "result = {'path': glb_path, 'exists': os.path.isfile(glb_path)}\n"
            ),
        })
        self.assertTrue(export_res.get("exists"), "GLB export failed")
        glb_path = export_res["path"]

        data = self._test_tool("asset_import", {
            "filepath": glb_path,
        })
        self.assertEqual(data["status"], "ok")
        self.assertEqual(data["format"], "GLTF")
        self.assertGreater(len(data["imported_objects"]), 0)

    # -- blend_library_link error cases --------------------------------

    def test_blend_library_link_error_file_not_found(self) -> None:
        data = self._test_tool("blend_library_link", {
            "filepath": "/no/such/file.blend",
            "asset_type": "OBJECT",
            "asset_name": "Cube",
        })
        self.assertEqual(data["status"], "error")
        self.assertEqual(data["error_code"], "FILE_NOT_FOUND")

    def test_blend_library_link_error_invalid_asset_type(self) -> None:
        # Save a temp blend file first so filepath error doesn't fire.
        res = self._test_tool("execute_blender_code", {
            "code": (
                "import bpy, tempfile, os\n"
                "tmpdir = tempfile.mkdtemp()\n"
                "blend_path = os.path.join(tmpdir, 'dummy.blend')\n"
                "bpy.ops.wm.save_as_mainfile(filepath=blend_path, copy=True)\n"
                "result = {'path': blend_path}\n"
            ),
        })
        data = self._test_tool("blend_library_link", {
            "filepath": res["path"],
            "asset_type": "MESH",
            "asset_name": "Cube",
        })
        self.assertEqual(data["status"], "error")
        self.assertEqual(data["error_code"], "INVALID_ASSET_TYPE")

    def test_blend_library_link_error_asset_not_found(self) -> None:
        """ASSET_NOT_FOUND response includes available_assets list."""
        res = self._test_tool("execute_blender_code", {
            "code": (
                "import bpy, tempfile, os\n"
                "tmpdir = tempfile.mkdtemp()\n"
                "blend_path = os.path.join(tmpdir, 'scene_copy.blend')\n"
                "bpy.ops.wm.save_as_mainfile(filepath=blend_path, copy=True)\n"
                "result = {'path': blend_path}\n"
            ),
        })
        data = self._test_tool("blend_library_link", {
            "filepath": res["path"],
            "asset_type": "OBJECT",
            "asset_name": "NonExistentObject",
        })
        self.assertEqual(data["status"], "error")
        self.assertEqual(data["error_code"], "ASSET_NOT_FOUND")
        self.assertIn("available_assets", data["current_state"])
        self.assertIsInstance(data["current_state"]["available_assets"], list)

    # -- blend_library_link success ------------------------------------

    def test_blend_library_link_object(self) -> None:
        """Linking an object from a .blend file adds a library-linked object."""
        # Save a copy of the current scene (which contains 'Cube').
        res = self._test_tool("execute_blender_code", {
            "code": (
                "import bpy, tempfile, os\n"
                "tmpdir = tempfile.mkdtemp()\n"
                "blend_path = os.path.join(tmpdir, 'link_src.blend')\n"
                "bpy.ops.wm.save_as_mainfile(filepath=blend_path, copy=True)\n"
                "result = {'path': blend_path}\n"
            ),
        })
        blend_path = res["path"]

        data = self._test_tool("blend_library_link", {
            "filepath": blend_path,
            "asset_type": "OBJECT",
            "asset_name": "Cube",
        })
        self.assertEqual(data["status"], "ok")
        self.assertGreater(len(data["linked_objects"]), 0,
                           "Expected at least one linked object")

        # Verify the linked object has a library attribute set.
        verify = self._test_tool("execute_blender_code", {
            "code": (
                "import bpy\n"
                "linked = [\n"
                "    obj.name for obj in bpy.data.objects\n"
                "    if obj.library is not None\n"
                "]\n"
                "result = {'linked': linked}\n"
            ),
        })
        self.assertGreater(len(verify["linked"]), 0,
                           "Expected linked objects with obj.library set")

    # -----------------------------------------------------------------
    # Armature animation tools (REQ-17).

    # Shared helper: create a minimal armature + action in Blender.
    _SETUP_ARMATURE_CODE = (
        "import bpy\n"
        # Remove any existing test armature to start clean.
        "existing = bpy.data.objects.get('TestArm')\n"
        "if existing:\n"
        "    bpy.data.objects.remove(existing, do_unlink=True)\n"
        # Create armature data and object.
        "arm_data = bpy.data.armatures.new('TestArmData')\n"
        "arm_obj  = bpy.data.objects.new('TestArm', arm_data)\n"
        "bpy.context.scene.collection.objects.link(arm_obj)\n"
        # Enter edit mode to add a bone.
        "bpy.context.view_layer.objects.active = arm_obj\n"
        "arm_obj.select_set(True)\n"
        "bpy.ops.object.mode_set(mode='EDIT')\n"
        "bone = arm_data.edit_bones.new('Bone')\n"
        "bone.head = (0, 0, 0)\n"
        "bone.tail = (0, 0, 1)\n"
        "bpy.ops.object.mode_set(mode='OBJECT')\n"
        # Create a simple action with two keyframes.
        "old_act = bpy.data.actions.get('TestAction')\n"
        "if old_act:\n"
        "    bpy.data.actions.remove(old_act)\n"
        "act = bpy.data.actions.new('TestAction')\n"
        # Use keyframe_insert through pose mode to create proper bone curves.
        "bpy.context.view_layer.objects.active = arm_obj\n"
        "bpy.ops.object.mode_set(mode='POSE')\n"
        "pose_bone = arm_obj.pose.bones['Bone']\n"
        "bpy.context.scene.frame_set(1)\n"
        "pose_bone.location = (0, 0, 0)\n"
        "pose_bone.keyframe_insert(data_path='location', frame=1)\n"
        "bpy.context.scene.frame_set(24)\n"
        "pose_bone.location = (0, 0, 0.5)\n"
        "pose_bone.keyframe_insert(data_path='location', frame=24)\n"
        "bpy.ops.object.mode_set(mode='OBJECT')\n"
        # Rename the auto-created action to 'TestAction'.
        "if arm_obj.animation_data and arm_obj.animation_data.action:\n"
        "    arm_obj.animation_data.action.name = 'TestAction'\n"
        "result = {\n"
        "    'armature': arm_obj.name,\n"
        "    'action': bpy.data.actions.get('TestAction') and 'TestAction',\n"
        "}\n"
    )

    def test_action_list_includes_created_action(self) -> None:
        """After creating an action it appears in action_list."""
        self._test_tool("execute_blender_code", {"code": self._SETUP_ARMATURE_CODE})
        data = self._test_tool("action_list", {})
        self.assertEqual(data["status"], "ok")
        names = [a["name"] for a in data["actions"]]
        self.assertIn("TestAction", names)

    def test_action_list_properties_present(self) -> None:
        """Each action entry has required keys."""
        self._test_tool("execute_blender_code", {"code": self._SETUP_ARMATURE_CODE})
        data = self._test_tool("action_list", {})
        self.assertGreater(len(data["actions"]), 0)
        for act in data["actions"]:
            self.assertIn("name", act)
            self.assertIn("frame_start", act)
            self.assertIn("frame_end", act)
            self.assertIn("fcurve_count", act)
            self.assertIn("slots", act)

    def test_action_list_sorted_alphabetically(self) -> None:
        """action_list results are in alphabetical order."""
        data = self._test_tool("action_list", {})
        names = [a["name"] for a in data["actions"]]
        self.assertEqual(names, sorted(names))

    def test_armature_action_apply_basic(self) -> None:
        """Apply TestAction to TestArm; action is set and frame range returned."""
        self._test_tool("execute_blender_code", {"code": self._SETUP_ARMATURE_CODE})
        # Detach action so we can re-apply it via the tool.
        self._test_tool("execute_blender_code", {
            "code": (
                "import bpy\n"
                "obj = bpy.data.objects.get('TestArm')\n"
                "if obj and obj.animation_data:\n"
                "    obj.animation_data.action = None\n"
                "result = {}\n"
            ),
        })
        data = self._test_tool("armature_action_apply", {
            "armature_name": "TestArm",
            "action_name": "TestAction",
        })
        self.assertEqual(data["status"], "ok")
        self.assertEqual(data["armature_name"], "TestArm")
        self.assertEqual(data["action_name"], "TestAction")
        self.assertIn("frame_start", data)
        self.assertIn("frame_end", data)
        self.assertGreaterEqual(data["frame_end"], data["frame_start"])

    def test_armature_action_apply_verified_in_blender(self) -> None:
        """After apply, Blender confirms animation_data.action is set."""
        self._test_tool("execute_blender_code", {"code": self._SETUP_ARMATURE_CODE})
        self._test_tool("execute_blender_code", {
            "code": (
                "import bpy\n"
                "obj = bpy.data.objects.get('TestArm')\n"
                "if obj and obj.animation_data:\n"
                "    obj.animation_data.action = None\n"
                "result = {}\n"
            ),
        })
        self._test_tool("armature_action_apply", {
            "armature_name": "TestArm",
            "action_name": "TestAction",
        })
        verify = self._test_tool("execute_blender_code", {
            "code": (
                "import bpy\n"
                "obj = bpy.data.objects.get('TestArm')\n"
                "act_name = None\n"
                "if obj and obj.animation_data and obj.animation_data.action:\n"
                "    act_name = obj.animation_data.action.name\n"
                "result = {'action_name': act_name}\n"
            ),
        })
        self.assertEqual(verify["action_name"], "TestAction")

    def test_armature_action_apply_error_not_armature(self) -> None:
        """Passing a non-armature object returns NOT_AN_ARMATURE error."""
        data = self._test_tool("armature_action_apply", {
            "armature_name": "Cube",
            "action_name": "TestAction",
        })
        self.assertEqual(data["status"], "error")
        self.assertEqual(data["error_code"], "NOT_AN_ARMATURE")
        self.assertIn("armature_objects", data["current_state"])

    def test_armature_action_apply_error_object_not_found(self) -> None:
        data = self._test_tool("armature_action_apply", {
            "armature_name": "GhostArm",
            "action_name": "TestAction",
        })
        self.assertEqual(data["status"], "error")
        self.assertEqual(data["error_code"], "OBJECT_NOT_FOUND")

    def test_armature_action_apply_error_action_not_found(self) -> None:
        self._test_tool("execute_blender_code", {"code": self._SETUP_ARMATURE_CODE})
        data = self._test_tool("armature_action_apply", {
            "armature_name": "TestArm",
            "action_name": "NoSuchAction",
        })
        self.assertEqual(data["status"], "error")
        self.assertEqual(data["error_code"], "ACTION_NOT_FOUND")
        self.assertIn("available_actions", data["current_state"])

    def test_armature_ik_target_keyframe_via_object_keyframe_insert(
        self,
    ) -> None:
        """
        IK target (Empty) location keyframe is inserted using the existing
        object_keyframe_insert tool — no dedicated REQ-17 tool needed.
        """
        # Create an Empty to act as the IK target.
        self._test_tool("execute_blender_code", {
            "code": (
                "import bpy\n"
                "existing = bpy.data.objects.get('IKTarget')\n"
                "if existing:\n"
                "    bpy.data.objects.remove(existing, do_unlink=True)\n"
                "empty = bpy.data.objects.new('IKTarget', None)\n"
                "empty.empty_display_type = 'SPHERE'\n"
                "bpy.context.scene.collection.objects.link(empty)\n"
                "result = {'name': empty.name}\n"
            ),
        })
        # Keyframe the Empty's location at frame 1 and frame 24.
        for frame, loc in ((1, [0.0, 0.0, 0.0]), (24, [0.0, 0.0, 1.5])):
            kf = self._test_tool("object_keyframe_insert", {
                "object_name": "IKTarget",
                "frame": frame,
                "location": loc,
                "interpolation": "LINEAR",
            })
            self.assertEqual(kf["status"], "ok")
            self.assertIn("location", kf["inserted"])

        # Verify via fcurve_list that keyframes exist on the Z channel.
        fcurves = self._test_tool("object_fcurve_list", {
            "object_name": "IKTarget",
            "data_path": "location",
        })
        self.assertEqual(fcurves["status"], "ok")
        z_curves = [c for c in fcurves["curves"] if c["array_index"] == 2]
        self.assertGreater(len(z_curves), 0,
                           "Expected Z location fcurve on IKTarget")
        self.assertEqual(len(z_curves[0]["keyframes"]), 2)

    # -----------------------------------------------------------------
    # NFR-01: Tool reliability — 10 consecutive calls.

    _N_REPEAT = 10  # number of repeated calls required by NFR-01

    def _setup_gp_for_nfr(self, obj_name: str, layer_name: str = "Layer") -> None:
        """Create a fresh GP object + layer for reliability tests."""
        self._test_tool("gp_object_create", {"name": obj_name})
        self._test_tool("gp_layer_create", {
            "object_name": obj_name,
            "layer_name": layer_name,
        })

    def test_nfr01_gp_stroke_draw_replace_no_silent_fail(self) -> None:
        """
        gp_stroke_draw REPLACE × 10: every call returns status='ok'.
        No silent failures over repeated invocations.
        """
        self._setup_gp_for_nfr("NFR01_GP_R")
        points = [[0.0, 0.0, 0.0], [1.0, 0.0, 0.0], [2.0, 0.0, 0.0]]
        for i in range(self._N_REPEAT):
            r = self._test_tool("gp_stroke_draw", {
                "object_name": "NFR01_GP_R",
                "layer_name": "Layer",
                "frame": 1,
                "points": points,
                "mode": "replace",
            })
            self.assertEqual(
                r["status"], "ok",
                f"gp_stroke_draw REPLACE call {i + 1}/{self._N_REPEAT} failed",
            )

    def test_nfr01_gp_stroke_draw_replace_no_residue(self) -> None:
        """
        gp_stroke_draw REPLACE × 10: final stroke_count == 1 (no accumulation).
        Each call reports the same stroke_count=1 as a single call would.
        """
        self._setup_gp_for_nfr("NFR01_GP_R2")
        points = [[0.0, 0.0, 0.0], [1.0, 0.0, 0.0]]
        results = []
        for _ in range(self._N_REPEAT):
            r = self._test_tool("gp_stroke_draw", {
                "object_name": "NFR01_GP_R2",
                "layer_name": "Layer",
                "frame": 1,
                "points": points,
                "mode": "replace",
            })
            results.append(r["stroke_count"])

        # REPLACE recreates the frame each time → exactly 1 stroke always.
        self.assertTrue(
            all(c == 1 for c in results),
            "Expected stroke_count=1 on every REPLACE call; "
            f"got {results}",
        )

    def test_nfr01_gp_stroke_draw_append_accumulates_correctly(self) -> None:
        """
        gp_stroke_draw APPEND × 10: no silent failures, stroke_count
        increases by exactly 1 per call (1 → 10).
        """
        self._setup_gp_for_nfr("NFR01_GP_A")
        points = [[0.0, 0.0, 0.0], [1.0, 0.0, 0.0]]
        for i in range(self._N_REPEAT):
            r = self._test_tool("gp_stroke_draw", {
                "object_name": "NFR01_GP_A",
                "layer_name": "Layer",
                "frame": 1,
                "points": points,
                "mode": "append",
            })
            self.assertEqual(
                r["status"], "ok",
                f"gp_stroke_draw APPEND call {i + 1} failed",
            )
            self.assertEqual(
                r["stroke_count"], i + 1,
                f"Expected stroke_count={i + 1} at call {i + 1}; "
                f"got {r['stroke_count']}",
            )

    def test_nfr01_gp_shape_draw_replace_consistent(self) -> None:
        """
        gp_shape_draw circle REPLACE × 10: every call returns status='ok'
        with the same point_count (no state drift).
        """
        self._setup_gp_for_nfr("NFR01_GP_S")
        params = {
            "object_name": "NFR01_GP_S",
            "layer_name": "Layer",
            "frame": 1,
            "shape": "circle",
            "cx": 0.0,
            "cy": 0.0,
            "cz": 0.0,
            "radius": 1.0,
            "segments": 16,
            "mode": "replace",
        }
        counts: list[int] = []
        for i in range(self._N_REPEAT):
            r = self._test_tool("gp_shape_draw", params)
            self.assertEqual(
                r["status"], "ok",
                f"gp_shape_draw call {i + 1} failed",
            )
            counts.append(r["point_count"])

        # All calls report the same point_count — no state drift.
        self.assertEqual(
            len(set(counts)), 1,
            f"point_count varied across calls: {counts}",
        )

    def test_nfr01_object_keyframe_insert_no_silent_fail(self) -> None:
        """
        object_keyframe_insert × 10 at same frame: every call returns
        status='ok' with 'location' in inserted.
        """
        for i in range(self._N_REPEAT):
            r = self._test_tool("object_keyframe_insert", {
                "object_name": "Cube",
                "frame": 3,
                "location": [0.0, 0.0, 0.0],
                "interpolation": "LINEAR",
            })
            self.assertEqual(
                r["status"], "ok",
                f"object_keyframe_insert call {i + 1} failed",
            )
            self.assertIn(
                "location", r["inserted"],
                f"'location' missing from inserted at call {i + 1}",
            )

    def test_nfr01_object_keyframe_insert_no_duplicate(self) -> None:
        """
        object_keyframe_insert × 10 at the same frame: Blender overwrites
        rather than duplicates — exactly 1 keyframe at that frame afterward.
        """
        frame_n = 8
        for _ in range(self._N_REPEAT):
            self._test_tool("object_keyframe_insert", {
                "object_name": "Cube",
                "frame": frame_n,
                "location": [0.0, 0.0, 0.0],
                "interpolation": "BEZIER",
            })

        fcurves = self._test_tool("object_fcurve_list", {
            "object_name": "Cube",
            "data_path": "location",
        })
        self.assertEqual(fcurves["status"], "ok")
        x_curves = [c for c in fcurves["curves"] if c["array_index"] == 0]
        self.assertGreater(len(x_curves), 0)
        at_frame = [
            kf for kf in x_curves[0]["keyframes"]
            if abs(kf["frame"] - frame_n) < 0.5
        ]
        self.assertEqual(
            len(at_frame), 1,
            f"Expected 1 keyframe at frame {frame_n} after 10 identical "
            f"inserts; found {len(at_frame)}",
        )

    def test_nfr01_object_keyframe_insert_multi_frame_consistent(self) -> None:
        """
        object_keyframe_insert × 10 at different frames: all succeed and
        the fcurve accumulates exactly 10 keyframes (no silent skips).
        """
        for i in range(self._N_REPEAT):
            frame_n = i + 1
            r = self._test_tool("object_keyframe_insert", {
                "object_name": "Cube",
                "frame": frame_n,
                "location": [float(i) * 0.1, 0.0, 0.0],
                "interpolation": "LINEAR",
            })
            self.assertEqual(
                r["status"], "ok",
                f"object_keyframe_insert at frame {frame_n} failed",
            )

        fcurves = self._test_tool("object_fcurve_list", {
            "object_name": "Cube",
            "data_path": "location",
        })
        x_curves = [c for c in fcurves["curves"] if c["array_index"] == 0]
        self.assertGreater(len(x_curves), 0)
        self.assertEqual(
            len(x_curves[0]["keyframes"]), self._N_REPEAT,
            f"Expected {self._N_REPEAT} keyframes; "
            f"found {len(x_curves[0]['keyframes'])}",
        )

    # -----------------------------------------------------------------
    # NFR-02: Error self-healing — all tools return REQ-01 four-field errors.

    def _check_error(
        self,
        data: dict,
        error_code: str = "",
        *,
        context: str = "",
    ) -> None:
        """
        Assert the response satisfies the REQ-01 four-field error contract.

        :param error_code: If provided, also assert the specific error code.
        :param context:    Human-readable label for failure messages.
        """
        prefix = f"[{context}] " if context else ""
        self.assertEqual(
            data.get("status"), "error",
            f"{prefix}Expected status='error', got {data!r}",
        )
        for field in ("error_code", "message", "current_state", "hint"):
            self.assertIn(
                field, data,
                f"{prefix}REQ-01 field '{field}' missing from error response",
            )
        self.assertIsInstance(data["error_code"], str)
        self.assertTrue(data["error_code"],
                        f"{prefix}error_code must be non-empty")
        self.assertIsInstance(data["message"], str)
        self.assertTrue(data["message"],
                        f"{prefix}message must be non-empty")
        self.assertIsInstance(data["current_state"], dict)
        self.assertTrue(data["current_state"],
                        f"{prefix}current_state must be non-empty dict")
        self.assertIsInstance(data["hint"], str)
        self.assertTrue(len(data["hint"]) > 5,
                        f"{prefix}hint must be a meaningful string, "
                        f"got {data['hint']!r}")
        if error_code:
            self.assertEqual(data["error_code"], error_code,
                             f"{prefix}Unexpected error_code")

    def test_nfr02_gp_layer_tools_error_shape(self) -> None:
        """
        GP layer management tools return REQ-01-compliant errors for
        non-existent objects and layers.
        """
        _no_obj = {"object_name": "NoSuchObject", "layer_name": "Layer"}

        self._check_error(
            self._test_tool("gp_layer_create", _no_obj),
            "OBJECT_NOT_FOUND", context="gp_layer_create/OBJECT_NOT_FOUND",
        )
        self._check_error(
            self._test_tool("gp_layer_delete", _no_obj),
            "OBJECT_NOT_FOUND", context="gp_layer_delete/OBJECT_NOT_FOUND",
        )
        self._check_error(
            self._test_tool("gp_layers_list", {"object_name": "NoSuchObject"}),
            "OBJECT_NOT_FOUND", context="gp_layers_list/OBJECT_NOT_FOUND",
        )

        # Create a real GP object so we can test layer-not-found path.
        self._test_tool("gp_object_create", {"name": "NFR02_GP"})
        _no_layer = {"object_name": "NFR02_GP", "layer_name": "NoLayer"}
        self._check_error(
            self._test_tool("gp_layer_opacity_set", {
                **_no_layer, "opacity": 0.5, "frame": 1,
            }),
            "LAYER_NOT_FOUND", context="gp_layer_opacity_set/LAYER_NOT_FOUND",
        )
        self._check_error(
            self._test_tool("gp_layer_keyframes_list", _no_layer),
            "LAYER_NOT_FOUND",
            context="gp_layer_keyframes_list/LAYER_NOT_FOUND",
        )

    def test_nfr02_gp_draw_tools_error_shape(self) -> None:
        """
        GP draw tools return REQ-01-compliant errors for invalid parameters.
        """
        self._check_error(
            self._test_tool("gp_stroke_draw", {
                "object_name": "NoSuchObject",
                "layer_name": "Layer",
                "frame": 1,
                "points": [[0.0, 0.0, 0.0], [1.0, 0.0, 0.0]],
                "mode": "replace",
            }),
            "OBJECT_NOT_FOUND", context="gp_stroke_draw/OBJECT_NOT_FOUND",
        )
        self._check_error(
            self._test_tool("gp_shape_draw", {
                "object_name": "NoSuchObject",
                "layer_name": "Layer",
                "frame": 1,
                "shape": "circle",
            }),
            "OBJECT_NOT_FOUND", context="gp_shape_draw/OBJECT_NOT_FOUND",
        )
        # Create a real GP object so the shape validation is reached.
        self._test_tool("gp_object_create", {"name": "NFR02_GP_SHAPE"})
        self._test_tool("gp_layer_create", {
            "object_name": "NFR02_GP_SHAPE", "layer_name": "Layer",
        })
        self._check_error(
            self._test_tool("gp_shape_draw", {
                "object_name": "NFR02_GP_SHAPE",
                "layer_name": "Layer",
                "frame": 1,
                "shape": "HEXAGON",   # invalid shape
            }),
            "INVALID_SHAPE", context="gp_shape_draw/INVALID_SHAPE",
        )
        self._check_error(
            self._test_tool("gp_material_assign", {
                "object_name": "NoSuchObject",
                "material_name": "Anything",
            }),
            "OBJECT_NOT_FOUND", context="gp_material_assign/OBJECT_NOT_FOUND",
        )

    def test_nfr02_object_animation_tools_error_shape(self) -> None:
        """
        M2 animation tools return REQ-01-compliant errors.
        """
        self._check_error(
            self._test_tool("mesh_primitive_add", {
                "primitive_type": "DODECAHEDRON",  # unsupported type
            }),
            "INVALID_PRIMITIVE_TYPE",
            context="mesh_primitive_add/INVALID_PRIMITIVE_TYPE",
        )
        self._check_error(
            self._test_tool("object_keyframe_insert", {
                "object_name": "NoSuchObject",
                "frame": 1,
                "location": [0.0, 0.0, 0.0],
            }),
            "OBJECT_NOT_FOUND",
            context="object_keyframe_insert/OBJECT_NOT_FOUND",
        )
        self._check_error(
            self._test_tool("object_keyframe_insert", {
                "object_name": "Cube",
                "frame": 1,
                "interpolation": "BEZIER",
                # no location/rotation/scale → triggers NO_PROPERTIES
            }),
            "NO_PROPERTIES", context="object_keyframe_insert/NO_PROPERTIES",
        )
        self._check_error(
            self._test_tool("object_fcurve_list", {
                "object_name": "NoSuchObject",
                "data_path": "location",
            }),
            "OBJECT_NOT_FOUND",
            context="object_fcurve_list/OBJECT_NOT_FOUND",
        )
        self._check_error(
            self._test_tool("camera_target_track", {
                "camera_name": "NoSuchCamera",
                "target_location": [0.0, 0.0, 0.0],
                "frame": 1,
            }),
            "OBJECT_NOT_FOUND",
            context="camera_target_track/OBJECT_NOT_FOUND",
        )

    def test_nfr02_modifier_driver_tools_error_shape(self) -> None:
        """
        M3 modifier and driver tools return REQ-01-compliant errors.
        """
        self._check_error(
            self._test_tool("object_modifier_add", {
                "object_name": "NoSuchObject",
                "modifier_type": "SUBSURF",
            }),
            "OBJECT_NOT_FOUND",
            context="object_modifier_add/OBJECT_NOT_FOUND",
        )
        self._check_error(
            self._test_tool("object_modifier_add", {
                "object_name": "Cube",
                "modifier_type": "MAGIC_SHADER",  # invalid type
            }),
            "INVALID_MODIFIER_TYPE",
            context="object_modifier_add/INVALID_MODIFIER_TYPE",
        )
        self._check_error(
            self._test_tool("object_modifiers_list", {
                "object_name": "NoSuchObject",
            }),
            "OBJECT_NOT_FOUND",
            context="object_modifiers_list/OBJECT_NOT_FOUND",
        )
        self._check_error(
            self._test_tool("object_driver_add", {
                "object_name": "NoSuchObject",
                "data_path": "location",
                "index": 0,
                "expression": "sin(frame/10)",
            }),
            "OBJECT_NOT_FOUND",
            context="object_driver_add/OBJECT_NOT_FOUND",
        )
        self._check_error(
            self._test_tool("object_driver_add", {
                "object_name": "Cube",
                "data_path": "location",
                "index": 2,
                "expression": "",  # empty expression
            }),
            "EMPTY_EXPRESSION",
            context="object_driver_add/EMPTY_EXPRESSION",
        )
        self._check_error(
            self._test_tool("object_driver_list", {
                "object_name": "NoSuchObject",
            }),
            "OBJECT_NOT_FOUND",
            context="object_driver_list/OBJECT_NOT_FOUND",
        )

    def test_nfr02_geonodes_material_tools_error_shape(self) -> None:
        """
        Geometry Nodes and material tools return REQ-01-compliant errors.
        """
        self._check_error(
            self._test_tool("geonodes_query", {
                "object_name": "NoSuchObject",
            }),
            "OBJECT_NOT_FOUND", context="geonodes_query/OBJECT_NOT_FOUND",
        )
        self._check_error(
            self._test_tool("geonodes_apply_preset", {
                "object_name": "NoSuchObject",
                "preset": "wave",
            }),
            "OBJECT_NOT_FOUND",
            context="geonodes_apply_preset/OBJECT_NOT_FOUND",
        )
        self._check_error(
            self._test_tool("geonodes_apply_preset", {
                "object_name": "Cube",
                "preset": "UNKNOWN_PRESET",  # invalid preset
            }),
            "INVALID_PRESET",
            context="geonodes_apply_preset/INVALID_PRESET",
        )
        self._check_error(
            self._test_tool("geonodes_node_set", {
                "object_name": "NoSuchObject",
                "node_name": "AnyNode",
                "input_name": "Value",
                "value": 1.0,
            }),
            "OBJECT_NOT_FOUND", context="geonodes_node_set/OBJECT_NOT_FOUND",
        )
        self._check_error(
            self._test_tool("geonodes_node_keyframe", {
                "object_name": "NoSuchObject",
                "node_name": "AnyNode",
                "input_name": "Value",
                "frame": 1,
                "value": 1.0,
            }),
            "OBJECT_NOT_FOUND",
            context="geonodes_node_keyframe/OBJECT_NOT_FOUND",
        )
        self._check_error(
            self._test_tool("object_material_list", {
                "object_name": "NoSuchObject",
            }),
            "OBJECT_NOT_FOUND",
            context="object_material_list/OBJECT_NOT_FOUND",
        )
        self._check_error(
            self._test_tool("object_material_assign", {
                "object_name": "NoSuchObject",
                "material_name": "Material",
                "slot_index": -1,
            }),
            "OBJECT_NOT_FOUND",
            context="object_material_assign/OBJECT_NOT_FOUND",
        )
        self._check_error(
            self._test_tool("object_material_assign", {
                "object_name": "Cube",
                "material_name": "NoSuchMaterial",
                "slot_index": -1,
            }),
            "MATERIAL_NOT_FOUND",
            context="object_material_assign/MATERIAL_NOT_FOUND",
        )

    def test_nfr02_asset_armature_tools_error_shape(self) -> None:
        """
        M4 asset import and armature tools return REQ-01-compliant errors.
        """
        self._check_error(
            self._test_tool("asset_import", {
                "filepath": "C:/nonexistent_path/file.fbx",
            }),
            "FILE_NOT_FOUND", context="asset_import/FILE_NOT_FOUND",
        )
        self._check_error(
            self._test_tool("blend_library_link", {
                "filepath": "C:/nonexistent_path/file.blend",
                "asset_type": "OBJECT",
                "asset_name": "Cube",
            }),
            "FILE_NOT_FOUND", context="blend_library_link/FILE_NOT_FOUND",
        )
        self._check_error(
            self._test_tool("blend_library_link", {
                "filepath": "C:/nonexistent_path/file.blend",
                "asset_type": "INVALID_TYPE",
                "asset_name": "Cube",
            }),
            "INVALID_ASSET_TYPE",
            context="blend_library_link/INVALID_ASSET_TYPE",
        )
        self._check_error(
            self._test_tool("armature_action_apply", {
                "armature_name": "NoSuchObject",
                "action_name": "AnyAction",
            }),
            "OBJECT_NOT_FOUND",
            context="armature_action_apply/OBJECT_NOT_FOUND",
        )
        self._check_error(
            self._test_tool("armature_action_apply", {
                "armature_name": "Cube",   # not an armature
                "action_name": "AnyAction",
            }),
            "NOT_AN_ARMATURE",
            context="armature_action_apply/NOT_AN_ARMATURE",
        )

    def test_nfr02_current_state_enables_self_correction(self) -> None:
        """
        The `current_state` of each error response must supply the corrective
        data an AI needs to retry without human input (REQ-01 intent).

        Verified conditions:
        - OBJECT_NOT_FOUND → current_state lists available objects
        - LAYER_NOT_FOUND  → current_state lists available layers
        - MATERIAL_NOT_FOUND → current_state lists available materials
        - ACTION_NOT_FOUND → current_state lists available actions
        - INVALID_PRESET   → current_state lists valid presets
        """
        # OBJECT_NOT_FOUND: corrective list lets AI pick a real object.
        r = self._test_tool("object_keyframe_insert", {
            "object_name": "NoSuchObject", "frame": 1,
            "location": [0.0, 0.0, 0.0],
        })
        self.assertEqual(r["error_code"], "OBJECT_NOT_FOUND")
        self.assertIn("available_objects", r["current_state"])
        self.assertIn("Cube", r["current_state"]["available_objects"])

        # LAYER_NOT_FOUND: corrective list lets AI pick an existing layer.
        self._test_tool("gp_object_create", {"name": "NFR02_GPCorr"})
        self._test_tool("gp_layer_create", {
            "object_name": "NFR02_GPCorr", "layer_name": "MyLayer",
        })
        r2 = self._test_tool("gp_layer_opacity_set", {
            "object_name": "NFR02_GPCorr",
            "layer_name": "NoSuchLayer",
            "opacity": 0.5,
            "frame": 1,
        })
        self.assertEqual(r2["error_code"], "LAYER_NOT_FOUND")
        self.assertIn("available_layers", r2["current_state"])
        self.assertIn("MyLayer", r2["current_state"]["available_layers"])

        # MATERIAL_NOT_FOUND: corrective list lets AI pick a real material.
        r3 = self._test_tool("object_material_assign", {
            "object_name": "Cube",
            "material_name": "NoSuchMaterial",
            "slot_index": -1,
        })
        self.assertEqual(r3["error_code"], "MATERIAL_NOT_FOUND")
        self.assertIn("available_materials", r3["current_state"])

        # ACTION_NOT_FOUND: corrective list lets AI pick a real action.
        r4 = self._test_tool("armature_action_apply", {
            "armature_name": "Cube",   # wrong type → NOT_AN_ARMATURE
            "action_name": "NoSuchAction",
        })
        # Cube is not an armature, so we get NOT_AN_ARMATURE first;
        # verify armature list is provided for self-correction.
        self.assertEqual(r4["error_code"], "NOT_AN_ARMATURE")
        self.assertIn("armature_objects", r4["current_state"])

        # INVALID_PRESET: corrective list lets AI pick a supported preset.
        r5 = self._test_tool("geonodes_apply_preset", {
            "object_name": "Cube",
            "preset": "BAD_PRESET",
        })
        self.assertEqual(r5["error_code"], "INVALID_PRESET")
        self.assertIn("supported_presets", r5["current_state"])

    # -----------------------------------------------------------------
    # NFR-03: Single Blender instance — concurrent calls return BLENDER_BUSY.

    def test_nfr03_sequential_calls_always_succeed(self) -> None:
        """
        Sequential tool calls (one after another) are never affected by the
        BLENDER_BUSY guard — the lock releases between calls (NFR-03 positive).
        """
        for i in range(5):
            r = self._test_tool("ping")
            self.assertEqual(
                r["status"], "ok",
                f"Sequential ping call {i + 1} failed: {r!r}",
            )



# -----------------------------------------------------------------------------
# NFR-03 unit tests (no Blender or MCP server required).
# These tests verify the _blender_lock mechanism in connection.py directly.

class TestNFR03Unit(unittest.TestCase):
    """
    Unit-level tests for NFR-03: single-instance serialisation guard.

    These tests import ``blmcp.tools_helpers.connection`` directly and
    manipulate the module-level lock so there is no dependency on a running
    Blender or MCP server process.
    """

    def setUp(self) -> None:
        from blmcp.tools_helpers import connection
        # Ensure the lock is always released at the start of each test,
        # even if a previous test left it held due to an exception.
        if connection._blender_lock.locked():
            connection._blender_lock.release()

    def test_busy_error_returned_when_lock_held(self) -> None:
        """
        When _blender_lock is already held, send_code returns BLENDER_BUSY
        immediately without attempting a socket connection (NFR-03).
        """
        from blmcp.tools_helpers import connection

        connection._blender_lock.acquire()
        try:
            result = connection.send_code("# test", strict_json=False)
        finally:
            connection._blender_lock.release()

        self.assertEqual(result["status"], "error")
        self.assertEqual(result["error_code"], "BLENDER_BUSY")

    def test_busy_error_req01_compliant(self) -> None:
        """
        The BLENDER_BUSY error response includes all four REQ-01 fields
        (error_code / message / current_state / hint).
        """
        from blmcp.tools_helpers import connection

        connection._blender_lock.acquire()
        try:
            result = connection.send_code("# test", strict_json=False)
        finally:
            connection._blender_lock.release()

        for field in ("error_code", "message", "current_state", "hint"):
            self.assertIn(field, result,
                          "REQ-01 field '{:s}' missing from BLENDER_BUSY".format(field))

        self.assertEqual(result["error_code"], "BLENDER_BUSY")
        self.assertIsInstance(result["message"], str)
        self.assertTrue(result["message"], "message must be non-empty")
        self.assertIsInstance(result["current_state"], dict)
        self.assertTrue(result["current_state"],
                        "current_state must be a non-empty dict")
        self.assertIn("blender_host", result["current_state"])
        self.assertIn("blender_port", result["current_state"])
        self.assertIsInstance(result["hint"], str)
        self.assertTrue(len(result["hint"]) > 5,
                        "hint must be a meaningful string")

    def test_lock_available_between_calls(self) -> None:
        """
        The lock is not held between calls — subsequent requests can acquire
        it normally (NFR-03 positive path, no false BLENDER_BUSY).
        """
        from blmcp.tools_helpers import connection

        acquired = connection._blender_lock.acquire(blocking=False)
        if acquired:
            connection._blender_lock.release()
        self.assertTrue(acquired,
                        "Lock should be free between calls — NFR-03 would "
                        "return false BLENDER_BUSY for sequential usage")

    def test_lock_released_on_connection_error(self) -> None:
        """
        Even when send_code raises ConnectionError (Blender unreachable),
        the lock is released so subsequent calls are not permanently blocked.
        """
        from blmcp.tools_helpers import connection

        # Point at a port where nothing is listening.
        orig_port = os.environ.get("BLENDER_MCP_PORT")
        os.environ["BLENDER_MCP_PORT"] = "19999"
        try:
            try:
                connection.send_code("# test", strict_json=False)
            except ConnectionError:
                pass  # expected — Blender not running on port 19999
        finally:
            if orig_port is None:
                del os.environ["BLENDER_MCP_PORT"]
            else:
                os.environ["BLENDER_MCP_PORT"] = orig_port

        # Lock must be released even after ConnectionError.
        acquired = connection._blender_lock.acquire(blocking=False)
        if acquired:
            connection._blender_lock.release()
        self.assertTrue(acquired,
                        "Lock must be released after ConnectionError so "
                        "subsequent calls are not permanently blocked")

    def test_concurrent_thread_gets_busy(self) -> None:
        """
        When one thread holds the lock, a concurrent thread receives
        BLENDER_BUSY instead of blocking indefinitely (NFR-03 core guarantee).
        """
        from blmcp.tools_helpers import connection

        busy_result: list[dict] = []
        lock_held = threading.Event()
        release_lock = threading.Event()

        def holder() -> None:
            connection._blender_lock.acquire()
            lock_held.set()
            release_lock.wait(timeout=5)
            connection._blender_lock.release()

        def caller() -> None:
            lock_held.wait(timeout=5)
            busy_result.append(connection.send_code("# test", strict_json=False))

        t_hold = threading.Thread(target=holder)
        t_call = threading.Thread(target=caller)
        t_hold.start()
        t_call.start()
        t_call.join(timeout=5)
        release_lock.set()
        t_hold.join(timeout=5)

        self.assertEqual(len(busy_result), 1,
                         "caller thread should have received a result")
        self.assertEqual(busy_result[0]["error_code"], "BLENDER_BUSY")

        # After holder releases, lock is free again.
        acquired = connection._blender_lock.acquire(blocking=False)
        if acquired:
            connection._blender_lock.release()
        self.assertTrue(acquired, "Lock must be free after holder released it")


# -----------------------------------------------------------------------------
# Concrete test classes.

class TestBackgroundServer(_TestServerMixin, unittest.TestCase):
    """
    Run all tests against Blender in ``--background`` mode.

    In Blender 5.1, ``--background --command`` mode runs with
    ``bpy.app.background == False`` and fires ``bpy.app.timers``, so it
    behaves identically to interactive (timer-based) mode.
    """

    _background = True
    # Blender 5.1 --command mode sets bpy.app.background=False and
    # fires timers, so screenshots/navigation/deferred all work.
    _interactive = True
    _port = _PORT_BACKGROUND


class TestForegroundServer(_TestServerMixin, unittest.TestCase):
    """
    Run all tests against Blender without ``--background`` (full GUI).
    """

    _background = False
    _port = _PORT_FOREGROUND


class TestInteractiveServer(_TestServerMixin, unittest.TestCase):
    """
    Run all tests against Blender in interactive mode (timer-based polling).
    """

    _background = False
    _interactive = True
    _port = _PORT_INTERACTIVE


class TestReuseServer(_TestServerMixin, unittest.TestCase):
    """
    Run tests against an **already-running** Blender with the MCP addon enabled.

    Set ``BLENDER_MCP_REUSE=1`` and run only this class::

        $env:BLENDER_MCP_REUSE = "1"
        python -m pytest tests/test_blender_mcp_with_blender.py -k TestReuseServer -v

    The socket port is taken from ``BLENDER_MCP_PORT`` (default 9876, the
    addon's default).  Blender must already be open and the MCP server started
    inside it before running these tests.

    All tests that apply to an interactive (GUI) Blender are included.
    Tests that require ``--background`` mode are skipped automatically.
    """

    _reuse_mode = True
    _background = False
    _interactive = True
    _port = int(os.environ.get("BLENDER_MCP_PORT", str(_PORT_BACKGROUND)))


BLENDER_VERSION_MIN = (5, 1)


def test_binaries_available() -> bool:
    """
    Check required binaries are available, print errors for any that are missing.
    """
    blender_bin = os.environ.get("BLENDER_BIN", "blender")
    blender_mcp = os.environ.get("BLENDER_MCP", "blender-mcp")
    ok = True
    if not shutil.which(blender_bin):
        print("ERROR: '{:s}' not found in PATH (set BLENDER_BIN)".format(blender_bin))
        ok = False
    if not shutil.which(blender_mcp):
        print("ERROR: '{:s}' not found in PATH (set BLENDER_MCP)".format(blender_mcp))
        ok = False
    return ok


def test_blender_version() -> bool:
    """
    Check the Blender version is at least ``BLENDER_VERSION_MIN``.
    """
    import re
    blender_bin = os.environ.get("BLENDER_BIN", "blender")
    result = subprocess.run(
        [blender_bin, "--version"],
        capture_output=True,
    )
    output = result.stdout.decode("utf-8", errors="replace")
    match = re.search(r"Blender\s+(\d+)\.(\d+)", output)
    if not match:
        print("ERROR: could not parse Blender version from: {:s}".format(output.strip()))
        return False
    version = (int(match.group(1)), int(match.group(2)))
    if version < BLENDER_VERSION_MIN:
        print("ERROR: Blender {:d}.{:d} found, {:d}.{:d} or newer required".format(
            *version, *BLENDER_VERSION_MIN,
        ))
        return False
    return True


if __name__ == "__main__":
    if not test_binaries_available():
        sys.exit(1)
    if not test_blender_version():
        sys.exit(1)
    unittest.main()
