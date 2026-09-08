# SPDX-FileCopyrightText: 2026 Blender Authors
#
# SPDX-License-Identifier: GPL-3.0-or-later

"""
Tool-code for returning a tree of collections and their objects.
"""

__all__ = (
    "Result",
    "main",
)

from typing import Any, NamedTuple

# Placeholder types for Blender Python objects (no stubs available).
_Object = Any
_Collection = Any
_LayerCollection = Any


class Result(NamedTuple):
    status: str
    scene_name: str
    active_workspace: str | None
    active_object: str | None
    object_mode: str | None
    camera_object: str | None
    collections: list[dict[str, Any]]


def _object_info(obj: _Object) -> dict[str, Any]:
    info: dict[str, Any] = {
        "name": obj.name,
        "type": obj.type,
        "parent": obj.parent.name if obj.parent else None,
        "data_name": obj.data.name if obj.data else None,
        "selected": obj.select_get(),
        "visible": obj.visible_get(),
        "hide_viewport": obj.hide_get(),
    }
    if obj.type == 'EMPTY' and obj.instance_type == 'COLLECTION' and obj.instance_collection is not None:
        info["instance_collection"] = obj.instance_collection.name
    return info


def _layer_collection_tree(lc: _LayerCollection) -> dict[str, Any]:
    col = lc.collection
    return {
        "name": col.name,
        "exclude": lc.exclude,
        "hide_viewport": col.hide_viewport,
        "objects": sorted(
            [_object_info(obj) for obj in col.objects],
            key=lambda o: o["name"],
        ),
        "children": sorted(
            [_layer_collection_tree(child) for child in lc.children],
            key=lambda c: c["name"],
        ),
    }


def main(params: None) -> Result:
    del params
    from bpy import context  # pylint: disable=import-error,no-name-in-module

    scene = context.scene
    view_layer = context.view_layer

    root = view_layer.layer_collection
    collections = sorted(
        [_layer_collection_tree(root)],
        key=lambda c: c["name"],
    )

    active = view_layer.objects.active
    window = getattr(context, "window", None)
    return Result(
        status="ok",
        scene_name=scene.name,
        active_workspace=window.workspace.name if window else None,
        active_object=active.name if active else None,
        object_mode=context.mode if active else None,
        camera_object=scene.camera.name if scene.camera else None,
        collections=collections,
    )
