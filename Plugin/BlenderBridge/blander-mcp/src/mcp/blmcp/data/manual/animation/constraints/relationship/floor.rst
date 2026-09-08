.. index:: Object Constraints; Floor Constraint
.. _bpy.types.FloorConstraint:

****************
Floor Constraint
****************

The *Floor* constraint sets up a flat and infinitely large floor (or wall, or ceiling)
which the constrained object or bone cannot pass through.

Like other constraints, the *Floor* constraint only looks at the
:doc:`origin </scene_layout/object/origin>` for objects; their geometry is not taken into account.
This means that, if a cube's origin is at its center and a *Floor* constraint is added targeting a
floor plane, the cube will still be able to sink halfway into the plane.
The *Offset* can be used to mitigate this.

.. seealso::

   :doc:`/animation/constraints/transform/limit_location`


Options
=======

.. figure:: /images/animation_constraints_relationship_floor_panel.png

   Floor constraint.

:ref:`Target <rigging-constraints-interface-common-target>`
   The object or bone that defines the location, and optionally the rotation, of the floor.

Offset
   Moves the virtual floor "up" or "down" by a certain distance. This makes it possible to,
   say, make foot bones stay a certain distance above the floor geometry to leave room for
   the actual feet.

Min/Max
   The axis that's perpendicular to the floor and points towards its "walkable" area.
   Setting this to Z creates a floor; X or Y creates a wall; and -Z creates a ceiling.

   By default, these axes correspond to the global axes.

Use Rotation
   Use the *Target*'s local axes for *Min/Max* instead of the global axes.

:ref:`Target/Owner <rigging-constraints-interface-common-space>`
   The spaces for evaluating and limiting the coordinates of the target and owner.

:ref:`bpy.types.constraint.influence`
   How strongly the constraint affects the owner.


Example
=======

.. peertube:: 03319687-56a4-460c-8b82-42b80e5b7980
