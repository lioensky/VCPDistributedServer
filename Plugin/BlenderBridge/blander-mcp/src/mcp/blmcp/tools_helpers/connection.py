# SPDX-FileCopyrightText: 2026 Blender Authors
#
# SPDX-License-Identifier: GPL-3.0-or-later

"""
Socket client for communicating with the Blender add-on.

Used by MCP "tools" that send-code to the Blender add-on.
"""

__all__ = (
    "get_connection_params",
    "send_code",
)

import json
import os
import socket
import threading

_DEFAULT_HOST = "localhost"
_DEFAULT_PORT = 9876
_TIMEOUT = 300.0
_RECV_BUFFER_SIZE = 65536

# Serialises access to the single Blender socket.  Only one tool call may
# talk to Blender at a time; a second concurrent attempt returns an
# explicit BLENDER_BUSY error instead of silently queuing (NFR-03).
_blender_lock = threading.Lock()


def get_connection_params() -> tuple[str, int]:
    host = os.environ.get("BLENDER_MCP_HOST", _DEFAULT_HOST)
    port = int(os.environ.get("BLENDER_MCP_PORT", str(_DEFAULT_PORT)))
    return host, port


def send_code(code: str, strict_json: bool) -> dict[str, object]:
    """
    Send Python code to the Blender add-on socket server for execution.

    Returns the full response dict from the add-on containing
    ``status`` (``"ok"`` or ``"error"``), ``result`` (on success),
    ``message`` (on error), and optionally ``stdout``/``stderr``
    captured during execution.

    When another call is already in progress, returns a structured
    ``BLENDER_BUSY`` error without blocking (NFR-03).

    Raises ``ConnectionError`` when Blender is unreachable or
    returns an invalid response.
    """
    host, port = get_connection_params()

    if not _blender_lock.acquire(blocking=False):
        return {
            "status": "error",
            "error_code": "BLENDER_BUSY",
            "message": (
                "Blender at {:s}:{:d} is already processing another request. "
                "Only one concurrent connection is supported.".format(host, port)
            ),
            "current_state": {
                "blender_host": host,
                "blender_port": port,
            },
            "hint": (
                "Retry this call after the current operation completes. "
                "Sequential tool calls are fully supported."
            ),
        }

    try:
        request = json.dumps({
            "type": "execute",
            "code": code,
            "strict_json": strict_json,
        }) + "\0"

        try:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
                sock.settimeout(_TIMEOUT)
                sock.connect((host, port))
                sock.sendall(request.encode("utf-8"))

                # Read response until the null byte delimiter.
                buf = bytearray()
                while True:
                    chunk = sock.recv(_RECV_BUFFER_SIZE)
                    if not chunk:
                        break
                    buf.extend(chunk)
                    if b"\0" in buf:
                        break
        except ConnectionRefusedError as ex:
            raise ConnectionError(
                "Cannot connect to Blender at {:s}:{:d}. "
                "Ensure Blender is running with the MCP addon enabled and the server started.".format(
                    host, port,
                )
            ) from ex
        except socket.timeout as ex:
            raise ConnectionError(
                "Blender connection timed out at {:s}:{:d}".format(host, port)
            ) from ex
        except OSError as ex:
            # NOTE: intentionally not catching `Exception` here.
            # Callers use `ConnectionError` to trigger a fallback path;
            # a broader catch would mask real bugs as connection failures.
            raise ConnectionError(
                "Socket error communicating with Blender at {:s}:{:d}: {:s}".format(
                    host, port, str(ex),
                )
            ) from ex

        if not buf:
            raise ConnectionError("Empty response from Blender")

        # Parse only up to the first null byte delimiter.
        line, _sep, _rest = buf.partition(b"\0")
        try:
            response: dict[str, object] = json.loads(line.decode("utf-8"))
        except (json.JSONDecodeError, UnicodeDecodeError) as ex:
            raise ConnectionError(
                "Invalid response from Blender at {:s}:{:d}: {:s}".format(
                    host, port, str(ex),
                )
            ) from ex
        return response
    finally:
        _blender_lock.release()
