# SPDX-FileCopyrightText: 2026 Blender Authors
#
# SPDX-License-Identifier: GPL-3.0-or-later

"""
Tool-code for assigning a GP material to a Grease Pencil object (GPv3).
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


class Result(NamedTuple):
    status: str
    object_name: str
    material_name: str
    slot_index: int


def _get_gp_object_names() -> list[str]:
    import bpy  # pylint: disable=import-error,no-name-in-module
    return sorted(
        obj.name for obj in bpy.data.objects if obj.type == "GREASEPENCIL"
    )


def _get_gp_material_names() -> list[str]:
    import bpy  # pylint: disable=import-error,no-name-in-module
    return sorted(m.name for m in bpy.data.materials if m.is_grease_pencil)


def main(params: Params) -> "Result | ErrorResult":
    import bpy  # pylint: disable=import-error,no-name-in-module

    obj = bpy.data.objects.get(params.object_name)
    if obj is None:
        return ErrorResult(
            status="error",
            error_code="OBJECT_NOT_FOUND",
            message="Object {!r} not found.".format(params.object_name),
            current_state={"available_gp_objects": _get_gp_object_names()},
            hint=(
                "Use `gp_object_create` to create a Grease Pencil object, "
                "or pick from `current_state.available_gp_objects`."
            ),
        )

    if obj.type != "GREASEPENCIL":
        return ErrorResult(
            status="error",
            error_code="INVALID_OBJECT_TYPE",
            message="Object {!r} is type {!r}, expected 'GREASEPENCIL'.".format(
                params.object_name, obj.type
            ),
            current_state={"available_gp_objects": _get_gp_object_names()},
            hint="Pick a Grease Pencil object from `current_state.available_gp_objects`.",
        )

    mat = bpy.data.materials.get(params.material_name)
    if mat is None:
        return ErrorResult(
            status="error",
            error_code="MATERIAL_NOT_FOUND",
            message="Material {!r} not found.".format(params.material_name),
            current_state={"available_gp_materials": _get_gp_material_names()},
            hint=(
                "Use `gp_material_create` to create a GP material first, "
                "or pick from `current_state.available_gp_materials`."
            ),
        )

    if not mat.is_grease_pencil:
        return ErrorResult(
            status="error",
            error_code="NOT_GP_MATERIAL",
            message="Material {!r} is not a Grease Pencil material.".format(
                params.material_name
            ),
            current_state={"available_gp_materials": _get_gp_material_names()},
            hint="Use `gp_material_create` to create a GP-compatible material.",
        )

    # Return existing slot index if material is already assigned.
    for i, slot in enumerate(obj.data.materials):
        if slot and slot.name == params.material_name:
            return Result(
                status="ok",
                object_name=obj.name,
                material_name=mat.name,
                slot_index=i,
            )

    obj.data.materials.append(mat)
    slot_index = len(obj.data.materials) - 1

    return Result(
        status="ok",
        object_name=obj.name,
        material_name=mat.name,
        slot_index=slot_index,
    )
