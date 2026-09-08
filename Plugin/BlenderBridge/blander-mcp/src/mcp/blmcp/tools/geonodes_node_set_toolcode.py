# SPDX-FileCopyrightText: 2026 Blender Authors
#
# SPDX-License-Identifier: GPL-3.0-or-later

"""
Tool-code for setting a node input's default value in a Geometry Nodes graph.
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
    node_name: str
    input_name: str
    value: float    # scalar float; for ints/bools Blender coerces automatically


class Result(NamedTuple):
    status: str
    object_name: str
    node_name: str
    input_name: str
    old_value: float
    new_value: float


def _get_object_names() -> list[str]:
    import bpy  # pylint: disable=import-error,no-name-in-module
    return sorted(obj.name for obj in bpy.data.objects)


def _find_gn_modifier(obj: object) -> "object | None":
    for mod in obj.modifiers:  # type: ignore[attr-defined]
        if mod.type == "NODES" and mod.node_group is not None:
            return mod
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

    mod = _find_gn_modifier(obj)
    if mod is None:
        return ErrorResult(
            status="error",
            error_code="NO_GEONODES_MODIFIER",
            message=(
                "Object {!r} has no Geometry Nodes modifier with a node "
                "tree.".format(params.object_name)
            ),
            current_state={},
            hint="Use `geonodes_apply_preset` to add a Geometry Nodes preset.",
        )

    nt = mod.node_group
    node = nt.nodes.get(params.node_name)
    if node is None:
        available = [n.name for n in nt.nodes]
        return ErrorResult(
            status="error",
            error_code="NODE_NOT_FOUND",
            message="Node {!r} not found in tree {!r}.".format(
                params.node_name, nt.name,
            ),
            current_state={"available_nodes": available},
            hint=(
                "Use `geonodes_query` to list nodes, or pick from "
                "`current_state.available_nodes`."
            ),
        )

    inp = node.inputs.get(params.input_name)
    if inp is None:
        available_inputs = [i.name for i in node.inputs]
        return ErrorResult(
            status="error",
            error_code="INPUT_NOT_FOUND",
            message="Input {!r} not found on node {!r}.".format(
                params.input_name, params.node_name,
            ),
            current_state={"available_inputs": available_inputs},
            hint=(
                "Use `geonodes_query` to list node inputs, "
                "or pick from `current_state.available_inputs`."
            ),
        )

    try:
        old_value = float(inp.default_value)
        inp.default_value = params.value
        new_value = float(inp.default_value)
    except (AttributeError, TypeError, ValueError) as exc:
        return ErrorResult(
            status="error",
            error_code="SET_FAILED",
            message="Cannot set input {!r}: {}".format(params.input_name, exc),
            current_state={},
            hint=(
                "Only scalar (float/int/bool) inputs are supported. "
                "For vector or geometry inputs use `execute_blender_code`."
            ),
        )

    return Result(
        status="ok",
        object_name=obj.name,
        node_name=node.name,
        input_name=inp.name,
        old_value=round(old_value, 6),
        new_value=round(new_value, 6),
    )
