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
from blmcp.tools.gp_material_assign_toolcode import Params
from mcp.server.fastmcp import FastMCP  # pylint: disable=import-error,no-name-in-module
from mcp.types import ToolAnnotations  # pylint: disable=import-error,no-name-in-module

_TOOL_CALL = toolcode_wrap_with_calling_convention(toolcode_load_from_filepath(__file__))


def register(mcp: FastMCP) -> None:
    @mcp.tool(
        annotations=ToolAnnotations(
            title="Assign GP Material to Object",
            destructiveHint=True,
        )
    )
    def gp_material_assign(
        object_name: str,
        material_name: str,
    ) -> dict[str, object]:
        """
        Assign a Grease Pencil material to a GP object's material slots.

        If the material is already in a slot on ``object_name``, the
        existing ``slot_index`` is returned without creating a duplicate.
        Otherwise the material is appended to the end of the slot list.

        The returned ``slot_index`` (0-based) is the value to pass as
        ``material_index`` when calling ``gp_stroke_draw`` or
        ``gp_shape_draw``.

        Returns an error if the object is not found, is not a Grease
        Pencil object, or the material does not exist or is not a GP
        material (use ``gp_material_create`` to make one).
        """
        p = Params(object_name=object_name, material_name=material_name)
        return send_code(toolcode_format_call(_TOOL_CALL, p), strict_json=True)
