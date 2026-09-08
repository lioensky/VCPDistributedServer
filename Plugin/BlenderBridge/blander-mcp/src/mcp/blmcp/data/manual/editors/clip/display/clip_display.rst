.. _clip-editor-clip-display-label:

************
Clip Display
************

This pop-over contains various display settings for both Tracking mode and Mask mode.

.. _bpy.types.SpaceClipEditor.show_red_channel:
.. _bpy.types.SpaceClipEditor.show_green_channel:
.. _bpy.types.SpaceClipEditor.show_blue_channel:

R, G, B
   Controls the color channels used for the frame preview. The tracking algorithm works with grayscale images,
   and with these options, you can check which combination of enabled and disabled channels will yield
   the best contrast and the least noise.

   Note that this only affects the preview. To select which channels to use for the actual tracking,
   use the :doc:`Track tab in the Toolbar </movie_clip/tracking/clip/toolbar/track>` to set a default
   for newly created markers, or the :doc:`Track tab in the Sidebar </movie_clip/tracking/clip/sidebar/track/track>`
   to configure existing markers.

.. _bpy.types.SpaceClipEditor.use_grayscale_preview:

Grayscale Preview (B/W)
   Shows the whole frame as a grayscale image.

.. _bpy.types.SpaceClipEditor.use_mute_footage:

:bl-icon:`hide_off` Mute Footage :kbd:`M`
   Hides the movie clip and displays a black image instead.
   This helps to find markers that are tracked inaccurately or not at all.

.. _bpy.types.MovieClipUser.use_render_undistorted:

Render Undistorted
   Applies the :ref:`Lens settings <motion_tracking-camera-lens>` to the
   video preview to undo lens distortion. Does not change the footage itself.

.. _bpy.types.SpaceClipEditor.show_stable:

Show Stable
   Applies the :doc:`2D stabilization </movie_clip/tracking/clip/sidebar/stabilization/introduction>`
   settings to the video preview. Does not change the footage itself.

.. _bpy.types.SpaceClipEditor.show_grid:

Grid
   Displays a grid which is originally orthographic, but is distorted by the Lens settings.
   This can be used for manual calibration: the distorted grid lines should match lines
   in the footage that are meant to be straight.

.. _bpy.types.SpaceClipEditor.use_manual_calibration:

Calibration
   Applies the Lens settings to annotation strokes.
   Like the Grid, this option also helps to perform manual calibration.

.. _bpy.types.MovieClip.display_aspect:

Display Aspect Ratio
   Changes the aspect ratio for displaying only. It does not affect the tracking or solving process.


Marker Display
==============

Determines how markers are displayed in the editor.

Pattern
   Whether to show the pattern areas of tracks. Can be used to reduce clutter and
   check how good tracking is.

Search :kbd:`Alt-S`
   Whether to show the search areas of *selected* tracks. Can be used to reduce clutter and
   check how good tracking is.

Path
   Shows past (red) and future (blue) positions of tracks relative to the current frame,
   visualizing how they move. This makes it easier to spot irregularities.

Length
   Length (in frames) of the *Path*.

Show Disabled :kbd:`Alt-D`
   When unchecked, hides the tracks that are disabled on the current frame
   (except for the active track, i.e. the one that was selected last).
   This helps to make the view more clear and see if the tracking is accurate enough.

Info
   Displays the name and status of each selected track.
   The status can be "keyframed," "tracked," "disabled" and so on.

3D Markers
   Shows the result of :doc:`solving </movie_clip/tracking/clip/toolbar/solve>` the
   markers' 3D locations based on their 2D movement. Each 3D location is projected
   back to the movie clip and displayed as a small point, which is colored green if
   it's close to the original 2D marker (meaning a good solve) or red if it's far away
   (meaning it needs to be tweaked).

Display Thin
   By default, marker areas are displayed as bright boxes with a black outline.
   This option displays them using thin dashed lines instead.
