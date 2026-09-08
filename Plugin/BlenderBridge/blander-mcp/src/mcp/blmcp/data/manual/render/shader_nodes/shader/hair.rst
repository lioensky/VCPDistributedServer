.. _bpy.types.ShaderNodeBsdfHair:

*********
Hair BSDF
*********

.. figure:: /images/node-types_ShaderNodeBsdfHair.webp
   :align: right
   :alt: Hair BSDF node.

:guilabel:`Cycles Only`

The *Hair* :abbr:`BSDF (Bidirectional Scattering Distribution Function)`
node is used to add shading for :doc:`Hair </physics/particles/hair/index>`.


Inputs
======

Color
   Color of the hair.
Offset
   Controls the way the light is rotated (angular shift) for the reflection/transmission.

   .. figure:: /images/render_shader-nodes_shader_hair_reflect-offset.png
      :align: center

      Reflection Offset.

   .. figure:: /images/render_shader-nodes_shader_hair_trans-offset.png
      :align: center

      Transmission Offset.

Roughness U/V
   Controls the roughness in the direction light is skewed, and perpendicular to it.

   .. list-table::

      * - .. figure:: /images/render_shader-nodes_shader_hair_reflect-roughness-uv.png

             Roughness when using the Reflection Component.

        - .. figure:: /images/render_shader-nodes_shader_hair_trans-roughness-uv.png

             Roughness when using the Transmission Component.

Tangent
   Input tangent.


Properties
==========

Component
   There are two components that can be used to control the look of the hair.
   Usually you are going to want each of these and use a :doc:`Mix Node </render/shader_nodes/shader/mix>`.

   :Reflection: The light that bounces off the surface of the hair.
   :Transmission: The light that passes through the hair and exits on the other side.

   .. figure:: /images/render_shader-nodes_shader_hair_mix-node.png
      :align: center

      With Mix node: 0 is full Reflection, 1 is full Transmission.


Outputs
=======

BSDF
   Standard shader output.
