# SPDX-FileCopyrightText: 2026 Blender Authors
#
# SPDX-License-Identifier: GPL-3.0-or-later

"""
Tool-code for listing modifiers and their parameters on a scene object.
"""

__all__ = (
    "Params",
    "Result",
    "main",
)

from typing import Any, NamedTuple

# @include_begin: _template_tool_error.py
# @include_end

# Properties shared by every modifier that are not useful as params.
_SKIP_PROPS = frozenset({
    "name", "type", "is_active",
    "show_viewport", "show_render", "show_in_editmode",
    "show_on_cage", "show_expanded", "use_apply_on_spline",
    "rna_type",
})

# RNA property types that can be serialised to simple Python values.
_SIMPLE_TYPES = frozenset({
    "BOOLEAN", "INT", "FLOAT", "STRING", "ENUM",
})


class Params(NamedTuple):
    object_name: str


class Result(NamedTuple):
    status: str
    object_name: str
    modifiers: list[dict[str, Any]]


def _get_object_names() -> list[str]:
    import bpy  # pylint: disable=import-error,no-name-in-module
    return sorted(obj.name for obj in bpy.data.objects)


def _extract_params(mod: object) -> dict[str, Any]:
    """Extract serialisable properties from a modifier via RNA introspection."""
    params: dict[str, Any] = {}
    for prop in mod.bl_rna.properties:
        pid = prop.identifier
        if pid.startswith("_") or pid in _SKIP_PROPS:
            continue
        if prop.is_hidden:
            continue
        if prop.type not in _SIMPLE_TYPES:
            continue
        try:
            val = getattr(mod, pid)
            if isinstance(val, bool):
                params[pid] = val
            elif isinstance(val, int):
                params[pid] = val
            elif isinstance(val, float):
                params[pid] = round(val, 6)
            elif isinstance(val, str):
                params[pid] = val
        except (AttributeError, TypeError):
            pass
    return params


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

    modifiers = []
    for mod in obj.modifiers:
        modifiers.append({
            "name": mod.name,
            "type": mod.type,
            "show_viewport": mod.show_viewport,
            "show_render": mod.show_render,
            "params": _extract_params(mod),
        })

    return Result(
        status="ok",
        object_name=obj.name,
        modifiers=modifiers,
    )
