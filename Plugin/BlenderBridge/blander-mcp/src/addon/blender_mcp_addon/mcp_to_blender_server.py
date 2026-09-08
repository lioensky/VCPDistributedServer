# SPDX-FileCopyrightText: 2026 Blender Authors
#
# SPDX-License-Identifier: GPL-3.0-or-later

"""
Non-blocking TCP socket server that runs inside Blender.

Listens for null-byte-delimited JSON requests, executes Python code
directly in the calling thread, and returns JSON responses.
All socket operations are non-blocking so the server never blocks
Blender's main thread.
"""

__all__ = (
    "DEFAULT_HOST",
    "DEFAULT_PORT",
    "TIMER_INTERVAL_ACTIVE",
    "is_running",
    "poll",
    "poll_blocking",
    "start",
    "stop",
    "timer_idle_interval",
    "timer_idle_reset",
    "timer_internal_vars_calc",
    "use_log",
)

import json
import math
import select
import socket
import sys
import traceback
from collections.abc import Callable
from typing import NamedTuple

DEFAULT_HOST = "localhost"
DEFAULT_PORT = 9876

# Seconds between main-thread timer ticks.
TIMER_INTERVAL_ACTIVE = 0.05
# Seconds between main-thread timer ticks while idle (no pending work).
_TIMER_INTERVAL_IDLE = 1.0
# Seconds of inactivity before switching to the idle interval.
_TIMER_INTERVAL_IDLE_DELAY = 5.0


class _TimerState:
    """
    Mutable singleton holding timer-related runtime state.

    This is manipulated from the preferences and updated via ``timer_internal_vars_calc``.
    """

    __slots__ = (
        "interval_active",
        "interval_idle",
        "interval_idle_delay",
        "idle_countdown_reset",
        "idle_countdown",
        "client_timeout_countdown",
    )

    def __init__(self) -> None:
        self.interval_active: float = TIMER_INTERVAL_ACTIVE
        self.interval_idle: float = _TIMER_INTERVAL_IDLE
        self.interval_idle_delay: float = _TIMER_INTERVAL_IDLE_DELAY
        # Number of active-rate ticks before switching to idle.
        self.idle_countdown_reset: int = 0
        # Current countdown. When zero, `timer_idle_interval` returns idle.
        self.idle_countdown: int = 0
        # Poll ticks before an idle client is evicted.
        self.client_timeout_countdown: int = 2


_timer = _TimerState()


def timer_internal_vars_calc(
        active: float | None = None,
        idle: float | None = None,
        idle_delay: float | None = None,
) -> None:
    """
    Optionally update ``TIMER_*`` constants and recalculate internal variables.

    When keyword arguments are provided they replace the corresponding
    module-level ``TIMER_*`` value. Pass ``None`` (the default) to leave
    a value unchanged.
    """
    if active is not None:
        _timer.interval_active = active
    if idle is not None:
        _timer.interval_idle = idle
    if idle_delay is not None:
        _timer.interval_idle_delay = idle_delay
    # Round up so the delay is never shorter than requested.
    _timer.idle_countdown_reset = math.ceil(_timer.interval_idle_delay / _timer.interval_active)
    _timer.idle_countdown = _timer.idle_countdown_reset
    _timer.client_timeout_countdown = max(2, math.ceil(_CLIENT_TIMEOUT / _timer.interval_active))


def timer_idle_reset() -> None:
    """
    Signal that work was processed, resetting the idle countdown.
    """
    _timer.idle_countdown = _timer.idle_countdown_reset


def timer_idle_interval() -> float:
    """
    Return the appropriate timer interval, decrementing the idle countdown.

    Returns ``TIMER_INTERVAL_ACTIVE`` while the countdown is positive,
    then ``_TIMER_INTERVAL_IDLE`` once it reaches zero.
    """
    if _timer.idle_countdown > 0:
        _timer.idle_countdown -= 1
        return _timer.interval_active
    return _timer.interval_idle


# When True, print every request and response status to STDERR.
use_log: bool = False

_MAX_REQUEST_BYTES = 10 * 1024 * 1024  # 10 MiB.
# Maximum number of queued incoming connections.
_LISTEN_BACKLOG = 5
_RECV_BUFFER_SIZE = 4096
# Seconds before a client that has not sent a complete request is closed.
_CLIENT_TIMEOUT = 10.0
# How often `poll_blocking` checks for shutdown.
_POLL_BLOCKING_TIMEOUT = 1.0
_DEFERRED_UNSUPPORTED_MESSAGE = (
    "Deferred responses via `check_is_finished` are only supported "
    "by the interactive addon server, and are not available in "
    "background mode. Finish the request synchronously instead."
)

