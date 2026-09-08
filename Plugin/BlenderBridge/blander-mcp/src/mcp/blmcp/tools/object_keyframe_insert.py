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
from blmcp.tools.object_keyframe_insert_toolcode import Params
from mcp.server.fastmcp import FastMCP  # pylint: disable=import-error,no-name-in-module
from mcp.types import ToolAnnotations  # pylint: disable=import-error,no-name-in-module

_TOOL_CALL = toolcode_wrap_with_calling_convention(toolcode_load_from_filepath(__file__))


def register(mcp: FastMCP) -> None:
    @mcp.tool(
        annotations=ToolAnnotations(
            title="Insert Object Transform Keyframe",
            destructiveHint=True,
        )
    )
    def object_keyframe_insert(
        object_name: str,
        frame: int,
        location: list[float] | None = None,
        rotation: list[float] | None = None,
        scale: list[float] | None = None,
        interpolation: str = "BEZIER",
    ) -> dict[str, object]:
        """
        Insert transform keyframes on a scene object at the given frame.

        At least one of ``location``, ``rotation``, or ``scale`` must be
        provided.

        - ``location``  — ``[x, y, z]`` in world space
        - ``rotation``  — ``[x, y, z]`` Euler angles in **radians**
          (uses the object's ``rotation_euler`` channel)
        - ``scale``     — ``[x, y, z]`` scale factors (1.0 = unchanged)
        - ``interpolation`` — keyframe interpolation mode for the new
          keyframe points: ``"BEZIER"`` (default), ``"LINEAR"``,
          or ``"CONSTANT"``

        Only the properties explicitly provided receive a keyframe; others
        are left untouched. The returned ``inserted`` list names which
        data-paths were keyed (e.g. ``["location", "rotation_euler"]``).

        Use ``object_fcurve_list`` to verify the written keyframes.
        """
        p = Params(
            object_name=object_name,
            frame=frame,
            location=location if location is not None else [],
            rotation=rotation if rotation is not None else [],
            scale=scale if scale is not None else [],
            interpolation=interpolation,
        )
        return send_code(toolcode_format_call(_TOOL_CALL, p), strict_json=True)
