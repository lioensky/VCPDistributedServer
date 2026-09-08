
***********
Plane Track
***********

.. figure:: /images/movie-clip_tracking_clip_sidebar_track_plane-track_panel.png
   :align: right
   :width: 195px

   Plane Track panel.

Its properties are shown only when a plane track is selected.

.. _bpy.types.MovieTrackingPlaneTrack.name:

Name
   The name of the selected plane track is shown. It can also be changed from here.

.. _bpy.types.MovieTrackingPlaneTrack.use_auto_keying:

Auto Keyframe
   Toggles the auto-keyframing for corners of the plane track.
   With this enabled, keyframes will automatically get inserted when any corner is moved.

Image
   Field to select or create an image which will be displayed inside the plane track.
   This image is for preview purposes in the Movie Clip editor only.
   To include it in your final render,
   see :doc:`Plane Track Deform node </compositing/types/tracking/plane_track_deform>`.

New Image from Plane Track
    Creates an image from the pixels of the Movie Clip that the plane marker "sees" at the current frame.
    This allows to create an unwarped texture of any flat surface in the footage.
    The resulting image can then be used for editing and retouching, for example to paint out certain parts
    of the footage.
Update Image from Plane Track
    Updates the pixels of the active Plane Track's image.

.. _bpy.types.MovieTrackingPlaneTrack.image_opacity:

Opacity
   Used to set the opacity of this image. Again,
   this is for display purposes only, and will not affect your final render.
