# SPDX-FileCopyrightText: 2026 Blender Authors
#
# SPDX-License-Identifier: GPL-3.0-or-later

"""
Tool-code for rendering a single frame to an image file.

Supports optional overrides for frame number, resolution, and frame-rate.
All overrides are applied temporarily and restored after the render.
"""

__all__ = (
    "Params",
    "Result",
    "main",
)

import contextlib
import typing
from collections.abc import Callable
from typing import NamedTuple


class Params(NamedTuple):
    output_path: str
    frame: int | None = None
    width: int | None = None
    height: int | None = None
    fps: int | None = None


class Result(NamedTuple):
    status: str
    filepath: str | None = None
    frame: int | None = None
    width: int | None = None
    height: int | None = None
    fps: int | None = None
    message: str | None = None


# @include_begin: _template_backup_attrs_and_assign_multi.py
@contextlib.contextmanager
def _backup_attrs_and_assign_multi(
        *obj_attrs: tuple[object, dict[str, object]],
) -> typing.Generator[None, None, None]:
    yield
# @include_end


def main(params: Params) -> "Result | Callable[[], dict[str, object] | None]":
    import os
    import bpy  # pylint: disable=import-error,no-name-in-module

    use_deferred = not bpy.app.background
    scene = bpy.context.scene
    rd = scene.render

    # Resolve output path: absolute paths are used as-is; relative paths
    # are placed inside the MCP scratch directory.
    if os.path.isabs(params.output_path):
        output_path = params.output_path
    else:
        output_path = os.path.join(
            bpy.app.tempdir,
            "blender_mcp",
            os.path.basename(params.output_path),
        )
    parent = os.path.dirname(output_path)
    if parent:
        os.makedirs(parent, exist_ok=True)

    # Build attribute overrides for temporary settings changes.
    obj_attrs: list[tuple[object, dict[str, object]]] = []

    # Optional frame override.
    if params.frame is not None:
        obj_attrs.append((scene, {"frame_current": params.frame}))

    # Optional resolution / fps overrides.
    rd_attrs: dict[str, object] = {}
    if params.width is not None and params.width > 0:
        rd_attrs["resolution_x"] = params.width
    if params.height is not None and params.height > 0:
        rd_attrs["resolution_y"] = params.height
    if rd_attrs:
        rd_attrs["resolution_percentage"] = 100
    if params.fps is not None and params.fps > 0:
        rd_attrs["fps"] = params.fps
        rd_attrs["fps_base"] = 1
    if rd_attrs:
        obj_attrs.append((rd, rd_attrs))

    # NOTE: `filepath` is saved/restored manually (not via the context
    # manager) because `write_still` reads it after the render completes.
    # With `INVOKE_DEFAULT` the context manager would restore it too early.
    orig_filepath = rd.filepath
    rd.filepath = output_path

    render_args: tuple[str, ...] = ('INVOKE_DEFAULT',) if use_deferred else ()

    with _backup_attrs_and_assign_multi(*obj_attrs):
        actual_frame = scene.frame_current
        actual_w = rd.resolution_x
        actual_h = rd.resolution_y
        actual_fps = rd.fps
        try:
            bpy.ops.render.render(*render_args, write_still=True)
        except RuntimeError as ex:
            rd.filepath = orig_filepath
            return Result(status="error", message=str(ex))

    if use_deferred:
        def _check() -> dict[str, object] | None:
            if bpy.app.is_job_running('RENDER'):
                return None
            rd.filepath = orig_filepath
            if os.path.exists(output_path):
                return {
                    "status": "ok",
                    "filepath": output_path,
                    "frame": actual_frame,
                    "width": actual_w,
                    "height": actual_h,
                    "fps": actual_fps,
                }
            return {
                "status": "error",
                "message": "Render completed but output file was not created",
            }
        return _check

    rd.filepath = orig_filepath
    return Result(
        status="ok",
        filepath=output_path,
        frame=actual_frame,
        width=actual_w,
        height=actual_h,
        fps=actual_fps,
    )
