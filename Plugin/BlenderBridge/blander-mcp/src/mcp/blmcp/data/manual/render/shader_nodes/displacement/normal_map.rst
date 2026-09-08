.. _bpy.types.ShaderNodeNormalMap:

***************
Normal Map Node
***************

.. figure:: /images/node-types_ShaderNodeNormalMap.webp
   :align: right
   :alt: Normal Map Node.

The *Normal Map* node generates a perturbed normal from an RGB normal map image.
This is usually chained with an *Image Texture* node in the color input,
to specify the normal map image. For tangent space normal maps,
the UV coordinates for the image must match,
and the image texture should be set to *Non-Color* mode to give correct results.


Inputs
======

Strength
   Strength of the normal mapping effect.

   .. figure:: /images/render_shader-nodes_vector_normal-map_strength.jpg

      Strength is set to 0, 0.5, 1, 2 (from left to right).

Color
   RGB color that encodes the normal map in the specified space.


Properties
==========

Space
   The input RGB color can be in one of three spaces: Tangent, Object and World space.
   Tangent space normal maps are the most common, as they support object transformation and mesh deformations.
   Object space normal maps keep sticking to the surface under object transformations,
   while World normal maps do not.
Convention
   Blender uses the OpenGL convention by default for rendering and baking, where the Y axis in
   the green channel points up. The DirectX convention can be used for normal maps from other
   software, that assumes the Y axis points down.
UV Map
   Name of the UV map to derive normal mapping tangents from. When chained with an Image Texture node,
   this UV map should be the same as the UV map used to map the texture.


Outputs
=======

Normal
   Normal that can be used as an input to BSDF nodes.


Example
=======

.. figure:: /images/render_shader-nodes_vector_normal-map_example.jpg
   :align: center

   The Normal Map Strength is set to 1.
