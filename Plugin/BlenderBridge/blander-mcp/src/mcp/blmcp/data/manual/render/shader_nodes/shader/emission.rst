.. _bpy.types.ShaderNodeEmission:

********
Emission
********

.. figure:: /images/node-types_ShaderNodeEmission.webp
   :align: right
   :alt: Emission Shader node.

The *Emission* node is used to add Lambertian emission shader.
This can for example, be used for material and light surface outputs.

Light strength for point, spot and area lights is specified in Watts.

Sun lights are specified in Watts/m\ :sup:`2`, which require much smaller values like 1 W/m\ :sup:`2`.
This can be confusing, but specifying strength in Watts would not have been convenient;
the real sun for example has strength 384.6×10\ :sup:`24`\ W.
Emission shaders on meshes are also in Watts/m\ :sup:`2`.


Inputs
======

Color
   Color of the emitted light.
Strength
   Strength of the emitted light. For point and area lights, the unit is Watts.
   For materials, a value of 1.0 will ensure that the object in the image has
   the exact same color as the Color input, i.e. make it 'shadeless'.


Properties
==========

This node has no properties.


Outputs
=======

Emission
   The Emission shader output can both be plugged into the *Surface Input* as well as
   the *Volume Input* of the :doc:`Material Output </render/shader_nodes/output/material>` node.


Examples
========

.. list-table::

   * - .. figure:: /images/render_shader-nodes_shader_emission_example.jpg

          Emission shader, with strength at 1.0.

     - .. figure:: /images/render_shader-nodes_shader_emission_example-bright.jpg

          Emission shader, with strength at 3.0.
