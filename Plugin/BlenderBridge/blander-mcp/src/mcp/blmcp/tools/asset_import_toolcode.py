# SPDX-FileCopyrightText: 2026 Blender Authors
#
# SPDX-License-Identifier: GPL-3.0-or-later

"""
Tool-code for importing external 3D files (FBX, GLTF/GLB, OBJ) into the scene.
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

_EXT_TO_FORMAT: dict[str, str] = {
    ".fbx": "FBX",
    ".gltf": "GLTF",
    ".glb": "GLTF",
    ".obj": "OBJ",
}

_SUPPORTED_FORMATS = ("FBX", "GLTF", "OBJ")


class Params(NamedTuple):
    filepath: str
    format: str     # "" = auto-detect from extension; or "FBX"|"GLTF"|"OBJ"


class Result(NamedTuple):
    status: str
    filepath: str
    format: str
    imported_objects: list[str]


def _detect_format(filepath: str) -> str:
    ext = os.path.splitext(filepath)[1].lower()
    return _EXT_TO_FORMAT.get(ext, "")


def _call_import(filepath: str, fmt: str) -> None:
    import bpy  # pylint: disable=import-error,no-name-in-module

    if fmt == "FBX":
        try:
            ret = bpy.ops.import_scene.fbx(filepath=filepath)
        except (AttributeError, RuntimeError) as exc:
            raise RuntimeError(
                "FBX import failed — make sure the FBX extension is "
                "enabled in Blender: {:s}".format(str(exc))
            ) from exc
    elif fmt == "GLTF":
        try:
            ret = bpy.ops.import_scene.gltf(filepath=filepath)
        except (AttributeError, RuntimeError) as exc:
            raise RuntimeError(
                "GLTF import failed — make sure the GLTF extension is "
                "enabled in Blender: {:s}".format(str(exc))
            ) from exc
    elif fmt == "OBJ":
        try:
            ret = bpy.ops.wm.obj_import(filepath=filepath)
        except AttributeError:
            try:
                ret = bpy.ops.import_scene.obj(filepath=filepath)
            except (AttributeError, RuntimeError) as exc:
                raise RuntimeError(
                    "OBJ import failed: {:s}".format(str(exc))
                ) from exc
        except RuntimeError as exc:
            raise RuntimeError(
                "OBJ import failed: {:s}".format(str(exc))
            ) from exc
    else:
        raise ValueError("Unsupported format: {!r}".format(fmt))

    if "FINISHED" not in ret:
        raise RuntimeError(
            "Import operator returned {:s}".format(str(ret))
        )


def main(params: Params) -> "Result | ErrorResult":
    if not os.path.isfile(params.filepath):
        return ErrorResult(
            status="error",
            error_code="FILE_NOT_FOUND",
            message="File not found: {!r}".format(params.filepath),
            current_state={"supported_formats": list(_SUPPORTED_FORMATS)},
            hint="Provide an absolute path to an existing FBX, GLTF, or OBJ file.",
        )

    fmt = (params.format.upper() if params.format else
           _detect_format(params.filepath))

    if not fmt:
        ext = os.path.splitext(params.filepath)[1]
        return ErrorResult(
            status="error",
            error_code="UNSUPPORTED_FORMAT",
            message=(
                "Cannot determine format for extension {!r}. "
                "Supported: {}.".format(ext, ", ".join(_SUPPORTED_FORMATS))
            ),
            current_state={"supported_formats": list(_SUPPORTED_FORMATS)},
            hint=(
                "Pass format='FBX', 'GLTF', or 'OBJ' explicitly, "
                "or rename the file with a supported extension."
            ),
        )

    if fmt not in _SUPPORTED_FORMATS:
        return ErrorResult(
            status="error",
            error_code="UNSUPPORTED_FORMAT",
            message="Format {!r} is not supported.".format(fmt),
            current_state={"supported_formats": list(_SUPPORTED_FORMATS)},
            hint=(
                "Use one of: "
                + ", ".join(repr(f) for f in _SUPPORTED_FORMATS)
                + "."
            ),
        )

    import bpy  # pylint: disable=import-error,no-name-in-module
    before = set(bpy.data.objects.keys())

    try:
        _call_import(params.filepath, fmt)
    except (RuntimeError, ValueError) as exc:
        return ErrorResult(
            status="error",
            error_code="IMPORT_FAILED",
            message=str(exc),
            current_state={},
            hint=(
                "Ensure the file is valid and the corresponding Blender "
                "extension (FBX / GLTF / OBJ) is installed and enabled."
            ),
        )

    after = set(bpy.data.objects.keys())
    imported = sorted(after - before)

    return Result(
        status="ok",
        filepath=params.filepath,
        format=fmt,
        imported_objects=imported,
    )
