# SPDX-FileCopyrightText: 2026 Blender Authors
#
# SPDX-License-Identifier: GPL-3.0-or-later

# pylint: disable=C0114  # See tool doc-string.

__all__ = ("register",)

from blmcp.tools_helpers import (
    toolcode_format_call,
    toolcode_load_from_filepath,
    toolcode_wrap_with_calling_convention,
)
from blmcp.tools_helpers.connection import send_code
from blmcp.tools.geonodes_node_keyframe_toolcode import Params
from mcp.server.fastmcp import FastMCP  # pylint: disable=import-error,no-name-in-module
from mcp.types import ToolAnnotations  # pylint: disable=import-error,no-name-in-module

_TOOL_CALL = toolcode_wrap_with_calling_convention(toolcode_load_from_filepath(__file__))


def register(mcp: FastMCP) -> None:
    @mcp.tool(
        annotations=ToolAnnotations(title="Keyframe Geometry Nodes Node Parameter",
                                    destructiveHint=True)
    )
    def geonodes_node_keyframe(
        object_name: str,
        node_name: str,
        input_name: str,
        frame: int,
        value: float,
        interpolation: str = "BEZIER",
    ) -> dict[str, object]:
        """
        Insert a keyframe for a node input socket in a Geometry Nodes graph.

        Sets ``value`` on the socket's ``default_value`` and inserts a
        keyframe at ``frame``.  The keyframe is stored in the node tree's
        animation data and will appear in the Graph Editor under the node
        tree name.

        ``interpolation`` is one of ``"BEZIER"`` (default), ``"LINEAR"``,
        or ``"CONSTANT"``.

        Only scalar (float / int / bool) socket types are supported. For
        vector inputs use ``execute_blender_code``.

        Use ``geonodes_query`` to find node and input names.
        """
        p = Params(
            object_name=object_name,
            node_name=node_name,
            input_name=input_name,
            frame=frame,
            value=value,
            interpolation=interpolation,
        )
        return send_code(toolcode_format_call(_TOOL_CALL, p), strict_json=True)
