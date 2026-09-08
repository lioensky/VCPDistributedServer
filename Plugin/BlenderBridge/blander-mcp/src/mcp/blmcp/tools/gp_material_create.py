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
from blmcp.tools.gp_material_create_toolcode import Params
from mcp.server.fastmcp import FastMCP  # pylint: disable=import-error,no-name-in-module
from mcp.types import ToolAnnotations  # pylint: disable=import-error,no-name-in-module

_TOOL_CALL = toolcode_wrap_with_calling_convention(toolcode_load_from_filepath(__file__))


def register(mcp: FastMCP) -> None:
    @mcp.tool(
        annotations=ToolAnnotations(
            title="Create Grease Pencil Material",
            destructiveHint=True,
        )
    )
    def gp_material_create(
        name: str = "GPMaterial",
        stroke_color: list[float] = [0.0, 0.0, 0.0, 1.0],
        fill_color: list[float] = [1.0, 1.0, 1.0, 0.0],
    ) -> dict[str, object]:
        """
        Create a Grease Pencil material with stroke and fill colors (GPv3).

        Colors are RGBA lists with values in ``[0.0, 1.0]``:

        - ``stroke_color``: outline color, default opaque black
          ``[0.0, 0.0, 0.0, 1.0]``.
        - ``fill_color``: interior fill color, default fully transparent
          ``[1.0, 1.0, 1.0, 0.0]``.  Set alpha ``> 0`` to make fill
          visible.

        Blender uses **linear** color space internally; the values you
        provide are treated as linear, not sRGB.  Pure black
        ``[0, 0, 0, 1]`` and pure white ``[1, 1, 1, 1]`` are
        unaffected; intermediate colors will appear slightly different
        from sRGB equivalents.

        After creation, assign the material to a GP object with
        ``gp_material_assign``, then reference it by slot index when
        drawing strokes via ``gp_stroke_draw`` or ``gp_shape_draw``.

        The returned ``name`` is the actual name Blender assigned
        (may differ if a material with that name already exists).
        """
        p = Params(name=name, stroke_color=stroke_color, fill_color=fill_color)
        return send_code(toolcode_format_call(_TOOL_CALL, p), strict_json=True)
