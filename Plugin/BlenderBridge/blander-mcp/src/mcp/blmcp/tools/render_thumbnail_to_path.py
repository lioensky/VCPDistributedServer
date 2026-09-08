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
from blmcp.tools.render_thumbnail_to_path_toolcode import Params
from mcp.server.fastmcp import FastMCP  # pylint: disable=import-error,no-name-in-module
from mcp.types import ToolAnnotations  # pylint: disable=import-error,no-name-in-module

_TOOL_CALL = toolcode_wrap_with_calling_convention(toolcode_load_from_filepath(__file__))


def register(mcp: FastMCP) -> None:
    @mcp.tool(
        annotations=ToolAnnotations(
            title="Render Thumbnail to Path",
            destructiveHint=True,
        )
    )
    def render_thumbnail_to_path(output_path: str) -> dict[str, object]:
        """
        Render a small, low-quality thumbnail to *output_path* (temporarily overrides settings).
        """
        p = Params(output_path=output_path)
        code = toolcode_format_call(_TOOL_CALL, p)
        return send_code(code, strict_json=True)
