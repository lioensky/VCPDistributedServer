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
from blmcp.tools.geonodes_node_set_toolcode import Params
from mcp.server.fastmcp import FastMCP  # pylint: disable=import-error,no-name-in-module
from mcp.types import ToolAnnotations  # pylint: disable=import-error,no-name-in-module

_TOOL_CALL = toolcode_wrap_with_calling_convention(toolcode_load_from_filepath(__file__))


def register(mcp: FastMCP) -> None:
    @mcp.tool(
        annotations=ToolAnnotations(title="Set Geometry Nodes Node Parameter",
                                    destructiveHint=True)
    )
    def geonodes_node_set(
        object_name: str,
        node_name: str,
        input_name: str,
        value: float,
    ) -> dict[str, object]:
        """
        Set the ``default_value`` of a node input socket in a Geometry Nodes
        graph.

        ``node_name`` is the display name of the node as returned by
        ``geonodes_query`` (e.g. ``"Multiply Frequency"``).

        ``input_name`` is the socket label (e.g. ``"Value"``,
        ``"Scale"``, ``"Strength"``).

        ``value`` is a scalar float; Blender automatically coerces it for
        integer or boolean socket types. For vector or geometry sockets
        use ``execute_blender_code``.

        Returns ``old_value`` and ``new_value`` so you can verify the
        change.
        """
        p = Params(
            object_name=object_name,
            node_name=node_name,
            input_name=input_name,
            value=value,
        )
        return send_code(toolcode_format_call(_TOOL_CALL, p), strict_json=True)
