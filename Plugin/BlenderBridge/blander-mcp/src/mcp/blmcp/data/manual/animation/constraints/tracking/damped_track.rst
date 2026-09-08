.. index:: Object Constraints; Damped Track Constraint
.. _bpy.types.DampedTrackConstraint:

***********************
Damped Track Constraint
***********************

The *Damped Track* constraint makes an object or bone point towards a certain target.
It's typically called "Look At" or "Aim" in other 3D software.

The word "damped" means that the constraint uses a pure :term:`swing` rotation
to minimize rolling around the tracking axis. This is in contrast to the
:doc:`/animation/constraints/tracking/track_to` which applies an "Up" axis
in addition to the tracking.


Options
=======

.. figure:: /images/animation_constraints_tracking_damped-track_panel.png

   Damped Track constraint.

:ref:`Target <rigging-constraints-interface-common-target>`
   The object or bone to point towards.

Track Axis
   The local axis of the owner that should point at the target.
   For bones, this should typically be Y.

   A negative axis will make the owner point away from the target instead.

:ref:`bpy.types.constraint.influence`
   How strongly the constraint affects the owner.


Example
=======

.. peertube:: 7a287522-9515-44f6-a4f2-34c5b5fb5f7a
