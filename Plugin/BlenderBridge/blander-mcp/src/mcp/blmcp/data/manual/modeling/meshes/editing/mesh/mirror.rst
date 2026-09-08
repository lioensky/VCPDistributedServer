
******
Mirror
******

Interactive Mirror
==================

.. reference::

   :Mode:      Object and Edit Modes
   :Menu:      :menuselection:`Object/Mesh/Curves --> Mirror --> Interactive Mirror`
   :Shortcut:  :kbd:`Ctrl-M`

The *Mirror* operator flips the selected elements around the
:doc:`Pivot Point </editors/3dview/controls/pivot_point/index>` along an axis of the
:doc:`Transformation Orientation </editors/3dview/controls/orientation>`.
Mirroring is equivalent to scaling the selection by -1 along the selected axis,
but it offers a faster and more direct workflow.

.. hint::

   After mirroring a mesh, the face normals tend to get flipped inside out
   (see the :ref:`bpy.types.View3DOverlay.show_face_orientation` overlay).
   The :ref:`Flip Normals <bpy.ops.mesh.flip_normals>` operator can fix this.

.. seealso::

   - The :doc:`/modeling/meshes/editing/mesh/symmetrize` operator creates a mirrored
     copy of the mesh.
   - The :doc:`/modeling/modifiers/generate/mirror` creates a mirrored copy that's
     automatically kept up to date.

Usage
-----

#. Place the pivot point at the desired mirror location.
#. When not mirroring along a global axis, ensure the transform orientation has an axis
   pointing along the desired mirror direction (perpendicular to the mirror plane).
#. Press :kbd:`Ctrl-M` to activate the *Mirror* operator.
#. Choose an axis by dragging with :kbd:`MMB` or by pressing :kbd:`X`, :kbd:`Y`, or :kbd:`Z`.
   (The chosen axis is shown at the top of the 3D Viewport.) Press an axis key a second
   time to toggle between the transform orientation axis and the global axis.
#. Press :kbd:`LMB` or :kbd:`Return` to confirm, or :kbd:`RMB` or :kbd:`Esc` to cancel.


Options
-------

Orientation
   The transform orientation to take the *Constraint Axis* from.

Constraint Axis
   The axis (or axes) to mirror across.
   For example, mirroring across the X axis flips the selection horizontally.


X/Y/Z Global
============

.. reference::

   :Mode:      Object and Edit Modes
   :Menu:      :menuselection:`Object/Mesh/Curves --> Mirror --> X/Y/Z Global`

These operations perform a non-interactive mirror along the global X, Y, or Z axis.


X/Y/Z Local
===========

.. reference::

   :Mode:      Object and Edit Modes
   :Menu:      :menuselection:`Object/Mesh/Curves --> Mirror --> X/Y/Z Local`

These operations perform a non-interactive mirror along the object's local X, Y, or Z axis.


Examples
========

Mirroring along the global X axis around the object origin:

.. list-table::

   * - .. figure:: /images/modeling_meshes_editing_mesh_mirror_cursor-before.png
          :width: 320px

          Mesh before mirroring.

     - .. figure:: /images/modeling_meshes_editing_mesh_mirror_individual-after.png
          :width: 320px

          Mesh after mirroring.

Mirroring around the :doc:`/editors/3dview/3d_cursor`:

.. list-table::

   * - .. figure:: /images/modeling_meshes_editing_mesh_mirror_cursor-before.png
          :width: 320px

          Mesh before mirroring.

     - .. figure:: /images/modeling_meshes_editing_mesh_mirror_cursor-after.png
          :width: 320px

          Mesh after mirroring.
