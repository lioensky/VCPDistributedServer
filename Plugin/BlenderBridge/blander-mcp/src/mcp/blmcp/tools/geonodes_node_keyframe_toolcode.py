# SPDX-FileCopyrightText: 2026 Blender Authors
#
# SPDX-License-Identifier: GPL-3.0-or-later

"""
Tool-code for inserting a keyframe on a Geometry Nodes node input.
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
    node_name: str
    input_name: str
    frame: int
    value: float
    interpolation: str


class Result(NamedTuple):
    status: str
    object_name: str
    node_name: str
    input_name: str
    frame: int
    value: float
    interpolation: str


def _get_object_names() -> list[str]:
    import bpy  # pylint: disable=import-error,no-name-in-module
    return sorted(obj.name for obj in bpy.data.objects)


def _find_gn_modifier(obj: object) -> "object | None":
    for mod in obj.modifiers:  # type: ignore[attr-defined]
        if mod.type == "NODES" and mod.node_group is not None:
            return mod
    return None


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

    interp = params.interpolation.upper()
    if interp not in _VALID_INTERPOLATIONS:
        return ErrorResult(
            status="error",
            error_code="INVALID_INTERPOLATION",
            message="Interpolation {!r} is not supported.".format(
                params.interpolation,
            ),
            current_state={"supported_interpolations": list(_VALID_INTERPOLATIONS)},
            hint=(
                "Use one of: "
                + ", ".join(repr(i) for i in _VALID_INTERPOLATIONS)
                + "."
            ),
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
            hint="Use `geonodes_query` to list nodes.",
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
            hint="Use `geonodes_query` to list node inputs.",
        )

    try:
        inp.default_value = params.value
        inp.keyframe_insert(data_path="default_value", frame=params.frame)
    except (AttributeError, TypeError, ValueError) as exc:
        return ErrorResult(
            status="error",
            error_code="KEYFRAME_FAILED",
            message="Cannot keyframe input {!r}: {}".format(
                params.input_name, exc,
            ),
            current_state={},
            hint=(
                "Only scalar (float/int/bool) inputs support keyframing. "
                "For other types use `execute_blender_code`."
            ),
        )

    # Apply interpolation mode to the new keyframe point.
    anim_data = nt.animation_data
    if anim_data and anim_data.action:
        inp_index = list(node.inputs).index(inp)
        target_path = (
            'nodes["{:s}"].inputs[{:d}].default_value'.format(
                node.name, inp_index,
            )
        )
        slot = getattr(anim_data, "action_slot", None)
        for fcurve in _iter_action_fcurves(anim_data.action, slot):
            if fcurve.data_path != target_path:
                continue
            for kp in fcurve.keyframe_points:
                if abs(kp.co[0] - params.frame) < 0.5:
                    kp.interpolation = interp
            fcurve.update()

    return Result(
        status="ok",
        object_name=obj.name,
        node_name=node.name,
        input_name=inp.name,
        frame=params.frame,
        value=round(float(inp.default_value), 6),
        interpolation=interp,
    )
