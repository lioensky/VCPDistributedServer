.. _bpy.ops.mesh.select_mirror:

*************
Select Mirror
*************

.. reference::

   :Mode:      Edit Mode
   :Menu:      :menuselection:`Select --> Select Mirror`
   :Shortcut:  :kbd:`Shift-Ctrl-M`

Flips the selection to the opposite side of the mesh.

Options
=======

Axis
   The local axis around which to mirror. The mesh's :doc:`origin </scene_layout/object/origin>`
   is used as the centerpoint.

Extend
   Add to the selection instead of replacing it.

.. figure:: /images/modeling_meshes_selecting_mirror_extend.png

   From left to right: initial selection -- mirrored around the X axis -- with Extend.

It's possible to select multiple axes by holding :kbd:`Shift`. If *Extend* is disabled,
this will mirror once across the combination of all the axes. If *Extend* is enabled,
this will mirror across each possible combination of the axes.

.. figure:: /images/modeling_meshes_selecting_mirror_axis-xz-extend.png

   From left to right: initial selection -- mirrored around the X and Z axes -- with Extend.
