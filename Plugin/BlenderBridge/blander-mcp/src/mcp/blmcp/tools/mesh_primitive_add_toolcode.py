# SPDX-FileCopyrightText: 2026 Blender Authors
#
# SPDX-License-Identifier: GPL-3.0-or-later

"""
Tool-code for creating a basic 3D mesh primitive in the scene.
"""

__all__ = (
    "Params",
    "Result",
    "main",
)

from typing import NamedTuple

# @include_begin: _template_tool_error.py
# @include_end

_SUPPORTED_TYPES = ("CUBE", "SPHERE", "PLANE", "CYLINDER")


class Params(NamedTuple):
    primitive_type: str
    name: str
    location: list  # list[float], length 3


class Result(NamedTuple):
    status: str
    name: str
    primitive_type: str
    location: list  # list[float], length 3


def main(params: Params) -> "Result | ErrorResult":
    import bpy  # pylint: disable=import-error,no-name-in-module

    ptype = params.primitive_type.upper()
    if ptype not in _SUPPORTED_TYPES:
        return ErrorResult(
            status="error",
            error_code="INVALID_PRIMITIVE_TYPE",
            message=(
                "Primitive type {!r} is not supported.".format(params.primitive_type)
            ),
            current_state={"supported_types": list(_SUPPORTED_TYPES)},
            hint=(
                "Use one of the supported types: "
                + ", ".join(repr(t) for t in _SUPPORTED_TYPES)
                + "."
            ),
        )

    loc = tuple(params.location) if params.location else (0.0, 0.0, 0.0)

    if ptype == "CUBE":
        bpy.ops.mesh.primitive_cube_add(size=2.0, location=loc)
    elif ptype == "SPHERE":
        bpy.ops.mesh.primitive_uv_sphere_add(
            segments=32, ring_count=16, radius=1.0, location=loc,
        )
    elif ptype == "PLANE":
        bpy.ops.mesh.primitive_plane_add(size=2.0, location=loc)
    elif ptype == "CYLINDER":
        bpy.ops.mesh.primitive_cylinder_add(
            vertices=32, radius=1.0, depth=2.0, location=loc,
        )

    obj = bpy.context.active_object
    if params.name:
        obj.name = params.name
        obj.data.name = params.name

    actual_loc = list(obj.location)
    return Result(
        status="ok",
        name=obj.name,
        primitive_type=ptype,
        location=actual_loc,
    )
