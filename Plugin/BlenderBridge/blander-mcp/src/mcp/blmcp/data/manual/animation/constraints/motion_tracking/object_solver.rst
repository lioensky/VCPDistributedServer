.. index:: Object Constraints; Object Solver Constraint
.. _bpy.types.ObjectSolverConstraint:

************************
Object Solver Constraint
************************

The *Object Solver* constraint makes a Blender object imitate the motion of a real-world object.

Usage
=====

Start by loading a video file into the :doc:`Movie Clip Editor </editors/clip/introduction>`,
registering the physical object in the :doc:`/movie_clip/tracking/clip/sidebar/track/objects`,
and using :doc:`motion tracking </movie_clip/tracking/introduction>` to track at least
eight :doc:`markers </movie_clip/tracking/clip/marker>` on that physical object.
Then use :ref:`bpy.ops.clip.solve_camera` to reconstruct the motion of the physical object,
and finally add this constraint to a Blender object.


Options
=======

.. figure:: /images/animation_constraints_motion-tracking_object-solver_panel.png

   Object Solver constraint.

Active Clip
   Whether the physical object is in the scene's :ref:`Active Clip <bpy.types.Scene.active_clip>`.
   If unchecked, a selector appears for choosing another clip.

Object
   The physical object whose motion to imitate. See the :doc:`/movie_clip/tracking/clip/sidebar/track/objects`
   in the Movie Clip Editor's Sidebar for setting this up.

Camera
   The Blender camera matching the physical camera that recorded the object.
   If left empty, the scene's :ref:`active camera <bpy.types.Scene.camera>` is used.

   If the physical camera was in motion, the Blender camera should have a
   :doc:`/animation/constraints/motion_tracking/camera_solver`. This constraint is useful even if
   the physical camera was stationary, because it makes the tracking markers appear at their
   reconstructed world positions in the 3D Viewport (if the :ref:`bpy.types.SpaceView3D.show_reconstruction`
   overlay is enabled).

Set Inverse
   Tell the constraint that the current Location of the Blender object (that is, its position with the constraint
   *disabled*) is the correct position for the current frame. Once this information is saved, the object will
   also be in the correct position for the other frames.

   - When initially adding the constraint:

     - Bring the object into position for the current frame.
     - Add the constraint.
     - Click *Set Inverse*.

   - When tweaking the object's position at a later point:

     - Run :ref:`Apply Visual Transform <bpy.ops.object.visual_transform_apply>`. (This may move the object
       to a different position.)
     - Disable the constraint. (This will bring the object back to its previous position.)
     - Tweak the object's position as desired.
     - Click *Set Inverse*.
     - Enable the constraint.

Clear Inverse
   Resets the relative transformation that was stored by *Set Inverse*.

Constraint to F-Curve
   Replaces the constraint by a set of equivalent keyframes.

:ref:`bpy.types.constraint.influence`
   How strongly the constraint affects its owner.
