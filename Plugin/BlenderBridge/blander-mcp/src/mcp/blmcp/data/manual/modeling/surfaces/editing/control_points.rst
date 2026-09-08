
**************
Control Points
**************

Extrude Curve and Move
======================

.. reference::

   :Mode:      Edit Mode
   :Menu:      :menuselection:`Control Points --> Extrude Curve and Move`
   :Shortcut:  :kbd:`E`

Extruding is the main way of adding new control points to a surface. It's not possible
to do this directly as would be the case with Curves.

Start by selecting a complete border of the surface grid. Then press :kbd:`E` to duplicate
the control points, and move the mouse to bring them to the desired position.
Finally, click :kbd:`LMB` to confirm. (Alternatively, click :kbd:`RMB` or press :kbd:`Esc`
to cancel the move and keep the new control points at their original position.)

Example
-------

First, we select a border control point and expand the selection to the complete row
using :ref:`bpy.ops.curve.select_row`.

.. list-table::

   * - .. figure:: /images/modeling_surfaces_editing_control-points_selecting-point.png

          Selecting control point

     - .. figure:: /images/modeling_surfaces_editing_control-points_selecting-row.png

          Selecting remaining control points in the row

Then, we extrude a few times:

.. figure:: /images/modeling_surfaces_editing_control-points_extruding.png

   Control points extruded twice


Make Segment
============

.. reference::

   :Mode:      Edit Mode
   :Menu:      :menuselection:`Control Points --> Make Segment`
   :Shortcut:  :kbd:`F`

While this operator sounds like it creates a single segment (grid line) between two control points,
it's really more similar to :ref:`bpy.ops.mesh.bridge_edge_loops` for meshes: it bridges the gap
between two disjoint surfaces by creating as many new segments as necessary. Simply select a border
row (or column) in each surface, then press :kbd:`F` to connect those borders.

Note that the two surfaces need to be part of the same Surface object. If you have two separate
objects, these first need to be combined into one using :doc:`/scene_layout/object/editing/join`.
Also, the borders to connect must have the same number of control points.

Example
-------

The images below show bridging of two "surfaces" consisting of just a curve, but it's also possible to
connect sheets.

.. list-table::

   * - .. figure:: /images/modeling_surfaces_editing_control-points_joining-ready.png

          Before bridging.

     - .. figure:: /images/modeling_surfaces_editing_control-points_joining-complete.png

          After bridging.


Smooth
======

.. reference::

   :Mode:      Edit Mode
   :Menu:      :menuselection:`Control Points --> Smooth`

Moves the selected control points to give the surface a smoother appearance.


Hooks
=====

.. reference::

   :Mode:      Edit Mode
   :Menu:      :menuselection:`Control Points --> Hooks`
   :Shortcut:  :kbd:`Ctrl-H`

Adds a :doc:`/modeling/modifiers/deform/hooks` that makes the selected control points
follow a particular object or bone.


Make Vertex Parent
==================

.. reference::

   :Mode:      Edit Mode
   :Menu:      :menuselection:`Control Points --> Make Vertex Parent`
   :Shortcut:  :kbd:`Ctrl-P`

Creates a :ref:`parent-child relationship <object-parenting>` that makes a particular object
follow the selected control point(s).

While in Edit Mode, select another object by either clicking it with :kbd:`Ctrl-LMB` in the
3D Viewport or by selecting it the :doc:`Outliner </editors/outliner/introduction>`.
Then, select one or three control points of the surface and press :kbd:`Ctrl-P`.
Parenting an object to three control points will make it follow their averaged position.
