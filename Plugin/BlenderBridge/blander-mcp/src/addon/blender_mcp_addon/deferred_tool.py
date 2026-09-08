# SPDX-FileCopyrightText: 2026 Blender Authors
#
# SPDX-License-Identifier: GPL-3.0-or-later

"""
Deferred response handling for Blender background jobs.

When tool-code starts a background job (e.g. rendering with
``INVOKE_DEFAULT``), the response cannot be sent immediately. This
module holds the client connection open and polls a checker callable
until the operation completes, then sends the result.

The checker (``check_fn``) is called on the server's standard timer
which starts at an active interval but backs off when idle.

Checkers should be lightweight (e.g. check a flag or file existence)
so they don't block the UI, yet return promptly so the user is not left waiting after the job finishes.

"""

__all__ = (
    "add",
    "close_all",
    "has_pending",
    "poll",
)

import json
import socket
import time
import traceback
from collections.abc import Callable

from .mcp_to_blender_server import _encode_response

# Total wall-time in seconds allowed for a background task (e.g. rendering) to complete.
# When exceeded, an error response is sent and the connection is closed.
# The background task itself continues to run in Blender.
# One hour is long for what should typically be an interactive experience,
# but renders can take a long time and it's not desirable for them to simply give up.
_DEFERRED_TIMEOUT = (60.0 * 60.0)


class _DeferredClient:
    """
    A client connection waiting for a background job to complete.
    """

    __slots__ = (
        "conn",
        "check_fn",
        "strict_json",
        "stdout",
        "stderr",
        "deadline",
    )

    def __init__(
        self,
        conn: socket.socket,
        check_fn: Callable[[], dict[str, object] | None],
        strict_json: bool,
        stdout: str,
        stderr: str,
    ) -> None:
        self.conn: socket.socket = conn
        self.check_fn: Callable[[], dict[str, object] | None] = check_fn
        self.strict_json: bool = strict_json
        self.stdout: str = stdout
        self.stderr: str = stderr
        self.deadline: float = time.monotonic() + _DEFERRED_TIMEOUT


# Connections waiting for a background job to finish, polled each timer tick.
_deferred_clients: list[_DeferredClient] = []


def _send_and_close(dc: _DeferredClient, response: dict[str, object]) -> None:
    try:
        dc.conn.sendall(_encode_response(response))
    except OSError:
        pass
    try:
        dc.conn.close()
    except OSError:
        pass
    try:
        _deferred_clients.remove(dc)
    except ValueError:
        pass


def _is_disconnected(conn: socket.socket) -> bool:
    """
    Return ``True`` if the remote end has closed the connection.
    """
    try:
        data = conn.recv(1, socket.MSG_PEEK)
        # Empty data means the peer closed the connection.
        return len(data) == 0
    except BlockingIOError:
        # No data available - connection is still alive.
        return False
    except OSError:
        return True


def add(
    conn: socket.socket,
    check_fn: Callable[[], dict[str, object] | None],
    strict_json: bool,
    stdout: str,
    stderr: str,
) -> None:
    """
    Register a deferred client to be polled for completion.
    """
    _deferred_clients.append(_DeferredClient(conn, check_fn, strict_json, stdout, stderr))


def poll() -> bool:
    """
    Check all deferred clients for completion.

    Return ``True`` if at least one client was resolved or removed.
    """
    did_work = False
    for dc in _deferred_clients[:]:
        # Check for client disconnection.
        if _is_disconnected(dc.conn):
            try:
                dc.conn.close()
            except OSError:
                pass
            try:
                _deferred_clients.remove(dc)
            except ValueError:
                pass
            did_work = True
            continue

        # Check for timeout.
        if time.monotonic() > dc.deadline:
            _send_and_close(dc, {
                "status": "error",
                "message": "Deferred operation timed out after {:.0f} seconds".format(_DEFERRED_TIMEOUT),
            })
            did_work = True
            continue

        # Call the checker.
        try:
            result = dc.check_fn()
        except Exception:  # pylint: disable=broad-exception-caught
            _send_and_close(dc, {
                "status": "error",
                "message": traceback.format_exc(),
            })
            did_work = True
            continue

        if result is None:
            # Still pending.
            continue

        if not isinstance(result, dict):
            _send_and_close(dc, {
                "status": "error",
                "message": "check_is_finished must return None or dict, not {:s}".format(
                    type(result).__name__,
                ),
            })
            did_work = True
            continue

        # Validate JSON serializability when strict_json is set.
        if dc.strict_json:
            try:
                json.dumps(result)
            except (TypeError, ValueError) as ex:
                _send_and_close(dc, {
                    "status": "error",
                    "message": "Deferred result is not JSON-serializable: {:s}".format(str(ex)),
                })
                did_work = True
                continue

        # Build the final response with the standard envelope.
        response: dict[str, object] = {"status": "ok", "result": result}
        if dc.stdout:
            response["stdout"] = dc.stdout
        if dc.stderr:
            response["stderr"] = dc.stderr
        _send_and_close(dc, response)
        did_work = True

    return did_work


def has_pending() -> bool:
    """
    Return ``True`` if there are deferred clients awaiting completion.
    """
    return bool(_deferred_clients)


def close_all() -> None:
    """
    Close all deferred client connections without sending responses.
    """
    for dc in _deferred_clients:
        try:
            dc.conn.close()
        except OSError:
            pass
    _deferred_clients.clear()
