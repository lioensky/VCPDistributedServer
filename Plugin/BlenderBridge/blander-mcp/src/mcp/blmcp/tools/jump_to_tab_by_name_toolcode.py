# SPDX-FileCopyrightText: 2026 Blender Authors
#
# SPDX-License-Identifier: GPL-3.0-or-later

"""
Tool-code for switching workspace tabs by name.
"""

__all__ = (
    "Params",
    "Result",
    "main",
)

from typing import NamedTuple

# @include_begin: _template_tool_error.py
# @include_end


class Params(NamedTuple):
    name: str


class Result(NamedTuple):
    status: str
    workspace: str


def main(params: Params) -> "Result | ErrorResult":
    import bpy  # pylint: disable=import-error,no-name-in-module

    if bpy.app.background:
        return ErrorResult(
            status="error",
            error_code="BACKGROUND_MODE",
            message="Not available in background mode.",
            current_state={},
            hint="Rerun with an interactive Blender session.",
        )
    if bpy.context.window is None:
        return ErrorResult(
            status="error",
            error_code="NO_ACTIVE_WINDOW",
            message="No active window.",
            current_state={},
            hint="Ensure Blender has a visible window.",
        )

    ws = bpy.data.workspaces.get(params.name)
    if ws is None:
        available = [w.name for w in bpy.data.workspaces]
        return ErrorResult(
            status="error",
            error_code="WORKSPACE_NOT_FOUND",
            message="Workspace {!r} not found.".format(params.name),
            current_state={"available_workspaces": available},
            hint=(
                "Use a name from `current_state.available_workspaces`."
            ),
        )

    bpy.context.window.workspace = ws
    return Result(status="ok", workspace=ws.name)
