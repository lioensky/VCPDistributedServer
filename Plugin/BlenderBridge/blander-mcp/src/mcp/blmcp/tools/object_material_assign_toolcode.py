# SPDX-FileCopyrightText: 2026 Blender Authors
#
# SPDX-License-Identifier: GPL-3.0-or-later

"""
Tool-code for assigning a material to a scene object's material slot.
"""

__all__ = (
    "Params",
    "Result",
    "main",
)

from typing import NamedTuple

# @include_begin: _template_tool_error.py
# @include_end


class Params(NamedTuple):
    object_name: str
    material_name: str
    slot_index: int     # -1 = append a new slot; >= 0 = overwrite that slot


class Result(NamedTuple):
    status: str
    object_name: str
    material_name: str
    slot_index: int
    action: str         # "appended" | "assigned"
    total_slots: int


def _get_object_names() -> list[str]:
    import bpy  # pylint: disable=import-error,no-name-in-module
    return sorted(obj.name for obj in bpy.data.objects)


def _get_material_names() -> list[str]:
    import bpy  # pylint: disable=import-error,no-name-in-module
    return sorted(m.name for m in bpy.data.materials)


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

    mat = bpy.data.materials.get(params.material_name)
    if mat is None:
        return ErrorResult(
            status="error",
            error_code="MATERIAL_NOT_FOUND",
            message="Material {!r} not found.".format(params.material_name),
            current_state={"available_materials": _get_material_names()},
            hint=(
                "Use `material_list` to see available materials. "
                "Create one first if needed."
            ),
        )

    # Objects that carry geometry support material assignment via .data.materials.
    # For objects without data.materials (e.g. lights, cameras) fall back to
    # material_slots which is still writable.
    data_mats = getattr(getattr(obj, "data", None), "materials", None)

    if params.slot_index < 0:
        # Append mode: add a new slot.
        if data_mats is not None:
            data_mats.append(mat)
        else:
            return ErrorResult(
                status="error",
                error_code="CANNOT_APPEND_SLOT",
                message=(
                    "Object {!r} (type {!r}) does not support appending "
                    "material slots.".format(params.object_name, obj.type)
                ),
                current_state={},
                hint=(
                    "Only mesh, curve, surface, and volume objects support "
                    "material slots. Use slot_index >= 0 to overwrite an "
                    "existing slot if one is present."
                ),
            )
        final_index = len(obj.material_slots) - 1
        action = "appended"
    else:
        # Overwrite mode.
        slot_count = len(obj.material_slots)
        if params.slot_index >= slot_count:
            return ErrorResult(
                status="error",
                error_code="SLOT_INDEX_OUT_OF_RANGE",
                message=(
                    "Slot index {:d} is out of range; object {!r} has "
                    "{:d} slot(s).".format(
                        params.slot_index, params.object_name, slot_count,
                    )
                ),
                current_state={"total_slots": slot_count},
                hint=(
                    "Use slot_index=-1 to append a new slot, or pick an "
                    "index in 0..{:d}.".format(max(0, slot_count - 1))
                ),
            )
        if data_mats is not None:
            data_mats[params.slot_index] = mat
        else:
            obj.material_slots[params.slot_index].material = mat
        final_index = params.slot_index
        action = "assigned"

    return Result(
        status="ok",
        object_name=obj.name,
        material_name=mat.name,
        slot_index=final_index,
        action=action,
        total_slots=len(obj.material_slots),
    )
