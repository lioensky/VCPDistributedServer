# SPDX-FileCopyrightText: 2026 Blender Authors
#
# SPDX-License-Identifier: GPL-3.0-or-later

"""
Tool-code for assigning an existing Action to an Armature object.
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
    armature_name: str
    action_name: str


class Result(NamedTuple):
    status: str
    armature_name: str
    action_name: str
    frame_start: float
    frame_end: float


def _get_object_names() -> list[str]:
    import bpy  # pylint: disable=import-error,no-name-in-module
    return sorted(obj.name for obj in bpy.data.objects)


def _get_action_names() -> list[str]:
    import bpy  # pylint: disable=import-error,no-name-in-module
    return sorted(a.name for a in bpy.data.actions)


def _assign_action(obj: object, action: object) -> None:
    """
    Assign *action* to *obj*, handling both the legacy single-action API and
    the new slot-based API introduced in Blender 4.4.
    """
    anim_data = getattr(obj, "animation_data", None)
    if anim_data is None:
        obj.animation_data_create()  # type: ignore[attr-defined]
        anim_data = obj.animation_data  # type: ignore[attr-defined]

    anim_data.action = action  # type: ignore[attr-defined]

    # Blender 4.4+ slot-based API: ensure a slot is selected.
    if (
        hasattr(anim_data, "action_slot")
        and hasattr(action, "slots")
        and anim_data.action_slot is None
    ):
        slots = list(getattr(action, "slots", []))
        if slots:
            anim_data.action_slot = slots[0]


def main(params: Params) -> "Result | ErrorResult":
    import bpy  # pylint: disable=import-error,no-name-in-module

    obj = bpy.data.objects.get(params.armature_name)
    if obj is None:
        return ErrorResult(
            status="error",
            error_code="OBJECT_NOT_FOUND",
            message="Object {!r} not found.".format(params.armature_name),
            current_state={"available_objects": _get_object_names()},
            hint="Use `get_scene_state` to list objects.",
        )

    if obj.type != "ARMATURE":
        return ErrorResult(
            status="error",
            error_code="NOT_AN_ARMATURE",
            message=(
                "Object {!r} is of type {!r}, expected 'ARMATURE'.".format(
                    params.armature_name, obj.type,
                )
            ),
            current_state={
                "object_type": obj.type,
                "armature_objects": [
                    o.name for o in bpy.data.objects if o.type == "ARMATURE"
                ],
            },
            hint=(
                "Pick an object of type 'ARMATURE' from "
                "`current_state.armature_objects`."
            ),
        )

    action = bpy.data.actions.get(params.action_name)
    if action is None:
        return ErrorResult(
            status="error",
            error_code="ACTION_NOT_FOUND",
            message="Action {!r} not found.".format(params.action_name),
            current_state={"available_actions": _get_action_names()},
            hint=(
                "Use `action_list` to see available actions, or pick from "
                "`current_state.available_actions`."
            ),
        )

    _assign_action(obj, action)

    try:
        fr = action.frame_range
        frame_start = round(float(fr[0]), 2)
        frame_end = round(float(fr[1]), 2)
    except (AttributeError, TypeError, IndexError):
        frame_start = 0.0
        frame_end = 0.0

    return Result(
        status="ok",
        armature_name=obj.name,
        action_name=action.name,
        frame_start=frame_start,
        frame_end=frame_end,
    )
