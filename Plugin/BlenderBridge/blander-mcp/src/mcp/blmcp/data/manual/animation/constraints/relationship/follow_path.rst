.. index:: Object Constraints; Follow Path Constraint
.. _bpy.types.FollowPathConstraint:

**********************
Follow Path Constraint
**********************

The *Follow Path* constraint positions an object or bone on a :doc:`Curve </modeling/curves/introduction>`.
The desired position can be specified in two ways:

- Using a frame number, namely the :ref:`bpy.types.Curve.eval_time` of the Curve with an optional
  *Offset* in the constraint.
- Using a number between 0 and 1, namely the *Offset Factor* in the constraint.

By animating these properties, the object or bone can be made to move along the Curve.
It's also possible to make it rotate to match the Curve's direction.
Use cases include cameras on rails, vehicles on roads, boxes on conveyor belts, and so on.

To set up the constraint more quickly, select the object, add the Curve to the selection,
press :kbd:`Ctrl-P`, and click *Path Constraint*.

.. tip::

   The *Follow Path* constraint can be combined with a
   :doc:`tracking constraint </animation/constraints/tracking/index>` to, for example,
   keep a moving camera pointed at an object.

.. seealso::

   The :doc:`/animation/constraints/tracking/clamp_to` snaps an object or bone to
   a Curve based on its location.


Position Offsetting
===================

The constraint uses its owner's position and rotation in :term:`World Space`
as offsets to the position and rotation on the Curve. If *Follow Curve*
is disabled, the offsets are added in the Curve's :term:`Local Space`.
If it's enabled, the offsets are added in the space of the current curve point,
with the global Y axis corresponding to the tangent direction.

In both cases, the Curve's scale acts as a multiplier for the position offset.

.. list-table::
   :widths: 1 1 1

   * - .. figure:: /images/animation_constraints_relationship_follow-path_offset-no-constraint.png

          Before adding the constraint, the cone is offset along the world Y axis.

     - .. figure:: /images/animation_constraints_relationship_follow-path_offset-no-follow-curve.png

          After adding the constraint, the cone is offset along the Curve's local Y axis.

     - .. figure:: /images/animation_constraints_relationship_follow-path_offset-follow-curve.png

          When enabling Follow Curve, the cone is offset along the curve point's tangent.

To have the owner perfectly positioned and aligned on the Curve, ensure its
world position and rotation are both zero. This can be done by pressing :kbd:`Alt-G`
and :kbd:`Alt-R` respectively.


Options
=======

.. figure:: /images/animation_constraints_relationship_follow-path_panel.png

   Follow Path constraint.

:ref:`Target <rigging-constraints-interface-common-target>`
   The Curve object to follow.

Offset :guilabel:`Fixed Position disabled`
   The number of frames to subtract from the Curve's *Evaluation Time*. A positive value will
   move the owner to an earlier point on the Curve, while a negative value will move it to
   a later point.

Offset Factor :guilabel:`Fixed Position enabled`
   Relative position along the Curve, independent of its *Evaluation Time*. A value of 0 corresponds
   to the start of the Curve while a value of 1 corresponds to the end.

Forward Axis
   The local axis of the owner that should be aligned to the Curve's tangent direction.
   Requires that *Follow Curve* is enabled.

   A negative axis will make the owner point in the opposite direction.

Up Axis
   The local axis of the owner that should be aligned (as much as possible) to the global Z axis.
   Requires that *Follow Curve* is enabled.

.. important::

   The *Forward Axis* and the *Up Axis* must be different. If they are the same,
   the constraint will stop working and its icon will turn red.

Fixed Position
   Ignore the Curve's *Evaluation Time* and position the owner using only the *Offset Factor*.

   Despite the name of this property, the owner can still be moved over time by animating
   the *Offset Factor*.

Curve Radius
   Scale the owner based on the :ref:`radii <modeling-curve-radius>` of the Curve's
   control points.

Follow Curve
   Rotate the owner according to the *Forward Axis* and the *Up Axis*.

.. _bpy.ops.constraint.followpath_path_animate:

Animate Path
   By default, the Curve's *Evaluation Time* is static and the constraint owner doesn't move.
   Clicking this button will animate the *Evaluation Time* so that it's always equal to the
   current scene frame.

   Of course, it's also possible to skip this button and animate the *Evaluation Time* by hand.

:ref:`bpy.types.constraint.influence`
   How strongly the constraint affects the owner.


Example
=======

.. peertube:: 24507160-624d-423e-a8dd-5110ff8823d1
