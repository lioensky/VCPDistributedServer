.. index:: Object Constraints; Clamp To Constraint
.. _bpy.types.ClampToConstraint:

*******************
Clamp To Constraint
*******************

The *Clamp To* constraint snaps an object or bone to a :doc:`Curve </modeling/curves/introduction>`.
Specifically, it works as follows:

- If no explicit *Main Axis* is chosen, the constraint picks one automatically based on the longest
  side of the Curve's bounding box.
- Using this axis, it compares the original coordinate of the object or bone to the minimum and maximum
  coordinates of the Curve, and remaps it to the range 0-1 accordingly.
- This remapped coordinate is then used as a "curve time" to determine the position along the Curve,
  where a value of 0 corresponds to the first control point and 1 to the last.

Unless the Curve is a perfectly straight line, the object's/bone's coordinate along the *Main Axis*
will likely change.

If the object or bone moves along the Curve in the opposite direction than the expected one,
use :ref:`bpy.ops.curve.switch_direction` to flip the order of the Curve's control points.

.. important::

   While the object's/bone's original coordinate is evaluated in world space, the Curve's bounding box
   is evaluated in the Curve's local space.

   This means that, if the Curve originally stretched from -5 to 10 on the global X axis but was then moved,
   rotated, and scaled so that it now stretches from 20 to 90 on the global Z axis, the *Main Axis* will
   still be chosen as X, and the object/bone still needs to move from -5 to 10 on the global X axis to be
   successfully moved along the Curve.

   For the most intuitive results, keep the Curve object at the default rotation.

.. note::

   :ref:`Bézier handles <curve-bezier>` and control point :ref:`radii <modeling-curve-radius>`
   are included in the calculation of the bounding box.

.. seealso::

   The :doc:`/animation/constraints/relationship/follow_path` can not just position an
   object/bone on a Curve, but also orient it along the Curve's direction.


Options
=======

.. figure:: /images/animation_constraints_tracking_clamp-to_panel.png

   Clamp To constraint.

:ref:`Target <rigging-constraints-interface-common-target>`
   The Curve object to snap to.

Main Axis
   The axis for determining the constraint owner's coordinate and the Curve's minimum/maximum
   coordinates.

Cyclic
   When disabled, the constraint owner will stop at the start/end of the Curve when it leaves
   the range of the Curve's bounding box. When enabled, it will jump to the opposite side
   and begin another run along the Curve.

   This option is mainly useful for Curves that are also :ref:`cyclic <bpy.ops.curve.cyclic_toggle>`
   (closed).

:ref:`bpy.types.constraint.influence`
   How strongly the constraint affects the object.


Example
=======

.. peertube:: c3e07449-aff7-43d6-b017-5bbd888cf52c
