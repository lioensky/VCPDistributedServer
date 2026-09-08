# SPDX-FileCopyrightText: 2026 Blender Authors
#
# SPDX-License-Identifier: GPL-3.0-or-later

"""
Tool-code for querying the Geometry Nodes graph of a scene object.
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
    object_name: str
    modifier_name: str   # "" = first NODES modifier found


class Result(NamedTuple):
    status: str
    object_name: str
    modifier_name: str
    node_tree_name: str
    nodes: list[dict[str, Any]]


def _get_object_names() -> list[str]:
    import bpy  # pylint: disable=import-error,no-name-in-module
    return sorted(obj.name for obj in bpy.data.objects)


def _input_value(inp: object) -> "Any":
    """Return a serialisable default_value for a node socket input."""
    try:
        val = inp.default_value  # type: ignore[attr-defined]
    except (AttributeError, TypeError):
        return None
    if isinstance(val, (bool, int, float, str)):
        return val
    if hasattr(val, "__iter__"):
        try:
            return [round(float(v), 6) for v in val]
        except (TypeError, ValueError):
            pass
    return None


def main(params: Params) -> "Result | ErrorResult":
    import bpy  # pylint: disable=import-error,no-name-in-module

    obj = bpy.data.objects.get(params.object_name)
    if obj is None:
        return ErrorResult(
            status="error",
            error_code="OBJECT_NOT_FOUND",
            message="Object {!r} not found.".format(params.object_name),
            current_state={"available_objects": _get_object_names()},
            hint="Use `get_scene_state` to list objects.",
        )

    # Resolve modifier.
    mod = None
    if params.modifier_name:
        mod = obj.modifiers.get(params.modifier_name)
        if mod is None or mod.type != "NODES":
            gn_names = [m.name for m in obj.modifiers if m.type == "NODES"]
            return ErrorResult(
                status="error",
                error_code="MODIFIER_NOT_FOUND",
                message=(
                    "Geometry Nodes modifier {!r} not found on {!r}.".format(
                        params.modifier_name, params.object_name,
                    )
                ),
                current_state={"available_gn_modifiers": gn_names},
                hint=(
                    "Use `geonodes_apply_preset` to add a Geometry Nodes "
                    "modifier, or pick from `current_state`."
                ),
            )
    else:
        for m in obj.modifiers:
            if m.type == "NODES":
                mod = m
                break

    if mod is None:
        return ErrorResult(
            status="error",
            error_code="NO_GEONODES_MODIFIER",
            message=(
                "Object {!r} has no Geometry Nodes modifier.".format(
                    params.object_name,
                )
            ),
            current_state={},
            hint=(
                "Use `geonodes_apply_preset` to add a preset Geometry Nodes "
                "modifier first."
            ),
        )

    nt = mod.node_group
    if nt is None:
        return Result(
            status="ok",
            object_name=obj.name,
            modifier_name=mod.name,
            node_tree_name="",
            nodes=[],
        )

    nodes: list[dict[str, Any]] = []
    for node in nt.nodes:
        inputs_info: list[dict[str, Any]] = []
        for inp in node.inputs:
            entry: dict[str, Any] = {
                "name": inp.name,
                "type": inp.type,
                "is_linked": inp.is_linked,
                "default_value": _input_value(inp),
            }
            inputs_info.append(entry)

        nodes.append({
            "name": node.name,
            "bl_idname": node.bl_idname,
            "location": [
                round(node.location.x, 1),
                round(node.location.y, 1),
            ],
            "inputs": inputs_info,
        })

    return Result(
        status="ok",
        object_name=obj.name,
        modifier_name=mod.name,
        node_tree_name=nt.name,
        nodes=nodes,
    )
