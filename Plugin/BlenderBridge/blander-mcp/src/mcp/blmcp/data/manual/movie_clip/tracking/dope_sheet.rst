
***************
Dope Sheet View
***************

.. figure:: /images/movie-clip_tracking_dope-sheet_example.png

   Dope Sheet View.

The Dope Sheet View is used to visualize motion tracking data,
it is implemented as separate view of the Movie Clip editor just like the Graph View.

It displays channels for selected tracks and each channel visualizes tracked
segments of tracks as dark bars and keyframed positions of tracks as small diamonds.

The background is highlighted depending on the number of tracks in a frame.
This means that if for a frame (or sequence of frames) there are less than eight tracks,
the background will turn red;
if there are from eight to sixteen tracks, the background will be yellow.

This is only a visual feedback, which doesn't mean that the camera motion will not
reconstruct with less than eight tracks. It only means that you should pay attention to those frames and
check if all possible good feature points are tracked there. Remember, if there are no good feature points in
the frame and there are less than 16 tracks in the frame, it doesn't mean the solution won't be accurate.
Rather, adding more tracks on bad feature points will reduce the accuracy of solution.


Header
======

.. figure:: /images/movie-clip_tracking_dope-sheet_sort.png
   :align: right

   Sort order of the channels.

:bl-icon:`restrict_select_off` Only Show Selected
   Limits Dope Sheet channels to only information about selected tracks.
:bl-icon:`ghost_enabled` Display Hidden
   Includes information from hidden tracks.

.. _bpy.types.MovieTrackingDopesheet.sort_method:

Dopesheet Sort Field
   Sort order of the tracks.

   :Name: Sort selected tracks in alphabetical order based on their names.
   :Longest: Sort tracks by longest tracked segment length.
   :Total: Sort tracks by overall amount of frames.
   :Average Error: Sort tracks by their average reprojection error after solving camera or object motion.
   :Start Frame: Sort channels by first frame number.
   :End Frame: Sort channels by last frame number.

.. _bpy.types.MovieTrackingDopesheet.use_invert_sort:

Invert
   To change the sort order from ascending to descending.


Usage
=====

The Dope Sheet View is for visualization and does not have any tools to actually edit data.
