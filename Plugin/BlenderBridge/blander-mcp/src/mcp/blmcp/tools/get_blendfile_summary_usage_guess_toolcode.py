# SPDX-FileCopyrightText: 2026 Blender Authors
#
# SPDX-License-Identifier: GPL-3.0-or-later

"""
Tool-code for guessing blend file use-cases.
"""

__all__ = (
    "Result",
    "main",
)

from collections.abc import Callable
from typing import Any, NamedTuple

# Vertex count of Blender's default cube.
_DEFAULT_CUBE_VERTS = 8


class Result(NamedTuple):
    status: str
    usage_guesses: dict[str, dict[str, int]]


def _summarize(signals: list[tuple[float, float]]) -> tuple[int, int]:
    """
    Return the average all (`contribution`, `certainty`) factors as integer percentages.

    This allows us to accumulate any number of contributing factors,
    then collect the result as a normalized value.
    """
    if not signals:
        return (0, 0)
    n = len(signals)
    return (
        round(100 * sum(c for c, _ in signals) / n),
        round(100 * sum(k for _, k in signals) / n),
    )


def _summarize_as_dict(
    use_case: str,
    signals: list[tuple[float, float]],
) -> tuple[str, dict[str, int]]:
    """
    Summarize signals into a use-case name and `score`/`certainty` dict pair.
    """
    score, certainty = _summarize(signals)
    return (use_case, {"score": score, "certainty": certainty})


# -----------------------------------------------------------------------------
# Per-category probability functions.

def _usage_probability_for_animation(data: Any, scene: Any) -> tuple[str, dict[str, int]]:
    """
    Score likelihood that the file is used for animation.
    """
    del scene
    signals: list[tuple[float, float]] = []
    signals.append((float(bool(data.actions)), 1.0))
    signals.append((float(bool(data.armatures)), 1.0))
    signals.append((float(any(bool(obj.constraints) for obj in data.objects)), 0.5))
    return _summarize_as_dict("Animation", signals)


def _usage_probability_for_rendering(data: Any, scene: Any) -> tuple[str, dict[str, int]]:
    """
    Score likelihood that the file is used for rendering.
    """
    del data
    signals: list[tuple[float, float]] = []
    signals.append((float(scene.render.engine not in ("BLENDER_EEVEE_NEXT", "BLENDER_EEVEE")), 0.5))
    # Blender's default output paths, indicating no intentional render setup.
    default_paths = ("/tmp/", "/tmp\\", "")
    signals.append((float(scene.render.filepath not in default_paths), 0.8))
    node_tree = getattr(scene, "node_tree", None)
    signals.append((
        float(bool(node_tree and any(n.type == "R_LAYERS" for n in node_tree.nodes))),
        1.0,
    ))
    return _summarize_as_dict("Rendering", signals)


def _usage_probability_for_scripting(data: Any, scene: Any) -> tuple[str, dict[str, int]]:
    """
    Score likelihood that the file is used for scripting.
    """
    del scene
    signals: list[tuple[float, float]] = []
    signals.append((float(bool(data.texts)), 1.0))
    return _summarize_as_dict("Scripting", signals)


def _usage_probability_for_video_editing(data: Any, scene: Any) -> tuple[str, dict[str, int]]:
    """
    Score likelihood that the file is used for video editing.
    """
    del scene
    signals: list[tuple[float, float]] = []
    has_sequences = any(
        s.sequence_editor and bool(getattr(s.sequence_editor, "strips", ()))
        for s in data.scenes
    )
    signals.append((float(has_sequences), 1.0))
    return _summarize_as_dict("Video Editing", signals)


def _usage_probability_for_modeling(data: Any, scene: Any) -> tuple[str, dict[str, int]]:
    """
    Score likelihood that the file is used for modeling.
    """
    del scene
    signals: list[tuple[float, float]] = []
    # Exclude the default cube (named `Cube` with exactly 8 vertices).
    non_default = [
        m for m in data.meshes
        if m.name != "Cube" or len(m.vertices) != _DEFAULT_CUBE_VERTS
    ]
    signals.append((float(bool(non_default)), 0.8))
    # Meshes are created with a single `UVMap` layer by default.
    signals.append((float(bool(
        non_default and any(
            len(m.uv_layers) > 1 or bool(m.color_attributes) for m in non_default
        )
    )), 0.7))
    signals.append((float(bool(data.curves) or bool(data.metaballs)), 0.7))
    signals.append((float(any(bool(obj.modifiers) for obj in data.objects)), 0.5))
    return _summarize_as_dict("Modeling", signals)


