
******
Header
******

.. figure:: /images/video-editing_preview_introduction_header.png

   Header in Preview mode.


.. _bpy.types.SpaceSequenceEditor.show:

View Menu
=========

Toolbar :kbd:`T`
   Show or hide the :ref:`Toolbar <ui-region-toolbar>`.
Sidebar :kbd:`N`
   Show or hide the :ref:`Sidebar <ui-region-sidebar>`.
Tool Settings
   Show or hide the settings for the currently selected tool.
Footer
   Show or hide the :ref:`Sidebar <ui-region-footer>`.

----------

.. _bpy.types.SpaceSequenceEditor.show_transform_preview:

Preview During Transform
   Show a preview of the start or end frame of a strip while transforming its respective handle.

----------

Refresh All
   Reloads external files and refreshes the current frame preview.
   This is useful when you modified an external file or made a change in a scene that Blender
   didn't detect.

----------

Frame Selected
   Pan and zoom the view to focus on the selected image.
Fit Preview in Window :kbd:`Home`
   Pan and zoom the view so that the entire video is visible.
   This enables *Zoom to Fit*.

Zoom
   Menu with convenient zoom levels and operations.
   The zoom levels are calculated based on the images resolution compared to the screen resolution.

   - 12.5% (1:8) :kbd:`Numpad8` zoom out to a factor of 12.5%.
   - 25% (1:4) :kbd:`Numpad4` zoom out to a factor of 25%.
   - 50% (1:2) :kbd:`Numpad2` zoom out to a factor of 50%.
   - 100% (1:1) :kbd:`Numpad1` resets the zoom to 100%.
   - 200% (2:1) :kbd:`Ctrl-Numpad2` zoom in to a factor of 200%.
   - 400% (4:1) :kbd:`Ctrl-Numpad4` zoom in to a factor of 400%.
   - 800% (8:1) :kbd:`Ctrl-Numpad8` zoom in to a factor of 800%.

   Zoom In/Out :kbd:`Wheel`
      Zooms the view in or out.
   Zoom to Fit :kbd:`Shift-Home`
      Like *Frame All*, but uses as much space in the editor as possible.
   Zoom Region :kbd:`Shift-B`
      Zoom in the view to the nearest item contained in the border.

.. _bpy.types.SpaceSequenceEditor.use_zoom_to_fit:

Auto Zoom
   As long as this option is enabled, the preview will automatically zoom to keep the
   video size synchronized with the editor size.

----------

Proxy
   See :doc:`/editors/video_sequencer/sequencer/sidebar/proxy`.

----------

Sequence Render Image
   Show the current frame preview as a Render Result where you can save it as an image file.
Sequence Render Animation
   Save previews of the frames in the scene range (or the preview range, if active) to a video file
   or a series of image files. See the :doc:`/render/output/properties/output` panel for details.

.. note::
   *Sequence Render Image* and *Sequence Render Animation* don't render the final video by default --
   specifically, they don't render Scene Strips, instead using the preview's
   :doc:`shading mode </editors/3dview/display/shading>` (which is initially Solid).

   To output a video where the Scene Strips are rendered, use the *Render* menu in the top-bar,
   or change :menuselection:`Sidebar --> View --> Scene Strip Display --> Shading` to *Rendered*.

----------

.. _bpy.ops.sequencer.export_subtitles:

Export Subtitles
   Exports :doc:`Text strips </video_editing/edit/montage/strips/text>`,
   which can act as subtitles, to a `SubRip <https://en.wikipedia.org/wiki/SubRip>`__ file (``.srt``).
   The exported file contains all Text strips in the video sequence.

----------

Toggle Sequencer/Preview :kbd:`Ctrl-Tab`
   Switch the editor mode between *Sequencer* and *Preview*.

----------

Area
   Area controls. See the :doc:`user interface </interface/window_system/areas>`
   documentation for more information.


Select Menu
===========

See :doc:`/video_editing/edit/montage/selecting`.

Strip Menu
==========

See :doc:`/video_editing/edit/montage/editing` for more information.

Mirror
   Interactive Mirror :kbd:`Ctrl-M`
      Starts mirror operation based on mouse cursor position
   X Global
      Mirrors the image in global X coordinates
   Y Global
      Mirrors the image in global Y coordinates
   X Local
      Mirrors the image in local X coordinates
   Y Local
      Mirrors the image in local Y coordinates

.. _bpy.ops.sequencer.preview_duplicate_move:

Duplicate :kbd:`Shift-D`
   The *Duplicate* operator creates a copy of the selected strip(s)
   and places them in the nearest available channel above the original.

   The duplicated content remain selected, allowing immediate repositioning.

.. seealso::

   :ref:`bpy.ops.sequencer.duplicate_move`

Copy :kbd:`Ctrl-C`
   Adds selected strips to copy-paste buffer.

Paste :kbd:`Ctrl-V`
   Paste strips from copy-paste buffer.

Animation
   Insert Keyframe :kbd:`I`
      See :ref:`Insert Keyframe <bpy.ops.anim.keyframe_insert>`.

   Insert Keyframe with Keying Set :kbd:`K`
      See :ref:`Insert Keyframe with Keying Set <bpy.ops.anim.keyframe_insert_menu>`.

   Change Keying Set :kbd:`Shift-K`
      See :ref:`Set Active Keying Set <bpy.ops.anim.keying_set_active_set>`.

   Delete Keyframes :kbd:`Alt-I`
      See :ref:`Delete Keyframes <bpy.ops.anim.keyframe_delete>`.

   Clear Keyframes :kbd:`Shift-Alt-I`
      See :ref:`Clear Keyframes <bpy.ops.anim.keyframe_clear>`.

.. seealso::
   :doc:`Editing Keyframes </animation/keyframes/editing>`

Show/Hide
   Show Hidden Strips :kbd:`Alt-H`
      Reveals all hidden/muted strips.
   Hide Selected :kbd:`H`
      Mutes the selected strips.
   Hide Unselected :kbd:`Shift-H`
      Mutes all strips except for the currently selected strips.

Delete
   Delete selected strips

Image Menu
==========

Transform
   Move Origin :kbd:`Ctrl-Period`
      Moves the origin of the image strip without changing the strip's content position.

      This is useful for adjusting the reference point for transformations like rotation, scaling, or further
      positioning. For example, shifting the origin to a corner of the image allows rotations to pivot around that
      corner, rather than the default center.

Clear
   Resets the position, rotation, or scale of the selected images.
Apply
   Scale to Fit
      Resizes the selected images so that they're as large as possible while still
      fitting completely inside the video. They don't get cropped, and their aspect ratio
      stays the same.

   Scale to Fill
      Resizes the selected images to that they fill the entire video space.
      They may get cropped, but their aspect ratio stays the same.

   Stretch to Fill
      Resizes the selected images to match the video dimensions.
      They don't get cropped, but their aspect ratio may change.


Pivot Point
===========

See :doc:`/editors/video_sequencer/preview/controls/pivot_point`.


Display Mode
============

See :doc:`/editors/video_sequencer/preview/display/display_mode`.


Display Channels
================

Color & Alpha
   Display the preview image with transparency over a checkerboard pattern.
Color
   Ignore the transparency of the preview image (fully transparent areas will be black).


Gizmos
======

See :doc:`/editors/video_sequencer/preview/display/gizmos`.

Overlays
========

See :doc:`/editors/video_sequencer/preview/display/overlays`.