timer_internal_vars_calc()


# ---------------------------------------------------------------------------
# Client connection state.

class _Client:
    """
    Per-connection state for a client (the MCP server process) that has not yet sent a complete request.
    """

    __slots__ = (
        "conn",
        "buffer",
        "timeout",
    )

    def __init__(self, conn: socket.socket) -> None:
        self.conn: socket.socket = conn
        # Accumulates data until the null-byte delimiter is received.
        self.buffer: bytearray = bytearray()
        # Poll ticks remaining before this client is evicted.
        self.timeout: int = _timer.client_timeout_countdown


# ---------------------------------------------------------------------------
# Server state.

class _State:
    """
    Mutable singleton holding the runtime state of this socket server (the Blender add-on side).
    """

    __slots__ = (
        "sock",
        "clients",
    )

    def __init__(self) -> None:
        # The listening socket, or `None` when not running.
        self.sock: socket.socket | None = None
        # Connected clients that have not yet sent a complete request.
        self.clients: list[_Client] = []


_state = _State()


class _ExecResult(NamedTuple):
    """
    Result of executing tool-code.

    When *check_fn* is not ``None``, the caller must defer the response
    and poll the callable for completion (see ``deferred_tool``).
    Otherwise *response* is the final result to send.
    """

    response: dict[str, object]
    check_fn: Callable[[], dict[str, object] | None] | None = None


def _encode_response(response: dict[str, object]) -> bytes:
    """
    Serialize a response dict as null-byte-delimited JSON bytes.
    """
    return (json.dumps(response) + "\0").encode("utf-8")


def _execute_code(
        code: str,
        strict_json: bool,
) -> _ExecResult:
    """
    Execute *code* and return an ``_ExecResult``.

    :param strict_json: When true, the response *must* be serializable.
        Should always be true, when executing Python code we have full-control over,
        because any non-serializable data is effectively a bug.

        Only allow it to be false when executing arbitrary LLM generated code,
        in this case it's not worth the overhead of correcting the LLM mistake,
        just ``__repr__`` the value so it can fumble its way forward.
    """
    from .capture_output import CaptureOutput
    from .weak_sandbox import WeakSandboxForLLM

    namespace: dict[str, object] = {"result": {}}
    with CaptureOutput() as captured, WeakSandboxForLLM():
        try:
            exec(code, namespace)
        except Exception:  # pylint: disable=broad-exception-caught
            response: dict[str, object] = {"status": "error", "message": traceback.format_exc()}
            if captured.stdout:
                response["stdout"] = captured.stdout
            if captured.stderr:
                response["stderr"] = captured.stderr
            return _ExecResult(response)

    # Check for a deferred response (background job in progress).
    check_fn_raw = namespace.get("check_is_finished")
    if check_fn_raw is not None and callable(check_fn_raw):
        check_fn: Callable[[], dict[str, object] | None] = check_fn_raw
        response = {}
        if captured.stdout:
            response["stdout"] = captured.stdout
        if captured.stderr:
            response["stderr"] = captured.stderr
        return _ExecResult(response, check_fn)

    result = namespace["result"]
    if not isinstance(result, dict):
        response = {
            "status": "error",
            "message": (
                "The `result` variable must be a dict, not {:s}. "
                "Wrap your return value: `result = {{\"key\": value}}`"
            ).format(type(result).__name__),
        }
    else:
        # Guard against LLM-generated code storing non-serializable values
        # such as Blender objects, e.g. `result = {"obj": bpy.context.active_object}`.
        # Without this, `json.dumps` fails inside `_encode_response`.
        if strict_json:
            try:
                json.dumps(result)
            except (TypeError, ValueError) as ex:
                response = {
                    "status": "error",
                    "message": "The `result` value is not JSON-serializable: {:s}".format(str(ex)),
                }
            else:
                response = {"status": "ok", "result": result}
        else:
            # Use `repr` as a fallback so non-serializable objects
            # (e.g. Blender ID types) appear as their string representation.
            result = json.loads(json.dumps(result, default=repr))
            response = {"status": "ok", "result": result}
    if captured.stdout:
        response["stdout"] = captured.stdout
    if captured.stderr:
        response["stderr"] = captured.stderr
    return _ExecResult(response)


