.. _bpy.types.ShaderNodeFresnel:

************
Fresnel Node
************

.. figure:: /images/node-types_ShaderNodeFresnel.webp
   :align: right
   :alt: Fresnel Node.

The *Fresnel* or *Dielectric Fresnel* node computes how much light is reflected off a layer,
where the rest will be refracted through the layer.
The resulting weight can be used for layering shaders with the *Mix Shader* node.
It is dependent on the angle between the surface normal and the viewing direction.

The most common use is to mix between two BSDFs using it as a blending factor in a Mix Shader node.
For a simple glass material you would mix between a glossy refraction and glossy reflection.
At grazing angles more light will be reflected than refracted as happens in reality.

For a two-layered material with a diffuse base and a glossy coating,
you can use the same setup, mixing between a diffuse and glossy BSDF. By using the Fresnel as
the blending factor you are specifying that any light which is refracted through the glossy
coating layer would hit the diffuse base and be reflected off that.


Inputs
======

IOR
   Index of refraction (:term:`IOR`) of the material being entered.
Normal
   Input meant for plugging in bump or normal maps which will affect the output.


Properties
==========

This node has no properties.


Outputs
=======

Factor
   Fresnel weight, indicating the probability with which light
   will reflect off the layer rather than passing through.
