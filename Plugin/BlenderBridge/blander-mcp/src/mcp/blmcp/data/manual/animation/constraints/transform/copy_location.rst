.. index:: Object Constraints; Copy Location Constraint
.. _bpy.types.CopyLocationConstraint:

************************
Copy Location Constraint
************************

The *Copy Location* constraint forces an object or bone to match the location of a target.

.. important::

   This constraint has no effect on :ref:`connected bones <bpy.types.EditBone.use_connect>`
   as their position is determined by their parent bone.


Options
=======

.. figure:: /images/animation_constraints_transform_copy-location_panel.png

   Copy Location constraint.

:ref:`Target <rigging-constraints-interface-common-target>`
   The object or bone whose location to copy.

Axis
   The axes for which to copy location coordinates.

Invert
   The axes for which invert the sign (so a coordinate of 10 becomes -10 and vice versa).

Offset
   When enabled, the target's current position (from all its constraints) is not copied over,
   but added to the owner's original position (from its preceding constraints).

:ref:`Target/Owner <rigging-constraints-interface-common-space>`
   The spaces for retrieving the coordinates from the target and for applying them to the owner.

:ref:`bpy.types.constraint.influence`
   How strongly the constraint affects the owner.


Examples
========

Bones and Vertex Groups
-----------------------

This video shows the effect of the *Head/Tail* setting when targeting a bone,
as well as the *Vertex Group* setting when targeting a mesh.

.. peertube:: 2f3dc43b-ef61-42ae-9d8e-7924a1758411


Solar System
------------

In the animation below, the camera follows the moon as it orbits the Earth,
switches to following the Earth as it orbits the Sun, and finally moves to a fixed
location for showing the Sun. This is done using two *Copy Location* constraints --
one for the moon and one for the Earth -- with animated *Influence* values for
smoothly disabling one while enabling the other.

.. peertube:: ff427260-9631-40d9-bd39-65f21f95e9ad

..
   You can download
   the `blend-file <https://archive.blender.org/wiki/2015/index.php/File:ManAnimationTechsUsingConstraintsExSolarSys.blend>`__
   used to create this animation.

   ^ Commented out because the drivers no longer work in the current Blender version
