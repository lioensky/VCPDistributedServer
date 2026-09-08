.. index:: Object Constraints; Track To Constraint
.. _bpy.types.TrackToConstraint:

*******************
Track To Constraint
*******************

The *Track To* constraint makes an object or bone point towards a certain target,
then roll to make a certain local axis point upwards.
It's typically called "Look At" or "Aim" in other 3D software.

If the constraint owner is almost directly above the target, the roll around
the tracking axis will become unstable. For this scenario, it's recommended to
use the :doc:`/animation/constraints/tracking/damped_track` instead.


Options
=======

.. figure:: /images/animation_constraints_tracking_track-to_panel.png

   Track To constraint.

:ref:`Target <rigging-constraints-interface-common-target>`
   The object or bone to point towards.

Track Axis
   The local axis of the owner that should point at the target.
   For bones, this should typically be Y.

   A negative axis will make the owner point away from the target instead.

Up
   The local axis of the owner that should point upwards in the world.

.. important::

   The *Track Axis* and the *Up* axis must be different. If they are the same,
   the constraint will stop working and its icon will turn red.

Target Z
   Align the owner's *Up* axis as closely as possible to the target's Z axis
   instead of the global one.

:ref:`Target/Owner <rigging-constraints-interface-common-space>`
   The spaces for evaluating the target and owner transforms.

:ref:`bpy.types.constraint.influence`
   How strongly the constraint affects the owner.


Example
=======

.. peertube:: 891bf27f-f782-4908-bfa0-f99e5dc46107
