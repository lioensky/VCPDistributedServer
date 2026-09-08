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
from blmcp.tools.blend_library_link_toolcode import Params
from mcp.server.fastmcp import FastMCP  # pylint: disable=import-error,no-name-in-module
from mcp.types import ToolAnnotations  # pylint: disable=import-error,no-name-in-module

_TOOL_CALL = toolcode_wrap_with_calling_convention(toolcode_load_from_filepath(__file__))


def register(mcp: FastMCP) -> None:
    @mcp.tool(
        annotations=ToolAnnotations(title="Link Asset from Blend File",
                                    destructiveHint=True)
    )
    def blend_library_link(
        filepath: str,
        asset_type: str,
        asset_name: str,
    ) -> dict[str, object]:
        """
        Link an object or collection from another ``.blend`` file into the
        current scene using Blender's **Library Link** mechanism.

        Linked assets remain read-only and are associated with the source
        file.  They appear in the Outliner with the external-link indicator
        (``obj.library`` is set).

        ``filepath`` — absolute path to the source ``.blend`` file.

        ``asset_type`` — ``"OBJECT"`` to link a single object, or
        ``"COLLECTION"`` to link a whole collection.

        ``asset_name`` — exact name of the object or collection inside the
        source file.  If the name is not found the error response includes
        ``current_state.available_assets`` listing what is in the file, so
        you can retry with a correct name.

        Returns ``linked_objects`` — the names of objects added to the
        scene.  For ``asset_type="COLLECTION"`` this includes all objects
        belonging to the linked collection.
        """
        p = Params(
            filepath=filepath,
            asset_type=asset_type,
            asset_name=asset_name,
        )
        return send_code(toolcode_format_call(_TOOL_CALL, p), strict_json=True)
