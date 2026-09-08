# SPDX-FileCopyrightText: 2026 Blender Authors
#
# SPDX-License-Identifier: GPL-3.0-or-later

"""
Tool-code for JSON window layout description.
"""

__all__ = (
    "Result",
    "main",
)

from typing import NamedTuple


class Result(NamedTuple):
    status: str
    window_width: int
    window_height: int
    screen_name: str
    workspace: str
    scene: str
    areas: list[dict[str, object]]
    active_object: dict[str, object] | None
    selected_objects: list[dict[str, str]]
    message: str | None = None


def main(params: None) -> Result:
    del params
    import bpy  # pylint: disable=import-error,no-name-in-module
    from bpy import context  # pylint: disable=import-error,no-name-in-module

    error: str | None = None
    window = context.window
    if bpy.app.background:
        error = "Window layout is not available in background mode"
    elif window is None:
        error = "No active window"

    if error is not None:
        return Result(
            status="error",
            window_width=0,
            window_height=0,
            screen_name="",
            workspace="",
            scene="",
            areas=[],
            active_object=None,
            selected_objects=[],
            message=error,
        )
    screen = window.screen

    areas: list[dict[str, object]] = []
    for area in screen.areas:
        area_info: dict[str, object] = {
            "type": area.type,
            "x": area.x,
            "y": area.y,
            "width": area.width,
            "height": area.height,
        }

        space = area.spaces.active
        if space:
            space_info: dict[str, object] = {"type": space.type}

            if space.type == "VIEW_3D":
                r3d = space.region_3d
                if r3d:
                    space_info["view_perspective"] = r3d.view_perspective
                    space_info["view_location"] = list(r3d.view_location)
                if hasattr(space, "shading"):
                    space_info["shading_type"] = space.shading.type
                space_info["show_overlays"] = space.overlay.show_overlays

            elif space.type == "PROPERTIES":
                space_info["context"] = space.context

            elif space.type == "OUTLINER":
                space_info["display_mode"] = space.display_mode

            elif space.type == "TEXT_EDITOR":
                if space.text:
                    space_info["text_name"] = space.text.name

            elif space.type == "NODE_EDITOR":
                space_info["tree_type"] = space.tree_type
                if space.node_tree:
                    space_info["node_tree_name"] = space.node_tree.name

            area_info["space"] = space_info

        regions: list[dict[str, object]] = []
        for region in area.regions:
            if region.width > 0 and region.height > 0:
                regions.append({
                    "type": region.type,
                    "x": region.x,
                    "y": region.y,
                    "width": region.width,
                    "height": region.height,
                })
        area_info["regions"] = regions
        areas.append(area_info)

    active = context.active_object
    active_info = None
    if active:
        active_info = {
            "name": active.name,
            "type": active.type,
            "mode": context.mode,
            "location": list(active.location),
        }

    selected = [{"name": obj.name, "type": obj.type} for obj in context.selected_objects]

    return Result(
        status="ok",
        window_width=window.width,
        window_height=window.height,
        screen_name=screen.name,
        workspace=window.workspace.name,
        scene=context.scene.name,
        areas=areas,
        active_object=active_info,
        selected_objects=selected,
    )
