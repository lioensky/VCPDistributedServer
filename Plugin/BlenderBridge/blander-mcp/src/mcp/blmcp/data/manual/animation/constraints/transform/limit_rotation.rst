.. index:: Object Constraints; Limit Rotation Constraint
.. _bpy.types.LimitRotationConstraint:

*************************
Limit Rotation Constraint
*************************

The *Limit Rotation* constraint limits the Euler rotation angle for each axis
to a certain range.

Angles outside a range are clamped to whichever boundary is closer on a circle.
For example, if an axis is limited to the range 0°-90° and the original rotation
is 340°, the constraint changes this to 0°, not 90°.

This constraint doesn't work for bones that are affected by :doc:`Inverse Kinematics
</animation/armatures/posing/bone_constraints/inverse_kinematics/introduction>`.
Please use the *Limit* settings in the bone's :ref:`IK panel <bpy.types.PoseBone.ik>`
instead.


Options
=======

.. figure:: /images/animation_constraints_transform_limit-rotation_panel.png

   Limit Rotation constraint.

Limit X, Y, Z
   The number fields determine the angle range for each axis.
   The checkboxes determine whether each range applies.

   .. tip::

      Even if all limits are disabled, the constraint still removes shearing
      as a side effect.

Order
   The :term:`Euler` order to use when applying the limits.
   Defaults to the order of the owner, or XYZ if the owner uses a non-Euler
   rotation.

Affect Transform
   When the owner is manually rotated, restrict not just its
   :ref:`visual <constraint-visual-transform>` rotation but also its
   *Rotation* in the :doc:`/editors/properties_editor`'s *Transform* panel.

Legacy Behavior
   For backwards compatibility: make the constraint behave in the semi-broken
   way it did prior to Blender 4.2. This old behavior does not properly account
   for the looping nature of rotations, and therefore causes
   unpredictable/erratic rotation snapping. However, this behavior can still be
   useful in some specific circumstances when `Owner` is set to *Local Space*, and
   some older rig setups utilize that. However, that behavior is better and more
   robustly accomplished with drivers directly on the object/bone's rotation
   properties, so new rigs should favor that approach over using this option.

:ref:`Owner <rigging-constraints-interface-common-space>`
   The space for determining and limiting the rotation of the owner.

:ref:`bpy.types.constraint.influence`
   How strongly the constraint affects the owner.


Example
=======

.. peertube:: 3ce2539e-3bb9-4caf-9911-1217a1e8907c
