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
from blmcp.tools.object_driver_list_toolcode import Params
from mcp.server.fastmcp import FastMCP  # pylint: disable=import-error,no-name-in-module
from mcp.types import ToolAnnotations  # pylint: disable=import-error,no-name-in-module

_TOOL_CALL = toolcode_wrap_with_calling_convention(toolcode_load_from_filepath(__file__))


def register(mcp: FastMCP) -> None:
    @mcp.tool(
        annotations=ToolAnnotations(
            title="List Object Drivers",
            readOnlyHint=True,
        )
    )
    def object_driver_list(
        object_name: str,
    ) -> dict[str, object]:
        """
        List all drivers attached to a scene object.

        Returns a ``drivers`` list sorted by ``data_path`` then ``index``.
        Each entry contains:

        - ``data_path``   — the driven property (e.g. ``"location"``)
        - ``index``       — array component (0/1/2 for X/Y/Z, -1 for scalar)
        - ``driver_type`` — ``"SCRIPTED"`` for expression drivers,
          ``"AVERAGE"`` / ``"SUM"`` / ``"MIN"`` / ``"MAX"`` for
          variable-based drivers
        - ``expression``  — the formula string (non-empty for
          ``"SCRIPTED"`` type only)
        - ``is_valid``    — ``false`` if Blender flagged the driver as
          invalid (e.g. syntax error in expression)

        If the object has no drivers, ``drivers`` is an empty list.

        Use ``object_driver_add`` to add or update drivers.
        """
        p = Params(object_name=object_name)
        return send_code(toolcode_format_call(_TOOL_CALL, p), strict_json=True)
