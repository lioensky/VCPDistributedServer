.. _bpy.types.ShaderNodeBsdfTranslucent:

****************
Translucent BSDF
****************

.. figure:: /images/node-types_ShaderNodeBsdfTranslucent.webp
   :align: right
   :alt: Translucent BSDF node.

The *Translucent* :abbr:`BSDF (Bidirectional Scattering Distribution Function)`
is used to add Lambertian diffuse transmission.


Inputs
======

Color
   Color of the surface, or physically speaking, the probability that light is transmitted for each wavelength.
Normal
   Normal used for shading; if nothing is connected the default shading normal is used.


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

   * - .. figure:: /images/render_shader-nodes_shader_translucent_example.jpg

          Translucent shader example.

     - .. figure:: /images/render_shader-nodes_shader_translucent_behavior.svg
          :width: 308px

          Translucent shader behavior.
