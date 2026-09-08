# SPDX-FileCopyrightText: 2026 Blender Authors
#
# SPDX-License-Identifier: GPL-3.0-or-later

"""
Tool-code for inserting transform keyframes on a scene object.
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
    object_name: str
    frame: int
    # Empty list means "not provided".
    location: list    # list[float] len 3, or []
    rotation: list    # list[float] len 3 (Euler radians), or []
    scale: list       # list[float] len 3, or []
    interpolation: str


class Result(NamedTuple):
    status: str
    object_name: str
    frame: int
    inserted: list    # list[str] of data_paths that received a keyframe
    interpolation: str


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

    interp = params.interpolation.upper()
    if interp not in _VALID_INTERPOLATIONS:
        return ErrorResult(
            status="error",
            error_code="INVALID_INTERPOLATION",
            message=(
                "Interpolation {!r} is not supported.".format(params.interpolation)
            ),
            current_state={"supported_interpolations": list(_VALID_INTERPOLATIONS)},
            hint=(
                "Use one of: "
                + ", ".join(repr(i) for i in _VALID_INTERPOLATIONS)
                + "."
            ),
        )

    if not params.location and not params.rotation and not params.scale:
        return ErrorResult(
            status="error",
            error_code="NO_PROPERTIES",
            message="No transform properties specified.",
            current_state={
                "transform_properties": ["location", "rotation", "scale"],
            },
            hint="Provide at least one of: location, rotation, scale.",
        )

    inserted: list[str] = []

    if params.location:
        obj.location = params.location
        obj.keyframe_insert(data_path="location", frame=params.frame)
        inserted.append("location")

    if params.rotation:
        obj.rotation_euler = params.rotation
        obj.keyframe_insert(data_path="rotation_euler", frame=params.frame)
        inserted.append("rotation_euler")

    if params.scale:
        obj.scale = params.scale
        obj.keyframe_insert(data_path="scale", frame=params.frame)
        inserted.append("scale")

    # Apply interpolation to the newly inserted keyframe points.
    anim_data = obj.animation_data
    if anim_data and anim_data.action:
        slot = getattr(anim_data, "action_slot", None)
        for fcurve in _iter_action_fcurves(anim_data.action, slot):
            if fcurve.data_path not in inserted:
                continue
            for kp in fcurve.keyframe_points:
                if abs(kp.co[0] - params.frame) < 0.5:
                    kp.interpolation = interp
            fcurve.update()

    return Result(
        status="ok",
        object_name=obj.name,
        frame=params.frame,
        inserted=inserted,
        interpolation=interp,
    )
