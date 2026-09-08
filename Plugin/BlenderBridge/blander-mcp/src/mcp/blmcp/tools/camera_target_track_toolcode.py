# SPDX-FileCopyrightText: 2026 Blender Authors
#
# SPDX-License-Identifier: GPL-3.0-or-later

"""
Tool-code for setting up a camera Track-To target and keying its position.
"""

__all__ = (
    "Params",
    "Result",
    "main",
)

from typing import NamedTuple

# @include_begin: _template_tool_error.py
# @include_end

_VALID_INTERPOLATIONS = ("BEZIER", "LINEAR", "CONSTANT")


class Params(NamedTuple):
    # "" means use the scene camera.
    camera_name: str
    # "" means auto-generate "{camera_name}_Target".
    target_name: str
    # [] means don't change the target's location.
    target_location: list   # list[float] len 3, or []
    # -1 means don't insert a keyframe.
    frame: int
    interpolation: str


class Result(NamedTuple):
    status: str
    camera_name: str
    target_name: str
    constraint_name: str
    # -1 if no keyframe was inserted.
    frame: int


def _iter_action_fcurves(action: object, slot: object) -> "object":
    """Yield F-curves, handling both legacy and layered actions."""
    fcurves_direct = getattr(action, "fcurves", None)
    if fcurves_direct is not None:
        yield from fcurves_direct
        return
    for _layer in getattr(action, "layers", ()):
        for _strip in getattr(_layer, "strips", ()):
            _cb = None
            if slot is not None and hasattr(_strip, "channelbag_for_slot"):
                try:
                    _cb = _strip.channelbag_for_slot(slot)
                except Exception:  # pylint: disable=broad-exception-caught
                    pass
            if _cb is not None:
                yield from getattr(_cb, "fcurves", ())
            else:
                for _cb2 in getattr(_strip, "channelbags", ()):
                    yield from getattr(_cb2, "fcurves", ())


def _get_camera_names() -> list[str]:
    import bpy  # pylint: disable=import-error,no-name-in-module
    return sorted(obj.name for obj in bpy.data.objects if obj.type == "CAMERA")


def main(params: Params) -> "Result | ErrorResult":
    import bpy  # pylint: disable=import-error,no-name-in-module

    # Resolve camera object.
    if params.camera_name:
        cam_obj = bpy.data.objects.get(params.camera_name)
        if cam_obj is None:
            return ErrorResult(
                status="error",
                error_code="OBJECT_NOT_FOUND",
                message="Object {!r} not found.".format(params.camera_name),
                current_state={"available_cameras": _get_camera_names()},
                hint=(
                    "Pick a camera from `current_state.available_cameras`, "
                    "or leave `camera_name` empty to use the active scene camera."
                ),
            )
        if cam_obj.type != "CAMERA":
            return ErrorResult(
                status="error",
                error_code="INVALID_OBJECT_TYPE",
                message=(
                    "Object {!r} is type {!r}, expected 'CAMERA'.".format(
                        params.camera_name, cam_obj.type,
                    )
                ),
                current_state={"available_cameras": _get_camera_names()},
                hint=(
                    "Pick a camera from `current_state.available_cameras`, "
                    "or leave `camera_name` empty to use the active scene camera."
                ),
            )
    else:
        cam_obj = bpy.context.scene.camera
        if cam_obj is None:
            return ErrorResult(
                status="error",
                error_code="NO_SCENE_CAMERA",
                message="The scene has no active camera.",
                current_state={"available_cameras": _get_camera_names()},
                hint=(
                    "Add a camera with `bpy.ops.object.camera_add()` via "
                    "`execute_blender_code`, set it as the scene camera, "
                    "then call this tool again."
                ),
            )

    interp = params.interpolation.upper()
    if interp not in _VALID_INTERPOLATIONS:
        return ErrorResult(
            status="error",
            error_code="INVALID_INTERPOLATION",
            message="Interpolation {!r} is not supported.".format(params.interpolation),
            current_state={"supported_interpolations": list(_VALID_INTERPOLATIONS)},
            hint=(
                "Use one of: "
                + ", ".join(repr(i) for i in _VALID_INTERPOLATIONS)
                + "."
            ),
        )

    # Resolve or create target Empty.
    target_name = params.target_name or (cam_obj.name + "_Target")
    target = bpy.data.objects.get(target_name)
    if target is None:
        # Create an Empty (no mesh data) and link it to the scene.
        target = bpy.data.objects.new(target_name, None)
        bpy.context.scene.collection.objects.link(target)

    # Set target location if requested.
    if params.target_location:
        target.location = params.target_location

    # Find or create Track-To constraint on the camera.
    constraint = None
    for c in cam_obj.constraints:
        if c.type == "TRACK_TO" and c.target == target:
            constraint = c
            break
    if constraint is None:
        constraint = cam_obj.constraints.new(type="TRACK_TO")
        constraint.target = target
        constraint.track_axis = "TRACK_NEGATIVE_Z"
        constraint.up_axis = "UP_Y"

    # Insert keyframe on target if a frame and location were provided.
    keyed_frame = -1
    if params.frame >= 0 and params.target_location:
        target.keyframe_insert(data_path="location", frame=params.frame)
        keyed_frame = params.frame

        anim_data = target.animation_data
        if anim_data and anim_data.action:
            slot = getattr(anim_data, "action_slot", None)
            for fcurve in _iter_action_fcurves(anim_data.action, slot):
                if fcurve.data_path != "location":
                    continue
                for kp in fcurve.keyframe_points:
                    if abs(kp.co[0] - params.frame) < 0.5:
                        kp.interpolation = interp
                fcurve.update()

    return Result(
        status="ok",
        camera_name=cam_obj.name,
        target_name=target.name,
        constraint_name=constraint.name,
        frame=keyed_frame,
    )
