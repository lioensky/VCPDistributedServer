# SPDX-FileCopyrightText: 2026 Blender Authors
#
# SPDX-License-Identifier: GPL-3.0-or-later

"""
Tool-code for focusing the 3D viewport on an object.
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
    name: str
    allow_edits: bool


class Result(NamedTuple):
    status: str
    object: str
    type: str
    location: list[float]
    message: str | None = None


def main(params: Params) -> "Result | ErrorResult":
    import bpy  # pylint: disable=import-error,no-name-in-module

    if bpy.app.background:
        return ErrorResult(
            status="error",
            error_code="BACKGROUND_MODE",
            message="Not available in background mode.",
            current_state={},
            hint="Rerun with an interactive Blender session.",
        )
    if bpy.context.window is None:
        return ErrorResult(
            status="error",
            error_code="NO_ACTIVE_WINDOW",
            message="No active window.",
            current_state={},
            hint="Ensure Blender has a visible window.",
        )

    obj = bpy.data.objects.get(params.name)
    if obj is None:
        available = sorted(bpy.data.objects.keys())
        return ErrorResult(
            status="error",
            error_code="OBJECT_NOT_FOUND",
            message="Object {!r} not found.".format(params.name),
            current_state={"available_objects": available},
            hint=(
                "Call `get_objects_summary` to see all objects, "
                "then retry with a name from `current_state.available_objects`."
            ),
        )

    if params.allow_edits:
        if obj.hide_viewport:
            obj.hide_viewport = False
        if obj.hide_get():
            obj.hide_set(False)

        def _enable_collections(layer_col: Any, target: Any) -> bool:
            found = False
            for child in layer_col.children:
                if _enable_collections(child, target):
                    found = True
            if target.name in layer_col.collection.objects:
                found = True
            if found:
                layer_col.exclude = False
                layer_col.hide_viewport = False
            return found

        _enable_collections(bpy.context.view_layer.layer_collection, obj)

    if bpy.context.mode != "OBJECT":
        bpy.ops.object.mode_set(mode="OBJECT")

    bpy.ops.object.select_all(action="DESELECT")
    obj.select_set(True)
    bpy.context.view_layer.objects.active = obj

    view3d_found = False
    for area in bpy.context.screen.areas:
        if area.type == "VIEW_3D":
            view3d_found = True
            r3d = area.spaces.active.region_3d
            if r3d and r3d.view_perspective == "CAMERA":
                r3d.view_perspective = "PERSP"
            for region in area.regions:
                if region.type == "WINDOW":
                    with bpy.context.temp_override(area=area, region=region):
                        bpy.ops.view3d.view_selected()
                    break
            break

    return Result(
        status="ok",
        object=params.name,
        type=obj.type,
        location=list(obj.location),
        message=None if view3d_found else (
            "No 3D viewport found, object selected but not framed"
        ),
    )
