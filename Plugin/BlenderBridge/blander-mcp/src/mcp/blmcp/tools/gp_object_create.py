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
from blmcp.tools.gp_object_create_toolcode import Params
from mcp.server.fastmcp import FastMCP  # pylint: disable=import-error,no-name-in-module
from mcp.types import ToolAnnotations  # pylint: disable=import-error,no-name-in-module

_TOOL_CALL = toolcode_wrap_with_calling_convention(toolcode_load_from_filepath(__file__))


def register(mcp: FastMCP) -> None:
    @mcp.tool(
        annotations=ToolAnnotations(
            title="Create Grease Pencil Object",
            destructiveHint=True,
        )
    )
    def gp_object_create(name: str = "GreasePencil") -> dict[str, object]:
        """
        Create a new Grease Pencil object in the active scene.

        Blender deduplicates names automatically: if an object named
        ``name`` already exists, the new object receives a ``.001`` suffix
        (or the next available number). The returned ``name`` field always
        reflects the actual name assigned by Blender.

        The object is linked to the scene's root collection.
        Call ``gp_layer_create`` next to add at least one drawing layer.
        """
        p = Params(name=name)
        return send_code(toolcode_format_call(_TOOL_CALL, p), strict_json=True)
