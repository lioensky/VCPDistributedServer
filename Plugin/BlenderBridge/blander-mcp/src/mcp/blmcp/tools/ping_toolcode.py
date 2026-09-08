# SPDX-FileCopyrightText: 2026 Blender Authors
#
# SPDX-License-Identifier: GPL-3.0-or-later

"""
Tool-code for verifying Blender connectivity and returning its version.
"""

__all__ = (
    "Result",
    "main",
)

from typing import NamedTuple


class Result(NamedTuple):
    status: str
    blender_version: str


def main(params: None) -> Result:
    del params
    import bpy  # pylint: disable=import-error,no-name-in-module

    return Result(
        status="ok",
        blender_version=bpy.app.version_string,
    )
