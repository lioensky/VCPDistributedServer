
**********
Navigating
**********

Header
======

.. figure:: /images/video-editing_sequencer_navigating_header.png
   :align: center

   Video Sequencer Header.


.. _bpy.types.SpaceSequenceEditor.show_region_hud:

View Menu
---------

The View menu controls the editor's view settings.

Toolbar :kbd:`T`
   Show or hide the :ref:`Toolbar <ui-region-toolbar>`.
Sidebar :kbd:`N`
   Show or hide the :ref:`Sidebar <ui-region-sidebar>`.
Tool Settings
   Show or hide the settings for the currently selected tool.
Adjust Last Operation
   Displays a pop-up panel to alter properties of the last
   completed operation. See :ref:`bpy.ops.screen.redo_last`.
Channels
   Show or hide the :ref:`bpy.types.SequenceTimelineChannel`.
Playback Controls
   Show or hide the :ref:`Playback Controls <animation-editors-footer>`.

----------

.. _bpy.ops.sequencer.refresh_all:

Refresh All :kbd:`Ctrl-E`
   Reloads external files and refreshes the current frame preview.
   This is useful when you modified an external file or made a change in a scene that Blender
   didn't detect.

----------

Frame Selected :kbd:`NumpadPeriod`
   Zooms the display to show only the selected strips.
Frame All :kbd:`Home`
   Zooms the display to show all strips.
Frame Scene/Preview Range
   Reset the horizontal view to the current scene frame range,
   taking the preview range into account if it is active.
Go to Current Frame :kbd:`Numpad0`
   Centers the horizontal timeline on the current frame.
Zoom to Border :kbd:`Shift-B`
   Click and drag to draw a rectangle and zoom to this rectangle.

.. _bpy.types.SpaceSequenceEditor.use_clamp_view:

Limit View to Contents
   Prevents you from panning higher than the highest used channel.

----------

Show Markers
   Shows the marker region. When disabled, the *Marker* menu is also hidden
   and marker operators are not available in this editor.
Use Timecode :kbd:`Ctrl-T`
   Shows seconds instead of frames on the time axis.
Sync Visible Range
   Synchronizes the horizontal panning and scale of the editor
   with other time-based editors that also have this option enabled.
   That way, they always show the same section of time.

----------

Navigation
   Play Animation :kbd:`Spacebar`
      Start or stop animation playback. This will start playback in all editors.
   Go to Current Frame :kbd:`Numpad0`
      Scrolls the timeline so the current frame is in the center.
   Jump to Previous Strip :kbd:`PageUp`
      Moves the playhead to the nearest strip border (start or end) that's before the current frame.
   Jump to Next Strip :kbd:`PageDown`
      Moves the playhead to the nearest strip border (start or end) that's after the current frame.
   Jump to Previous Strip (Center) :kbd:`Alt-PageUp`
      Moves the playhead to the nearest strip center that's before the current frame.
   Jump to Next Strip (Center) :kbd:`Alt-PageDown`
      Moves the playhead to the nearest strip center that's after the current frame.

Range
   Set Preview Range :kbd:`P`
      Interactively define the frame range used for preview playback/rendering.

      As long as this range is active, playback will be limited to it, letting you repeatedly view a
      segment of the video without having to manually rewind each time. It also limits the range
      that gets rendered by *Sequence Render Animation* (see below).

   .. _bpy.ops.sequencer.set_range_to_strips:

   Set Preview Range to Strips
      Apply a preview range that encompasses the selected strips.
   Clear Preview Range :kbd:`Alt-P`
      Clears the preview range.
   Set Start Frame :kbd:`Ctrl-Home`
      Set the Start frame of the scene to the current frame.
   Set End Frame :kbd:`Ctrl-End`
      Set the End frame of the scene to the current frame.
   Set Frame Range to Strips
      Set the Start and End frames of the scene so they encompass the selected strips.

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
   The latter option is only available if the Video Sequencer is in the *Preview* or
   *Sequencer & Preview* mode.

----------

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


Marker Menu
-----------

:doc:`Markers </animation/markers>` are used to denote frames with key points or significant events
within an animation. Like with most animation editors, markers are shown at the bottom of the editor.

.. figure:: /images/editors_graph-editor_introduction_markers.png

   Markers in animation editor.

See :ref:`Editing Markers <animation-markers-editing>` for details.


Sequencer Scene
---------------

A :ref:`data-block menu <ui-data-block>` to select a scene.
The :doc:`Sequencer Scene </video_editing/sequencer_scene>`
is the scene that the edit shown in the Sequencer is contained in.


Playback Controls
=================

The Playback Controls region contains controls and options
related to playback, keying, auto keyframing, and transport.

These settings allow you to:

- Control how animations are previewed and synchronized with audio.
- Insert and manage keyframes through keying sets and auto keying.
- Navigate the timeline using playback and transport controls.
- Adjust frame ranges and preview specific segments of the animation.

Sync Scene Time
   Set the active scene and time based on the current scene strip.
   See the :ref:`workspace settings <bpy.types.WorkSpace.use_scene_time_sync>`.

.. seealso::

   For a detailed description of all properties and controls commonly found in the footer,
   see the :ref:`Playback Controls <animation-editors-footer>` documentation.


Main View
=========

Adjusting the View
------------------

Use these shortcuts to adjust the view:

- Pan: :kbd:`MMB`
- Horizontal scroll: use :kbd:`Ctrl-Wheel`, or drag the horizontal scrollbar.
- Vertical scroll: use :kbd:`Shift-Wheel`, or drag the vertical scrollbar.
- Zoom: :kbd:`Wheel`
- Scale view: :kbd:`Ctrl-MMB` and drag left/right (horizontal scale) or up/down (vertical scale).
  Alternatively, you can drag the circles on the scrollbars with :kbd:`LMB`.

Playhead
--------

The Playhead is the blue vertical line with the current time at the top. To see how to interact with it
see the :ref:`Playhead <playhead>` documentation. In addition to that, the Video
Sequencer has a special case where if you start dragging on a strip, that strip will be highlighted
and displayed *solo* in the preview (all other strips are temporarily muted).

If scrubbing (or regular playback) performs poorly, you can speed it up by creating
:doc:`proxies </editors/video_sequencer/sequencer/sidebar/proxy>`.

.. hint::

   The current frame is synchronized across all editors, so if you move the Playhead in the
   Timeline editor for example, it will move in the Video Sequence editor as well (and vice versa).
