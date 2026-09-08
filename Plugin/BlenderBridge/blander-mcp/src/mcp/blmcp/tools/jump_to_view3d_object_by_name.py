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
from blmcp.tools.jump_to_view3d_object_by_name_toolcode import Params
from mcp.server.fastmcp import FastMCP  # pylint: disable=import-error,no-name-in-module
from mcp.types import ToolAnnotations  # pylint: disable=import-error,no-name-in-module

_TOOL_CALL = toolcode_wrap_with_calling_convention(toolcode_load_from_filepath(__file__))


def register(mcp: FastMCP) -> None:
    @mcp.tool(
        annotations=ToolAnnotations(
            title="Focus on Object",
            destructiveHint=True,
        )
    )
    def jump_to_view3d_object_by_name(
        name: str,
        allow_edits: bool = False,
    ) -> dict[str, object]:
        """
        Move the 3D viewport to focus on an object by *name*.

        If *allow_edits* is True the object may be un-hidden and its
        collections enabled to make it visible.
        """
        p = Params(name=name, allow_edits=allow_edits)
        code = toolcode_format_call(_TOOL_CALL, p)
        return send_code(code, strict_json=True)
