.. index:: Object Constraints; Limit Scale Constraint
.. _bpy.types.LimitScaleConstraint:

**********************
Limit Scale Constraint
**********************

The *Limit Scale* constraint applies a lower and/or upper bound to an
object or bone's scale along each axis.

.. important::

   While it's possible to set limits of 0 or less, these will not work correctly
   and should be avoided.


Options
=======

.. figure:: /images/animation_constraints_transform_limit-scale_panel.png

   Limit Scale constraint.

Minimum/Maximum X, Y, Z
   The number fields determine the boundaries for each axis.
   The checkboxes determine whether each boundary applies.

   .. note::

      If a *Minimum* is higher than the corresponding *Maximum*,
      the constraint uses the *Maximum* for both.

Affect Transform
   When the owner is manually scaled, restrict not just its
   :ref:`visual <constraint-visual-transform>` scale but also its
   *Scale* in the :doc:`/editors/properties_editor`'s *Transform* panel.

:ref:`Owner <rigging-constraints-interface-common-space>`
   The space for determining and limiting the scale of the owner.

:ref:`bpy.types.constraint.influence`
   How strongly the constraint affects the owner.


Example
=======

.. peertube:: b73800d7-dda8-4888-b48b-f649e9b7ae3b
