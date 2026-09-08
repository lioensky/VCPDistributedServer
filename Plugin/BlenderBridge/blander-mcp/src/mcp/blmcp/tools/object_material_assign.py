# SPDX-FileCopyrightText: 2026 Blender Authors
#
# SPDX-License-Identifier: GPL-3.0-or-later

# pylint: disable=C0114  # See tool doc-string.

__all__ = ("register",)

from blmcp.tools_helpers import (
    toolcode_format_call,
    toolcode_load_from_filepath,
    toolcode_wrap_with_calling_convention,
)
from blmcp.tools_helpers.connection import send_code
from blmcp.tools.object_material_assign_toolcode import Params
from mcp.server.fastmcp import FastMCP  # pylint: disable=import-error,no-name-in-module
from mcp.types import ToolAnnotations  # pylint: disable=import-error,no-name-in-module

_TOOL_CALL = toolcode_wrap_with_calling_convention(toolcode_load_from_filepath(__file__))


def register(mcp: FastMCP) -> None:
    @mcp.tool(
        annotations=ToolAnnotations(title="Assign Material to Object",
                                    destructiveHint=True)
    )
    def object_material_assign(
        object_name: str,
        material_name: str,
        slot_index: int = -1,
    ) -> dict[str, object]:
        """
        Assign an existing material to a scene object's material slot.

        ``material_name`` must already exist in ``bpy.data.materials``.
        Use ``material_list`` to find available materials.

        ``slot_index`` controls which slot receives the material:

        - ``-1`` (default) — append a new slot and assign the material there.
        - ``0, 1, …``      — overwrite the material at that slot index.

        Returns ``slot_index`` (the final slot index used), ``action``
        (``"appended"`` or ``"assigned"``), and ``total_slots`` after the
        operation.

        Use ``object_material_list`` to verify the result.
        """
        p = Params(
            object_name=object_name,
            material_name=material_name,
            slot_index=slot_index,
        )
        return send_code(toolcode_format_call(_TOOL_CALL, p), strict_json=True)
