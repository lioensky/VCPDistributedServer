.. _bpy.ops.curve.pen:

*********
Curve Pen
*********

.. reference::

   :Mode:      Edit Mode
   :Tool:      :menuselection:`Toolbar --> Curve Pen`

The Curve Pen tool allows you to construct and edit curves rapidly.


Usage
=====

.. figure:: /images/modeling_curves_tools_pen_curve-properties.jpg
   :align: right

   Curve Pen Preferences

The following preferences can be configured from:
:menuselection:`Preferences --> Keymap --> 3D View --> Curve --> 3D View Tool: Edit Curve, Curve Pen`.

Extrude Point
   :kbd:`LMB` click to add a new point connected to an existing point.

Extrude Handle Type
   The :ref:`handle type <curve-bezier-handle-type>` of the extruded points.
   Can be either *Vector* or *Auto*.
   However, the handle type switches to *Align* when handles are moved (See *Move Point*).

Delete Point
   :kbd:`Ctrl-LMB` click on an existing point to delete it.

Insert Point
   :kbd:`Ctrl-LMB` click on a :term:`Curve Segment` to insert a new control point between the two
   adjacent control points. :kbd:`Ctrl-LMB` click and drag to control the handles of the inserted points.

Move Segment
   :kbd:`LMB` drag on a segment in between two control points to adjust the handles, changing the shape of the
   curve without affecting the location of any control points.

Select Point
   :kbd:`LMB` click to select a single point or handle at a time.

Move point
   :kbd:`LMB` drag to move existing points or handles. With an endpoint of a spline selected,
   click and drag on empty space to *Extrude Point* and move the handle at the same time.

Close Spline
   Make the spline :term:`Cyclic` by clicking the endpoints consecutively.

Close Spline Method
   The condition for *Close Spline* to activate.

   :None: Turn off the Close Spline functionality.
   :On Press:
      Close the spline on mouse down. With this option, you may click and drag to adjust the handles of the endpoint.
   :On Click:
      Activate on mouse release. With this option, the *Close Spline* functionality will not be
      triggered on click and drag.

Toggle Vector
   Double :kbd:`LMB` click on a handle to switch handle between *Vector* and *Auto* handle types.
   Can be used to easily switch between sharp corners and smooth curves.

Cycle Handle Type
   Double :kbd:`LMB` click on the control point to cycle through all handle types.


Hotkeys
=======

Free-Align Toggle
   Hold :kbd:`LeftShift` while dragging a handle to switch between ``Free`` and ``Align`` handle types.
   Can be used to create sharp corners along the curve.

Move Adjacent Handle
   Hold :kbd:`LeftCtrl` while dragging a handle to move the closer handle of the adjacent control point.
   Can be helpful to make adjustments to newly created curve segments.

Move Entire
   Hold :kbd:`Spacebar` while dragging a handle to move the entire point.

Link Handles
   Press :kbd:`RightCtrl` while dragging a handle to mirror its movement on the opposite handle of the same point.

Lock Handle Angle
   Hold :kbd:`LeftAlt` while dragging a handle to limit the movement of the handle to its current direction,
   so only its length can be adjusted.
