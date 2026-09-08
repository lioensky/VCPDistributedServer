# SPDX-FileCopyrightText: 2026 Blender Authors
#
# SPDX-License-Identifier: GPL-3.0-or-later

"""
Tool-code for creating a Grease Pencil material (GPv3).
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
    stroke_color: list[float]
    fill_color: list[float]


class Result(NamedTuple):
    status: str
    name: str
    stroke_color: list[float]
    fill_color: list[float]


def _validate_color(color: list[float], field: str) -> "str | None":
    """Return an error message if *color* is not a valid RGBA list, else None."""
    if len(color) != 4:
        return (
            "{} must have exactly 4 components [R, G, B, A], "
            "got {}.".format(field, len(color))
        )
    return None


def main(params: Params) -> "Result | ErrorResult":
    import bpy  # pylint: disable=import-error,no-name-in-module

    err = _validate_color(params.stroke_color, "stroke_color")
    if err:
        return ErrorResult(
            status="error",
            error_code="INVALID_COLOR",
            message=err,
            current_state={},
            hint=(
                "Use four floats in [0.0, 1.0]: "
                "[R, G, B, A].  Example: [0.0, 0.0, 0.0, 1.0] = opaque black."
            ),
        )

    err = _validate_color(params.fill_color, "fill_color")
    if err:
        return ErrorResult(
            status="error",
            error_code="INVALID_COLOR",
            message=err,
            current_state={},
            hint=(
                "Use four floats in [0.0, 1.0]: "
                "[R, G, B, A].  Set A=0 to make fill invisible."
            ),
        )

    mat = bpy.data.materials.new(params.name)
    bpy.data.materials.create_gpencil_data(mat)

    gp = mat.grease_pencil
    gp.color = tuple(params.stroke_color)
    gp.fill_color = tuple(params.fill_color)

    return Result(
        status="ok",
        name=mat.name,
        stroke_color=list(gp.color),
        fill_color=list(gp.fill_color),
    )
