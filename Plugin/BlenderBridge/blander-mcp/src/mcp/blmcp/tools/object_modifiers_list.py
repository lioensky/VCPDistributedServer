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
from blmcp.tools.object_modifiers_list_toolcode import Params
from mcp.server.fastmcp import FastMCP  # pylint: disable=import-error,no-name-in-module
from mcp.types import ToolAnnotations  # pylint: disable=import-error,no-name-in-module

_TOOL_CALL = toolcode_wrap_with_calling_convention(toolcode_load_from_filepath(__file__))


def register(mcp: FastMCP) -> None:
    @mcp.tool(
        annotations=ToolAnnotations(
            title="List Object Modifiers",
            readOnlyHint=True,
        )
    )
    def object_modifiers_list(
        object_name: str,
    ) -> dict[str, object]:
        """
        List all modifiers on a scene object together with their parameters.

        Returns a ``modifiers`` list. Each entry contains:

        - ``name``          — modifier display name
        - ``type``          — modifier type string (e.g. ``"SUBSURF"``)
        - ``show_viewport`` — whether the modifier is visible in the viewport
        - ``show_render``   — whether the modifier is applied at render time
        - ``params``        — dict of the modifier's current attribute values
          (booleans, integers, floats, strings, and enums only)

        If the object has no modifiers, ``modifiers`` is an empty list.

        Use ``object_modifier_add`` to add modifiers to the object.
        Use ``get_object_detail_summary`` for a higher-level overview.
        """
        p = Params(object_name=object_name)
        return send_code(toolcode_format_call(_TOOL_CALL, p), strict_json=True)
