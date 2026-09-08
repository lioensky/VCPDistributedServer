.. _bpy.types.ShaderNodeBsdfTransparent:

****************
Transparent BSDF
****************

.. figure:: /images/node-types_ShaderNodeBsdfTransparent.webp
   :align: right
   :alt: Transparent BSDF node.

The *Transparent* :abbr:`BSDF (Bidirectional Scattering Distribution Function)`
is used to add transparency without refraction, passing straight through the surface,
as if there were no geometry there. Useful with alpha maps, for example.
This shader :ref:`affects light paths somewhat differently <render-cycles-light-paths-transparency>`
than other BSDFs.
Note that only pure white transparent shaders are completely transparent.


Inputs
======

Color
   Color of the surface, or physically speaking,
   the probability for each wavelength that light is blocked or passes straight through the surface.


Properties
==========

This node has no properties.


Outputs
=======

BSDF
   Standard shader output.


Examples
========

.. list-table::
   :widths: auto

   * - .. figure:: /images/render_shader-nodes_shader_transparent_example.jpg

          Transparent shader (pure white).

     - .. figure:: /images/render_shader-nodes_shader_transparent_behavior.svg
          :width: 308px

          Transparent shader behavior.

   * - .. figure:: /images/render_shader-nodes_shader_transparent_example-dark.jpg

          Transparent shader (gray).

     - ..
