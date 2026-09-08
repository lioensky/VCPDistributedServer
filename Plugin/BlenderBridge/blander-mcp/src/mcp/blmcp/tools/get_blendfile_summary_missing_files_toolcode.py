# SPDX-FileCopyrightText: 2026 Blender Authors
#
# SPDX-License-Identifier: GPL-3.0-or-later

"""
Tool-code for reporting missing external file references.
"""

__all__ = (
    "Result",
    "main",
)

import os
from typing import NamedTuple


class Result(NamedTuple):
    status: str
    missing_files: list[dict[str, str]]
    total_checked: int


def main(params: None) -> Result:
    del params
    import bpy  # pylint: disable=import-error,no-name-in-module

    missing: list[dict[str, str]] = []
    checked = 0

    def _visit(id_data: object, path: str, _placeholder: object) -> None:
        nonlocal checked
        checked += 1
        filepath = bpy.path.abspath(path)
        if not os.path.exists(filepath):
            missing.append({
                "id_type": type(id_data).__name__,
                "id_name": getattr(id_data, "name", ""),
                "path": filepath,
            })

    bpy.data.file_path_foreach(
        _visit,
        flags={"SKIP_PACKED", "SKIP_WEAK_REFERENCES", "RESOLVE_TOKEN"},
    )

    return Result(status="ok", missing_files=missing, total_checked=checked)
