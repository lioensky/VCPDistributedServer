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
from blmcp.tools.geonodes_apply_preset_toolcode import Params
from mcp.server.fastmcp import FastMCP  # pylint: disable=import-error,no-name-in-module
from mcp.types import ToolAnnotations  # pylint: disable=import-error,no-name-in-module

_TOOL_CALL = toolcode_wrap_with_calling_convention(toolcode_load_from_filepath(__file__))


def register(mcp: FastMCP) -> None:
    @mcp.tool(
        annotations=ToolAnnotations(title="Apply Geometry Nodes Preset",
                                    destructiveHint=True)
    )
    def geonodes_apply_preset(
        object_name: str,
        preset: str,
        modifier_name: str = "",
    ) -> dict[str, object]:
        """
        Add a Geometry Nodes modifier with a pre-built node graph to an object.

        ``preset`` selects the graph template:

        - ``"wave"``           — Sine-wave Z-displacement driven by vertex
          X position. Exposed inputs: ``Amplitude`` (default 0.3),
          ``Frequency`` (default 2.0), ``Phase`` (default 0.0).
        - ``"noise_displace"`` — Random Z-displacement from a noise texture.
          Exposed inputs: ``Strength`` (default 0.5),
          ``Scale`` (default 2.0).

        ``modifier_name`` sets the modifier display name (defaults to a
        title-cased version of the preset name).

        If a NODES modifier with the same name already exists its node
        tree is replaced. Call ``geonodes_query`` to inspect the result,
        and ``geonodes_node_set`` / ``geonodes_node_keyframe`` to adjust
        parameters.
        """
        p = Params(
            object_name=object_name,
            preset=preset,
            modifier_name=modifier_name,
        )
        return send_code(toolcode_format_call(_TOOL_CALL, p), strict_json=True)
