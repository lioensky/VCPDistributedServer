# SPDX-FileCopyrightText: 2026 Blender Authors
#
# SPDX-License-Identifier: GPL-3.0-or-later

"""
Simple synchronous MCP client for testing.

Speaks newline-delimited JSON-RPC 2.0 over stdio to a subprocess.
Supports concurrent calls from multiple threads via per-request queue routing.
"""

__all__ = (
    "MCPClient",
)

import json
import os
import queue
import subprocess
import threading
import time
from typing import Any, Self

# Scale all timeouts (e.g. `GLOBAL_TIMEOUT_SCALE=2` doubles every limit).
_TIMEOUT_SCALE = float(os.environ.get("GLOBAL_TIMEOUT_SCALE", "1"))

# Per-request timeout in seconds.
_REQUEST_TIMEOUT = int(30 * _TIMEOUT_SCALE)

# Maximum time to wait for a local process to respond or exit (seconds).
_TIMEOUT_LOCAL_PROC = int(5 * _TIMEOUT_SCALE)


class MCPClient:
    """
    Synchronous MCP client that communicates via stdin/stdout with a subprocess.

    Thread-safe: multiple threads may call :meth:`call_tool` concurrently.
    Responses are routed to their originating thread by request id so that
    concurrent in-flight requests do not interfere with each other.
    """

    def __init__(
        self,
        command: list[str],
        env: dict[str, str] | None = None,
    ) -> None:
        self._proc = subprocess.Popen(
            command,
            stdin=subprocess.PIPE,
            stdout=subprocess.PIPE,
            env=env,
        )
        self._next_id = 1
        self._id_lock = threading.Lock()
        self._write_lock = threading.Lock()

        # Per-request response queues keyed by request id.
        self._response_queues: dict[int, queue.Queue[dict[str, Any] | None]] = {}
        self._response_lock = threading.Lock()

        # Fallback queue for messages that arrive without a matching pending id
        # (e.g. server-initiated notifications).
        self._line_queue: queue.Queue[bytes | None] = queue.Queue()

        self._reader_thread = threading.Thread(
            target=self._read_stdout, daemon=True,
        )
        self._reader_thread.start()

    def _read_stdout(self) -> None:
        assert self._proc.stdout is not None
        try:
            for line in self._proc.stdout:
                stripped = line.strip()
                if not stripped:
                    continue
                try:
                    response = json.loads(stripped)
                    req_id = response.get("id")
                    if req_id is not None:
                        with self._response_lock:
                            q = self._response_queues.get(req_id)
                        if q is not None:
                            q.put(response)
                            continue
                except json.JSONDecodeError:
                    pass
                # Notifications and unrouted messages go to the fallback queue.
                self._line_queue.put(line)
        finally:
            # Unblock all waiting threads.
            with self._response_lock:
                for q in self._response_queues.values():
                    q.put(None)
            self._line_queue.put(None)

    def _send_request(
        self,
        method: str,
        params: dict[str, object] | None = None,
        timeout: int | None = None,
    ) -> dict[str, Any]:
        """
        Send a JSON-RPC request and wait for the matching response.

        *timeout* overrides the default ``_REQUEST_TIMEOUT`` for this call.
        """
        effective_timeout = timeout if timeout is not None else _REQUEST_TIMEOUT

        with self._id_lock:
            request_id = self._next_id
            self._next_id += 1

        response_queue: queue.Queue[dict[str, Any] | None] = queue.Queue(maxsize=1)
        with self._response_lock:
            self._response_queues[request_id] = response_queue

        msg: dict[str, object] = {
            "jsonrpc": "2.0",
            "id": request_id,
            "method": method,
        }
        if params is not None:
            msg["params"] = params

        assert self._proc.stdin is not None

        data = json.dumps(msg) + "\n"
        with self._write_lock:
            self._proc.stdin.write(data.encode("utf-8"))
            self._proc.stdin.flush()

        try:
            deadline = time.monotonic() + effective_timeout
            remaining = max(0.1, deadline - time.monotonic())
            try:
                response = response_queue.get(timeout=remaining)
            except queue.Empty:
                raise RuntimeError(
                    "Timeout ({:d}s) waiting for response to {:s}".format(
                        effective_timeout, method,
                    )
                )
            if response is None:
                raise RuntimeError("MCP server closed stdout unexpectedly")
            if "error" in response:
                raise RuntimeError("JSON-RPC error: {!r}".format(response["error"]))
            return response.get("result", {})
        finally:
            with self._response_lock:
                self._response_queues.pop(request_id, None)

    def _send_notification(
        self,
        method: str,
        params: dict[str, object] | None = None,
    ) -> None:
        """
        Send a JSON-RPC notification (no id, no response expected).
        """
        msg: dict[str, object] = {
            "jsonrpc": "2.0",
            "method": method,
        }
        if params is not None:
            msg["params"] = params

        assert self._proc.stdin is not None

        data = json.dumps(msg) + "\n"
        with self._write_lock:
            self._proc.stdin.write(data.encode("utf-8"))
            self._proc.stdin.flush()

    def initialize(self) -> dict[str, Any]:
        """
        Perform the MCP initialize handshake.
        """
        result = self._send_request("initialize", {
            "protocolVersion": "2024-11-05",
            "capabilities": {},
            "clientInfo": {"name": "test-client", "version": "0.1.0"},
        })
        self._send_notification("notifications/initialized")
        return result

    def list_tools(self) -> list[str]:
        """
        Return the names of all tools the server exposes.
        """
        result = self._send_request("tools/list")
        return [t["name"] for t in result.get("tools", [])]

    def call_tool(
        self,
        name: str,
        arguments: dict[str, object] | None = None,
        timeout: int | None = None,
    ) -> dict[str, Any]:
        """
        Call an MCP tool by name and return the result.

        *timeout* overrides the default per-request timeout for slow tools
        such as those that launch ``blender --background``.
        """
        params: dict[str, object] = {"name": name}
        if arguments is not None:
            params["arguments"] = arguments
        return self._send_request("tools/call", params, timeout=timeout)

    def close(self) -> None:
        """
        Close the connection and terminate the subprocess.
        """
        if self._proc.stdin is not None:
            self._proc.stdin.close()
        if self._proc.stdout is not None:
            self._proc.stdout.close()
        self._proc.terminate()
        try:
            self._proc.wait(timeout=_TIMEOUT_LOCAL_PROC)
        except subprocess.TimeoutExpired:
            self._proc.kill()
            self._proc.wait(timeout=_TIMEOUT_LOCAL_PROC)

    def __enter__(self) -> Self:
        return self

    def __exit__(self, *args: object) -> None:
        self.close()
