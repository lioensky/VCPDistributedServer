# SPDX-FileCopyrightText: 2026 Blender Authors
#
# SPDX-License-Identifier: GPL-3.0-or-later

"""
Tool-code for capturing a single area screenshot as PNG.
"""

__all__ = (
    "AreaUIType",
    "Params",
    "Result",
    "main",
)

import base64
import os
import tempfile
from typing import Literal, NamedTuple

# MCP messages are limited to 1,048,576 bytes (1 MB). The image is base64-encoded
# which expands data by 4/3. A typical full-resolution PNG screenshot exceeds
# this, so we downscale iteratively until it fits.
_IMAGE_SIZE_LIMIT_IN_BYTES = (1_048_576 * 3) // 4

# Rarely changes, regenerate with:
# `list(bpy.types.Area.bl_rna.properties["ui_type"].enum_items.keys())`
AreaUIType = Literal[
    # "EMPTY",  # Part of the enum but never visible to users.
    "VIEW_3D",
    "IMAGE_EDITOR",
    "UV",
    "ShaderNodeTree",
    "CompositorNodeTree",
    "GeometryNodeTree",
    "TextureNodeTree",
    "SEQUENCE_EDITOR",
    "CLIP_EDITOR",
    "DOPESHEET_EDITOR",
    "GRAPH_EDITOR",
    "NLA_EDITOR",
    "TEXT_EDITOR",
    "CONSOLE",
    "INFO",
    "TOPBAR",
    "STATUSBAR",
    "OUTLINER",
    "PROPERTIES",
    "FILE_BROWSER",
    "SPREADSHEET",
    "PREFERENCES",
]


class Params(NamedTuple):
    area_ui_type: AreaUIType
    size_limit_in_bytes: int = 0


class Result(NamedTuple):
    status: str
    image_base64: str | None = None
    message: str | None = None


# @include_begin: _template_image_downscale_to_size_limit.py
def _image_downscale_to_size_limit(
        tmpdir: str, filepath: str, size_limit_in_bytes: int, size_tolerance_in_bytes: int = 0,
) -> bytes:
    return b''
# @include_end


def main(params: Params) -> Result:
    import bpy  # pylint: disable=import-error,no-name-in-module
    from bpy import context  # pylint: disable=import-error,no-name-in-module

    if bpy.app.background:
        return Result(status="error", message="Screenshots are not available in background mode")

    window = context.window
    if window is None:
        return Result(status="error", message="No active window")
    screen = window.screen

    # Prefer the context's active area if it matches,
    # otherwise pick the largest matching area.
    area = context.area
    if area is None or area.ui_type != params.area_ui_type:
        area = next(iter(sorted(
            (a for a in screen.areas if a.ui_type == params.area_ui_type),
            key=lambda a: -(a.width * a.height),
        )), None)
    if area is None:
        available = sorted({a.ui_type for a in screen.areas})
        return Result(
            status="error",
            message="No area with type {!r} found. Available: {:s}".format(
                params.area_ui_type, ", ".join(available),
            ),
        )

    size_limit = params.size_limit_in_bytes if params.size_limit_in_bytes > 0 else _IMAGE_SIZE_LIMIT_IN_BYTES

    with tempfile.TemporaryDirectory(prefix="blmcp_screenshot_") as tmpdir:
        filepath_screenshot = os.path.join(tmpdir, "screenshot.png")
        with context.temp_override(window=window, area=area):
            try:
                bpy.ops.screen.screenshot_area(filepath=filepath_screenshot)
            except RuntimeError as ex:
                return Result(status="error", message=str(ex))

        image_data = _image_downscale_to_size_limit(
            tmpdir, filepath_screenshot,
            size_limit_in_bytes=size_limit,
            size_tolerance_in_bytes=size_limit // 16,
        )
        data = base64.b64encode(image_data).decode("ascii")

    return Result(status="ok", image_base64=data)
