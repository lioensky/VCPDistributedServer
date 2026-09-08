# SPDX-FileCopyrightText: 2026 Blender Authors
#
# SPDX-License-Identifier: GPL-3.0-or-later

"""
Tool-code for applying a preset Geometry Nodes graph to a scene object.
"""

__all__ = (
    "Params",
    "Result",
    "main",
)

from typing import Any, NamedTuple

# @include_begin: _template_tool_error.py
# @include_end

_SUPPORTED_PRESETS = ("wave", "noise_displace")


class Params(NamedTuple):
    object_name: str
    preset: str        # "wave" | "noise_displace"
    modifier_name: str  # "" = auto-generate name


class Result(NamedTuple):
    status: str
    object_name: str
    modifier_name: str
    node_tree_name: str
    preset: str
    nodes_created: list[str]


def _get_object_names() -> list[str]:
    import bpy  # pylint: disable=import-error,no-name-in-module
    return sorted(obj.name for obj in bpy.data.objects)


def _build_wave(nt: object) -> list[str]:
    """
    Build a wave-deform node graph.

    Exposed inputs: Amplitude (float, 0.3), Frequency (float, 2.0),
    Phase (float, 0.0).
    Formula: offset_Z = sin(pos_X * Frequency + Phase) * Amplitude
    """
    import bpy  # pylint: disable=import-error,no-name-in-module

    nodes = nt.nodes
    links = nt.links

    # Interface sockets.
    iface = nt.interface
    iface.new_socket("Geometry", in_out="INPUT",
                     socket_type="NodeSocketGeometry")
    amp_sock = iface.new_socket("Amplitude", in_out="INPUT",
                                socket_type="NodeSocketFloat")
    amp_sock.default_value = 0.3
    freq_sock = iface.new_socket("Frequency", in_out="INPUT",
                                 socket_type="NodeSocketFloat")
    freq_sock.default_value = 2.0
    phase_sock = iface.new_socket("Phase", in_out="INPUT",
                                  socket_type="NodeSocketFloat")
    phase_sock.default_value = 0.0
    iface.new_socket("Geometry", in_out="OUTPUT",
                     socket_type="NodeSocketGeometry")

    # Nodes.
    in_node = nodes.new("NodeGroupInput")
    in_node.location = (-700, 0)
    out_node = nodes.new("NodeGroupOutput")
    out_node.location = (400, 0)

    pos_node = nodes.new("GeometryNodeInputPosition")
    pos_node.location = (-700, -200)

    sep_node = nodes.new("ShaderNodeSeparateXYZ")
    sep_node.location = (-500, -200)

    mul_freq = nodes.new("ShaderNodeMath")
    mul_freq.operation = "MULTIPLY"
    mul_freq.name = "Multiply Frequency"
    mul_freq.location = (-300, -200)

    add_phase = nodes.new("ShaderNodeMath")
    add_phase.operation = "ADD"
    add_phase.name = "Add Phase"
    add_phase.location = (-100, -200)

    sine_node = nodes.new("ShaderNodeMath")
    sine_node.operation = "SINE"
    sine_node.name = "Sine"
    sine_node.location = (100, -200)

    mul_amp = nodes.new("ShaderNodeMath")
    mul_amp.operation = "MULTIPLY"
    mul_amp.name = "Multiply Amplitude"
    mul_amp.location = (200, -200)

    comb_node = nodes.new("ShaderNodeCombineXYZ")
    comb_node.location = (200, -50)

    set_pos = nodes.new("GeometryNodeSetPosition")
    set_pos.location = (200, 100)

    # Links.
    links.new(in_node.outputs["Geometry"], set_pos.inputs["Geometry"])
    links.new(pos_node.outputs["Position"], sep_node.inputs["Vector"])
    links.new(sep_node.outputs["X"], mul_freq.inputs[0])
    links.new(in_node.outputs["Frequency"], mul_freq.inputs[1])
    links.new(mul_freq.outputs["Value"], add_phase.inputs[0])
    links.new(in_node.outputs["Phase"], add_phase.inputs[1])
    links.new(add_phase.outputs["Value"], sine_node.inputs[0])
    links.new(sine_node.outputs["Value"], mul_amp.inputs[0])
    links.new(in_node.outputs["Amplitude"], mul_amp.inputs[1])
    links.new(mul_amp.outputs["Value"], comb_node.inputs["Z"])
    links.new(comb_node.outputs["Vector"], set_pos.inputs["Offset"])
    links.new(set_pos.outputs["Geometry"], out_node.inputs["Geometry"])

    return [n.name for n in nodes]


