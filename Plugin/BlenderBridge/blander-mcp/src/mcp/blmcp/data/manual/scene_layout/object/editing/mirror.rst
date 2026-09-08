.. _bpy.ops.transform.mirror:

******
Mirror
******

Interactive Mirror
==================

.. reference::

   :Mode:      Object and Edit Modes, Video Sequencer Preview
   :Menu:      :menuselection:`Object/Mesh/Curves/Strip --> Mirror --> Interactive Mirror`
   :Shortcut:  :kbd:`Ctrl-M`

The *Mirror* operator flips the selected elements across a chosen axis.
Mirroring objects, geometry, or curves is equivalent to scaling the selection by -1 along the selected axis,
but it offers a faster and more direct workflow.

When mirroring VSE strips, the selected axis' :ref:`mirror value <bpy.types.ImageStrip.use_flip>` gets changed instead
of scaling by -1. The rotation and position are also changed to achieve the same effect as when mirroring objects.

The mirror is relative to the :doc:`Transformation Orientation </editors/3dview/controls/orientation>`
and :doc:`Pivot Point </editors/3dview/controls/pivot_point/index>`
This gives full control over how and where the mirroring occurs, for example:

- Position the pivot point wherever you want the center of symmetry.
- Choose a transformation orientation (e.g. *Global*, *Local*, *Normal*).
- Select an axis (X, Y, or Z) along which to mirror.

.. tip::

   To mirror non-destructively, use the :doc:`Mirror Modifier </modeling/modifiers/generate/mirror>`.


Usage
-----

To mirror along a specific axis:

- Press :kbd:`Ctrl-M`, then :kbd:`X`, :kbd:`Y`, or :kbd:`Z` to select an axis.
- Pressing the same key again toggles the orientation between the active
  :doc:`Transform Orientation </editors/3dview/controls/orientation>` and the global orientation.
- Hold :kbd:`MMB` and drag to mirror interactively in the desired direction.


Properties
----------

Orientation
   The :doc:`Transform Orientation </editors/3dview/controls/orientation>` used to align the X, Y, and Z axes.

Constraint Axis
   The axis (or axes) to mirror across.
   For example, mirroring across the X axis flips the selection horizontally.


X/Y/Z Global
============

.. reference::

   :Mode:      Object and Edit Modes, Video Sequencer Preview
   :Menu:      :menuselection:`Object/Mesh/Curves/Strip --> Mirror --> X/Y/Z Global`

These operations perform a non-interactive mirror along the global X, Y, or Z axis.

X Global
   Mirrors the selection along the global X axis.
Y Global
   Mirrors the selection along the global Y axis.
Z Global
   Mirrors the selection along the global Z axis.


X/Y/Z Local
===========

.. reference::

   :Mode:      Object and Edit Modes, Video Sequencer Preview
   :Menu:      :menuselection:`Object/Mesh/Curves/Strip --> Mirror --> X/Y/Z Local`

These operations perform a non-interactive mirror along the object's local axes.

X Local
   Mirrors the selection along the object's local X axis.
Y Local
   Mirrors the selection along the object's local Y axis.
Z Local
   Mirrors the selection along the object's local Z axis.


Examples
========

.. list-table:: Mirror around the individual origins.

   * - .. figure:: /images/modeling_meshes_editing_mesh_mirror_cursor-before.png
          :width: 320px

          Mesh before mirroring.

     - .. figure:: /images/modeling_meshes_editing_mesh_mirror_individual-after.png
          :width: 320px

          Mesh after mirroring along the X axis.

The next example shows mirroring around the *3D Cursor*, with the orientation set to *Local*:

.. list-table:: Mirror around the 3D Cursor.

   * - .. figure:: /images/modeling_meshes_editing_mesh_mirror_cursor-before.png
          :width: 320px

          Mesh before mirroring.

     - .. figure:: /images/modeling_meshes_editing_mesh_mirror_cursor-after.png
          :width: 320px

          Mesh after mirroring along the X axis using the 3D Cursor as the pivot point.
