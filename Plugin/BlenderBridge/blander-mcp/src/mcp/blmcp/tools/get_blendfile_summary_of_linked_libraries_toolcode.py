# SPDX-FileCopyrightText: 2026 Blender Authors
#
# SPDX-License-Identifier: GPL-3.0-or-later

"""
Tool-code for linked library tree.
"""

__all__ = (
    "Result",
    "main",
)

from typing import NamedTuple


class Result(NamedTuple):
    status: str
    direct_libraries: list[dict[str, object]]
    indirect_libraries: list[dict[str, object]]
    total_library_count: int


def main(params: None) -> Result:
    del params
    import bpy  # pylint: disable=import-error,no-name-in-module

    direct: list[dict[str, object]] = []
    indirect: list[dict[str, object]] = []

    for lib in bpy.data.libraries:
        info: dict[str, object] = {
            "filepath": lib.filepath,
            "name": lib.name,
        }

        count = 0
        for attr in dir(bpy.data):
            collection = getattr(bpy.data, attr, None)
            if not hasattr(collection, "__iter__"):
                continue
            try:
                for item in collection:  # type: ignore[union-attr]
                    if hasattr(item, "library") and item.library == lib:
                        count += 1
            except Exception:  # pylint: disable=broad-exception-caught
                # Some `bpy.data` attributes look iterable but raise
                # when traversed. Safe to skip for counting purposes.
                pass
        info["linked_datablocks_count"] = count

        if lib.parent is None:
            direct.append(info)
        else:
            info["parent_library"] = lib.parent.name
            indirect.append(info)

    return Result(
        status="ok",
        direct_libraries=direct,
        indirect_libraries=indirect,
        total_library_count=len(bpy.data.libraries),
    )
