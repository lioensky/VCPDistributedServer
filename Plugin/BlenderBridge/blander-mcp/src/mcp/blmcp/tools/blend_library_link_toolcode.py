# SPDX-FileCopyrightText: 2026 Blender Authors
#
# SPDX-License-Identifier: GPL-3.0-or-later

"""
Tool-code for linking objects or collections from a .blend file (Library Link).
"""

__all__ = (
    "Params",
    "Result",
    "main",
)

import os
from typing import NamedTuple

# @include_begin: _template_tool_error.py
# @include_end

_VALID_ASSET_TYPES = ("OBJECT", "COLLECTION")


class Params(NamedTuple):
    filepath: str       # absolute path to the .blend file
    asset_type: str     # "OBJECT" | "COLLECTION"
    asset_name: str     # name of the asset to link


class Result(NamedTuple):
    status: str
    filepath: str
    asset_type: str
    asset_name: str
    linked_objects: list[str]   # object names added to the scene


def _list_available(filepath: str, asset_type: str) -> list[str]:
    """Return names of available assets in the .blend file (read-only query)."""
    import bpy  # pylint: disable=import-error,no-name-in-module
    with bpy.data.libraries.load(filepath) as (data_src, _):
        if asset_type == "OBJECT":
            return sorted(data_src.objects)
        return sorted(data_src.collections)


def main(params: Params) -> "Result | ErrorResult":
    import bpy  # pylint: disable=import-error,no-name-in-module

    # Validate asset_type before the file-existence check so callers get
    # the most actionable error when multiple things are wrong.
    asset_type = params.asset_type.upper()
    if asset_type not in _VALID_ASSET_TYPES:
        return ErrorResult(
            status="error",
            error_code="INVALID_ASSET_TYPE",
            message="Asset type {!r} is not supported.".format(params.asset_type),
            current_state={"valid_asset_types": list(_VALID_ASSET_TYPES)},
            hint=(
                "Use asset_type='OBJECT' to link a single object, or "
                "'COLLECTION' to link a collection."
            ),
        )

    if not os.path.isfile(params.filepath):
        return ErrorResult(
            status="error",
            error_code="FILE_NOT_FOUND",
            message="Blend file not found: {!r}".format(params.filepath),
            current_state={"valid_asset_types": list(_VALID_ASSET_TYPES)},
            hint="Provide an absolute path to an existing .blend file.",
        )

    # Verify the asset exists in the file.
    try:
        available = _list_available(params.filepath, asset_type)
    except Exception as exc:  # pylint: disable=broad-exception-caught
        return ErrorResult(
            status="error",
            error_code="FILE_READ_ERROR",
            message="Cannot read {!r}: {}".format(params.filepath, exc),
            current_state={"valid_asset_types": list(_VALID_ASSET_TYPES)},
            hint="Ensure the file is a valid .blend file.",
        )

    if params.asset_name not in available:
        return ErrorResult(
            status="error",
            error_code="ASSET_NOT_FOUND",
            message=(
                "{:s} {!r} not found in {!r}.".format(
                    asset_type.title(), params.asset_name, params.filepath,
                )
            ),
            current_state={"available_assets": available},
            hint=(
                "Pick a name from `current_state.available_assets` "
                "and retry."
            ),
        )

    # Link the asset.
    before_objs = set(bpy.data.objects.keys())

    with bpy.data.libraries.load(params.filepath, link=True) as (_, data_to):
        if asset_type == "OBJECT":
            data_to.objects = [params.asset_name]
        else:
            data_to.collections = [params.asset_name]

    linked_objects: list[str] = []

    if asset_type == "OBJECT":
        for obj in data_to.objects:
            if obj is not None:
                try:
                    bpy.context.scene.collection.objects.link(obj)
                except RuntimeError:
                    # Object might already be linked to the scene.
                    pass
                linked_objects.append(obj.name)
    else:
        for coll in data_to.collections:
            if coll is not None:
                try:
                    bpy.context.scene.collection.children.link(coll)
                except RuntimeError:
                    pass
                # Collect all object names from the linked collection.
                for obj in coll.all_objects:
                    linked_objects.append(obj.name)

    # Also capture any brand-new objects that appeared in bpy.data.objects.
    after_objs = set(bpy.data.objects.keys())
    new_names = sorted(after_objs - before_objs)
    for name in new_names:
        if name not in linked_objects:
            linked_objects.append(name)

    return Result(
        status="ok",
        filepath=params.filepath,
        asset_type=asset_type,
        asset_name=params.asset_name,
        linked_objects=sorted(set(linked_objects)),
    )
