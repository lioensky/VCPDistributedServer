.. _bpy.types.ShaderNodeShaderToRGB:

******************
Shader To RGB Node
******************

.. figure:: /images/node-types_ShaderNodeShaderToRGB.webp
   :align: right
   :alt: Shader to RGB.

:guilabel:`EEVEE Only`

The Shader to RGB node is typically used for non-photorealistic rendering,
to apply additional effects on the output of BSDFs.
For example, a color ramp on the output of a diffuse BSDF can be used to create a flexible toon shader.

Using this conversion breaks the :abbr:`PBR (Physically Based Rendering)` pipeline and
thus makes the result unpredictable when used in combination with effects such as
ambient occlusion, contact shadows, soft shadows and screen space refraction.

Some effects require multiple samples to converge, and applying arbitrary changes to
noisy input may not convert to a smooth result.

.. warning::

   If a Shader to RGB node is used, any upstream BSDF will be invisible to the following effects:

   - Screen Space Reflection
   - Subsurface Scattering
   - Alpha Clip and Alpha Hashed blend modes

   Shader to RGB node doesn't give expected results in render passes.


Inputs
======

Shader
   Any shader such as a BSDF or Emission node can be linked here.


Properties
==========

This node has no properties.


Outputs
=======

Color
   Surface color computed from BSDFs and lighting.
Alpha
   Alpha transparency from any Transparent BSDFs in the input.


Examples
========

.. figure:: /images/render_shader-nodes_converter_shader-to-rgb_example.jpg

   Simple toon shading with Shader to RGB and Freestyle.
