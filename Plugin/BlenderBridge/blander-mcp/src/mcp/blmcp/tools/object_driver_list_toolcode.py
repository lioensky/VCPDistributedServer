# SPDX-FileCopyrightText: 2026 Blender Authors
#
# SPDX-License-Identifier: GPL-3.0-or-later

"""
Tool-code for listing drivers on a scene object.
"""

__all__ = (
    "Params",
    "Result",
    "main",
)

from typing import Any, NamedTuple

# @include_begin: _template_tool_error.py
# @include_end


class Params(NamedTuple):
    object_name: str


class Result(NamedTuple):
    status: str
    object_name: str
    # list of {"data_path", "index", "expression", "driver_type", "is_valid"}
    drivers: list[dict[str, Any]]


def _get_object_names() -> list[str]:
    import bpy  # pylint: disable=import-error,no-name-in-module
    return sorted(obj.name for obj in bpy.data.objects)


def main(params: Params) -> "Result | ErrorResult":
    import bpy  # pylint: disable=import-error,no-name-in-module

    obj = bpy.data.objects.get(params.object_name)
    if obj is None:
        return ErrorResult(
            status="error",
            error_code="OBJECT_NOT_FOUND",
            message="Object {!r} not found.".format(params.object_name),
            current_state={"available_objects": _get_object_names()},
            hint=(
                "Use `get_scene_state` to list objects, "
                "or `mesh_primitive_add` to create one."
            ),
        )

    drivers: list[dict[str, Any]] = []
    if obj.animation_data:
        for fc in obj.animation_data.drivers:
            drv = fc.driver
            drivers.append({
                "data_path": fc.data_path,
                "index": fc.array_index,
                "driver_type": drv.type,
                "expression": (
                    drv.expression if drv.type == "SCRIPTED" else ""
                ),
                "is_valid": drv.is_valid,
            })

    drivers.sort(key=lambda d: (d["data_path"], d["index"]))

    return Result(
        status="ok",
        object_name=obj.name,
        drivers=drivers,
    )
