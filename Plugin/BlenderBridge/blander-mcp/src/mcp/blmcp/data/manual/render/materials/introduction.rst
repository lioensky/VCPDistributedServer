
************
Introduction
************

Materials control the appearance of meshes, curves, volumes and other objects.
They define the substance that the object is made of, its color and texture,
and how light interacts with it.

Physically based materials can be created using
the :doc:`Principled BSDF </render/shader_nodes/shader/principled>`,
:doc:`Principled Hair </render/shader_nodes/shader/hair_principled>`,
and :doc:`Principled Volume </render/shader_nodes/shader/volume_principled>` shaders.
With these uber shaders, a wide variety of materials including
plastic, glass, metal, cloth, skin, hair, smoke and fire can be created.

A flexible :doc:`shading nodes </render/shader_nodes/introduction>` system is used
to set up textures and create entirely different types of materials like toon shading.


Setting up Materials
====================

Materials can be created in either the :doc:`Material properties </editors/properties_editor>`,
or in the :doc:`Shader Editor </editors/shader_editor>`.
These provide a different view of the same shader nodes and material settings.

The default Shading workspace has a Shader Editor and a 3D Viewport that can be set to
Material Preview or Rendered shading, to interactively preview how the material interacts
with objects and lights in the scene.

Materials are data-blocks that can be :doc:`assigned </render/materials/assignment>`
to one or more objects, and different materials can be assigned to different parts of meshes.

Image textures can be created from scratch in :doc:`Texture Paint Mode </sculpt_paint/texture_paint/index>`,
or by loading in existing images with the :doc:`Image Texture node </render/shader_nodes/textures/image>`.
A variety of :doc:`procedural texture nodes </render/shader_nodes/textures/index>` is also available.


Components
==========

Materials consist of three shaders, defining the appearance of the surface,
the volume inside the object, and the displacement of the surface.

.. figure:: /images/render_materials_introduction_shaders.svg
   :align: center


Surface Shader
--------------

The :doc:`surface shader </render/materials/components/surface>` controls the textures
and light interaction at the surface of the mesh.


Volume Shader
-------------

The :doc:`volume shader </render/materials/components/volume>` defines the interior of the mesh.
A material can have just a volume shader for cases like smoke and fire,
or it can be combined with a surface shader for materials like cloudy glass.


Displacement
------------

The shape of the surface and the volume inside it may be altered by
:doc:`displacement </render/materials/components/displacement>`.
This way, textures can then be used to make the mesh surface more detailed.

Depending on the settings, the displacement may be virtual,
only modifying the surface normals to give the impression of displacement,
which is known as bump mapping, or a combination of real and virtual displacement.


Physically Based Shading
========================

The material system is built with physically-based rendering in mind,
separating how a material looks and which rendering algorithm is used to render it.
This makes it easier to achieve realistic results and balanced lighting,
though there are a few things to keep in mind.

In order for materials to work well with global illumination, they should be energy conserving.
That means they cannot reflect more light than comes in.
This property is not strictly enforced, but if colors are in the range 0.0 to 1.0, and
:abbr:`BSDF (Bidirectional Scattering Distribution Function)`\ s are only mixed together with
the Mix Shader node, this will automatically be true.

It is however, possible to break this,
with color values higher than 1.0 or using the Add Shader node, but one must be careful when
doing this to keep materials behaving predictably under various lighting conditions.
