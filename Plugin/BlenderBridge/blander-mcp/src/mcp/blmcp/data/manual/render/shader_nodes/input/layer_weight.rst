.. _bpy.types.ShaderNodeLayerWeight:

*****************
Layer Weight Node
*****************

.. figure:: /images/node-types_ShaderNodeLayerWeight.webp
   :align: right
   :alt: Layer Weight Node.

The *Layer Weight* node outputs a weight typically used for layering shaders with the *Mix Shader* node.


Inputs
======

Blend
   Bias the output towards all 0 or all 1. Useful for uneven mixing of shaders.
Normal
   Input meant for plugging in bump or normal maps which will affect the output.


Properties
==========

This node has no properties.


Outputs
=======

Fresnel
   Dielectric Fresnel weight, useful for example for layering diffuse and
   glossy shaders to create a plastic material. This is like the Fresnel node,
   except that the input of this node is in the often more convenient 0.0 to 1.0 range.
Facing
   Weight that blends from the first to the second shader
   as the surface goes from facing the viewer to viewing it at a grazing angle.
