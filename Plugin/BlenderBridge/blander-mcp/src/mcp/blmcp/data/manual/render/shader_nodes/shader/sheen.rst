.. _bpy.types.ShaderNodeBsdfSheen:

**********
Sheen BSDF
**********

.. figure:: /images/node-types_ShaderNodeBsdfSheen.png
   :align: right
   :alt: Sheen BSDF node.

:guilabel:`Cycles Only`

The *Sheen* :abbr:`BSDF (Bidirectional Scattering Distribution Function)`
is used to add reflection to materials that have micro surface details such as cloth or dust.
This shader is intended to be layered on top of other shaders such as
:term:`dielectric <Dielectric Material>` or metallic shader setups.


Inputs
======

Color
   Color of the surface, or physically speaking, the probability that light is reflected for each wavelength.
Roughness
   Controls the amount of color that is reflected back to the camera,
   higher values reflect more color and can give a dusty appearance, while lower values look fuzzy and darker.
Normal
   Normal used for shading; if nothing is connected the default shading normal is used.


Properties
==========

Distribution
   Sheen shading model.

   :Ashikhmin: Classic Ashikhmin velvet, used in Blender versions prior to 4.0
   :Microfiber: Microflake-based model of multiple scattering between normal-oriented fibers.


Outputs
=======

BSDF
   Standard shader output.


Examples
========

.. list-table::
   :widths: auto

   * - .. figure:: /images/render_shader-nodes_shader_sheen_example.png

          The Sheen shader example.

     - .. figure:: /images/render_shader-nodes_shader_sheen_behavior.svg
          :width: 308px

          The Sheen shader behavior.
