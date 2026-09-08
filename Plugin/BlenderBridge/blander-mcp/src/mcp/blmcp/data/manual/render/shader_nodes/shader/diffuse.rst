.. _bpy.types.ShaderNodeBsdfDiffuse:

************
Diffuse BSDF
************

.. figure:: /images/node-types_ShaderNodeBsdfDiffuse.webp
   :align: right
   :alt: Diffuse BSDF node.

The *Diffuse* :abbr:`BSDF (Bidirectional Scattering Distribution Function)`
node is used to add Lambertian and Oren-Nayar diffuse reflection.


Inputs
======

Color
   Color of the surface, or physically speaking,
   the probability that light is reflected or transmitted for each wavelength.
Roughness :guilabel:`Cycles Only`
   Surface roughness; 0.0 gives standard Lambertian reflection, higher values activate the Oren-Nayar BSDF.
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

   * - .. figure:: /images/render_shader-nodes_shader_diffuse_example.jpg

          Lambertian reflection.

     - .. figure:: /images/render_shader-nodes_shader_diffuse_behavior.svg
          :width: 308px

          Diffuse shader behavior.

   * - .. figure:: /images/render_shader-nodes_shader_diffuse_example-oren-nayar.jpg

          Oren-Nayar reflection.

     - ..
