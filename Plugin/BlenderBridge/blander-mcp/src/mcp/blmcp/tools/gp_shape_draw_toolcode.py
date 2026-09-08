# SPDX-FileCopyrightText: 2026 Blender Authors
#
# SPDX-License-Identifier: GPL-3.0-or-later

"""
Tool-code for drawing predefined shapes on a Grease Pencil layer (GPv3).
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
    shape: str
    cx: float
    cy: float
    cz: float
    radius: float
    width: float
    height: float
    segments: int
    mode: str
    stroke_radius: float
    material_index: int
    x1: float
    y1: float
    z1: float
    x2: float
    y2: float
    z2: float
    points_count: int


class Result(NamedTuple):
    status: str
    object_name: str
    layer_name: str
    frame: int
    shape: str
    point_count: int


_VALID_SHAPES = ("line", "rect", "circle")


def _get_gp_object_names() -> list[str]:
    import bpy  # pylint: disable=import-error,no-name-in-module
    return sorted(
        obj.name for obj in bpy.data.objects if obj.type == "GREASEPENCIL"
    )


def _line_points(
    x1: float,
    y1: float,
    z1: float,
    x2: float,
    y2: float,
    z2: float,
    points_count: int,
) -> list[list[float]]:
    n = max(points_count, 2)
    if n == 2:
        return [[x1, y1, z1], [x2, y2, z2]]
    pts = []
    for i in range(n):
        t = i / (n - 1)
        pts.append([
            x1 + t * (x2 - x1),
            y1 + t * (y2 - y1),
            z1 + t * (z2 - z1),
        ])
    return pts


def _rect_points(
    cx: float,
    cy: float,
    cz: float,
    width: float,
    height: float,
) -> list[list[float]]:
    hw, hh = width / 2.0, height / 2.0
    return [
        [cx - hw, cy, cz - hh],
        [cx + hw, cy, cz - hh],
        [cx + hw, cy, cz + hh],
        [cx - hw, cy, cz + hh],
        [cx - hw, cy, cz - hh],
    ]


def _circle_points(
    cx: float,
    cy: float,
    cz: float,
    radius: float,
    segments: int,
) -> list[list[float]]:
    import math
    pts = []
    for i in range(segments + 1):
        angle = 2.0 * math.pi * i / segments
        pts.append([
            cx + radius * math.cos(angle),
            cy,
            cz + radius * math.sin(angle),
        ])
    return pts


def _ensure_frame(layer: Any, frame_number: int, replace: bool) -> Any:
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

    if params.shape not in _VALID_SHAPES:
        return ErrorResult(
            status="error",
            error_code="INVALID_SHAPE",
            message="shape must be one of {}, got {!r}.".format(
                _VALID_SHAPES, params.shape
            ),
            current_state={"valid_shapes": list(_VALID_SHAPES)},
            hint=(
                "Use 'line' for a straight line, 'rect' for a rectangle, "
                "or 'circle' for a circle. "
                "For freeform strokes use `gp_stroke_draw` instead."
            ),
        )

    if params.mode not in ("replace", "append"):
        return ErrorResult(
            status="error",
            error_code="INVALID_MODE",
            message="mode must be 'replace' or 'append', got {!r}.".format(
                params.mode
            ),
            current_state={"valid_modes": ["replace", "append"]},
            hint=(
                "Use 'replace' to clear existing strokes on the frame "
                "before drawing, or 'append' to add alongside them."
            ),
        )

    if params.shape == "line":
        points = _line_points(
            params.x1, params.y1, params.z1,
            params.x2, params.y2, params.z2,
            params.points_count,
        )
    elif params.shape == "rect":
        points = _rect_points(
            params.cx, params.cy, params.cz, params.width, params.height
        )
    else:
        points = _circle_points(
            params.cx, params.cy, params.cz, params.radius, params.segments
        )

    frame = _ensure_frame(
        layer, params.frame, replace=(params.mode == "replace")
    )
    drawing = frame.drawing
    _add_stroke(
        drawing, points, params.stroke_radius, params.material_index
    )

    return Result(
        status="ok",
        object_name=obj.name,
        layer_name=layer.name,
        frame=params.frame,
        shape=params.shape,
        point_count=len(points),
    )
