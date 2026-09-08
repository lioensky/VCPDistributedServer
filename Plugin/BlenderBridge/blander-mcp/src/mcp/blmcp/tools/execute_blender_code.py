# SPDX-FileCopyrightText: 2026 Blender Authors
#
# SPDX-License-Identifier: GPL-3.0-or-later

# pylint: disable=C0114  # See tool doc-string.

__all__ = (
    "register",
)

from blmcp.tools_helpers.blender_cli import run_blender_cli, synced_blend_for_cli
from blmcp.tools_helpers.connection import send_code
from mcp.server.fastmcp import FastMCP  # pylint: disable=import-error,no-name-in-module
from mcp.types import ToolAnnotations  # pylint: disable=import-error,no-name-in-module


def register(mcp: FastMCP) -> None:
    @mcp.tool(
        annotations=ToolAnnotations(
            title="Execute Python Code",
            destructiveHint=True,
        )
    )
    def execute_blender_code(code: str) -> dict[str, object]:
        """
        Execute Python code in the connected Blender instance.

        The code runs in Blender's Python environment with full access to ``bpy``.
        To return data, assign a JSON-serialisable dict to a variable named ``result``.
        Deferred completion via ``check_is_finished`` is only supported by the
        interactive addon server, and is rejected in background mode.
        """
        # Not strict: LLM-generated code may return non-JSON-serializable values
        # (e.g. Blender objects). Use `repr` as a fallback instead of erroring.
        return send_code(code, strict_json=False)

    @mcp.tool(
        annotations=ToolAnnotations(
            title="Execute Python Code for Command-Line",
            destructiveHint=True,
        )
    )
    def execute_blender_code_for_cli(blend_file: str, code: str) -> dict[str, object]:
        """
        Execute Python code in a background Blender process.

        Opens *blend_file* with ``blender --background`` and runs *code*.
        Assign a dict to ``result`` to return data.
        """
        # LLM-generated code may return non-JSON-serializable values
        # (e.g. Blender objects), handled by `run_blender_cli` via `default=repr`.
        with synced_blend_for_cli(blend_file) as synced_path:
            value = run_blender_cli(synced_path, code)
            assert isinstance(value, dict), "Expected dict from `run_blender_cli`, got {!r}".format(type(value))
            return value
