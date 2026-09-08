.. index:: Object Constraints; Follow Track Constraint
.. _bpy.types.FollowTrackConstraint:

***********************
Follow Track Constraint
***********************

The *Follow Track* constraint makes an object imitate the movement of a
:doc:`motion tracking marker </movie_clip/tracking/clip/marker>`. This makes the object appear at the
same position in the render as where the marker appears in the motion-tracked video.

By default, the object follows the 2D motion of the marker in the video on a plane in the 3D world.
However, it's also possible to make the object follow the reconstructed 3D position of the marker.
The latter requires setting up at least eight markers and clicking :ref:`bpy.ops.clip.solve_camera`.

.. seealso::

   The :ref:`bpy.ops.clip.track_to_empty` button in the Movie Clip Editor creates an
   :doc:`Empty </modeling/empties>` and assigns it this constraint in one click.


Options
=======

.. figure:: /images/animation_constraints_motion-tracking_follow-track_panel.png

   Follow Track constraint.

Active Clip
   Whether the tracking marker is in the scene's :ref:`Active Clip <bpy.types.Scene.active_clip>`.
   If unchecked, a selector appears for choosing another clip.

3D Position
   Whether to use the tracking marker's reconstructed world position (instead of its position
   in the flat video).

Undistort
   Whether to use the tracking marker's video position after compensating for lens distortion
   (see :ref:`Lens settings <motion_tracking-camera-lens>`).
   Not available when *3D Position* is checked.

Frame Method
   How to handle a difference in aspect ratio between the tracked video footage and the rendered image.

   :Stretch:
      The object is positioned as though the video were stretched to exactly match the size of the
      rendered image.
   :Fit:
      The object is positioned as though the video were made as large as possible while still keeping
      its original aspect ratio and fitting inside the rendered image along both axes.
   :Crop:
      The object is positioned as though the video were made as large as possible while still keeping
      its original aspect ratio and fitting inside the rendered image along one axis.

   .. seealso::

      The :ref:`bpy.ops.clip.set_viewport_background` button in the Movie Clip Editor sets the video
      as the background for the camera. This background can then be resized by setting the same
      *Frame Method* in the :ref:`bpy.types.CameraBackgroundImage` panel of the camera's properties.

Object
   The physical object containing the tracking marker to follow. See the
   :doc:`/movie_clip/tracking/clip/sidebar/track/objects` in the Movie Clip Editor.
   If left empty, *Track* will list the markers used to reconstruct the physical camera.

Track
   The tracking marker to follow.

Camera
   The Blender camera in whose field of view the constrained object should appear.
   If left empty, the scene's :ref:`active camera <bpy.types.Scene.camera>` is used.

Depth Object
   If this object is set, the constrained object will be projected onto its surface.
   This can be used to create a facial makeup effect, for example.
   Not available when *3D Position* is checked.

Constraint to F-Curve
   Replaces the constraint by a set of equivalent :doc:`keyframes </animation/keyframes/introduction>`.

:ref:`bpy.types.constraint.influence`
   How strongly the constraint affects its owner.


Example
=======

`Follow Track Example Video <https://www.youtube.com/watch?v=KZalGrjGKSA>`__
