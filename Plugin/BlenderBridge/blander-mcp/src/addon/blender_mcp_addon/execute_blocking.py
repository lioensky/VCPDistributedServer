# SPDX-FileCopyrightText: 2026 Blender Authors
#
# SPDX-License-Identifier: GPL-3.0-or-later

"""
Blocking execution loop for the MCP server.

Uses ``select`` to wait for socket activity, intended for use in
``blender --background`` mode where ``bpy.app.timers`` do not fire.

Background mode does not support deferred responses; requests must complete
before returning.
"""

__all__ = (
    "run",
)

from . import mcp_to_blender_server


def run() -> None:
    """
    Block polling client connections until the server stops.

    Catches ``KeyboardInterrupt`` so that Ctrl+C exits cleanly.
    """
    try:
        while mcp_to_blender_server.is_running():
            mcp_to_blender_server.poll_blocking()
    except KeyboardInterrupt:
        pass
