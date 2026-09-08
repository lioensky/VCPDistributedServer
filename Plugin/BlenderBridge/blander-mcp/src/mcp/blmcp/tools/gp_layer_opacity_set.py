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
from blmcp.tools.gp_layer_opacity_set_toolcode import Params
from mcp.server.fastmcp import FastMCP  # pylint: disable=import-error,no-name-in-module
from mcp.types import ToolAnnotations  # pylint: disable=import-error,no-name-in-module

_TOOL_CALL = toolcode_wrap_with_calling_convention(toolcode_load_from_filepath(__file__))


def register(mcp: FastMCP) -> None:
    @mcp.tool(
        annotations=ToolAnnotations(
            title="Set GP Layer Opacity Keyframe",
            destructiveHint=True,
        )
    )
    def gp_layer_opacity_set(
        object_name: str,
        layer_name: str,
        frame: int,
        opacity: float,
    ) -> dict[str, object]:
        """
        Set the opacity of a Grease Pencil layer and insert a keyframe.

        ``opacity`` must be in ``[0.0, 1.0]``: ``0.0`` is fully
        transparent, ``1.0`` is fully opaque.

        The keyframe is inserted at ``frame`` in the scene timeline.
        If a keyframe already exists at that frame it is overwritten.

        Call this multiple times with different ``frame`` values to
        build an opacity animation.  Use ``gp_layer_keyframes_list``
        afterwards to verify the inserted keyframes.

        Returns an error if the object or layer is not found, or if
        ``opacity`` is outside ``[0.0, 1.0]``.
        """
        p = Params(
            object_name=object_name,
            layer_name=layer_name,
            frame=frame,
            opacity=opacity,
        )
        return send_code(toolcode_format_call(_TOOL_CALL, p), strict_json=True)
