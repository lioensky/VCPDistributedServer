.. index:: Object Constraints; Camera Solver Constraint
.. _bpy.types.CameraSolverConstraint:

************************
Camera Solver Constraint
************************

The *Camera Solver* constraint makes a Blender camera imitate the motion of a real-world camera.

Usage
=====

Start by loading a video file into the :doc:`Movie Clip Editor </editors/clip/introduction>`
and using :doc:`motion tracking </movie_clip/tracking/introduction>` to track at least
eight :doc:`markers </movie_clip/tracking/clip/marker>` in the real-world scene.
Then use :ref:`bpy.ops.clip.solve_camera` to reconstruct the motion of the physical camera,
and finally add this constraint to a Blender camera.

Options
=======

.. figure:: /images/animation_constraints_motion-tracking_camera-solver_panel.png

   Camera Solver constraint.

Active Clip
   Whether to follow the physical camera of the scene's :ref:`Active Clip <bpy.types.Scene.active_clip>`.
   If unchecked, a selector appears for choosing another clip.

Constraint to F-Curve
   Replaces the constraint by a set of equivalent :doc:`keyframes </animation/keyframes/introduction>`.

:ref:`bpy.types.constraint.influence`
   How strongly the constraint affects the Blender camera.
