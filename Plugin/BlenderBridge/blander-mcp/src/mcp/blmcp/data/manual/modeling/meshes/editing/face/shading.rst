
*******************
Shade Smooth & Flat
*******************

.. _bpy.ops.mesh.faces_shade_smooth:

Shade Smooth
============

.. reference::

   :Mode:      Edit Mode
   :Menu:      :menuselection:`Face --> Shade Smooth`

Marks the selected faces for smooth shading so that the boundaries between them become blurred
and hard to see. This is useful for rounded and organic surfaces.

More specifically, this makes the face corner normals at each vertex all point in the same direction
(namely the average of the face normals).

.. tip::

   After using *Shade Smooth* on a mesh and blurring all its edges, you can use
   :ref:`Mark Sharp <bpy.ops.mesh.mark_sharp>` to selectively make some edges sharp again.

   Alternatively, use :ref:`bpy.ops.object.shade_auto_smooth` to automatically apply smooth
   shading to flattish areas while keeping corners sharp.

.. _bpy.ops.mesh.faces_shade_flat:

Shade Flat
==========

.. reference::

   :Mode:      Edit Mode
   :Menu:      :menuselection:`Face --> Shade Flat`

Marks the selected faces for flat shading so that the boundaries between them become sharp and
clearly visible. This is useful for machines, crystals, etc.

More specifically, this makes each face corner normal match the corresponding face normal.

.. seealso::

   :doc:`/scene_layout/object/editing/shading`
