.. _mask-feather:

********
S-Curves
********

The curve type used for creating mask splines is almost a Bézier curve, but with some differences.
Smooth edges of the mask are defined by feathering.
The curve needed to support feathering in a way that stuck to the curve as you edited it,
for ease of editing an animation. These are called S-curves.

Besides the handles, every control point also has points that define the feather between
the current point and the next point on the spline.
Each feather point is stored in UW space,
where U means position across spline segment, and W (weight) means distance between main spline and feather points.

.. figure:: /images/movie-clip_masking_scurve_schematic.svg
   :width: 420px

   S-Curve explained.

This allows for deforming the main spline in almost any way,
and the feather will be updated automatically to reflect that change.

For example if there is just rotation of the spline,
feather would stay completely unchanged. If one point's feather is moved,
the other feathers will be automatically stretched uniformly along that segment
and the overall shape will be almost the same as artists would want it to be.


.. _bpy.ops.mask.primitive_circle_add:
.. _bpy.ops.mask.primitive_square_add:

Primitives
==========

.. reference::

   :Mode:      Mask Mode
   :Tool:      :menuselection:`Add`
   :Shortcut:  :kbd:`Shift-A`

There are two primitives available: a Bézier Circle and a Square with vector handles.
