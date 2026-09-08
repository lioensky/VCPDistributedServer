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
from blmcp.tools.armature_action_apply_toolcode import Params
from mcp.server.fastmcp import FastMCP  # pylint: disable=import-error,no-name-in-module
from mcp.types import ToolAnnotations  # pylint: disable=import-error,no-name-in-module

_TOOL_CALL = toolcode_wrap_with_calling_convention(toolcode_load_from_filepath(__file__))


def register(mcp: FastMCP) -> None:
    @mcp.tool(
        annotations=ToolAnnotations(title="Apply Action to Armature",
                                    destructiveHint=True)
    )
    def armature_action_apply(
        armature_name: str,
        action_name: str,
    ) -> dict[str, object]:
        """
        Assign an existing Action to an Armature object so that the bones
        animate according to the Action's F-Curves.

        ``armature_name`` must be an object of type ``ARMATURE`` in the
        scene.

        ``action_name`` must already exist in ``bpy.data.actions``.  Use
        ``action_list`` to discover available actions.

        Works with both legacy (single-slot) and the new slot-based actions
        introduced in Blender 4.4.

        Returns ``frame_start`` and ``frame_end`` — the time range of the
        applied action — so you can adjust the scene's frame range if needed.

        To animate an IK target after applying the action, create an Empty
        object and use ``object_keyframe_insert`` with ``location`` to
        keyframe its position at each key frame.
        """
        p = Params(armature_name=armature_name, action_name=action_name)
        return send_code(toolcode_format_call(_TOOL_CALL, p), strict_json=True)
