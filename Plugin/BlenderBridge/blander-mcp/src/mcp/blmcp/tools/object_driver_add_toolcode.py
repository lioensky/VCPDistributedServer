# SPDX-FileCopyrightText: 2026 Blender Authors
#
# SPDX-License-Identifier: GPL-3.0-or-later

"""
Tool-code for adding or updating a scripted driver on a scene object property.
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
    object_name: str
    data_path: str   # e.g. "location", "rotation_euler", "scale"
    index: int       # array index (0=X 1=Y 2=Z); -1 for scalar props
    expression: str  # driver formula, e.g. "sin(frame/10)"


class Result(NamedTuple):
    status: str
    object_name: str
    data_path: str
    index: int
    expression: str
    # "added" when a new driver FCurve was created, "updated" if one existed.
    action: str


def _get_object_names() -> list[str]:
    import bpy  # pylint: disable=import-error,no-name-in-module
    return sorted(obj.name for obj in bpy.data.objects)


def main(params: Params) -> "Result | ErrorResult":
    import bpy  # pylint: disable=import-error,no-name-in-module

    obj = bpy.data.objects.get(params.object_name)
    if obj is None:
        return ErrorResult(
            status="error",
            error_code="OBJECT_NOT_FOUND",
            message="Object {!r} not found.".format(params.object_name),
            current_state={"available_objects": _get_object_names()},
            hint=(
                "Use `get_scene_state` to list objects, "
                "or `mesh_primitive_add` to create one."
            ),
        )

    if not params.expression.strip():
        return ErrorResult(
            status="error",
            error_code="EMPTY_EXPRESSION",
            message="Driver expression must not be empty.",
            current_state={
                "example_expressions": [
                    "sin(frame/10)",
                    "cos(frame/20)",
                    "frame * 0.1",
                ],
            },
            hint=(
                "Provide a Python expression such as 'sin(frame/10)'. "
                "The variable 'frame' refers to the current scene frame."
            ),
        )

    # Check whether a driver already exists at this data_path / index.
    existing_fc = None
    if obj.animation_data:
        for fc in obj.animation_data.drivers:
            if (fc.data_path == params.data_path
                    and fc.array_index == params.index):
                existing_fc = fc
                break

    action = "updated" if existing_fc is not None else "added"

    if existing_fc is not None:
        fcurve = existing_fc
    else:
        try:
            if params.index >= 0:
                fcurve = obj.driver_add(params.data_path, params.index)
            else:
                fcurve = obj.driver_add(params.data_path)
        except Exception as exc:  # pylint: disable=broad-exception-caught
            return ErrorResult(
                status="error",
                error_code="DRIVER_ADD_FAILED",
                message=(
                    "Cannot add driver to {!r}[{}]: {}".format(
                        params.data_path, params.index, exc,
                    )
                ),
                current_state={
                    "common_paths": [
                        "location", "rotation_euler", "scale",
                    ],
                },
                hint=(
                    "Common drivable paths: 'location' (index 0/1/2), "
                    "'rotation_euler' (index 0/1/2), 'scale' (index 0/1/2). "
                    "Use index=-1 for scalar custom properties."
                ),
            )

    driver = fcurve.driver
    driver.type = "SCRIPTED"
    driver.expression = params.expression

    return Result(
        status="ok",
        object_name=obj.name,
        data_path=params.data_path,
        index=fcurve.array_index,
        expression=driver.expression,
        action=action,
    )
