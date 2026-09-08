.. _bpy.types.ImageStrip:

********************
Image/Sequence Strip
********************

Image strips are used to add still images or numbered image sequences
to the Video Sequencer. They are commonly used for slides, graphic overlays,
background plates, rendered image sequences, or frame-by-frame animation.

A single image strip displays one still image for a specified duration,
while an image sequence strip plays a series of images over time, with each image
representing a single frame. Both strip types support transforms, effects,
color management, and compositing with other strips in the timeline.

.. tip::

   Image strips can display thumbnails in the Sequencer overlaid on their strips
   by enabling the :ref:`Thumbnails <bpy.types.SequencerTimelineOverlay.show_thumbnails>` overlay.


Single Image
============

When you add a single still image (``*.jpg``, ``*.png``, etc.),
by default, Blender will create a 25 frame long strip which renders
the image throughout the strip's range in the timeline.
This length can be adjusted by adding images through the
"Add Image Strip" operator and changing the property in the sidebar.


Image Sequence
==============

In the case of (numbered) image sequences
(e.g. ``*-0001.jpg``, ``*-0002.jpg``, ``*-0003.jpg``, etc, of any image format), you have a choice:

Range
   Navigate into the directory and :kbd:`LMB` click and drag over a range of names to highlight multiple files.
   You can page down and continue :kbd:`Shift-LMB` click-dragging to add more to the selection.
Batch
   :kbd:`Shift-LMB` click selected non-related stills for batch processing; each image will be one frame,
   in sort order, and can be a mix of file types (``jpg``, ``png``, ``exr``, etc.).
All
   Press :kbd:`A` to select/deselect all files in the directory.

.. tip:: Dealing with Different Sizes

   Dealing with different sized images and different sized outputs is tricky.
   If you have a mismatch between the size of the input image and the render output size,
   the Video Sequencer will try to auto-scale the image to fit it entirely in the output.
   This may result in clipping. If you do not want that, use *Crop* and/or *Offset* in the Input
   panel to move and select a region of the image within the output. When you use *Crop* or *Offset*,
   the auto-scaling will be disabled and you can manually re-scale by adding the Transform effect.


.. _bpy.ops.sequencer.image_strip_add:

Add Image Strip
===============

.. reference::

   :Menu:      :menuselection:`Add --> Image/Sequence`

Move Strips
   Use the mouse to position the strip in the timeline immediately after adding it. If this option is enabled,
   Start Frame and Channel properties are not displayed since they are determined interactively.

Start Frame
   The :ref:`Start Frame <bpy.types.Strip.frame_start>` to place the left handle of the strip.

Channel
   The :doc:`Channel </editors/video_sequencer/sequencer/channels>` to place the strip.

Replace Selection
   Previously selected strips will be deselected. Only added strips will be selected.

Relative Path
   Store the location of the image file relative to the blend-file.

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

Import As
   Determines the method for importing images.

   :Auto Detect:
      Filenames that are numbered consecutively (see :ref:`image-formats-open-sequence`)
      will be imported as a single image sequence with length equal to the number of images.
      Otherwise, files are imported as separate image strips with the given length.
   :Image Sequence:
      All images are imported as a single image sequence, no matter their extension or filename.
      Note that since these files do not have to be numbered, placeholders are not supported for this mode.
   :Individual Images:
      Each image is imported as a separate image strip with the given length, placed one after the other.

Use Placeholders
   Image sequences can use placeholder files.
   This works by enabling *Use Placeholders* checkbox when adding an image strip.
   The option detects the frame range of opened images using Blender's frame naming scheme
   (``filename + frame number + .extension``) and makes an image sequence
   with all files in between even if they are missing.
   This allows you to render an image sequence with a few frames missing, while ensuring that the image sequence strip
   maintains the correct length. Placeholder frames are rendered in pink in the VSE preview.

   When the missing frames are rendered out or placed into the folder with the rest of the image sequence,
   you can :ref:`refresh <bpy.ops.sequencer.refresh_all>`
   the Sequencer and the placeholder frames will be filled in.
   The option is also available when using the *Change Data/File* operator and
   allows you to add more images to the range.

Length
   Length of added strip. This value is not used when importing image sequences,
   since their length in frames is determined by the number of images in the sequence.
