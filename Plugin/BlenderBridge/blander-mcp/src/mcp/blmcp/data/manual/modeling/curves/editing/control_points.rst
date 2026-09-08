
**************
Control Points
**************

.. _bpy.ops.curve.extrude_move:
.. _modeling-curves-extrude:

Extrude Curve and Move
======================

.. reference::

   :Mode:      Edit Mode
   :Menu:      :menuselection:`Control Points --> Extrude Curve and Move`
   :Shortcut:  :kbd:`E`

Extrudes points by duplicating the selected points, which then can be moved,
and connecting those points back to the original curve creating a continuous curve.


.. _bpy.ops.curve.make_segment:
.. _modeling-curves-make-segment:

Make Segment
============

.. reference::

   :Mode:      Edit Mode
   :Menu:      :menuselection:`Control Points --> Make Segment`
   :Shortcut:  :kbd:`F`

Connects two disconnected control points.
The selection must be loose points, or the first/last point of a curve, then press :kbd:`F`.
If the points belong to different curves, these are joined by a segment to become a single curve.

.. list-table::

   * - .. figure:: /images/modeling_curves_editing_control-points_two-curves.png

          Two curves before.

     - .. figure:: /images/modeling_curves_editing_curve_make-segment.png

          Curve after joining.

Note that you can only join curves of the same type (i.e. Bézier with Bézier, NURBS with NURBS).
Additionally, you can close a curve by toggling cyclic.


.. _bpy.ops.transform.tilt:
.. _modeling-curve-tilt:

Tilt
====

.. reference::

   :Mode:      Edit Mode
   :Tool:      :menuselection:`Toolbar --> Tilt`
   :Menu:      :menuselection:`Control Points --> Tilt`
   :Shortcut:  :kbd:`Ctrl-T`

This setting controls how the normals (visualized as arrows)
twist around each control point -- so it is only relevant with 3D curves!
The tilt will be interpolated from point to point (you can check it with the normals).

.. figure:: /images/modeling_curves_editing_control-points_extrude-mean-tilt.png
   :align: center
   :width: 50%

   30 degree Mean Tilt of all control points.


.. _bpy.ops.curve.tilt_clear:

Clear Tilt
==========

.. reference::

   :Mode:      Edit Mode
   :Menu:      :menuselection:`Control Points --> Clear Tilt`
   :Shortcut:  :kbd:`Alt-T`

You can also reset the tilt to its default value (i.e. perpendicular to the original curve plane).
With NURBS, the tilt is always smoothly interpolated. However, with Bézier,
you can choose the :ref:`interpolation algorithm <bpy.types.Spline.tilt_interpolation>`.


.. _bpy.ops.curve.handle_type_set:

Set Handle Type
===============

.. reference::

   :Mode:      Edit Mode
   :Menu:      :menuselection:`Control Points --> Set Handle Type`
   :Shortcut:  :kbd:`V`

Handle types are a property of :ref:`Bézier curves <curve-bezier>` and
can be used to alter features of the curve.
For example, switching to *Vector handles* can be used to create curves with sharp corners.
Read the :ref:`Bézier curves <curve-bezier-handle-type>` page for more details.

Toggle Free/Align
   Additionally, this operator can be used to toggle between Free and Aligned handle types.


.. _bpy.ops.curve.normals_make_consistent:

Recalculate Handles
===================

.. reference::

   :Mode:      Edit Mode
   :Menu:      :menuselection:`Control Points --> Recalculate Handles`
   :Shortcut:  :kbd:`Shift-N`

The *Recalculate Handles* operator rotates the selected control point's handle to be tangential to the curve.
This can be used to make curves smoother and more consistent looking.

Length
   Recalculates the length of the handles so they are all the same length.


.. _bpy.ops.curve.smooth:

Smooth
======

.. reference::

   :Mode:      Edit Mode
   :Menu:      :menuselection:`Control Points --> Smooth`

For Bézier curves, this smoothing operation reduces the distance between
the selected control point(s) and their neighbors,
while keeping the neighbors anchored. Does not effect control point tangents.

.. figure:: /images/modeling_curves_editing_control-points_smoothing-1.png

   Original, unsmoothed Curve.

.. figure:: /images/modeling_curves_editing_control-points_smoothing-2.png

   Entire curve smoothed over 20 times by holding :kbd:`Shift-R` to repeat last step.

.. figure:: /images/modeling_curves_editing_control-points_smoothing-3.png

   Only three control points in the center smoothed over 20 times.


.. _bpy.ops.curve.smooth_tilt:

Smooth Curve Tilt
=================

.. reference::

   :Mode:      Edit Mode
   :Menu:      :menuselection:`Control Points --> Smooth Curve Tilt`

The *Smooth Curve Tilt* operator interpolates the *Tilt* value for the selected control points.
This will reduce sharp changes in the curve's *Tilt* and give a smooth transition between points.


.. _bpy.ops.curve.smooth_radius:

Smooth Curve Radius
===================

.. reference::

   :Mode:      Edit Mode
   :Menu:      :menuselection:`Control Points --> Smooth Curve Radius`

The *Smooth Curve Radius* operator interpolates the *Radius* value for the selected control points.
This will reduce sharp changes in the curve's *Radius* and give a smooth transition between points.


.. _bpy.ops.curve.smooth_weight:

Smooth Curve Weight
===================

.. reference::

   :Mode:      Edit Mode
   :Menu:      :menuselection:`Control Points --> Smooth Curve Weight`

The *Smooth Curve Weight* operator interpolates the *Weight* value for the selected control points.
This will reduce sharp changes in the curve's *Weight* and give a smooth transition between points.


Hooks
=====

.. reference::

   :Mode:      Edit Mode
   :Menu:      :menuselection:`Control Points --> Hooks`
   :Shortcut:  :kbd:`Ctrl-H`

:doc:`Hooks </modeling/modifiers/deform/hooks>` can be added to control one or more points with other objects.


Make Vertex Parent
==================

.. reference::

   :Mode:      Edit Mode
   :Menu:      :menuselection:`Control Points --> Make Vertex Parent`
   :Shortcut:  :kbd:`Ctrl-P`

You can make other selected objects :ref:`children <object-parenting>`
of one or three control points, as with mesh objects.

To select a mesh (that is in view) while editing a curve, :kbd:`Ctrl-P` click on it.
Select either one or three control points,
then :kbd:`Ctrl-LMB` the object and use :kbd:`Ctrl-P` to make a vertex parent.
Selecting three control points will make the child follow
the median point between the three vertices. An alternative would be to use
a :doc:`Child Of constraint </animation/constraints/relationship/child_of>`.
See also the :doc:`Curve modifier </modeling/modifiers/deform/curve>`.
