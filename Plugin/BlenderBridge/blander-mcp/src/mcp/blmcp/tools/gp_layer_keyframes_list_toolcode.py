# SPDX-FileCopyrightText: 2026 Blender Authors
#
# SPDX-License-Identifier: GPL-3.0-or-later

"""
Tool-code for listing opacity keyframes on a Grease Pencil layer (GPv3).
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
    layer_name: str


class Result(NamedTuple):
    status: str
    object_name: str
    layer_name: str
    keyframes: list[dict[str, Any]]


def _get_gp_object_names() -> list[str]:
    import bpy  # pylint: disable=import-error,no-name-in-module
    return sorted(
        obj.name for obj in bpy.data.objects if obj.type == "GREASEPENCIL"
    )


def _iter_action_fcurves(action: object, slot: object) -> "Any":
    """
    Yield F-curves from *action*, handling both legacy and layered actions.

    Legacy actions (Blender < 4.4) expose ``action.fcurves`` directly.
    Layered actions (Blender 4.4+) store F-curves in
    ``action.layers[n].strips[n].channelbag_for_slot(slot).fcurves``.
    """
    # Legacy action: .fcurves attribute exists directly on the action.
    fcurves_direct = getattr(action, "fcurves", None)
    if fcurves_direct is not None:
        yield from fcurves_direct
        return

    # Layered action (Blender 4.4+): traverse layers → strips → channelbag.
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
                # Fallback: iterate all channelbags without slot filtering.
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
            current_state={"available_gp_objects": _get_gp_object_names()},
            hint=(
                "Use `gp_object_create` to create a Grease Pencil object, "
                "or pick from `current_state.available_gp_objects`."
            ),
        )

    if obj.type != "GREASEPENCIL":
        return ErrorResult(
            status="error",
            error_code="INVALID_OBJECT_TYPE",
            message="Object {!r} is type {!r}, expected 'GREASEPENCIL'.".format(
                params.object_name, obj.type
            ),
            current_state={"available_gp_objects": _get_gp_object_names()},
            hint="Pick a Grease Pencil object from `current_state.available_gp_objects`.",
        )

    layer = obj.data.layers.get(params.layer_name)
    if layer is None:
        available = [la.name for la in obj.data.layers]
        return ErrorResult(
            status="error",
            error_code="LAYER_NOT_FOUND",
            message="Layer {!r} not found on object {!r}.".format(
                params.layer_name, params.object_name
            ),
            current_state={"available_layers": available},
            hint=(
                "Use `gp_layer_create` to create a layer, "
                "or pick from `current_state.available_layers`."
            ),
        )

    keyframes: list[dict[str, Any]] = []
    gp_data = obj.data

    # Build the candidate data-path for the layer's opacity fcurve.
    # GPv3 may store the path using the layer name or an index;
    # fall back to simple suffix matching if path_from_id is unavailable.
    try:
        _exact_path: str | None = layer.path_from_id("opacity")
    except Exception:  # pylint: disable=broad-exception-caught
        _exact_path = None

    _found = False
    for _anim_data in (gp_data.animation_data, obj.animation_data):
        if not (_anim_data and _anim_data.action):
            continue
        _slot = getattr(_anim_data, "action_slot", None)
        for _fc in _iter_action_fcurves(_anim_data.action, _slot):
            _dp = _fc.data_path
            if _exact_path is not None:
                _match = (_dp == _exact_path)
            else:
                _match = (
                    _dp.endswith(".opacity")
                    and (
                        '["' + layer.name + '"]' in _dp
                        or "['" + layer.name + "']" in _dp
                    )
                )
            if not _match:
                continue
            _found = True
            for _kp in _fc.keyframe_points:
                keyframes.append({
                    "frame": int(round(_kp.co[0])),
                    "opacity": round(float(_kp.co[1]), 6),
                })
            break
        if _found:
            break

    keyframes.sort(key=lambda k: k["frame"])

    return Result(
        status="ok",
        object_name=obj.name,
        layer_name=layer.name,
        keyframes=keyframes,
    )
