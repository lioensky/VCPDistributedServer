
*******
Surface
*******

Transform
=========

.. reference::

   :Mode:      Edit Mode
   :Menu:      :menuselection:`Surface --> Transform`

Tools for moving control points.

Move, Rotate, Scale
   See :doc:`Basic Transformations </scene_layout/object/editing/transform/introduction>`.
To Sphere, Shear, Bend, Push/Pull, Warp, Randomize
   See :doc:`Mesh Transformations </modeling/meshes/editing/mesh/transform/index>`.
Move/Scale Texture Space
   See :ref:`properties-texture-space`.

Mirror
======

.. reference::

   :Mode:      Edit Mode
   :Menu:      :menuselection:`Surface --> Mirror`
   :Shortcut:  :kbd:`Ctrl-M`

See :doc:`/modeling/meshes/editing/mesh/mirror`.


Snap
====

.. reference::

   :Mode:      Edit Mode
   :Menu:      :menuselection:`Surface --> Snap`
   :Shortcut:  :kbd:`Shift-S`

See the :doc:`/scene_layout/object/editing/snap` menu,
as well as the :doc:`snapping options </editors/3dview/controls/snapping>`.


.. _bpy.ops.curve.spin:

Spin
====

.. reference::

   :Mode:      Edit Mode
   :Menu:      :menuselection:`Surface --> Spin`

Similar to its :doc:`mesh counterpart </modeling/meshes/tools/spin>`, this operator
extrudes the selected control points several times along a circle that's centered on
the :doc:`/editors/3dview/3d_cursor` and parallel to the viewing plane.
The :ref:`weights <modeling-surfaces-weight>` of the new control points are set up
to produce a circle, and the surface is marked as *Cyclic*, *Bézier*, and *Endpoint*
in the extrusion direction (see :doc:`/modeling/surfaces/properties/active_spline`).


.. _modeling_surface_editing_duplicating:

Add Duplicate
=============

.. reference::

   :Mode:      Edit Mode
   :Menu:      :menuselection:`Surface --> Add Duplicate`
   :Shortcut:  :kbd:`Shift-D`

Duplicates the selected control points and creates a new surface based on them.
The new control points are placed in the *Move* mode: move the mouse to bring
them to the desired position, then click :kbd:`LMB` to confirm. Alternatively,
press :kbd:`RMB` or :kbd:`Esc` to keep them at their original position.

Note that the selected control points must form a single, valid sub grid.
If this is not the case, the duplication will fail with an error.


Split
=====

.. reference::

   :Mode:      Edit Mode
   :Menu:      :menuselection:`Surface --> Split`
   :Shortcut:  :kbd:`Y`

Disconnects the selected sub grid from the rest of the surface, keeping it within
the same Surface object. The control points at the border are duplicated so that both
the original surface and the disconnected surface have them.

The sub grid must consist of one or more complete rows or columns of the surface grid.


Separate
========

.. reference::

   :Mode:      Edit Mode
   :Menu:      :menuselection:`Surface --> Separate`
   :Shortcut:  :kbd:`P`

Disconnects the selected sub grid from the rest of the surface and moves it into
a new Surface object. The control points at the border are duplicated so that both
the original surface and the disconnected surface have them.

The sub grid must consist of one or more complete rows or columns of the surface grid.


Toggle Cyclic
=============

.. reference::

   :Mode:      Edit Mode
   :Menu:      :menuselection:`Surface --> Toggle Cyclic`
   :Shortcut:  :kbd:`Alt-C`

Opens a popover menu with the options *Cyclic U* and *Cyclic V*. The surface is made
cyclic (closed) or non-cyclic (open) in the corresponding direction.

If a surface is cyclic, the last row or column of its control point grid is connected
back to the first. A cylinder is cyclic along either the U or V direction, while
a sphere is cyclic along both.

.. seealso::

   The *Cyclic* settings are also in the :doc:`/modeling/surfaces/properties/active_spline`
   panel in the Sidebar.



Set Spline Type
===============

.. reference::

   :Mode:      Edit Mode
   :Menu:      :menuselection:`Surface --> Set Spline Type`

This feature only works for :doc:`Curves </modeling/curves/index>`.


Show/Hide
=========

.. reference::

   :Mode:      Edit Mode
   :Menu:      :menuselection:`Surface --> Show/Hide`
   :Shortcut:  :kbd:`H`, :kbd:`Shift-H`, :kbd:`Alt-H`

Hides the selected or unselected control points, or unhides all hidden
control points.

By default, unhiding control points adds them to the selection.
To prevent this, uncheck the *Select* option in the :ref:`bpy.ops.screen.redo_last` panel.


Cleanup
=======

.. reference::

   :Mode:      Edit Mode
   :Menu:      :menuselection:`Surface --> Clean Up`

This feature only works for :doc:`Curves </modeling/curves/index>`.


Delete
======

.. reference::

   :Mode:      Edit Mode
   :Menu:      :menuselection:`Surface --> Delete`
   :Shortcut:  :kbd:`X`, :kbd:`Delete`

Removes the selected *Vertices* (control points) or *Segments* (lines) from the surface. In both cases,
the selection must consist of one or more complete rows or columns of the surface grid.

Vertices
   Deletes the selected control points. The resulting gap is bridged with new grid lines so that the surface
   stays contiguous.

Segments
   Deletes the lines and control points that lie between the outermost selected control points.
   The resulting gap is not bridged.

Dissolve Vertices
   This feature only works for :doc:`Curves </modeling/curves/index>`.

.. figure:: /images/modeling_surfaces_editing_surface_deleting.png

   Before and after deleting a row of control points.
