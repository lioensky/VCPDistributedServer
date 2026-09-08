# SPDX-FileCopyrightText: 2026 Blender Authors
#
# SPDX-License-Identifier: GPL-3.0-or-later

"""
Tool-code for creating a new Grease Pencil object in the scene.
"""

__all__ = (
    "Params",
    "Result",
    "main",
)

from typing import NamedTuple


class Params(NamedTuple):
    name: str


class Result(NamedTuple):
    status: str
    name: str
    collection: str


def main(params: Params) -> Result:
    import bpy  # pylint: disable=import-error,no-name-in-module

    gp_data = bpy.data.grease_pencils.new(params.name)
    obj = bpy.data.objects.new(params.name, gp_data)
    scene = bpy.context.scene
    scene.collection.objects.link(obj)

    return Result(
        status="ok",
        name=obj.name,
        collection=scene.collection.name,
    )
