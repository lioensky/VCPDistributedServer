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
from blmcp.tools.action_list_toolcode import Params
from mcp.server.fastmcp import FastMCP  # pylint: disable=import-error,no-name-in-module
from mcp.types import ToolAnnotations  # pylint: disable=import-error,no-name-in-module

_TOOL_CALL = toolcode_wrap_with_calling_convention(toolcode_load_from_filepath(__file__))


def register(mcp: FastMCP) -> None:
    @mcp.tool(
        annotations=ToolAnnotations(title="List Scene Actions",
                                    readOnlyHint=True)
    )
    def action_list() -> dict[str, object]:
        """
        Return all Actions stored in the current Blender file.

        Each entry in ``actions`` contains:

        - ``name``          — action name
        - ``frame_start``   — first frame of the action's time range
        - ``frame_end``     — last frame of the action's time range
        - ``fcurve_count``  — total number of F-Curves (0 = empty action)
        - ``slots``         — list of slot names for new-style actions
          (Blender 4.4+); empty list for legacy single-slot actions

        Results are sorted alphabetically by action name.

        Use ``armature_action_apply`` to assign one of these actions to an
        armature object.
        """
        p = Params()
        return send_code(toolcode_format_call(_TOOL_CALL, p), strict_json=True)
