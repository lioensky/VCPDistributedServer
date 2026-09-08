.. index:: Object Constraints; Copy Scale Constraint
.. _bpy.types.CopyScaleConstraint:

*********************
Copy Scale Constraint
*********************

The *Copy Scale* constraint forces an object or bone to match the scale of a target.


Options
=======

.. figure:: /images/animation_constraints_transform_copy-scale_panel.png

   Copy Scale constraint.

:ref:`Target <rigging-constraints-interface-common-target>`
   The object or bone whose scale to copy.

Axis
   The axes for which to copy scale factors.

Power
   Raises the target's scales to the specified power. This is done before applying
   the *Offset*.

Make Uniform
   Instead of applying the scale for each individual axis, apply a uniform scale
   to all axes that achieves the same overall change in volume.

Offset
   When enabled, the target's current scale (from all its constraints) is not
   copied over, but multiplied with the owner's original scale
   (from its preceding constraints).

Additive
   When *Offset* is enabled, don't use multiplication, but add the owner's scales minus 1.
   This option is kept for backwards compatibility, but generally makes no sense and should not be used.

:ref:`Target/Owner <rigging-constraints-interface-common-space>`
   The spaces for retrieving the scales from the target and for applying them to the owner.

:ref:`bpy.types.constraint.influence`
   How strongly the constraint affects the owner.

.. tip::

   Depending on the settings, *Power* can be used instead of *Influence* to get a better-looking result.

.. tip::

   To copy the scale from one axis of the target to all axes of the owner,
   disable the other axes, enable *Make Uniform*, and set *Power* to 3.


Example
=======

.. peertube:: 2d3eab8a-cc80-4d90-a3f1-419e2aa063f3
