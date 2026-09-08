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
from blmcp.tools.camera_target_track_toolcode import Params
from mcp.server.fastmcp import FastMCP  # pylint: disable=import-error,no-name-in-module
from mcp.types import ToolAnnotations  # pylint: disable=import-error,no-name-in-module

_TOOL_CALL = toolcode_wrap_with_calling_convention(toolcode_load_from_filepath(__file__))


def register(mcp: FastMCP) -> None:
    @mcp.tool(
        annotations=ToolAnnotations(
            title="Set Camera Track-To Target",
            destructiveHint=True,
        )
    )
    def camera_target_track(
        camera_name: str = "",
        target_name: str = "",
        target_location: list[float] | None = None,
        frame: int = -1,
        interpolation: str = "BEZIER",
    ) -> dict[str, object]:
        """
        Set up (or update) a Track-To constraint on a camera so it always
        looks at an Empty target object, and optionally insert a keyframe on
        the target's position.

        **Camera selection**
        - ``camera_name`` — name of a ``CAMERA`` object in the scene.
          Leave empty to use the active scene camera.

        **Target Empty**
        - ``target_name`` — name of the Empty to use as the look-at point.
          If the object does not exist it is created automatically.
          Defaults to ``"{camera_name}_Target"``.
        - ``target_location`` — ``[x, y, z]`` world-space position to move
          the target to. Omit to keep the target where it is.

        **Keyframing**
        - ``frame`` — frame number at which to insert a keyframe on the
          target's ``location`` channel. Requires ``target_location``.
          Pass ``-1`` (default) to skip keyframing.
        - ``interpolation`` — ``"BEZIER"`` (default), ``"LINEAR"``, or
          ``"CONSTANT"``.

        **Constraint details**
        The Track-To constraint uses ``track_axis = TRACK_NEGATIVE_Z``
        (camera looks along its −Z axis) and ``up_axis = UP_Y``.
        Calling this tool twice with the same target does not duplicate
        the constraint.

        To animate camera position, use ``object_keyframe_insert`` with
        the camera's name and the ``location`` channel.
        Use ``object_fcurve_list`` to verify written keyframes.
        """
        p = Params(
            camera_name=camera_name,
            target_name=target_name,
            target_location=target_location if target_location is not None else [],
            frame=frame,
            interpolation=interpolation,
        )
        return send_code(toolcode_format_call(_TOOL_CALL, p), strict_json=True)