def _execute_code_from_request(
        data: bytes,
) -> tuple[_ExecResult, bool]:
    """
    Parse a raw request and execute it.

    Return ``(exec_result, strict_json)``.
    """

    # NOTE: This function is not expected to raise exceptions because we control the MCP server, tool-code and add-on.
    # If there is an error, it will be handled by the caller (the LLM will get the stack trace).
    #
    # Even so, if a tool is misbehaving, or a change in the code causes an error,
    # give a "helpful" response - to avoid the hassles of searching about for the root cause.

    # Invalid JSON is not expected since the MCP server serializes requests with `json.dumps`.
    # Any error should be rare, the "default" exception path is fine.
    request = json.loads(data)

    if request.get("type") != "execute":
        return _ExecResult({
            "status": "error",
            "message": "Unknown request type: {!r}".format(request.get("type")),
        }), False
    code = request.get("code", "")

    # Not expected in normal use, but a clear message beats a cryptic trace-back,
    # Also make it clear where the error should be addressed.
    strict_json = request.get("strict_json")
    if not isinstance(strict_json, bool):
        return (
            _ExecResult({
                "status": "error",
                "message": (
                    "Internal error: a blender_mcp tool sent a request without the required 'strict_json' boolean key. "
                    "This is a bug in the tool that generated this code"
                ),
            }),
            False,
        )

    if use_log:
        print("request:\n{:s}".format(code), file=sys.stderr)
    exec_result = _execute_code(code, strict_json=strict_json)
    if use_log:
        if exec_result.check_fn is not None:
            print("response: deferred", file=sys.stderr)
        else:
            print("response: {:s}".format(json.dumps(exec_result.response, indent=2)), file=sys.stderr)

    return exec_result, strict_json


def _close_client(client: _Client) -> None:
    """
    Close a client connection and remove it from the active list.
    """
    try:
        client.conn.close()
    except Exception:  # pylint: disable=broad-exception-caught
        pass
    try:
        _state.clients.remove(client)
    except ValueError:
        pass


# ---------------------------------------------------------------------------
# Polling (called from the execution modules).

def _accept_clients() -> None:
    """
    Accept all pending connections on the listening socket.
    """
    if _state.sock is None:
        return
    while True:
        try:
            conn, _addr = _state.sock.accept()
            conn.setblocking(False)
            _state.clients.append(_Client(conn))
        except BlockingIOError:
            break
        except OSError:
            break


def _service_clients() -> bool:
    """
    Read from all connected clients, execute complete requests.

    Return ``True`` if at least one request was executed.
    """
    did_work = False
    # Iterate over a copy since clients may be removed during the loop.
    for client in _state.clients[:]:
        # Evict clients that have not sent a complete request in time.
        client.timeout -= 1
        if client.timeout <= 0:
            try:
                err: dict[str, object] = {
                    "status": "error",
                    "message": "Client timed out",
                }
                client.conn.sendall(_encode_response(err))
            except OSError:
                pass
            _close_client(client)
            continue

        try:
            chunk = client.conn.recv(_RECV_BUFFER_SIZE)
        except BlockingIOError:
            # No data available yet.
            continue
        except OSError:
            _close_client(client)
            continue

        if not chunk:
            # Client disconnected.
            _close_client(client)
            continue

        client.buffer.extend(chunk)

        # Guard against unbounded input from a misbehaving client.
        if len(client.buffer) > _MAX_REQUEST_BYTES:
            try:
                err = {
                    "status": "error",
                    "message": "Request exceeds {:d} byte limit".format(_MAX_REQUEST_BYTES),
                }
                client.conn.sendall(_encode_response(err))
            except OSError:
                pass
            _close_client(client)
            continue

        if b"\0" not in client.buffer:
            # Request not yet complete.
            continue

        # Execute the request and send the response.
        request_data = bytes(client.buffer[:client.buffer.index(b"\0")])
        try:
            exec_result, strict_json = _execute_code_from_request(request_data)
        except Exception:  # pylint: disable=broad-exception-caught
            exec_result = _ExecResult({"status": "error", "message": traceback.format_exc()})
            strict_json = False

        if exec_result.check_fn is not None:
            # Deferred response: hand the connection to deferred_tool.
            from . import deferred_tool
            deferred_tool.add(
                client.conn,
                exec_result.check_fn,
                strict_json,
                str(exec_result.response.get("stdout", "")),
                str(exec_result.response.get("stderr", "")),
            )
            # Remove from clients without closing the socket.
            try:
                _state.clients.remove(client)
            except ValueError:
                pass
        else:
            try:
                client.conn.sendall(_encode_response(exec_result.response))
            except OSError:
                pass
            _close_client(client)
        did_work = True

    return did_work


