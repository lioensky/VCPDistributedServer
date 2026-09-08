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
from blmcp.tools.object_material_list_toolcode import Params
from mcp.server.fastmcp import FastMCP  # pylint: disable=import-error,no-name-in-module
from mcp.types import ToolAnnotations  # pylint: disable=import-error,no-name-in-module

_TOOL_CALL = toolcode_wrap_with_calling_convention(toolcode_load_from_filepath(__file__))


def register(mcp: FastMCP) -> None:
    @mcp.tool(
        annotations=ToolAnnotations(title="List Object Material Slots",
                                    readOnlyHint=True)
    )
    def object_material_list(
        object_name: str,
    ) -> dict[str, object]:
        """
        Return the material slots of a scene object.

        Each entry in ``slots`` contains:

        - ``index``           — slot index (0-based)
        - ``material_name``   — material name, or ``null`` if the slot is empty
        - ``is_active``       — True for the currently active slot

        ``active_material_index`` is the index of the active slot.

        Use ``material_list`` to see all available materials in the scene.
        Use ``object_material_assign`` (REQ-15) to assign a material to a slot.
        """
        p = Params(object_name=object_name)
        return send_code(toolcode_format_call(_TOOL_CALL, p), strict_json=True)
