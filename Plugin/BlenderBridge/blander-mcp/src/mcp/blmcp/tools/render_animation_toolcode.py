# SPDX-FileCopyrightText: 2026 Blender Authors
#
# SPDX-License-Identifier: GPL-3.0-or-later

"""
Tool-code for rendering a frame sequence and writing a video file.

Video output uses Blender 5.1's ``media_type = 'VIDEO'`` API with an
H.264 / MPEG-4 codec.  Older Blender builds that expose ``file_format``
instead of ``media_type`` fall back to ``file_format = 'FFMPEG'``.
All settings are restored after the render.
"""

__all__ = (
    "Params",
    "Result",
    "main",
)

from collections.abc import Callable
from typing import NamedTuple


class Params(NamedTuple):
    output_path: str
    frame_start: int | None = None
    frame_end: int | None = None
    width: int | None = None
    height: int | None = None
    fps: int | None = None


class Result(NamedTuple):
    status: str
    filepath: str | None = None
    frame_start: int | None = None
    frame_end: int | None = None
    width: int | None = None
    height: int | None = None
    fps: int | None = None
    message: str | None = None


def main(params: Params) -> "Result | Callable[[], dict[str, object] | None]":
    import os
    import bpy  # pylint: disable=import-error,no-name-in-module

    use_deferred = not bpy.app.background
    scene = bpy.context.scene
    rd = scene.render
    image_settings = rd.image_settings
    ffmpeg = rd.ffmpeg

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

    # Save original values and apply overrides.
    # For animation rendering in deferred (INVOKE_DEFAULT) mode, Blender
    # re-reads render settings for every frame, so settings must stay
    # overridden until the entire render completes.  They are restored
    # inside _check() once the job finishes, or immediately on error.
    _saved: list[tuple[object, str, object]] = []

    def _set(obj: object, attr: str, value: object) -> None:
        _saved.append((obj, attr, getattr(obj, attr)))
        setattr(obj, attr, value)

    def _restore() -> None:
        for obj, attr, orig in reversed(_saved):
            setattr(obj, attr, orig)

    # Optional frame-range overrides.
    if params.frame_start is not None:
        _set(scene, "frame_start", params.frame_start)
    if params.frame_end is not None:
        _set(scene, "frame_end", params.frame_end)

    # Optional resolution / fps overrides.
    _has_res = False
    if params.width is not None and params.width > 0:
        _set(rd, "resolution_x", params.width)
        _has_res = True
    if params.height is not None and params.height > 0:
        _set(rd, "resolution_y", params.height)
        _has_res = True
    if _has_res:
        _set(rd, "resolution_percentage", 100)
    if params.fps is not None and params.fps > 0:
        _set(rd, "fps", params.fps)
        _set(rd, "fps_base", 1)

    # Video output format.
    # Blender 5.1+: image_settings.media_type = 'VIDEO'
    # Older builds:  image_settings.file_format = 'FFMPEG'
    if hasattr(image_settings, "media_type"):
        _set(image_settings, "media_type", "VIDEO")
    else:
        _set(image_settings, "file_format", "FFMPEG")

    # Codec settings (H.264 in MPEG-4 container, no audio).
    for attr, value in [("format", "MPEG4"), ("codec", "H264"), ("audio_codec", "NONE")]:
        if hasattr(ffmpeg, attr):
            _set(ffmpeg, attr, value)

    # Capture actual render settings after overrides are applied.
    actual_start = scene.frame_start
    actual_end = scene.frame_end
    actual_w = rd.resolution_x
    actual_h = rd.resolution_y
    actual_fps = rd.fps

    # NOTE: `filepath` is saved/restored manually because the animation
    # render reads it after completion.
    orig_filepath = rd.filepath
    rd.filepath = output_path

    render_args: tuple[str, ...] = ('INVOKE_DEFAULT',) if use_deferred else ()

    try:
        bpy.ops.render.render(*render_args, animation=True)
    except RuntimeError as ex:
        rd.filepath = orig_filepath
        _restore()
        return Result(status="error", message=str(ex))

    if use_deferred:
        def _check() -> dict[str, object] | None:
            if bpy.app.is_job_running('RENDER'):
                return None
            rd.filepath = orig_filepath
            _restore()
            if os.path.exists(output_path):
                return {
                    "status": "ok",
                    "filepath": output_path,
                    "frame_start": actual_start,
                    "frame_end": actual_end,
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
    _restore()
    return Result(
        status="ok",
        filepath=output_path,
        frame_start=actual_start,
        frame_end=actual_end,
        width=actual_w,
        height=actual_h,
        fps=actual_fps,
    )
