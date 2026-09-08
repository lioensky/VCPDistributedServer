.. _bpy.types.ShaderNodeVolumePrincipled:

*****************
Principled Volume
*****************

.. figure:: /images/node-types_ShaderNodeVolumePrincipled.webp
   :align: right
   :alt: Principled Volume node.

The *Principled Volume* shader combines all volume shading components into
a single easy to use node. Volumes like smoke and fire can be rendered with
a single shader node, which includes scattering, absorption and blackbody emission.


Inputs
======

Color
   Volume scattering color.
Color Attribute
   Volume grid for coloring the volume. Use "color" for smoke simulations.
Density
   Density of the volume.
Density Attribute
   Volume grid to define the density, typically "density".
Anisotropy
   Backward or forward scattering direction.
Absorption Color
   Volume shadow color tint.
Emission Strength
   Amount of light to emit.
Emission Color
   Emission color tint.
Blackbody Intensity
   Blackbody emission for fire. Set to 1 for physically accurate intensity.
Blackbody Tint
   Color tint for blackbody emission.
Temperature
   Temperature in kelvin for blackbody emission, higher values emit more.
Temperature Attribute
   Volume grid to define the temperature, typically "temperature".


Properties
==========

This node has no properties.


Outputs
=======

Volume
   The Volume Shader output must be plugged into the *Volume Input*
   of the :doc:`Material </render/shader_nodes/output/material>`
   or :doc:`World </render/shader_nodes/output/world>` Output node.


Examples
========

.. figure:: /images/render_materials_components_volume_principled.jpg
