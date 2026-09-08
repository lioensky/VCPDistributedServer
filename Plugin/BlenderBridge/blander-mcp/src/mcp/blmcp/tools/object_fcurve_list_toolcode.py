# SPDX-FileCopyrightText: 2026 Blender Authors
#
# SPDX-License-Identifier: GPL-3.0-or-later

"""
Tool-code for reading F-Curve keyframe data from a scene object.
"""

__all__ = (
    "Params",
    "Result",
    "main",
)

from typing import Any, NamedTuple

# @include_begin: _template_tool_error.py
# @include_end

_VALID_DATA_PATHS = ("location", "rotation_euler", "scale")


class Params(NamedTuple):
    object_name: str
    data_path: str   # "location" | "rotation_euler" | "scale"


class Result(NamedTuple):
    status: str
    object_name: str
    data_path: str
    # list of {"array_index": int, "keyframes": [{"frame": int, "value": float}]}
    curves: list[dict[str, Any]]


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

    if params.data_path not in _VALID_DATA_PATHS:
        return ErrorResult(
            status="error",
            error_code="INVALID_DATA_PATH",
            message=(
                "data_path {!r} is not supported.".format(params.data_path)
            ),
            current_state={"supported_data_paths": list(_VALID_DATA_PATHS)},
            hint=(
                "Use one of: "
                + ", ".join(repr(p) for p in _VALID_DATA_PATHS)
                + "."
            ),
        )

    curves: list[dict[str, Any]] = []

    anim_data = obj.animation_data
    if anim_data and anim_data.action:
        slot = getattr(anim_data, "action_slot", None)
        for fcurve in _iter_action_fcurves(anim_data.action, slot):
            if fcurve.data_path != params.data_path:
                continue
            keyframes = sorted(
                [
                    {
                        "frame": int(round(kp.co[0])),
                        "value": round(float(kp.co[1]), 6),
                        "interpolation": kp.interpolation,
                    }
                    for kp in fcurve.keyframe_points
                ],
                key=lambda k: k["frame"],
            )
            curves.append({
                "array_index": fcurve.array_index,
                "keyframes": keyframes,
            })

    curves.sort(key=lambda c: c["array_index"])

    return Result(
        status="ok",
        object_name=obj.name,
        data_path=params.data_path,
        curves=curves,
    )
