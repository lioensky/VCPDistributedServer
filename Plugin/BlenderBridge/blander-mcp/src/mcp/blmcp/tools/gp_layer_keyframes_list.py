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
from blmcp.tools.gp_layer_keyframes_list_toolcode import Params
from mcp.server.fastmcp import FastMCP  # pylint: disable=import-error,no-name-in-module
from mcp.types import ToolAnnotations  # pylint: disable=import-error,no-name-in-module

_TOOL_CALL = toolcode_wrap_with_calling_convention(toolcode_load_from_filepath(__file__))


def register(mcp: FastMCP) -> None:
    @mcp.tool(
        annotations=ToolAnnotations(
            title="List GP Layer Opacity Keyframes",
            readOnlyHint=True,
        )
    )
    def gp_layer_keyframes_list(
        object_name: str,
        layer_name: str,
    ) -> dict[str, object]:
        """
        Return all opacity keyframes on a Grease Pencil layer, sorted by frame.

        Each entry in ``keyframes`` contains:

        - ``frame``: the scene frame number (integer).
        - ``opacity``: the opacity value at that frame (float, 0.0–1.0).

        Returns an empty ``keyframes`` list if no opacity keyframes have
        been set on this layer yet.

        Use ``gp_layer_opacity_set`` to insert keyframes, then call
        this tool to verify the animation curve before rendering.

        Returns an error if the object or layer is not found.
        """
        p = Params(object_name=object_name, layer_name=layer_name)
        return send_code(toolcode_format_call(_TOOL_CALL, p), strict_json=True)
