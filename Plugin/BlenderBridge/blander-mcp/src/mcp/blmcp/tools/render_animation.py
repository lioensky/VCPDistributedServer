# SPDX-FileCopyrightText: 2026 Blender Authors
#
# SPDX-License-Identifier: GPL-3.0-or-later

# pylint: disable=C0114  # See tool doc-string.

__all__ = (
    "register",
)

from blmcp.tools_helpers import (
    toolcode_format_call,
    toolcode_load_from_filepath,
    toolcode_wrap_with_calling_convention,
)
from blmcp.tools_helpers.connection import send_code
from blmcp.tools.render_animation_toolcode import Params
from mcp.server.fastmcp import FastMCP  # pylint: disable=import-error,no-name-in-module
from mcp.types import ToolAnnotations  # pylint: disable=import-error,no-name-in-module

_TOOL_CALL = toolcode_wrap_with_calling_convention(toolcode_load_from_filepath(__file__))


def register(mcp: FastMCP) -> None:
    @mcp.tool(
        annotations=ToolAnnotations(
            title="Render Animation to Video",
            destructiveHint=False,
        )
    )
    def render_animation(
        output_path: str,
        frame_start: int | None = None,
        frame_end: int | None = None,
        width: int | None = None,
        height: int | None = None,
        fps: int | None = None,
    ) -> dict[str, object]:
        """
        Render a frame sequence and write a video file (H.264 / MPEG-4).

        ``output_path`` sets the destination.  Absolute paths are used
        as-is; relative paths are placed inside Blender's temp directory.
        The file extension should be ``.mp4``.

        Optional overrides (all default to current scene settings):

        - ``frame_start`` / ``frame_end``: inclusive frame range to render.
          Both default to ``scene.frame_start`` / ``scene.frame_end``.
        - ``width`` / ``height``: render resolution in pixels.
          Internally sets ``resolution_percentage = 100``.
        - ``fps``: frames-per-second.  Overrides ``scene.render.fps`` and
          sets ``fps_base`` to 1.

        Video encoding uses H.264 in an MPEG-4 container with no audio.
        On Blender 5.1+, ``image_settings.media_type = 'VIDEO'`` is used;
        older builds fall back to ``file_format = 'FFMPEG'``.
        All settings are restored after the render.

        Returns ``filepath``, ``frame_start``, ``frame_end``, ``width``,
        ``height``, and ``fps`` in the success result.
        """
        p = Params(
            output_path=output_path,
            frame_start=frame_start,
            frame_end=frame_end,
            width=width,
            height=height,
            fps=fps,
        )
        return send_code(toolcode_format_call(_TOOL_CALL, p), strict_json=True)
