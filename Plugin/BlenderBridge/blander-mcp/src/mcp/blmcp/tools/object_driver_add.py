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
from blmcp.tools.object_driver_add_toolcode import Params
from mcp.server.fastmcp import FastMCP  # pylint: disable=import-error,no-name-in-module
from mcp.types import ToolAnnotations  # pylint: disable=import-error,no-name-in-module

_TOOL_CALL = toolcode_wrap_with_calling_convention(toolcode_load_from_filepath(__file__))


def register(mcp: FastMCP) -> None:
    @mcp.tool(
        annotations=ToolAnnotations(
            title="Add/Update Object Driver",
            destructiveHint=True,
        )
    )
    def object_driver_add(
        object_name: str,
        data_path: str,
        index: int,
        expression: str,
    ) -> dict[str, object]:
        """
        Add (or update) a scripted driver on a property of a scene object.

        A *driver* is a Python expression that controls a property value
        at every frame, enabling procedural animation without manual
        keyframing.

        **Parameters**

        - ``data_path``  — property channel to drive. Common values:
          ``"location"``, ``"rotation_euler"``, ``"scale"``.
        - ``index``      — array component: ``0`` = X, ``1`` = Y, ``2`` = Z.
          Use ``-1`` for scalar (non-array) properties.
        - ``expression`` — Python expression string evaluated each frame.
          The variable ``frame`` contains the current scene frame number.
          Maths functions (``sin``, ``cos``, ``pi``, etc.) are available
          without imports.

        **Examples**

        - Oscillate Z position: ``data_path="location", index=2,``
          ``expression="sin(frame/10)"``
        - Constant rotation: ``data_path="rotation_euler", index=2,``
          ``expression="frame * 0.1"``

        If a driver already exists at the given ``data_path`` / ``index``
        it is updated in place (``action`` field returns ``"updated"``).

        Use ``object_driver_list`` to read back and verify drivers.
        """
        p = Params(
            object_name=object_name,
            data_path=data_path,
            index=index,
            expression=expression,
        )
        return send_code(toolcode_format_call(_TOOL_CALL, p), strict_json=True)
