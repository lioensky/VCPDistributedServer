# SPDX-FileCopyrightText: 2026 Blender Authors
#
# SPDX-License-Identifier: GPL-3.0-or-later

"""
Tool-code for drawing an arbitrary stroke on a Grease Pencil layer (GPv3).
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
    frame: int
    points: list[list[float]]
    mode: str
    stroke_radius: float
    material_index: int


class Result(NamedTuple):
    status: str
    object_name: str
    layer_name: str
    frame: int
    stroke_count: int


def _get_gp_object_names() -> list[str]:
    import bpy  # pylint: disable=import-error,no-name-in-module
    return sorted(
        obj.name for obj in bpy.data.objects if obj.type == "GREASEPENCIL"
    )


def _ensure_frame(layer: Any, frame_number: int, replace: bool) -> Any:
    """Return a drawing frame at *frame_number*, creating it if needed.

    In replace mode, deletes any existing frame first so the drawing is
    always empty on entry.
    """
    existing = {f.frame_number for f in layer.frames}
    if replace and frame_number in existing:
        layer.frames.remove(frame_number)
        existing = existing - {frame_number}
    if frame_number not in existing:
        return layer.frames.new(frame_number)
    return layer.get_frame_at(frame_number)


def _add_stroke(
    drawing: Any,
    points: list[list[float]],
    stroke_radius: float,
    material_index: int,
) -> None:
    """Append one stroke to *drawing*, setting positions and per-point radius."""
    n_pts_before = drawing.attributes.domain_size("POINT")
    n_curves_before = drawing.attributes.domain_size("CURVE")

    drawing.add_strokes([len(points)])

    pos_attr = drawing.attributes["position"]
    for i, pt in enumerate(points):
        pos_attr.data[n_pts_before + i].vector = (
            float(pt[0]),
            float(pt[1]),
            float(pt[2]),
        )

    try:
        radius_attr = drawing.attributes["radius"]
        for i in range(len(points)):
            radius_attr.data[n_pts_before + i].value = float(stroke_radius)
    except (KeyError, AttributeError):
        pass

    try:
        mat_attr = drawing.attributes["material_index"]
        mat_attr.data[n_curves_before].value = int(material_index)
    except (KeyError, AttributeError):
        pass


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

    if params.mode not in ("replace", "append"):
        return ErrorResult(
            status="error",
            error_code="INVALID_MODE",
            message="mode must be 'replace' or 'append', got {!r}.".format(
                params.mode
            ),
            current_state={},
            hint=(
                "Use 'replace' to clear existing strokes on the frame "
                "before drawing, or 'append' to add alongside them."
            ),
        )

    if not params.points:
        return ErrorResult(
            status="error",
            error_code="INVALID_POINTS",
            message="points must be a non-empty list of [x, y, z] coordinates.",
            current_state={},
            hint="Provide at least one point, e.g. [[0.0, 0.0, 0.0]].",
        )

    for pt in params.points:
        if len(pt) != 3:
            return ErrorResult(
                status="error",
                error_code="INVALID_POINT_FORMAT",
                message=(
                    "Each point must have exactly 3 coordinates [x, y, z], "
                    "got length {}.".format(len(pt))
                ),
                current_state={},
                hint="Format: [[x1, y1, z1], [x2, y2, z2], ...]",
            )

    frame = _ensure_frame(
        layer, params.frame, replace=(params.mode == "replace")
    )
    drawing = frame.drawing
    _add_stroke(
        drawing, params.points, params.stroke_radius, params.material_index
    )

    stroke_count = drawing.attributes.domain_size("CURVE")
    return Result(
        status="ok",
        object_name=obj.name,
        layer_name=layer.name,
        frame=params.frame,
        stroke_count=stroke_count,
    )
