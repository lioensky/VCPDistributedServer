.. _bpy.types.MovieStrip:

***********
Movie Strip
***********

To add a movie (with or without audio) select a movie file(s) in the File Browser
e.g. in the Audio-Video Interleaved format (``*.avi`` file).

.. note:: Clips can be Huge

   A three minute QuickTime ``.mov`` file can be 140MB.
   Loading it, even over a high-speed LAN can take some time.
   Do not assume your computer or Blender has locked up if nothing happens for awhile.

.. tip::

   Movie strips can display thumbnails in the Sequencer overlaid on their strips
   by enabling the :ref:`Thumbnails <bpy.types.SequencerTimelineOverlay.show_thumbnails>` overlay.


.. _bpy.ops.sequencer.movie_strip_add:

Add Movie Strip
===============

.. reference::

   :Menu:      :menuselection:`Add --> Movie`

Move Strips
   Use mouse to position strip in timeline immediately after adding. If this option is enabled, Start Frame and
   Channel properties are not displayed.
   
Start Frame
   The :ref:`Start Frame <bpy.types.Strip.frame_start>` to place the left handle of the strip.

Channel
   The :doc:`Channel </editors/video_sequencer/sequencer/channels>` to place the strip.


Relative Path
   Store the location of the image file relative to the blend-file.

Replace Selection
   Replaces the currently selected strips with the new strip.

Fit Method
   Determines how images with an aspect ratio different than the scene's
   :ref:`Resolution <bpy.types.RenderSettings.resolution_x>` are scaled to fit inside the render area.

   :Scale to Fit:
      Adjusts the strips :ref:`Scale Transforms <bpy.types.StripTransform.scale>` so the visual contents of
      the strip to fit exactly within the project's :ref:`Resolution <bpy.types.RenderSettings.resolution_x>`
      while maintaining the original aspect ratio.

      This may mean that the transparent areas may be added
      along the content's border to fit the content in the rendered area.
   :Scale to Fill:
      Adjusts the strips :ref:`Scale Transforms <bpy.types.StripTransform.scale>`
      so the visual contents of the strip to span the project's
      :ref:`Resolution <bpy.types.RenderSettings.resolution_x>` while maintaining the original aspect ratio.

      This may mean that portions of the original image no longer fit the content inside the rendered area.
   :Stretch to Fill:
      Adjusts the strips :ref:`Scale Transforms <bpy.types.StripTransform.scale>` so the visual contents of
      the strip to fill the project's :ref:`Resolution <bpy.types.RenderSettings.resolution_x>`. Note, unlike
      the other two methods described above, *Stretch to Fill* does not maintaining the original aspect ratio.

      This may mean that the original image becomes distorted to fit the content inside the rendered area.

Set View Transform
   Automatically sets an appropriate :ref:`View Transform <bpy.types.ColorManagedViewSettings.view_transform>`
   based on the :term:`Color Space` of the imported media. In most cases, the *Standard* should be used;
   using the wrong transform could result in inaccurate colors or degraded rendering performance.

Adjust Playback Rate
   Automatically adjusts the video's speed to playback at the original speed regardless of the scene's frame rate.

Sound
   Add a :doc:`Sound Strip </video_editing/edit/montage/strips/sound>` that contains the movie's audio track.

Set Scene Frame Rate
   Sets the :ref:`Scene Frame Rate <bpy.types.RenderSettings.fps>` to the frame rate encoded in the movie file.


Example
=======

.. figure:: /images/video-editing_sequencer_strips_movie-image_example.png

   Imported Movie strip with audio track underneath.

In the strip itself, you can see strip name, path to source file, and strip length.
