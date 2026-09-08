# SPDX-FileCopyrightText: 2026 Blender Authors
#
# SPDX-License-Identifier: GPL-3.0-or-later

"""
Tool-code for low-quality thumbnail rendering.
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

# Thumbnail render settings. Small resolution and low samples
# for a fast preview that is still useful for visual inspection.
# The longest dimension is clamped to this value, preserving aspect ratio.
_THUMB_DIMS_MAX = 320
_THUMB_SIMPLIFY_SUBDIV = 1
_THUMB_CYCLES_SAMPLES = 16
_THUMB_EEVEE_SAMPLES = 16


class Params(NamedTuple):
    output_path: str


class Result(NamedTuple):
    status: str
    filepath: str | None = None
    message: str | None = None


# @include_begin: _template_backup_attrs_and_assign_multi.py
@contextlib.contextmanager
def _backup_attrs_and_assign_multi(
        *obj_attrs: tuple[object, dict[str, object]],
) -> typing.Generator[None, None, None]:
    yield
# @include_end


# @include_begin: _template_deferred_tool_check_for_file_output.py
def _deferred_tool_check_for_file_output(
        job_type: str,
        output_path: str,
        restore_attrs: list[tuple[object, str, object]] | None = None,
) -> Callable[[], dict[str, object] | None]:
    return lambda: None
# @include_end


def main(params: Params) -> Result | Callable[[], dict[str, object] | None]:
    import os
    import bpy  # pylint: disable=import-error,no-name-in-module

    use_deferred = not bpy.app.background

    # Resolve the output path inside the MCP scratch directory.
    output_path = os.path.join(bpy.app.tempdir, "blender_mcp", os.path.basename(params.output_path))

    scene = bpy.context.scene
    rd = scene.render

    # Compute thumbnail resolution from originals, preserving aspect ratio.
    res_x = rd.resolution_x
    res_y = rd.resolution_y
    if res_x >= res_y:
        thumb_x = _THUMB_DIMS_MAX
        thumb_y = max(int(res_y * _THUMB_DIMS_MAX / res_x), 1)
    else:
        thumb_y = _THUMB_DIMS_MAX
        thumb_x = max(int(res_x * _THUMB_DIMS_MAX / res_y), 1)

    # NOTE: `filepath` is excluded from `_backup_attrs_and_assign_multi`
    # because `write_still` reads it after the render completes. With
    # `INVOKE_DEFAULT` the context manager would restore it before the
    # file is written. Instead, filepath is saved/restored manually.
    orig_filepath = rd.filepath
    rd.filepath = output_path

    obj_attrs: list[tuple[object, dict[str, object]]] = [
        (rd, {
            "resolution_x": thumb_x,
            "resolution_y": thumb_y,
            "resolution_percentage": 100,
            "use_simplify": True,
            "simplify_subdivision_render": _THUMB_SIMPLIFY_SUBDIV,
        }),
    ]
    if rd.engine == "CYCLES":
        obj_attrs.append((scene.cycles, {"samples": _THUMB_CYCLES_SAMPLES}))
    elif rd.engine == "BLENDER_EEVEE_NEXT":
        obj_attrs.append((scene.eevee, {"taa_render_samples": _THUMB_EEVEE_SAMPLES}))

    render_args = ('INVOKE_DEFAULT',) if use_deferred else ()

    with _backup_attrs_and_assign_multi(*obj_attrs):
        try:
            bpy.ops.render.render(*render_args, write_still=True)
        except RuntimeError as ex:
            rd.filepath = orig_filepath
            return Result(status="error", message=str(ex))

    if use_deferred:
        return _deferred_tool_check_for_file_output(
            'RENDER', output_path, restore_attrs=[(rd, "filepath", orig_filepath)],
        )

    rd.filepath = orig_filepath
    return Result(status="ok", filepath=output_path)
