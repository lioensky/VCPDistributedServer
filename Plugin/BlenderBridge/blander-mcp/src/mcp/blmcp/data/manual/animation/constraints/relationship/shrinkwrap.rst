.. index:: Object Constraints; Shrinkwrap Constraint
.. _bpy.types.ShrinkwrapConstraint:

*********************
Shrinkwrap Constraint
*********************

The *Shrinkwrap* constraint snaps an object or bone to the surface of a mesh. It's similar
to the :doc:`/modeling/modifiers/deform/shrinkwrap`, which snaps every vertex of a mesh to
the surface of another.

Like other constraints, the *Shrinkwrap* constraint ignores the geometry of its owner object
and purely works with its :doc:`origin </scene_layout/object/origin>`. This means that, if the
origin is at the object's center, the object will clip into the target mesh instead of sitting
on its surface. This can be mitigated with the *Distance* setting.

Options
=======

.. figure:: /images/animation_constraints_relationship_shrinkwrap_panel.png

   Shrinkwrap constraint.

:ref:`Target <rigging-constraints-interface-common-target>`
   The mesh object to snap to.

Distance
   How far to stay away from the surface.

Mode
   How to find the point to snap to.

   :Nearest Surface Point:
      Snap to the surface point that's closest to the constraint owner's original location.
   :Project:
      Project the owner's original location along a certain axis and snap to the first
      intersection with the target surface. See `Project Mode Settings`_.
   :Nearest Vertex:
      Snap to the mesh vertex that's closest to the owner's original location.
   :Target Normal Project:
      Snap to the nearest surface point that, if projected along its normal, intersects
      the constraint owner's original location.

      This mode produces better results than *Nearest Surface Point* but is also slower to
      calculate. In addition, the surface normal is obtained by interpolating the surrounding
      vertex normals, which may not match the expected normal if the mesh uses flat shading.

Snap Mode
   Determines how the *Distance* offset is applied.

   :On Surface:
      Snap to the point that's *Distance* away from the surface and is on the same side
      as the owner's original location: if the owner was previously outside the mesh,
      it stays outside, and if it was inside, it stays inside.
   :Outside Surface:
      Snap to the point that's *Distance* away from the surface and is on the outside,
      regardless of where the owner was originally.
   :Above Surface:
      Like *Outside Surface*, but applies the offset along the interpolated surface normal.
      (The other modes apply it along the line between the constraint owner's original location
      and the snapping point on the target surface).
   :Inside:
      "Shrinks" the mesh by *Distance* and traps the owner inside it. (If the owner was already
      inside the shrunk volume, the constraint does nothing.)
   :Outside:
      "Inflates" the mesh by *Distance* and pushes the owner out of it. (If the owner was already
      outside the inflated volume, the constraint does nothing.)

   The *Inside* and *Outside* modes can be used for very crude collision detection. Because
   they only check the closest face of the target mesh, they won't give the expected result
   near sharp corners.

   If *Mode* is set to *Nearest Vertex*, this setting is not available and the constraint
   owner is simply snapped to the nearest location that's *Distance* away from the nearest
   vertex, regardless of any surface normals.

Align To Normal
   Aligns the specified local axis of the owner to the interpolated surface normal of the target.
   This is done using a :term:`swing` rotation.

   Not available for the *Nearest Vertex* mode.

:ref:`bpy.types.constraint.influence`
   How strongly the constraint affects the owner.


Project Mode Settings
---------------------

Project Axis
   The axis and direction to project along. If no intersection is found, the owner's location is left unchanged.

Space
   Coordinate space for the projection axis.

Distance
   Distance cutoff after which projection is assumed to have failed, leaving the location unchanged.
   A value of 0 means there's no limit.

Project Opposite
   Also project in the opposite direction (along the same axis).

Face Cull
   :Off:
      Snap to the first encountered face regardless of its normal.
   :Front:
      Don't snap if the projection hit the front side of a face (specifically, if the normal of
      the face points towards the constraint owner). In general, this means the owner will
      get snapped to the surface if it's inside the target mesh, and keep its original location otherwise.
   :Back:
      Don't snap if the projection hit the back side of a face (specifically, if the normal of
      the face points away from the constraint owner). In general, this means the owner will get
      snapped to the surface if it's outside the target mesh, and keep its original location otherwise.
   :Invert Cull:
      If *Project Opposite* is enabled and an intersection is found in this opposite direction,
      use the opposite *Face Cull* option (so *Back* if *Front* was chosen and vice versa).

Example
=======

.. peertube:: 41a7d6c3-5bd2-450e-a49e-67edf078fe3a
