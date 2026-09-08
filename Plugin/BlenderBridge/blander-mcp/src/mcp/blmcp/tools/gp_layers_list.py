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
from blmcp.tools.gp_layers_list_toolcode import Params
from mcp.server.fastmcp import FastMCP  # pylint: disable=import-error,no-name-in-module
from mcp.types import ToolAnnotations  # pylint: disable=import-error,no-name-in-module

_TOOL_CALL = toolcode_wrap_with_calling_convention(toolcode_load_from_filepath(__file__))


def register(mcp: FastMCP) -> None:
    @mcp.tool(
        annotations=ToolAnnotations(
            title="List Grease Pencil Layers",
            readOnlyHint=True,
        )
    )
    def gp_layers_list(object_name: str) -> dict[str, object]:
        """
        Return all layers on a Grease Pencil object in their stack order.

        Each layer entry contains ``name``, ``opacity``, and ``hide``.
        Layers are listed top-to-bottom as they appear in Blender's
        layer panel (index 0 = topmost layer).

        Returns an error if the object is not found or is not a
        Grease Pencil object.
        """
        p = Params(object_name=object_name)
        return send_code(toolcode_format_call(_TOOL_CALL, p), strict_json=True)
