.. _bpy.types.ShaderNodeAddShader:

**********
Add Shader
**********

.. figure:: /images/node-types_ShaderNodeAddShader.webp
   :align: right
   :alt: Add Shader node.

The *Add* node is used to add two *Shaders* together.

.. (TODO) explain the difference Add vs Mix shaders (it's not obvious)
   adds lightness values... aren't necessarily physically correct...
   should be used with Emission and Background shaders...

   check the example image, is it correct to show the Mix shader here?


Inputs
======

Shaders
   Standard shader inputs.


Properties
==========

This node has no properties.


Outputs
=======

Shader
   Standard shader output.


Example
=======

.. figure:: /images/render_shader-nodes_shader_mix_example.jpg

   A mix of a glossy and a diffuse shader makes a nice ceramic material.
