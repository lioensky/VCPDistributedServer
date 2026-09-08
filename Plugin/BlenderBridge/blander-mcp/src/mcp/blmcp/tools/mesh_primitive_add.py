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
from blmcp.tools.mesh_primitive_add_toolcode import Params
from mcp.server.fastmcp import FastMCP  # pylint: disable=import-error,no-name-in-module
from mcp.types import ToolAnnotations  # pylint: disable=import-error,no-name-in-module

_TOOL_CALL = toolcode_wrap_with_calling_convention(toolcode_load_from_filepath(__file__))


def register(mcp: FastMCP) -> None:
    @mcp.tool(
        annotations=ToolAnnotations(
            title="Add Mesh Primitive",
            destructiveHint=True,
        )
    )
    def mesh_primitive_add(
        primitive_type: str,
        name: str = "",
        location: list[float] | None = None,
    ) -> dict[str, object]:
        """
        Create a basic 3D mesh primitive in the active scene.

        ``primitive_type`` selects the geometry to create. Supported values:

        - ``"CUBE"``     — 2×2×2 cube centred at *location*
        - ``"SPHERE"``   — UV sphere with radius 1 at *location*
        - ``"PLANE"``    — 2×2 plane at *location*
        - ``"CYLINDER"`` — cylinder with radius 1 and height 2 at *location*

        ``name`` sets the object (and mesh data) name. If omitted Blender
        assigns a default name such as ``"Cube"``, ``"Sphere"``, etc.
        Blender automatically appends ``.001`` suffixes when a name is
        already taken; the returned ``name`` always reflects the actual name.

        ``location`` is ``[x, y, z]`` in world space (default ``[0, 0, 0]``).

        After creation, use ``get_object_detail_summary`` to inspect the
        object, or ``get_scene_state`` to list all scene objects.
        """
        p = Params(
            primitive_type=primitive_type,
            name=name,
            location=location if location is not None else [0.0, 0.0, 0.0],
        )
        return send_code(toolcode_format_call(_TOOL_CALL, p), strict_json=True)
