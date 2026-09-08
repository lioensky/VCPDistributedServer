.. index:: Modeling Modifiers; UV Project Modifier
.. _bpy.types.UVProjectModifier:

*******************
UV Project Modifier
*******************

.. figure:: /images/modeling_modifiers_modify_uv-project_example.jpg
   :align: center
   :width: 350px

   Projecting the Blender logo onto Suzanne.

The *UV Project* modifier acts like a slide projector.
It emits a UV map from the negative Z axis of a controller object
(such as an :doc:`empty object </modeling/empties>`),
and applies it to the object as the "light" hits it.

`Download an example <https://archive.blender.org/wiki/2015/index.php/File:Uvproject.blend>`__.


Options
=======

.. figure:: /images/modeling_modifiers_modify_uv-project_panel.png
   :align: right
   :width: 300px

   The UV Project modifier.

UV Map
   Which UV map to modify. Defaults to the active rendering layer.

Aspect X/Y
   Changes the image's aspect ratio. Only apply when a camera is used as projector object.
Scale X/Y
   Scales the image. Only apply when a camera is used as projector object.

Projectors
   Up to ten projector objects are supported.
   Each face will choose the closest and aligned projector with its surface normal.
   Projections emit from the negative Z axis (i.e. straight down a camera or light).
   If the projector is a camera, the projection will adhere to its perspective/orthographic setting.

Object
   Specify the projector object(s).


Usage
=====

General
-------

*UV Project* is great for making spotlights more diverse, and also for creating decals to break up repetition.

Usually, an :doc:`Image Texture node </render/shader_nodes/textures/image>` mapped to the UV map
that the modifier targets is added to the object's material.


Known Limitations
=================

Perspective Projection on Low Poly Meshes
-----------------------------------------

Perspective UV projections onto low poly geometry (such as a plane) may cause noticeable artifacts.
This is an inherent limitation since UV interpolation doesn't account for perspective projection.

The issue can reduced by subdividing the geometry.


Vertices Behind the Camera
--------------------------

When projecting geometry in a perspective view, vertices behind the camera are not properly mapped.
You can workaround this by subdividing geometry so that faces in front of the camera have correctly mapped UVs.
