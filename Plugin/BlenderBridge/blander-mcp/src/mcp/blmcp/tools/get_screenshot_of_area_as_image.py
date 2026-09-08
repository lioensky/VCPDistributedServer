# SPDX-FileCopyrightText: 2026 Blender Authors
#
# SPDX-License-Identifier: GPL-3.0-or-later

# pylint: disable=C0114  # See tool doc-string.

__all__ = (
    "register",
)

import base64

from blmcp.tools_helpers import (
    toolcode_format_call,
    toolcode_load_from_filepath,
    toolcode_wrap_with_calling_convention,
)
from blmcp.tools_helpers.connection import send_code
from blmcp.tools.get_screenshot_of_area_as_image_toolcode import AreaUIType, Params
from mcp.server.fastmcp import FastMCP, Image  # pylint: disable=import-error,no-name-in-module
from mcp.types import ToolAnnotations  # pylint: disable=import-error,no-name-in-module

_TOOL_CALL = toolcode_wrap_with_calling_convention(toolcode_load_from_filepath(__file__))


def register(mcp: FastMCP) -> None:
    @mcp.tool(
        annotations=ToolAnnotations(
            title="Get Area Screenshot",
            readOnlyHint=True,
        )
    )
    def get_screenshot_of_area_as_image(
        area_ui_type: AreaUIType,
        size_limit_in_bytes: int = 0,
    ) -> Image:
        """
        Take a screenshot of a single Blender area and return it as a PNG image.

        *area_ui_type* matches the area's ``ui_type``.

        *size_limit_in_bytes* caps the image size in bytes.
        Zero (the default) uses the MCP message size limit.
        """
        p = Params(area_ui_type=area_ui_type, size_limit_in_bytes=size_limit_in_bytes)
        response = send_code(toolcode_format_call(_TOOL_CALL, p), strict_json=True)
        if response.get("status") != "ok":
            raise RuntimeError(str(response.get("message", "Unknown error")))
        result = response["result"]
        assert isinstance(result, dict)
        if result.get("status") != "ok":
            raise RuntimeError(str(result.get("message", "Unknown error")))
        return Image(data=base64.b64decode(str(result["image_base64"])), format="png")
