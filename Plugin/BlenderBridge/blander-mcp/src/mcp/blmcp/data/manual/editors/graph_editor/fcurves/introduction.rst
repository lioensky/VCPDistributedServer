
************
Introduction
************

Blender lets you animate almost any property, going from the X coordinate of an object to the
transparency of a material. The evolution of a property's value over time is described by
a *function curve*, or F-Curve for short.

An important aspect of F-Curves is that they can interpolate. This saves you the effort of
manually configuring a value on every single frame, which would be highly impractical.
Instead, you define just a few values on key frames, and let the curve calculate the
values on all the other frames.

.. figure:: /images/editors_graph-editor_fcurves_introduction_f-curves-concept.png
   :align: right
   :width: 200px

   Example of interpolation.

The example curve on the right has two such keyframes (indicated by black dots):
one on frame 0 with value 0, and another on frame 25 with value 10.
The curve automatically calculates the values for the other frames,
such as for frame 5 where the value is 2.


Direction of Time
=================

F-Curves are similar to :doc:`Curve objects </modeling/curves/introduction>` in that they interpolate
between a set of user-defined control points. However, because their purpose is to define a *single*
value on every frame, there's an important difference: F-curves can't be closed or otherwise made to
turn back on themselves. They always continue going further to the right.

If you try to make a curve go left by dragging one control point past another,
it switches the order of the points to prevent this.

.. list-table:: Two control points switching: the curve cannot go back in time!

   * - .. figure:: /images/editors_graph-editor_fcurves_introduction_moving1.png

          Before moving the second keyframe.

     - .. figure:: /images/editors_graph-editor_fcurves_introduction_moving2.png

          After moving the second keyframe.
