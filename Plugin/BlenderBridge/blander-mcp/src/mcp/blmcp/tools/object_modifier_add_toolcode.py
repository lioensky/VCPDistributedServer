# SPDX-FileCopyrightText: 2026 Blender Authors
#
# SPDX-License-Identifier: GPL-3.0-or-later

"""
Tool-code for adding a modifier to a scene object.
"""

__all__ = (
    "Params",
    "Result",
    "main",
)

from typing import Any, NamedTuple

# @include_begin: _template_tool_error.py
# @include_end

# Properties that are intrinsic to every modifier and should not be set
# via the user-supplied params dict.
_SKIP_PROPS = frozenset({
    "name", "type", "is_active",
    "show_viewport", "show_render", "show_in_editmode",
    "show_on_cage", "show_expanded",
})


class Params(NamedTuple):
    object_name: str
    modifier_type: str
    name: str                   # "" = auto-name from type
    params: dict[str, Any]      # modifier-specific attribute overrides


class Result(NamedTuple):
    status: str
    object_name: str
    modifier_name: str
    modifier_type: str
    applied_params: list[str]   # keys that were set successfully
    failed_params: list[str]    # keys that could not be set


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

    _COMMON_TYPES = [
        "SUBSURF", "WAVE", "SOLIDIFY", "BEVEL", "ARRAY",
        "MIRROR", "BOOLEAN", "DECIMATE", "SKIN",
    ]

    mod_name = params.name or params.modifier_type.capitalize()
    try:
        mod = obj.modifiers.new(name=mod_name, type=params.modifier_type)
    except Exception as exc:  # pylint: disable=broad-exception-caught
        # Blender raises RuntimeError for unknown modifier types.
        return ErrorResult(
            status="error",
            error_code="INVALID_MODIFIER_TYPE",
            message=(
                "Cannot add modifier of type {!r}: {}".format(
                    params.modifier_type, exc,
                )
            ),
            current_state={"common_types": _COMMON_TYPES},
            hint=(
                "Pick a type from `current_state.common_types`, "
                "e.g. 'SUBSURF' or 'WAVE'."
            ),
        )

    if mod is None:
        return ErrorResult(
            status="error",
            error_code="INVALID_MODIFIER_TYPE",
            message=(
                "Modifier type {!r} is not supported for object "
                "type {!r}.".format(params.modifier_type, obj.type)
            ),
            current_state={"common_types": _COMMON_TYPES},
            hint=(
                "Most deform and generate modifiers require a MESH object. "
                "Check the object type with `get_object_detail_summary`."
            ),
        )

    applied: list[str] = []
    failed: list[str] = []
    for key, val in params.params.items():
        if key in _SKIP_PROPS:
            failed.append(key)
            continue
        try:
            setattr(mod, key, val)
            applied.append(key)
        except (AttributeError, TypeError, ValueError):
            failed.append(key)

    return Result(
        status="ok",
        object_name=obj.name,
        modifier_name=mod.name,
        modifier_type=mod.type,
        applied_params=applied,
        failed_params=failed,
    )
