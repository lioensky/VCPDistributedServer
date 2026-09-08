.. _bpy.ops.curves.pen:

*********
Curve Pen
*********

.. reference::

   :Mode:      Edit Mode
   :Tool:      :menuselection:`Toolbar --> Curve Pen`

The Curve Pen tool allows you to construct and edit curves rapidly.


Usage
=====

Extrude Point
   :kbd:`LMB` click to add a new point connected to the currently selected point.
   The new point will have :ref:`handle type <curve-bezier-handle-type>` of *Vector*.
   :kbd:`Shift-LMB` click will add point as type *Auto*.
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

Move Point
   :kbd:`LMB` drag to move existing points or handles. With an endpoint of a stroke selected,
   click and drag on empty space to *Extrude Point* and move the handle at the same time.

Close Stroke
   Make the stroke :term:`Cyclic` by clicking the endpoints.

Cycle Handle Type
   Double :kbd:`LMB` click on the control point to cycle through all handle types.


Hotkeys
=======

Free-Align Toggle
   Hold :kbd:`LeftCtrl` while dragging a handle to switch between ``Free`` and ``Align`` handle types.
   Can be used to create sharp corners along the curve.

Move Entire Point
   Hold :kbd:`LeftAlt` while dragging a handle to move the entire point.

Snap Handle Angle
   Hold :kbd:`LeftShift` while dragging a handle to limit the movement of the handle to multiples 45 degrees,
   so the handle can only be vertical, horizontal or diagonal.


Tool Settings
=============

Radius
   Control newly added point's radius.
