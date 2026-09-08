# SPDX-FileCopyrightText: 2026 Blender Authors
#
# SPDX-License-Identifier: GPL-3.0-or-later

"""
Tool-code for returning timeline parameters and a flat object list.
"""

__all__ = (
    "Result",
    "main",
)

from typing import Any, NamedTuple


class Result(NamedTuple):
    status: str
    scene_name: str
    frame_start: int
    frame_end: int
    frame_current: int
    fps: float
    objects: list[dict[str, Any]]


def main(params: None) -> Result:
    del params
    import bpy  # pylint: disable=import-error,no-name-in-module

    scene = bpy.context.scene
    objects = sorted(
        [
            {
                "name": obj.name,
                "type": obj.type,
                "location": list(obj.location),
            }
            for obj in scene.objects
        ],
        key=lambda o: o["name"],
    )

    fps_base = scene.render.fps_base
    fps = round(scene.render.fps / fps_base, 4) if fps_base else float(scene.render.fps)

    return Result(
        status="ok",
        scene_name=scene.name,
        frame_start=scene.frame_start,
        frame_end=scene.frame_end,
        frame_current=scene.frame_current,
        fps=fps,
        objects=objects,
    )
