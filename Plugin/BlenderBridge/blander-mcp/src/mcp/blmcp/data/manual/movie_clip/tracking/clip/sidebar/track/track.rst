
*****
Track
*****

.. figure:: /images/movie-clip_tracking_clip_sidebar_track_track_panel.png
   :align: right
   :width: 195px

   Track panel.

.. _bpy.types.MovieTrackingTrack.name:

Name
   The track name can be changed with this field.
   Track names are used for linking tracking data to other areas, like a Follow Track constraint.

:bl-icon:`hide_off` Enable
   This toggle controls if the marker is enabled.
   If a marker is disabled, its position is not used either by solver nor by constraints.

.. _bpy.types.MovieTrackingTrack.lock:

:bl-icon:`unlock` / :bl-icon:`locked` Lock
   The toggle controls whether the track is locked. Locked tracks cannot be edited at all.
   This helps to prevent accidental changes to tracks which are "finished"
   (tracked accurate along the whole footage).


Track Preview Widget
====================

The widget in this panel is called "Track Preview" and it displays the content of the pattern area.
This helps to check how accurately the feature is being tracked
(controlling that there is no sliding off original position)
and also helps to move the track back to the correct position.
The track can be moved directly using this widget by mouse dragging.

If an anchor is used
(the position in the image which is tracking is different from the position which is used for parenting),
a preview widget will display the area around the anchor position.
This configuration helps in masking some things when there is no good feature at position where
the mask corner should be placed. Details of this technique will be written later.

There is small area below the preview widget which can be used to enlarge the vertical size of
preview widget (the area is highlighted with two horizontal lines).


Further Options
===============

.. _bpy.types.MovieTrackingTrack.use_red_channel:
.. _bpy.types.MovieTrackingTrack.use_green_channel:
.. _bpy.types.MovieTrackingTrack.use_blue_channel:

R, G, B
   Tracking happens in gray-scale space, so a high contrast between the feature and
   its background yields more accurate tracking.
   In such cases disabling some color channels can help.

.. _bpy.types.MovieTrackingTrack.use_grayscale_preview:

Grayscale Preview (B/W)
   Display the preview image as gray-scale even if all channels are enabled.

.. _bpy.types.MovieTrackingTrack.use_alpha_preview:

:bl-icon:`image_alpha` Alpha
   Applies mask defined by an annotation tool in the preview widget.

.. _bpy.types.MovieTrackingTrack.weight:

Weight
   When several tracks are used for 3D camera reconstruction, it is possible to assign
   a reduced weight to some tracks to control their influence on the solution result.
   This parameter can (and often need to) be animated.

   Altering the weights of problem tracking markers can correct or greatly reduce undesirable jumps
   as feature disappear or become difficult to track.

   Another use of Track Weights is when you want to reconstruct a scene from your camera solution.
   In that case you can first carefully track and solve your scene, and once you are done,
   lock all your markers with :kbd:`Ctrl-L`, set the tracker weight in the Extra Settings of
   the tracker settings to zero and use the feature detection to quickly add lots of markers.
   Now track them and solve the scene again. Since their weight is zero
   they will not influence your solution at all, but you will have lots of good reference points in your scene.

.. _bpy.types.MovieTrackingTrack.weight_stab:

Stabilization Weight
   While *Weight* parameter is used for 3D reconstruction,
   the *Stabilization Weight* is used to control 2D stabilization.

.. _bpy.ops.clip.track_copy_color:
.. _bpy.types.MovieTrackingTrack.use_custom_color:

Custom Color Presets
   The preset for the *Custom Color*.

.. _bpy.types.MovieTrackingTrack.color:

Custom Color
   This setting overrides the default marker color used in the Clip editor and 3D Viewport,
   and it helps to distinguish different type of features
   (for example, features in the background vs. foreground and so on).
   Color also can be used for "grouping" tracks so a whole group of tracks can be selected by
   color using the Select Grouped operator.

.. tip::

   To select good points for tracking, use points in the middle of the footage timeline
   and track backwards and forwards from there.
   This will provide a greater chance of the marker and point staying in the camera shot.