def _build_noise_displace(nt: object) -> list[str]:
    """
    Build a noise-displacement node graph.

    Exposed inputs: Strength (float, 0.5), Scale (float, 2.0).
    Formula: offset_Z = (noise(pos * Scale) - 0.5) * Strength * 2
    """
    import bpy  # pylint: disable=import-error,no-name-in-module

    nodes = nt.nodes
    links = nt.links

    # Interface sockets.
    iface = nt.interface
    iface.new_socket("Geometry", in_out="INPUT",
                     socket_type="NodeSocketGeometry")
    str_sock = iface.new_socket("Strength", in_out="INPUT",
                                socket_type="NodeSocketFloat")
    str_sock.default_value = 0.5
    scale_sock = iface.new_socket("Scale", in_out="INPUT",
                                  socket_type="NodeSocketFloat")
    scale_sock.default_value = 2.0
    iface.new_socket("Geometry", in_out="OUTPUT",
                     socket_type="NodeSocketGeometry")

    # Nodes.
    in_node = nodes.new("NodeGroupInput")
    in_node.location = (-700, 0)
    out_node = nodes.new("NodeGroupOutput")
    out_node.location = (400, 0)

    pos_node = nodes.new("GeometryNodeInputPosition")
    pos_node.location = (-700, -200)

    # Scale position vector by Scale factor using Vector Math.
    scale_vec = nodes.new("ShaderNodeVectorMath")
    scale_vec.operation = "SCALE"
    scale_vec.name = "Scale Position"
    scale_vec.location = (-500, -200)

    noise_node = nodes.new("ShaderNodeTexNoise")
    noise_node.location = (-300, -200)

    sub_half = nodes.new("ShaderNodeMath")
    sub_half.operation = "SUBTRACT"
    sub_half.name = "Subtract Half"
    sub_half.inputs[1].default_value = 0.5
    sub_half.location = (-100, -200)

    mul_str = nodes.new("ShaderNodeMath")
    mul_str.operation = "MULTIPLY"
    mul_str.name = "Multiply Strength"
    mul_str.location = (100, -200)

    comb_node = nodes.new("ShaderNodeCombineXYZ")
    comb_node.location = (200, -50)

    set_pos = nodes.new("GeometryNodeSetPosition")
    set_pos.location = (200, 100)

    # Links.
    links.new(in_node.outputs["Geometry"], set_pos.inputs["Geometry"])
    links.new(pos_node.outputs["Position"], scale_vec.inputs[0])
    links.new(in_node.outputs["Scale"], scale_vec.inputs["Scale"])
    links.new(scale_vec.outputs["Vector"], noise_node.inputs["Vector"])
    links.new(noise_node.outputs["Fac"], sub_half.inputs[0])
    links.new(sub_half.outputs["Value"], mul_str.inputs[0])
    links.new(in_node.outputs["Strength"], mul_str.inputs[1])
    links.new(mul_str.outputs["Value"], comb_node.inputs["Z"])
    links.new(comb_node.outputs["Vector"], set_pos.inputs["Offset"])
    links.new(set_pos.outputs["Geometry"], out_node.inputs["Geometry"])

    return [n.name for n in nodes]


def main(params: Params) -> "Result | ErrorResult":
    import bpy  # pylint: disable=import-error,no-name-in-module

    obj = bpy.data.objects.get(params.object_name)
    if obj is None:
        return ErrorResult(
            status="error",
            error_code="OBJECT_NOT_FOUND",
            message="Object {!r} not found.".format(params.object_name),
            current_state={"available_objects": _get_object_names()},
            hint="Use `get_scene_state` to list objects.",
        )

    preset = params.preset.lower()
    if preset not in _SUPPORTED_PRESETS:
        return ErrorResult(
            status="error",
            error_code="INVALID_PRESET",
            message="Preset {!r} is not supported.".format(params.preset),
            current_state={"supported_presets": list(_SUPPORTED_PRESETS)},
            hint=(
                "Use one of: "
                + ", ".join(repr(p) for p in _SUPPORTED_PRESETS)
                + "."
            ),
        )

    # Create or reuse NODES modifier.
    mod_name = params.modifier_name or preset.replace("_", " ").title()
    mod = obj.modifiers.get(mod_name)
    if mod is None or mod.type != "NODES":
        mod = obj.modifiers.new(mod_name, type="NODES")

    # Always create a fresh node tree for the preset.
    nt_name = mod_name + " Tree"
    # Remove any existing node group of the same name to start fresh.
    old_nt = bpy.data.node_groups.get(nt_name)
    if old_nt is not None:
        bpy.data.node_groups.remove(old_nt)

    nt = bpy.data.node_groups.new(nt_name, "GeometryNodeTree")
    mod.node_group = nt

    if preset == "wave":
        created = _build_wave(nt)
    else:
        created = _build_noise_displace(nt)

    return Result(
        status="ok",
        object_name=obj.name,
        modifier_name=mod.name,
        node_tree_name=nt.name,
        preset=preset,
        nodes_created=created,
    )
