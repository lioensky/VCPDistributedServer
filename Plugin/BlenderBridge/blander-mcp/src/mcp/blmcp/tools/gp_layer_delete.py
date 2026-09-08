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
from blmcp.tools.gp_layer_delete_toolcode import Params
from mcp.server.fastmcp import FastMCP  # pylint: disable=import-error,no-name-in-module
from mcp.types import ToolAnnotations  # pylint: disable=import-error,no-name-in-module

_TOOL_CALL = toolcode_wrap_with_calling_convention(toolcode_load_from_filepath(__file__))


def register(mcp: FastMCP) -> None:
    @mcp.tool(
        annotations=ToolAnnotations(
            title="Delete Grease Pencil Layer",
            destructiveHint=True,
        )
    )
    def gp_layer_delete(
        object_name: str,
        layer_name: str,
    ) -> dict[str, object]:
        """
        Remove a layer from a Grease Pencil object.

        All strokes and keyframes stored on the layer are permanently
        deleted. Use ``gp_layers_list`` first to verify the layer name.

        Returns an error if the object or layer is not found.
        """
        p = Params(object_name=object_name, layer_name=layer_name)
        return send_code(toolcode_format_call(_TOOL_CALL, p), strict_json=True)
