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
from blmcp.tools.material_list_toolcode import Params
from mcp.server.fastmcp import FastMCP  # pylint: disable=import-error,no-name-in-module
from mcp.types import ToolAnnotations  # pylint: disable=import-error,no-name-in-module

_TOOL_CALL = toolcode_wrap_with_calling_convention(toolcode_load_from_filepath(__file__))


def register(mcp: FastMCP) -> None:
    @mcp.tool(
        annotations=ToolAnnotations(title="List Scene Materials",
                                    readOnlyHint=True)
    )
    def material_list(
        include_grease_pencil: bool = False,
    ) -> dict[str, object]:
        """
        Return all materials stored in the current Blender file with their
        basic shading properties.

        Each entry in ``materials`` contains:

        - ``name``             — material name
        - ``use_nodes``        — whether node-based shading is enabled
        - ``is_grease_pencil`` — True for GP / annotation materials
        - ``diffuse_color``    — ``[R, G, B, A]`` from the material's
          base diffuse colour (always present)

        When ``use_nodes`` is True and a **Principled BSDF** node is found:

        - ``base_color``       — ``[R, G, B, A]`` from the Base Color input
        - ``metallic``         — float 0–1
        - ``roughness``        — float 0–1

        For Grease Pencil materials (when ``include_grease_pencil=True``):

        - ``stroke_color``     — ``[R, G, B, A]``
        - ``fill_color``       — ``[R, G, B, A]``
        - ``show_stroke``      — bool
        - ``show_fill``        — bool

        Results are sorted alphabetically by material name.
        """
        p = Params(include_grease_pencil=include_grease_pencil)
        return send_code(toolcode_format_call(_TOOL_CALL, p), strict_json=True)
