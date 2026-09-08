.. index:: Nodes; Shader Nodes

************
Introduction
************

Materials, lights and backgrounds are all defined using a network of shading nodes.
These nodes output values, vectors, colors and shaders.


Shaders
=======

An important concept to understand when building node setups is
that of the *shader socket*. The output of all surface and
volume shaders is a shader, describing lighting interaction at the surface or of the volume,
rather than the color of the surface.

There are a few types of shaders available as nodes:

:abbr:`BSDF (Bidirectional Scattering Distribution Function)` shader
   Describe light reflection, refraction and absorption at an object surface.
Emission shader
   Describe light emission at an object surface or in a volume.
Volume shader
   Describe light scattering inside a volume.
Background shader
   Describe light emission from the environment.

Each shader node has a color input, and outputs a shader.
These can then be mixed and added together using Mix and Add Shader nodes.
No other operations are permitted.
The resulting output can then be used by the renderer to compute all light interactions,
for direct lighting or global illumination.

.. seealso::

   :doc:`Shaders </render/shader_nodes/shader/index>`


Textures
========

Blender has various built in procedural texture nodes,
with texture coordinates and various parameters as input, and a color or value as output.
No texture data-blocks are needed; instead node groups can be used for reusing texture setups.

For UV mapping and texture painting in the 3D Viewport, the Image Texture node must be used.
When setting such a node as active, it will be displayed in the 3D Viewport
while using :doc:`Texture color </render/workbench/color>` mode.
This method can be used to preview painted textures while texture painting.

The default texture coordinates for all nodes are Generated coordinates,
except for Image textures that use UV coordinates by default.
Each node includes some options to modify the texture mapping and resulting color,
and these can be edited in the texture properties.

.. seealso::

   :doc:`Textures </render/shader_nodes/textures/index>`


More
====

Nodes for geometric data, texture coordinates,
layering shaders and non-physically-based tricks can be found in:

- :doc:`Vector Nodes </render/shader_nodes/utilities/vector/index>`
- :doc:`Color Nodes </render/shader_nodes/color/index>`
- :doc:`Utilities Nodes </render/shader_nodes/utilities/index>`


Open Shading Language
=====================

In Cycles, custom nodes can be written using the :doc:`Open Shading Language </render/cycles/osl/index>`
