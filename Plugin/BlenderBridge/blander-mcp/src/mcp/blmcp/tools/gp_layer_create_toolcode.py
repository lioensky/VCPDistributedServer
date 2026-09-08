# SPDX-FileCopyrightText: 2026 Blender Authors
#
# SPDX-License-Identifier: GPL-3.0-or-later

"""
Tool-code for adding a layer to a Grease Pencil object.
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
    layer_name: str


class Result(NamedTuple):
    status: str
    object_name: str
    layer_name: str


def _get_gp_object_names() -> list[str]:
    import bpy  # pylint: disable=import-error,no-name-in-module
    return sorted(obj.name for obj in bpy.data.objects if obj.type == "GREASEPENCIL")


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
                "or pick a name from `current_state.available_gp_objects`."
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
            hint=(
                "Use `gp_object_create` to create a Grease Pencil object, "
                "or pick a name from `current_state.available_gp_objects`."
            ),
        )

    layer = obj.data.layers.new(params.layer_name)
    return Result(
        status="ok",
        object_name=obj.name,
        layer_name=layer.name,
    )
