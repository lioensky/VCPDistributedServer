
*****
Track
*****

Clip
====

Set Scene Frames
   See :ref:`bpy.ops.clip.set_scene_frames`.
Prefetch
   See :ref:`bpy.ops.clip.prefetch`.
Reload
   See :ref:`bpy.ops.clip.reload`.


Marker
======

Add
   See :ref:`bpy.ops.clip.add_marker_move`.
Delete
   See :ref:`bpy.ops.clip.delete_track`.
Detect Features
   See :ref:`bpy.ops.clip.detect_features`.


.. _clip-tracking-settings:

Tracking Settings
=================

This panel contains all settings for the 2D tracking algorithms.
Preset tracking settings can be configured in the panel header.
These presets are based on tracking experience of real footage and
provides good start values to begin working with a specific footage.

Pattern Size, Search Size
   Defines size of a newly created tracks.

Motion Model
   Defines which possible motions tracking feature has. This option should be set depending on
   which motion a particular feature has and it will make tracking most accurate for such a motion.

   Location, Location & Rotation, Location & Scale, Location, Rotation & Scale, Affine

   Perspective
      Is usually used to track a planar feature,
      but often *Affine* is a good enough approximation and may have more stable tracks.

Match
   Controls which patterns get tracked; to be more precise,
   the pattern from which frame is getting tracked. Here is an example which should make things clearer.

   The tracker algorithm receives two images inside the search area and the position of a point
   to be tracked in the first image.
   The tracker tries to find the position of that point from the first image in the second image.

   Now, this is how tracking of the sequence happens.
   The second image is always from a frame at which the position of marker is not known
   (next tracking frame). But a different first image
   (instead of the one that immediately precedes the second image in the footage)
   can be sent to the tracker.

   Keyframe
      An image created from a frame on which the track was keyframed.
      This configuration prevents sliding from the original position
      (because the position which best corresponds to the original pattern is returned by the tracker),
      but it can lead to small jumps and can lead to failures when the feature point is deformed due to camera motion
      (perspective transformation, for example).
   Previous Frame
      Keyframes for tracks are creating every frames,
      and tracking between keyframed image and next image is used.
      In this configuration the pattern is tracking between two neighboring frames.
      It allows dealing with cases of large transformations of the feature point
      but can lead to sliding from the original position, so it should be controlled.

Prepass
   Enables a two pass tracking, where the first pass is a brute force tracking of location only, and
   the second pass will use tracking of the full motion model refining the first pass.

Normalize
   Means patterns will be normalized by their average intensity while tracking,
   to make them invariant to illumination changes. An example where this is useful is a scene where
   a marker moves in the shadow of an object.

R, G, B
   Defines color channels which will be used by a tracking algorithm.
   Disabling some colors might increase the contrast to enhance the feature detection.

Copy from Active Track
   Copies all settings from active track. Allows to ease creation of new tracks with the same setting.

.. (alt) Previous frame: An image created from the current frame is sent as first image to the tracker.


Tracking Extra Settings
-----------------------

Weight
   See Track :ref:`Weight <bpy.types.MovieTrackingTrack.weight>`.

Correlation
   This value defines the minimal correlation between
   a matched pattern and a reference to be considered a successful tracking.
   If the tracker is stops too early, decrease this value, or if the track is slipping too much
   when it should stop sooner, increase this value.

Margin
   Can be used disable tracks when they become too close to the image boundary.
   This slider sets "too close" in pixels.

Use Mask
   Allows to use annotation tool to mask part of a pattern, narrowing down what the tracker algorithm is
   attempting to match across frames.

Frames Limit
   Controls how many frames can be tracked when the Track Sequence operator is called.
   So, each Track Sequence operation would track maximum *Frames Limit* frames.
   This also helps to notice a slide-off of tracks and correct them.

Speed
   Marker settings only -- Can be used to control the speed of sequence tracking.
   This option does not affect the quality of tracking; it just helps to control if tracking happens accurately.
   In most cases tracking happens much faster than real-time, and it is difficult to notice when a track began
   to slide out of position. In such cases *Speed* can be set to Double or Half to add some delay between
   tracking two frames, so a slide-off would be noticed earlier and the tracking process can be canceled to
   adjust positions of tracks.


Track
=====

Track
   See :ref:`bpy.ops.clip.track_markers`.
Clear
   See :ref:`bpy.ops.clip.clear_track_path`.
Refine
   See :ref:`bpy.ops.clip.refine_markers`.
Merge
   Join Tracks
      See :ref:`bpy.ops.clip.join_tracks`.
