# SPDX-FileCopyrightText: 2026 Blender Authors
#
# SPDX-License-Identifier: GPL-3.0-or-later

"""
Tool-code for switching workspace tabs by space-type.
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
    space_type: str
    allow_edits: bool


class Result(NamedTuple):
    status: str
    workspace: str
    space_type: str
    created: bool | None = None


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

    def _largest_area(screen: "bpy.types.Screen") -> "bpy.types.Area | None":
        return max(screen.areas, key=lambda a: a.width * a.height, default=None)

    found = None
    for ws in bpy.data.workspaces:
        for screen in ws.screens:
            area = _largest_area(screen)
            if area is not None and area.type == params.space_type:
                found = ws
                break
        if found:
            break

    if found:
        bpy.context.window.workspace = found
        return Result(
            status="ok",
            workspace=found.name,
            space_type=params.space_type,
        )

    if params.allow_edits:
        try:
            bpy.ops.workspace.duplicate()
        except RuntimeError as ex:
            return ErrorResult(
                status="error",
                error_code="OPERATION_FAILED",
                message=str(ex),
                current_state={},
                hint="Try switching to a different workspace first.",
            )
        new_ws = bpy.context.window.workspace
        new_ws.name = params.space_type.replace("_", " ").title()
        area = _largest_area(bpy.context.screen)
        if area is not None:
            area.type = params.space_type
        return Result(
            status="ok",
            workspace=new_ws.name,
            space_type=params.space_type,
            created=True,
        )

    available = sorted({
        area.type
        for ws in bpy.data.workspaces
        for screen in ws.screens
        for area in ((_largest_area(screen),) if _largest_area(screen) else ())
        if area is not None
    })
    return ErrorResult(
        status="error",
        error_code="SPACE_TYPE_NOT_FOUND",
        message="No workspace with space type {!r} found.".format(
            params.space_type
        ),
        current_state={"available_space_types": available},
        hint=(
            "Set `allow_edits=True` to create a new workspace, "
            "or use a type from `current_state.available_space_types`."
        ),
    )