def _usage_probability_for_grease_pencil(data: Any, scene: Any) -> tuple[str, dict[str, int]]:
    """
    Score likelihood that the file is used for grease pencil.
    """
    del scene
    signals: list[tuple[float, float]] = []
    signals.append((float(bool(data.grease_pencils)), 1.0))
    return _summarize_as_dict("Grease Pencil", signals)


def _usage_probability_for_geometry_nodes(data: Any, scene: Any) -> tuple[str, dict[str, int]]:
    """
    Score likelihood that the file is used for geometry nodes.
    """
    del scene
    signals: list[tuple[float, float]] = []
    has_gn = any(
        any(mod.type == "NODES" and mod.node_group for mod in obj.modifiers)
        for obj in data.objects
    )
    signals.append((float(has_gn), 1.0))
    return _summarize_as_dict("Geometry Nodes", signals)


def _usage_probability_for_compositing(data: Any, scene: Any) -> tuple[str, dict[str, int]]:
    """
    Score likelihood that the file is used for compositing.
    """
    del data
    signals: list[tuple[float, float]] = []
    # Enabling `use_nodes` creates `Render Layers` and `Composite` nodes by default.
    node_tree = getattr(scene, "node_tree", None)
    signals.append((
        float(bool(node_tree and scene.use_nodes and len(node_tree.nodes) > 2)),
        1.0,
    ))
    return _summarize_as_dict("Compositing", signals)


def _usage_probability_for_uv_unwrapping(data: Any, scene: Any) -> tuple[str, dict[str, int]]:
    """
    Score likelihood that the file is used for UV unwrapping.
    """
    del scene
    signals: list[tuple[float, float]] = []
    # Meshes are created with a single `UVMap` layer by default.
    has_extra_uv = any(len(mesh.uv_layers) > 1 for mesh in data.meshes)
    has_renamed_uv = any(
        any(uv.name != "UVMap" for uv in mesh.uv_layers)
        for mesh in data.meshes
    )
    has_tex_image = any(
        mat.node_tree and any(n.type == "TEX_IMAGE" and n.image for n in mat.node_tree.nodes)
        for mat in data.materials
    )
    signals.append((float(has_extra_uv), 1.0))
    signals.append((float(has_renamed_uv), 0.7))
    signals.append((float(has_tex_image), 0.7))
    return _summarize_as_dict("UV Unwrapping", signals)


def _usage_probability_for_motion_tracking(data: Any, scene: Any) -> tuple[str, dict[str, int]]:
    """
    Score likelihood that the file is used for motion tracking.
    """
    del scene
    signals: list[tuple[float, float]] = []
    signals.append((float(bool(data.movieclips)), 1.0))
    return _summarize_as_dict("Motion Tracking", signals)


def _usage_probability_for_audio(data: Any, scene: Any) -> tuple[str, dict[str, int]]:
    """
    Score likelihood that the file is used for audio.
    """
    del scene
    signals: list[tuple[float, float]] = []
    signals.append((float(bool(data.sounds)), 1.0))
    signals.append((float(bool(data.speakers)), 1.0))
    return _summarize_as_dict("Audio", signals)


_UsageFn = Callable[[Any, Any], tuple[str, dict[str, int]]]

_USAGE_PROBABILITY_FUNCTIONS: tuple[_UsageFn, ...] = (
    _usage_probability_for_animation,
    _usage_probability_for_rendering,
    _usage_probability_for_scripting,
    _usage_probability_for_video_editing,
    _usage_probability_for_modeling,
    _usage_probability_for_grease_pencil,
    _usage_probability_for_geometry_nodes,
    _usage_probability_for_compositing,
    _usage_probability_for_uv_unwrapping,
    _usage_probability_for_motion_tracking,
    _usage_probability_for_audio,
)


# -----------------------------------------------------------------------------
# Main entry point.

def main(params: None) -> Result:
    del params
    import bpy  # pylint: disable=import-error,no-name-in-module

    data = bpy.data
    scene = bpy.context.scene

    # Each function scores a single use-case by accumulating
    # (contribution, certainty) signals and averaging them.
    usages: dict[str, dict[str, int]] = {}
    for fn in _USAGE_PROBABILITY_FUNCTIONS:
        use_case, scores = fn(data, scene)
        usages[use_case] = scores

    return Result(status="ok", usage_guesses=usages)
