.. _bpy.types.ShaderNodeBsdfToon:

*********
Toon BSDF
*********

.. figure:: /images/node-types_ShaderNodeBsdfToon.webp
   :align: right
   :alt: Toon BSDF node.

:guilabel:`Cycles Only`

The *Toon* :abbr:`BSDF (Bidirectional Scattering Distribution Function)`
is used to create *Diffuse* and *Glossy* materials with cartoon light effects.


Inputs
======

Color
   Color of the surface, or physically speaking, the probability that light is reflected for each wavelength.
Size
   Parameter between 0.0 and 1.0 that gives an angle of reflection between 0° and 90°.
Smooth
   This value specifies an angle over which a smooth transition from full to no reflection happens.
Normal
   Normal used for shading; if nothing is connected the default shading normal is used.


Properties
==========

Component
   The material component to base the toon effect.

   :Diffuse: Use shading based on the Diffuse BSDF.
   :Glossy: Use shading based on the Glossy BSDF for specular reflection.


Outputs
=======

BSDF
   Standard shader output.


Examples
========

.. figure:: /images/render_shader-nodes_shader_toon_example.jpg

   Example of Toon Shader.
