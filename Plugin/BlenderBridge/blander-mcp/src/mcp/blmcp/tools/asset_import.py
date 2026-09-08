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
from blmcp.tools.asset_import_toolcode import Params
from mcp.server.fastmcp import FastMCP  # pylint: disable=import-error,no-name-in-module
from mcp.types import ToolAnnotations  # pylint: disable=import-error,no-name-in-module

_TOOL_CALL = toolcode_wrap_with_calling_convention(toolcode_load_from_filepath(__file__))


def register(mcp: FastMCP) -> None:
    @mcp.tool(
        annotations=ToolAnnotations(title="Import 3D Asset File",
                                    destructiveHint=True)
    )
    def asset_import(
        filepath: str,
        format: str = "",
    ) -> dict[str, object]:
        """
        Import a 3D asset file into the current Blender scene.

        ``filepath`` must be an absolute path to an existing file.

        Supported formats:

        - ``"FBX"``   — Autodesk FBX (``*.fbx``)
        - ``"GLTF"``  — GL Transmission Format (``*.gltf``, ``*.glb``)
        - ``"OBJ"``   — Wavefront OBJ (``*.obj``)

        ``format`` overrides automatic detection; leave empty to detect
        from the file extension.

        Returns ``imported_objects`` — a list of the object names added
        to the scene by this import.  If the import adds no objects (e.g.
        the file is empty) the list is empty but ``status`` is still
        ``"ok"``.

        Requires the corresponding Blender extension to be installed and
        enabled (FBX, GLTF, or the built-in OBJ importer).
        """
        p = Params(filepath=filepath, format=format)
        return send_code(toolcode_format_call(_TOOL_CALL, p), strict_json=True)
