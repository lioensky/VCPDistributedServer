# SPDX-FileCopyrightText: 2026 Blender Authors
#
# SPDX-License-Identifier: GPL-3.0-or-later

# pylint: disable=C0114  # See tool doc-string.

__all__ = (
    "register",
)

from typing import Any

from blmcp.tools_helpers import (
    toolcode_format_call,
    toolcode_load_from_filepath,
    toolcode_wrap_with_calling_convention,
)
from blmcp.tools_helpers.connection import send_code
from blmcp.tools.object_modifier_add_toolcode import Params
from mcp.server.fastmcp import FastMCP  # pylint: disable=import-error,no-name-in-module
from mcp.types import ToolAnnotations  # pylint: disable=import-error,no-name-in-module

_TOOL_CALL = toolcode_wrap_with_calling_convention(toolcode_load_from_filepath(__file__))


def register(mcp: FastMCP) -> None:
    @mcp.tool(
        annotations=ToolAnnotations(
            title="Add Object Modifier",
            destructiveHint=True,
        )
    )
    def object_modifier_add(
        object_name: str,
        modifier_type: str,
        name: str = "",
        params: dict[str, Any] | None = None,
    ) -> dict[str, object]:
        """
        Add a modifier to a scene object and optionally configure its parameters.

        ``modifier_type`` is the Blender modifier type string (uppercase).
        Common values:

        - ``"SUBSURF"``   — Subdivision Surface (params: ``levels``,
          ``render_levels``, ``subdivision_type``)
        - ``"WAVE"``      — Wave deform (params: ``height``, ``width``,
          ``speed``, ``use_x``, ``use_y``)
        - ``"SOLIDIFY"``  — Solidify (params: ``thickness``, ``offset``)
        - ``"BEVEL"``     — Bevel (params: ``width``, ``segments``)
        - ``"ARRAY"``     — Array (params: ``count``, ``relative_offset_displace``)
        - ``"MIRROR"``    — Mirror (params: ``use_axis``)
        - ``"DECIMATE"``  — Decimate (params: ``ratio``)

        ``name`` sets the modifier's display name. Defaults to a
        capitalised form of ``modifier_type``.

        ``params`` is a dict of modifier-specific attribute names and
        values (e.g. ``{"levels": 2}``). Unknown or read-only keys are
        silently skipped and reported in ``failed_params``.

        Use ``object_modifiers_list`` to inspect the modifier after creation.
        Use ``get_object_detail_summary`` to confirm the modifier appears
        in the object's modifier stack.
        """
        p = Params(
            object_name=object_name,
            modifier_type=modifier_type,
            name=name,
            params=params if params is not None else {},
        )
        return send_code(toolcode_format_call(_TOOL_CALL, p), strict_json=True)
