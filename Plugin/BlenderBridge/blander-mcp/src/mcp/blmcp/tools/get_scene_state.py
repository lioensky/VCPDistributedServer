# SPDX-FileCopyrightText: 2026 Blender Authors
#
# SPDX-License-Identifier: GPL-3.0-or-later

# pylint: disable=C0114  # See tool doc-string.

__all__ = (
    "register",
)

from blmcp.tools_helpers import (
    toolcode_format_call,
    toolcode_load_from_filepath,
    toolcode_wrap_with_calling_convention,
)
from blmcp.tools_helpers.connection import send_code
from mcp.server.fastmcp import FastMCP  # pylint: disable=import-error,no-name-in-module
from mcp.types import ToolAnnotations  # pylint: disable=import-error,no-name-in-module

_TOOL_CALL = toolcode_wrap_with_calling_convention(toolcode_load_from_filepath(__file__))


def register(mcp: FastMCP) -> None:
    @mcp.tool(
        annotations=ToolAnnotations(
            title="Get Scene State",
            readOnlyHint=True,
        )
    )
    def get_scene_state() -> dict[str, object]:
        """
        Return the current scene's timeline parameters and a flat list of
        all objects with their name, type, and world-space location.

        Includes ``frame_start``, ``frame_end``, ``frame_current``, and
        ``fps`` so the AI can plan keyframe placement without a separate
        query. Works in both background and interactive Blender sessions.

        Call this at the start of any animation workflow to understand
        the scene layout and timeline before issuing further tool calls.
        """
        return send_code(toolcode_format_call(_TOOL_CALL, None), strict_json=True)
