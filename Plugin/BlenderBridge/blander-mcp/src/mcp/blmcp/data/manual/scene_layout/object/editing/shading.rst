
*******
Shading
*******

.. _bpy.ops.object.shade_smooth:

Shade Smooth
============

.. reference::

   :Mode:      Object Mode
   :Menu:      :menuselection:`Object --> Shade Smooth`

Sets an entire object as smooth or faceted.
This forces the assignment of the "smoothing" attribute to each face in the mesh,
including when you add or delete geometry.

This operator will also remove any :doc:`Smooth By Angle Modifiers </modeling/modifiers/normals/smooth_by_angle>`.

Notice that the outline of the object is still strongly faceted.
Activating the smoothing features does not actually modify the object's geometry;
it changes the way the shading is calculated across the surfaces (normals will be interpolated),
giving the illusion of a smooth surface.

Using :ref:`bpy.ops.object.shade_flat` will revert the shading back (normals will be constant)
to that shown in the first image below.

.. list-table:: Example mesh flat (left) and smooth-shaded (right).
   `Sample blend-file <https://archive.blender.org/wiki/2015/index.php/File:25-manual-meshsmooth-example.blend>`__.

   * - .. figure:: /images/scene-layout_object_editing_shading_example-flat.png
          :width: 200px

     - .. figure:: /images/scene-layout_object_editing_shading_example-smooth.png
          :width: 200px

Keep Sharp Edges
   Do not clear :ref:`Sharp <bpy.ops.mesh.mark_sharp>` edges (which are redundant with objects shaded as flat).
   This option is useful to not destroy data in case you want to revert changes later.


.. _bpy.ops.object.shade_auto_smooth:

Shade Auto Smooth
=================

.. reference::

   :Mode:      Object Mode
   :Menu:      :menuselection:`Object --> Shade Auto Smooth`

Adds a :doc:`/modeling/modifiers/normals/smooth_by_angle` to automatically set
the sharpness of mesh edges based on the angle between the neighboring faces.
Note, the modifier will be :ref:`pinned <bpy.types.Modifier.use_pin_to_last>` to be the last modifier.

Auto Smooth
   If disabled, any :doc:`Smooth By Angle Modifiers </modeling/modifiers/normals/smooth_by_angle>` are removed.
Angle
   Maximum angle between face normals that will be considered as smooth.


.. _bpy.ops.object.shade_flat:

Shade Flat
==========

.. reference::

   :Mode:      Object Mode
   :Menu:      :menuselection:`Object --> Shade Flat`

Signify the object to render and display faces uniformly,
using the :ref:`Face Normal's <modeling-meshes-structure-normals>` direction.
This is usually desirable for objects with flat surfaces.

This operator will also remove any :doc:`Smooth By Angle Modifiers </modeling/modifiers/normals/smooth_by_angle>`

Keep Sharp Edges
   Do not clear :ref:`Sharp <bpy.ops.mesh.mark_sharp>` edges (which are redundant with objects shaded as flat).
   This option is useful to not destroy data in case you want to revert changes later.
