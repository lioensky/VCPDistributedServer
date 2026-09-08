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
from blmcp.tools.render_frame_toolcode import Params
from mcp.server.fastmcp import FastMCP  # pylint: disable=import-error,no-name-in-module
from mcp.types import ToolAnnotations  # pylint: disable=import-error,no-name-in-module

_TOOL_CALL = toolcode_wrap_with_calling_convention(toolcode_load_from_filepath(__file__))


def register(mcp: FastMCP) -> None:
    @mcp.tool(
        annotations=ToolAnnotations(
            title="Render Frame to Image",
            destructiveHint=False,
        )
    )
    def render_frame(
        output_path: str,
        frame: int | None = None,
        width: int | None = None,
        height: int | None = None,
        fps: int | None = None,
    ) -> dict[str, object]:
        """
        Render a single frame of the current scene to an image file.

        ``output_path`` sets the destination. Absolute paths are used
        as-is; relative paths are placed inside Blender's temp directory.

        Optional overrides (all default to the current scene settings):

        - ``frame``: scene frame number to render (``None`` = current frame).
        - ``width`` / ``height``: render resolution in pixels; both default
          to the scene resolution.  If only one is provided the other keeps
          the scene value.  Set ``resolution_percentage`` to 100 internally
          so the values are exact.
        - ``fps``: frames-per-second; overrides ``scene.render.fps`` and
          sets ``fps_base`` to 1.

        All overrides are temporary and are restored after the render.

        Returns ``filepath``, ``frame``, ``width``, ``height``, and ``fps``
        in the success result.  Returns an error if Blender's render
        operator raises a ``RuntimeError``.
        """
        p = Params(
            output_path=output_path,
            frame=frame,
            width=width,
            height=height,
            fps=fps,
        )
        return send_code(toolcode_format_call(_TOOL_CALL, p), strict_json=True)
