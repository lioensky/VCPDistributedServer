# SPDX-FileCopyrightText: 2026 Blender Authors
#
# SPDX-License-Identifier: GPL-3.0-or-later

"""
Tool-code for listing all Actions stored in the current Blender file.
"""

__all__ = (
    "Params",
    "Result",
    "main",
)

from typing import Any, NamedTuple

# @include_begin: _template_tool_error.py
# @include_end


class Params(NamedTuple):
    pass  # no filter — always returns every action in bpy.data.actions


class Result(NamedTuple):
    status: str
    total: int
    actions: list[dict[str, Any]]


def _fcurve_count(action: object) -> int:
    """Return the total number of F-Curves across all layers/strips."""
    # Legacy actions expose fcurves directly.
    direct = getattr(action, "fcurves", None)
    if direct is not None:
        return len(direct)
    # New layered actions (Blender 4.4+).
    count = 0
    for layer in getattr(action, "layers", ()):
        for strip in getattr(layer, "strips", ()):
            for cb in getattr(strip, "channelbags", ()):
                count += len(getattr(cb, "fcurves", ()))
    return count


def main(params: Params) -> Result:
    import bpy  # pylint: disable=import-error,no-name-in-module

    actions: list[dict[str, Any]] = []
    for action in bpy.data.actions:
        try:
            fr = action.frame_range
            frame_start = round(float(fr[0]), 2)
            frame_end = round(float(fr[1]), 2)
        except (AttributeError, TypeError, IndexError):
            frame_start = 0.0
            frame_end = 0.0

        # Collect slot names for new-style actions (Blender 4.4+).
        slot_names: list[str] = []
        for slot in getattr(action, "slots", ()):
            slot_names.append(getattr(slot, "name", ""))

        actions.append({
            "name": action.name,
            "frame_start": frame_start,
            "frame_end": frame_end,
            "fcurve_count": _fcurve_count(action),
            "slots": slot_names,
        })

    return Result(
        status="ok",
        total=len(actions),
        actions=sorted(actions, key=lambda a: a["name"]),
    )
