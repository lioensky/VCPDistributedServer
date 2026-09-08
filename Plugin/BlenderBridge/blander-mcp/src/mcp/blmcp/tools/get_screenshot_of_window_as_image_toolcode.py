# SPDX-FileCopyrightText: 2026 Blender Authors
#
# SPDX-License-Identifier: GPL-3.0-or-later

"""
Tool-code for capturing a window screenshot as PNG.
"""

__all__ = (
    "Params",
    "Result",
    "main",
)

import base64
import os
import tempfile
from typing import NamedTuple

# MCP messages are limited to 1,048,576 bytes (1 MB). The image is base64-encoded
# which expands data by 4/3. A typical full-resolution PNG screenshot exceeds
# this, so we downscale iteratively until it fits.
_IMAGE_SIZE_LIMIT_IN_BYTES = (1_048_576 * 3) // 4


class Params(NamedTuple):
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

    size_limit = params.size_limit_in_bytes if params.size_limit_in_bytes > 0 else _IMAGE_SIZE_LIMIT_IN_BYTES

    with tempfile.TemporaryDirectory(prefix="blmcp_screenshot_") as tmpdir:
        filepath_screenshot = os.path.join(tmpdir, "screenshot.png")
        try:
            bpy.ops.screen.screenshot(filepath=filepath_screenshot)
        except RuntimeError as ex:
            return Result(status="error", message=str(ex))

        image_data = _image_downscale_to_size_limit(
            tmpdir, filepath_screenshot,
            size_limit_in_bytes=size_limit,
            size_tolerance_in_bytes=size_limit // 16,
        )
        data = base64.b64encode(image_data).decode("ascii")

    return Result(status="ok", image_base64=data)