def poll() -> bool:
    """
    Non-blocking poll: accept new connections, service existing clients,
    and check deferred responses.

    Return ``True`` if work was done or deferred clients are pending.
    """
    from . import deferred_tool
    _accept_clients()
    did_work = _service_clients()
    if deferred_tool.poll():
        did_work = True
    # Stay in active polling mode while deferred clients exist.
    if deferred_tool.has_pending():
        did_work = True
    return did_work


def _handle_blocking_client(conn: socket.socket) -> bool:
    """
    Handle a single client connection synchronously with blocking I/O.

    Return ``True`` if a request was executed.
    """
    conn.settimeout(_CLIENT_TIMEOUT)
    try:
        buf = bytearray()
        while b"\0" not in buf:
            chunk = conn.recv(_RECV_BUFFER_SIZE)
            if not chunk:
                # Client disconnected.
                return False
            buf.extend(chunk)
            if len(buf) > _MAX_REQUEST_BYTES:
                err: dict[str, object] = {
                    "status": "error",
                    "message": "Request exceeds {:d} byte limit".format(_MAX_REQUEST_BYTES),
                }
                conn.sendall(_encode_response(err))
                return False

        request_data = bytes(buf[:buf.index(b"\0")])
        try:
            exec_result, _strict_json = _execute_code_from_request(request_data)
            if exec_result.check_fn is not None:
                # Unpack to preserve stdout/stderr captured before the deferred handler was set up.
                response = {**exec_result.response, "status": "error", "message": _DEFERRED_UNSUPPORTED_MESSAGE}
                exec_result = _ExecResult(response)
        except Exception:  # pylint: disable=broad-exception-caught
            exec_result = _ExecResult({"status": "error", "message": traceback.format_exc()})
        conn.sendall(_encode_response(exec_result.response))
        return True
    except socket.timeout:
        try:
            err = {"status": "error", "message": "Client timed out"}
            conn.sendall(_encode_response(err))
        except OSError:
            pass
        return False
    except OSError:
        return False
    finally:
        conn.close()


def poll_blocking(timeout: float = _POLL_BLOCKING_TIMEOUT) -> bool:
    """
    Block until a connection arrives (up to *timeout* seconds), then
    handle it synchronously with blocking I/O.

    For use in background mode where the GUI is not running.
    Return ``True`` if a request was executed.
    """
    if _state.sock is None:
        return False

    try:
        readable, _writable, _errored = select.select([_state.sock], [], [], timeout)
    except (OSError, ValueError):
        return False

    if not readable:
        return False

    try:
        conn, _addr = _state.sock.accept()
    except (BlockingIOError, OSError):
        return False

    return _handle_blocking_client(conn)


# ---------------------------------------------------------------------------
# Public API.

def start(host: str, port: int) -> None:
    """
    Bind the listening socket and begin accepting connections.

    This does not block. The caller must arrange for ``poll`` to be
    called periodically (see ``execute_interactive`` and
    ``execute_blocking``).

    Callers should catch ``Exception`` broadly rather than specific types,
    since failures may be:
    - ``RuntimeError``, e.g. server already running.
    - ``OSError``, e.g. address already in use.
    ...other exceptions that are difficult to predict exhaustively.
    """
    if is_running():
        raise RuntimeError("Server is already running")

    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        sock.setblocking(False)
        sock.bind((host, port))
        sock.listen(_LISTEN_BACKLOG)
    except OSError:
        sock.close()
        raise

    _state.sock = sock


def stop() -> None:
    """
    Close the listening socket, all client connections, and deferred responses.
    """
    from . import deferred_tool

    sock = _state.sock
    _state.sock = None
    if sock is not None:
        try:
            sock.close()
        except Exception:  # pylint: disable=broad-exception-caught
            pass

    for client in _state.clients:
        try:
            client.conn.close()
        except Exception:  # pylint: disable=broad-exception-caught
            pass
    _state.clients.clear()

    deferred_tool.close_all()


def is_running() -> bool:
    """
    Return whether the server is currently listening.
    """
    return _state.sock is not None
