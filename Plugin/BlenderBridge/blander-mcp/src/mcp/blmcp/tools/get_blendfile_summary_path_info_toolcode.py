# SPDX-FileCopyrightText: 2026 Blender Authors
#
# SPDX-License-Identifier: GPL-3.0-or-later

"""
Tool-code for blend file path, save status, age, and backups.
"""

__all__ = (
    "Result",
    "main",
)

import os
import time
from typing import NamedTuple


# Blender appends a number (1-32) to the file path for each backup.
_MAX_BACKUPS = 32


class Result(NamedTuple):
    status: str
    filepath: str
    is_saved: bool
    is_dirty: bool
    age_seconds: float | None = None
    file_size_bytes: int | None = None
    backups: list[dict[str, object]] | None = None


def main(params: None) -> Result:
    del params
    import bpy  # pylint: disable=import-error,no-name-in-module

    filepath = bpy.data.filepath
    age = None
    size = None
    backups = None

    if filepath and os.path.exists(filepath):
        stat = os.stat(filepath)
        age = round(time.time() - stat.st_mtime, 1)
        size = stat.st_size

        backups = []
        for i in range(1, _MAX_BACKUPS + 1):
            backup_path = filepath + str(i)
            if not os.path.exists(backup_path):
                break
            bstat = os.stat(backup_path)
            backups.append({
                "path": backup_path,
                "age_seconds": round(time.time() - bstat.st_mtime, 1),
                "size_bytes": bstat.st_size,
            })

    return Result(
        status="ok",
        filepath=filepath,
        is_saved=bool(filepath),
        is_dirty=bpy.data.is_dirty,
        age_seconds=age,
        file_size_bytes=size,
        backups=backups,
    )
