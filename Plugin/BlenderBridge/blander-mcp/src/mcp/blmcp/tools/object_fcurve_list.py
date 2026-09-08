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
from blmcp.tools.object_fcurve_list_toolcode import Params
from mcp.server.fastmcp import FastMCP  # pylint: disable=import-error,no-name-in-module
from mcp.types import ToolAnnotations  # pylint: disable=import-error,no-name-in-module

_TOOL_CALL = toolcode_wrap_with_calling_convention(toolcode_load_from_filepath(__file__))


def register(mcp: FastMCP) -> None:
    @mcp.tool(
        annotations=ToolAnnotations(
            title="List Object F-Curve Keyframes",
            readOnlyHint=True,
        )
    )
    def object_fcurve_list(
        object_name: str,
        data_path: str,
    ) -> dict[str, object]:
        """
        Read F-Curve keyframe data for a transform property of a scene object.

        ``data_path`` selects the channel to query:

        - ``"location"``       — XYZ world-space position
        - ``"rotation_euler"`` — XYZ Euler rotation in radians
        - ``"scale"``          — XYZ scale factors

        Returns a ``curves`` list with one entry per axis (``array_index``
        0/1/2 for X/Y/Z). Each entry contains a sorted ``keyframes`` list
        of ``{"frame", "value", "interpolation"}`` dicts.

        If the object has no animation data or no keyframes for the
        requested path, ``curves`` is an empty list (not an error).

        Use ``object_keyframe_insert`` to add keyframes.
        """
        p = Params(object_name=object_name, data_path=data_path)
        return send_code(toolcode_format_call(_TOOL_CALL, p), strict_json=True)
