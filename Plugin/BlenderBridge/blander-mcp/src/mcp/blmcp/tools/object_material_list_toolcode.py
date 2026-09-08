# SPDX-FileCopyrightText: 2026 Blender Authors
#
# SPDX-License-Identifier: GPL-3.0-or-later

"""
Tool-code for querying the material slots of a specific scene object.
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
    active_material_index: int
    slots: list[dict[str, Any]]


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
            hint="Use `get_scene_state` to list objects.",
        )

    active_index = getattr(obj, "active_material_index", 0) or 0

    slots: list[dict[str, Any]] = []
    for idx, slot in enumerate(obj.material_slots):
        mat = slot.material
        slots.append({
            "index": idx,
            "material_name": mat.name if mat is not None else None,
            "is_active": idx == active_index,
        })

    return Result(
        status="ok",
        object_name=obj.name,
        active_material_index=active_index,
        slots=slots,
    )
