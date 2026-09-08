# SPDX-FileCopyrightText: 2026 Blender Authors
#
# SPDX-License-Identifier: GPL-3.0-or-later

"""
Tool-code for returning structured detail about a single object.
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
    name: str


class Result(NamedTuple):
    status: str
    name: str
    type: str
    location: list[float]
    rotation: list[float]
    scale: list[float]
    dimensions: list[float]
    parent: str | None
    children: list[str]
    modifiers: list[dict[str, object]]
    constraints: list[dict[str, object]]
    materials: list[str | None]
    visibility: dict[str, bool]
    data_name: str | None
    collections: list[str]


def main(params: Params) -> "Result | ErrorResult":
    import bpy  # pylint: disable=import-error,no-name-in-module

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

    return Result(
        status="ok",
        name=obj.name,
        type=obj.type,
        location=list(obj.location),
        rotation=list(obj.rotation_euler),
        scale=list(obj.scale),
        dimensions=list(obj.dimensions),
        parent=obj.parent.name if obj.parent else None,
        children=[child.name for child in obj.children],
        modifiers=[
            {
                "name": mod.name,
                "type": mod.type,
                "show_viewport": mod.show_viewport,
                "show_render": mod.show_render,
            }
            for mod in obj.modifiers
        ],
        constraints=[
            {
                "name": con.name,
                "type": con.type,
                "enabled": con.enabled,
            }
            for con in obj.constraints
        ],
        materials=[
            slot.material.name if slot.material else None
            for slot in obj.material_slots
        ],
        visibility={
            "hide_viewport": obj.hide_viewport,
            "hide_render": obj.hide_render,
            "hide_get": obj.hide_get(),
        },
        data_name=obj.data.name if obj.data else None,
        collections=[col.name for col in obj.users_collection],
    )
