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
from blmcp.tools.gp_stroke_draw_toolcode import Params
from mcp.server.fastmcp import FastMCP  # pylint: disable=import-error,no-name-in-module
from mcp.types import ToolAnnotations  # pylint: disable=import-error,no-name-in-module

_TOOL_CALL = toolcode_wrap_with_calling_convention(toolcode_load_from_filepath(__file__))


def register(mcp: FastMCP) -> None:
    @mcp.tool(
        annotations=ToolAnnotations(
            title="Draw Grease Pencil Stroke",
            destructiveHint=True,
        )
    )
    def gp_stroke_draw(
        object_name: str,
        layer_name: str,
        frame: int,
        points: list[list[float]],
        mode: str = "replace",
        stroke_radius: float = 0.01,
        material_index: int = 0,
    ) -> dict[str, object]:
        """
        Draw a stroke on a Grease Pencil layer at the given frame (GPv3).

        ``points`` is a list of ``[x, y, z]`` coordinates defining the
        stroke path. Provide two points for a straight line; three or more
        for a curve or polyline. Blender uses a right-hand coordinate system:
        X right, Y into the screen, Z up. For 2D animation draw in the XZ
        plane (Y = 0) and place the camera along -Y.

        ``mode`` controls existing strokes on that frame:

        - ``"replace"``: clears all existing strokes before drawing.
        - ``"append"``: adds the new stroke alongside existing ones.

        ``stroke_radius`` is the point radius in object-space units; it
        controls stroke thickness (default ``0.01``).

        ``material_index`` selects the GP material slot (0-based).

        The frame is created automatically if it does not exist.
        Returns an error if the object, layer, mode, or points are invalid.
        """
        p = Params(
            object_name=object_name,
            layer_name=layer_name,
            frame=frame,
            points=points,
            mode=mode,
            stroke_radius=stroke_radius,
            material_index=material_index,
        )
        return send_code(toolcode_format_call(_TOOL_CALL, p), strict_json=True)
