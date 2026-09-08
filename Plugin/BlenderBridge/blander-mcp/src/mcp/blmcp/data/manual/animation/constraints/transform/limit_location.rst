.. index:: Object Constraints; Limit Location Constraint
.. _bpy.types.LimitLocationConstraint:

*************************
Limit Location Constraint
*************************

The *Limit Location* constraint forces an object or bone to stay above a coordinate,
below a coordinate, or between two coordinates along one or more axes.

Like other constraints, *Limit Location* only looks at the :doc:`origin </scene_layout/object/origin>`
for objects; their geometry is not taken into account. This means that, if a cube's origin
is at its center and a *Limit Location* constraint is added for the coordinates of a
floor plane, the cube will still be able to sink halfway into the plane.

.. important::

   This constraint has no effect on :ref:`connected bones <bpy.types.EditBone.use_connect>`
   as their position is determined by their parent bone.

.. seealso::

   :doc:`/animation/constraints/relationship/floor`

Options
=======

.. figure:: /images/animation_constraints_transform_limit-location_panel.png

   Limit Location constraint.

Minimum/Maximum X, Y, Z
   The number fields determine the boundaries for each axis.
   The checkboxes determine whether each boundary applies.

   .. note::

      If a *Minimum* is higher than the corresponding *Maximum*,
      the constraint uses the *Maximum* for both.

Affect Transform
   When the owner is manually moved around, restrict not just its
   :ref:`visual <constraint-visual-transform>` position but also its
   *Location* in the :doc:`/editors/properties_editor`'s *Transform* panel.

:ref:`Owner <rigging-constraints-interface-common-space>`
   The space for determining and limiting the position of the owner.

:ref:`bpy.types.constraint.influence`
   How strongly the constraint affects the owner.


Example
=======

.. peertube:: 3a78daa9-3786-4510-98ae-f0045f692f5b
