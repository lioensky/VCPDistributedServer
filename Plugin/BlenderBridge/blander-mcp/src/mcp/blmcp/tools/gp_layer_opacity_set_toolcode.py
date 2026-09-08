# SPDX-FileCopyrightText: 2026 Blender Authors
#
# SPDX-License-Identifier: GPL-3.0-or-later

"""
Tool-code for setting a Grease Pencil layer opacity keyframe (GPv3).
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
    frame: int
    opacity: float


class Result(NamedTuple):
    status: str
    object_name: str
    layer_name: str
    frame: int
    opacity: float


def _get_gp_object_names() -> list[str]:
    import bpy  # pylint: disable=import-error,no-name-in-module
    return sorted(
        obj.name for obj in bpy.data.objects if obj.type == "GREASEPENCIL"
    )


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

    layer = obj.data.layers.get(params.layer_name)
    if layer is None:
        available = [la.name for la in obj.data.layers]
        return ErrorResult(
            status="error",
            error_code="LAYER_NOT_FOUND",
            message="Layer {!r} not found on object {!r}.".format(
                params.layer_name, params.object_name
            ),
            current_state={"available_layers": available},
            hint=(
                "Use `gp_layer_create` to create a layer, "
                "or pick from `current_state.available_layers`."
            ),
        )

    if not (0.0 <= params.opacity <= 1.0):
        return ErrorResult(
            status="error",
            error_code="INVALID_OPACITY",
            message="opacity must be in [0.0, 1.0], got {}.".format(params.opacity),
            current_state={"current_opacity": layer.opacity},
            hint="Use 0.0 for fully transparent and 1.0 for fully opaque.",
        )

    layer.opacity = params.opacity
    layer.keyframe_insert(data_path="opacity", frame=params.frame)

    return Result(
        status="ok",
        object_name=obj.name,
        layer_name=layer.name,
        frame=params.frame,
        opacity=layer.opacity,
    )
