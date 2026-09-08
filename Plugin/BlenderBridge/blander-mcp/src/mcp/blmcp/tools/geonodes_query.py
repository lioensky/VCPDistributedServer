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
from blmcp.tools.geonodes_query_toolcode import Params
from mcp.server.fastmcp import FastMCP  # pylint: disable=import-error,no-name-in-module
from mcp.types import ToolAnnotations  # pylint: disable=import-error,no-name-in-module

_TOOL_CALL = toolcode_wrap_with_calling_convention(toolcode_load_from_filepath(__file__))


def register(mcp: FastMCP) -> None:
    @mcp.tool(
        annotations=ToolAnnotations(title="Query Geometry Nodes Graph",
                                    readOnlyHint=True)
    )
    def geonodes_query(
        object_name: str,
        modifier_name: str = "",
    ) -> dict[str, object]:
        """
        Return the node graph structure of a Geometry Nodes modifier.

        ``modifier_name`` selects which NODES modifier to inspect. If
        empty the first NODES modifier on the object is used.

        Returns ``nodes`` — a list of node dicts, each with:

        - ``name``        — node display name
        - ``bl_idname``   — Blender node type identifier
        - ``location``    — ``[x, y]`` in the node editor
        - ``inputs``      — list of input sockets with ``name``,
          ``type``, ``is_linked``, and (when not linked)
          ``default_value``

        Use ``geonodes_apply_preset`` to create a Geometry Nodes modifier
        with a ready-made node graph.
        """
        p = Params(object_name=object_name, modifier_name=modifier_name)
        return send_code(toolcode_format_call(_TOOL_CALL, p), strict_json=True)
