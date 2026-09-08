# SPDX-FileCopyrightText: 2026 Blender Authors
#
# SPDX-License-Identifier: GPL-3.0-or-later

"""
Tool-code for listing all materials in the scene with their basic properties.
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
    include_grease_pencil: bool  # True = include GP materials too


class Result(NamedTuple):
    status: str
    total: int
    materials: list[dict[str, Any]]


def _rgba(v: object) -> list[float]:
    try:
        return [round(float(c), 4) for c in v]  # type: ignore[arg-type]
    except (TypeError, ValueError):
        return []


def _principled_props(mat: object) -> "dict[str, Any]":
    """Extract Base Color / Metallic / Roughness from a Principled BSDF."""
    try:
        principled = (
            mat.node_tree.nodes.get("Principled BSDF")  # type: ignore[attr-defined]
        )
        if principled is None:
            return {}
        return {
            "base_color": _rgba(
                principled.inputs["Base Color"].default_value
            ),
            "metallic": round(
                float(principled.inputs["Metallic"].default_value), 4
            ),
            "roughness": round(
                float(principled.inputs["Roughness"].default_value), 4
            ),
        }
    except (AttributeError, KeyError):
        return {}


def _gp_props(mat: object) -> "dict[str, Any]":
    """Extract Grease Pencil line / fill colours."""
    try:
        gp = mat.grease_pencil  # type: ignore[attr-defined]
        return {
            "stroke_color": _rgba(gp.color),
            "fill_color": _rgba(gp.fill_color),
            "show_stroke": bool(gp.show_stroke),
            "show_fill": bool(gp.show_fill),
        }
    except AttributeError:
        return {}


def main(params: Params) -> Result:
    import bpy  # pylint: disable=import-error,no-name-in-module

    materials: list[dict[str, Any]] = []
    for mat in bpy.data.materials:
        is_gp = bool(getattr(mat, "is_grease_pencil", False))
        if is_gp and not params.include_grease_pencil:
            continue

        entry: dict[str, Any] = {
            "name": mat.name,
            "use_nodes": bool(mat.use_nodes),
            "is_grease_pencil": is_gp,
            "diffuse_color": _rgba(mat.diffuse_color),
        }

        if is_gp:
            entry.update(_gp_props(mat))
        elif mat.use_nodes:
            entry.update(_principled_props(mat))

        materials.append(entry)

    return Result(
        status="ok",
        total=len(materials),
        materials=sorted(materials, key=lambda m: m["name"]),
    )
