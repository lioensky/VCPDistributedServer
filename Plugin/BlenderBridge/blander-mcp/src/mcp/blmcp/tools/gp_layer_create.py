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
from blmcp.tools.gp_layer_create_toolcode import Params
from mcp.server.fastmcp import FastMCP  # pylint: disable=import-error,no-name-in-module
from mcp.types import ToolAnnotations  # pylint: disable=import-error,no-name-in-module

_TOOL_CALL = toolcode_wrap_with_calling_convention(toolcode_load_from_filepath(__file__))


def register(mcp: FastMCP) -> None:
    @mcp.tool(
        annotations=ToolAnnotations(
            title="Create Grease Pencil Layer",
            destructiveHint=True,
        )
    )
    def gp_layer_create(
        object_name: str,
        layer_name: str = "Layer",
    ) -> dict[str, object]:
        """
        Add a new layer to an existing Grease Pencil object.

        ``object_name`` must refer to a ``GREASEPENCIL`` type object
        already in the scene (use ``gp_object_create`` to create one).
        ``layer_name`` is the display name of the new layer.

        Returns an error if the object is not found or is not a
        Grease Pencil object. Duplicate layer names are allowed by
        Blender and are not treated as errors.
        """
        p = Params(object_name=object_name, layer_name=layer_name)
        return send_code(toolcode_format_call(_TOOL_CALL, p), strict_json=True)
