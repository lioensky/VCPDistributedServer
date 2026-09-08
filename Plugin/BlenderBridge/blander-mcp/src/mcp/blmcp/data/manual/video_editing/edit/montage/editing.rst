
**************
Editing Strips
**************

Controls
========

.. _bpy.types.SequencerToolSettings.overlap_mode:

Overlap Mode
------------

Overlap Mode defines the result of transforming a strip so that it overlaps another strip.

:Expand:
   All strips on the right side of (each) transformed will be shifted forward to accommodate the overlapping strip.
:Overwrite: The overlapped strip will be overwritten, trimmed or split by the overlapping strip.
:Shuffle: The overlapping strip will be moved to the nearest free space so that it does not overlap.


.. _bpy.types.ToolSettings.use_snap_sequencer:

Snapping
--------

Snapping can be toggled by clicking :bl-icon:`snap_off` (Snap Off) / :bl-icon:`snap_on` (Snap On)
in the 3D Viewport's header, or temporarily by holding :kbd:`Ctrl` after starting to drag a strip.

The drop-down arrow offers the following options:

.. _bpy.types.SequencerToolSettings.snap_to_frame_range:
.. _bpy.types.SequencerToolSettings.snap_to_current_frame:
.. _bpy.types.SequencerToolSettings.snap_to_hold_offset:
.. _bpy.types.SequencerToolSettings.snap_to_markers:
.. _bpy.types.SequencerToolSettings.snap_to_retiming_keys:

Snap to
   Frame Range
      Snaps to the start and end frames of the preview or scene range or
      when inside a :doc:`Meta Strip </video_editing/edit/montage/meta>`
      snaps the target to the meta strip's display range.
   Current Frame
      Snaps the transformed selection to the Playhead.
   Hold Offset
      Snaps the transformed selection to the :ref:`Hold Offset <sequencer-duration-hard>`.
   Markers
      Snaps the transformed selection to :doc:`/animation/markers`.
   Retiming Keys
      Snaps the transformed selection to :ref:`sequencer-editing-retiming`.

.. _bpy.types.SequencerToolSettings.snap_ignore_muted:
.. _bpy.types.SequencerToolSettings.snap_ignore_sound:

Ignore
   Muted Strips
      Muted Strips are not considered as snap targets.
   Sound Strips
      Sound Strips are not considered as snap targets.


Transform
=========

.. _bpy.ops.transform.seq_slide:

Move
----

.. reference::

   :Menu:      :menuselection:`Strip --> Transform --> Move`
   :Shortcut:  :kbd:`G`

Pressing :kbd:`G` moves all the selected strip(s).
Move your mouse horizontally (left/right) to change the strip's position in time.
Move vertically (up/down) to change channels.

Holding down :kbd:`Ctrl` while dragging enables or disables snapping.

You can also lock the direction to time with :kbd:`X` or to change the strip's channel with :kbd:`Y`.

It is possible to move strips using mouse by dragging them while holding :kbd:`LMB`.
Currently it is possible to move only one strip by dragging.


Start Frame Offset
^^^^^^^^^^^^^^^^^^

The *Start Frame Offset* for that strip can be selected by clicking :kbd:`LMB` on the left handle of the strip;
holding it down (or pressing :kbd:`G` and then moving the mouse left/right)
changes the start frame within the strip by the number of frames you move it.
The frame number label under the strip displays the start frame of the strip.

- If you have a 20-image sequence strip, and drag the left handle to the right by 10 frames,
  the strip will start at image 11 (images 1 to 10 will be skipped).
  Use this to clip off a roll-up or undesired lead-in.
- Dragging the left handle left will create a lead-in (copies) of the first frame for as many frames as you drag it.
  Use this when you want some frames for a transition at the start of the clip.


End Frame
^^^^^^^^^

The *End Frame* of the strip could be selected by clicking :kbd:`LMB` on the right handle of the strip;
holding it down (or pressing :kbd:`G`) and then moving the mouse changes the ending frame within the strip.
The frame number label over the strip displays the end frame of the strip.

- Dragging the right handle to the left shortens the clip;
  any original images at the tail are ignored. Use this to quickly clip off a roll-down.
- Dragging the right handle to the right extends the clip.
  For movies and images sequences, more of the animation is used until exhausted.
  Extending a clip beyond its length will render as a copy of the last image.
  Use this for transitions out of this clip.

.. note:: Multiple selection

   You can select several (handles of) strips by :kbd:`Shift-LMB` clicking: when you press :kbd:`G`,
   everything that is selected will move with your mouse -- this means that,
   for example, you can at the same time move a strip, shorten two others, and extend a forth one.


Move/Extend from Current Frame
------------------------------

.. reference::

   :Menu:      :menuselection:`Strip --> Transform --> Move/Extend from Current Frame`
   :Shortcut:  :kbd:`E`

With a number of strips selected, pressing :kbd:`E` lets you interactively extend the strips.
This is similar to moving but is useful for extending (or shortening) time around the current frame.

All selected strip handles to the "mouse side" of the current frame indicator will transform together,
so you can change the duration of strips at the current frame.

.. hint::

   Extend is a convenient way to adjust the time of rough edits such as an "animatic" (sequential storyboards).
   Where it's possible to select everything and adjust the length of strips around the current frame.
   This can be especially useful when adding in audio or other elements that could cause
   the timing to need adjustment.

   When performing this operation you may want to enable :menuselection:`Markers --> Sync Markers`
   so markers are updated too.

   This simply a convenience operation, instead of manually selecting strips
   on one side of the current frame, as well as handles on one side of overlapping strips.
   Then selecting and transforming markers as well.
   This avoids the manual process, so re-timing can be accessed quickly.


.. _bpy.ops.sequencer.slip:

Slip Strip Contents
-------------------

.. reference::

   :Menu:      :menuselection:`Strip --> Transform --> Slip Strip Contents`
   :Shortcut:  :kbd:`S`

The *Slip Strip Contents* operator adjusts the start point of the source media inside a strip,
without changing the strip's position or length on the timeline.
This is useful for fine-tuning what portion of the media is shown.

It is commonly used when you want to preserve the strip's timing in the sequence
but choose a different part of the source to display.

Offset
   Number of frames to shift the content forward (positive) or backward (negative) in time.
Slip Keyframes
   If enabled, keyframes on the strip's properties (e.g. opacity, transform) will be moved along
   with the content. Disable this to keep keyframes fixed at their original timeline positions.

.. rubric:: Usage

Move the mouse left or right to shift the strip's content, then confirm the operation.
Additional options are available during the operation:

- **Confirm**: :kbd:`LMB`, :kbd:`Return`, :kbd:`Spacebar`
- **Cancel**: :kbd:`Esc`, :kbd:`RMB`
- **Precision Mode**: Hold :kbd:`Shift` to enable subframe slipping which slips the audio.
  The subframe amount is shown in the header as *Sound Offset*.
- **Clamp**: Press :kbd:`C` to clamp the slip range to the strip's start and end bounds.


.. _bpy.ops.sequencer.snap:

Snap Strips to the Current Frame
--------------------------------

.. reference::

   :Menu:      :menuselection:`Strip --> Transform --> Snap Strips to the Current Frame`
   :Shortcut:  :kbd:`Shift-S`

Moves the strip or control point to the current frame.


.. _bpy.ops.sequencer.offset_clear:

Clear Strip Offset
------------------

.. reference::

   :Menu:      :menuselection:`Strip --> Transform --> Clear Strip Offset`
   :Shortcut:  :kbd:`Alt-O`

To reset the (soft) start/end frame handles.


.. _bpy.ops.sequencer.swap:

Swap Strip
----------

.. reference::

   :Menu:      :menuselection:`Strip --> Transform --> Swap Strip`

Left :kbd:`Alt-Left`
   Swaps the active strip with the strip to the left.
Right :kbd:`Alt-Right`
   Swaps the active strip with the strip to the right.


.. _bpy.ops.sequencer.gap_remove:

Remove Gaps
-----------

.. reference::

   :Menu:      :menuselection:`Strip --> Transform --> Remove Gaps`
   :Shortcut:  :kbd:`Backspace`

Remove blank frames between the current frame and the first strip to the left,
independent of selection or locked state of strips.

All Gaps
   Remove gaps to the right of the strip along with the left.


Remove Gaps (All)
-----------------

.. reference::

   :Menu:      :menuselection:`Strip --> Transform --> Remove Gaps (All)`

Same as :ref:`bpy.ops.sequencer.gap_remove` but with *All Gaps* enabled.


.. _bpy.ops.sequencer.gap_insert:

Insert Gaps
-----------

.. reference::

   :Menu:      :menuselection:`Strip --> Transform --> Insert Gaps`
   :Shortcut:  :kbd:`Shift-Equals`

Insert blank frames between the current frame and the first strips to the right,
independent of selection or locked state of strips.


.. _sequencer-editing-retiming:

Retiming Keys
=============

.. figure:: /images/video-editing-retiming.png

Strips can be sped up or, slowed down by adding and moving retiming keys. Retiming controls can be activated for
individual strips, after which keys can be selected and moved.

.. note::

   - Only strip content is retimed, existing animation is not handled by the tool.
   - Effect strips can not be retimed.

.. hint::

   To quickly change selected strip speed, press :kbd:`R` and enter desired speed.


.. rubric:: Selecting Retiming Keys

Retiming keys are always shown on strip as inactive by default.
In order to select retiming keys, :ref:`Show Retiming Keys <bpy.types.Strip.show_retiming_keys>` must be enabled.
This property can also be enabled using :ref:`bpy.ops.sequencer.retiming_show`.

Multiple keys can be selected at once with box selection. Box select will select keys, only if a key is already
selected. Otherwise it will select strips only.

Use :kbd:`Ctrl-LMB` to select all keys to the right of the selected key.


.. rubric:: Moving Retiming Keys

Retiming key can be moved by dragging it with mouse, or by pressing :kbd:`G`. The key is mapped to particular frame
of strip content, so moving it effectively means moving a frame to a new position and therefore stretching, or
contracting time flow.

When a key is moved, this does not affect position of other keys inside of the strip. If strip has more keys inside,
multiple keys have to be selected, if only 1 segment has to be retimed. However if there are retiming keys outside
of strip boundary, these will be moved along with first or last key in strip in order to preserve
existing retiming, that is not visible.


.. _bpy.ops.sequencer.retiming_key_add:

Add Retiming Keys
-----------------

.. reference::

   :Editor:    Video Sequencer
   :Menu:      :menuselection:`Strip --> Retiming --> Add Retiming Key`

Retiming key can be added to selected strips from retiming menu
or by pressing :kbd:`I` and choosing Add Retiming Key option. This adds a key to current frame.
This operation will also create keys at strip start and end point, since these keys must be always present.

When keys are selected, strips are deselected, but it is still possible to add new keys.
In this case keys will be added to strips where any key is selected.


.. _bpy.ops.sequencer.retiming_add_freeze_frame_slide:

Add Freeze Frame and Slide
--------------------------

.. reference::

   :Editor:    Video Sequencer
   :Menu:      :menuselection:`Strip --> Retiming --> Add Freeze Frame and Slide`

Freeze frame is used to stop strip playback at particular frame for any duration.
Freeze frame can be added from strip retiming menu or context menu.

.. note::

   It is not possible to make smooth transition into or from freeze frame.


.. _bpy.ops.sequencer.retiming_add_transition_slide:

Add Speed Transition and Slide
------------------------------

.. reference::

   :Editor:    Video Sequencer
   :Menu:      :menuselection:`Strip --> Retiming --> Add Speed Transition and Slide`

It is possible to create smooth transition from one speed to another speed.
This can be done by selecting retiming key between 2 segments of different speeds,
and choosing Add Speed Transition either from strip retiming menu or context menu.
This will create 2 keys, that are linked and always move in opposite direction.
If both keys are moved at once, this changes where transition starts and ends.


Delete Retiming Keys
--------------------

.. reference::

   :Editor:    Video Sequencer
   :Menu:      :menuselection:`Strip --> Retiming --> Delete Retiming Keys`

Retiming key can be deleted by selecting and pressing :kbd:`Delete` or :kbd:`X`.
When handle is deleted, strip size will not change,
therefore speed will change to average between 2 retimed segments.

.. note::

   When transition key is removed, it will re-create simple retiming key from which transition was created.


.. _bpy.ops.sequencer.retiming_reset:

Reset Retiming
--------------

.. reference::

   :Editor:    Video Sequencer
   :Menu:      :menuselection:`Strip --> Retiming --> Reset Retiming`

Reverts all timing to the original strip.


.. _bpy.ops.sequencer.retiming_segment_speed_set:

Set Speed
---------

.. reference::

   :Editor:    Video Sequencer
   :Menu:      :menuselection:`Strip --> Retiming --> Set Speed`

Sets the speed of a retimed segment.

Speed
   The rate compared to the original time.
Preserve Current retiming
   Keeps the speed of the other retiming segments unchanged by adjusting the
   :ref:`Duration <bpy.types.Strip.frame_final_duration>` of the strip instead.


.. _bpy.ops.sequencer.retiming_show:

Toggle Retiming Keys
--------------------

.. reference::

   :Editor:    Video Sequencer
   :Menu:      :menuselection:`Strip --> Retiming --> Toggle Retiming Keys`
   :Shortcut:  :kbd:`Ctrl-R`

Enables the :ref:`Show Retiming Keys <bpy.types.Strip.show_retiming_keys>` strip property.
This allows retiming keys to be shown for the first time and enables interacting with them.


.. _bpy.ops.sequencer.split:

Split
=====

.. reference::

   :Menu:      :menuselection:`Strip --> Split`
   :Shortcut:  :kbd:`K`

This splits the selected strip in two at the current frame.
This will result in two strips which use the same source, fitting the original strip's timing and length.

.. hint::

   This can be thought of as a quick way to duplicate the current strip,
   adjusting the start/end frames to form two non-overlapping strips showing the same content as before.


Hold Split
==========

.. reference::

   :Menu:      :menuselection:`Strip --> Hold Split`
   :Shortcut:  :kbd:`Shift-K`

Like *Split*, it splits a strip in two distinct strips;
however you will not be able to drag the endpoints to show the frames past the split of each resulting strip.

Although you can adjust the :ref:`Hold Offset <sequencer-duration-hard>`
number fields in the *Strip Info* panel.

.. hint::

   This can be thought of as a way to simulate splitting the video file in two parts at the cut-point,
   replacing the current strip with each.


.. _bpy.ops.sequencer.duplicate_move:

Duplicate
=========

.. reference::

   :Menu:      :menuselection:`Strip --> Duplicate`
   :Shortcut:  :kbd:`Shift-D`

Duplicate a strip to make an unlinked copy;
drag it to a time and channel, and drop it by :kbd:`LMB` click.

For strips that reference an ID, for example scene strips, this will
duplicate the scene and use this new scene in the duplicated strip.

.. _bpy.ops.sequencer.duplicate_move_linked:

Duplicate Linked
================

.. reference::

   :Menu:      :menuselection:`Strip --> Duplicate Linked`
   :Shortcut:  :kbd:`Alt-D`

Duplicate a strip to make a linked copy;
drag it to a time and channel, and drop it by :kbd:`LMB` click.

For strips that reference an ID, for example scene strips, this will
use the same scene in the duplicated strip.

.. _bpy.ops.sequencer.delete:

Delete
======

.. reference::

   :Menu:      :menuselection:`Strip --> Delete`
   :Shortcut:  :kbd:`Delete`, :kbd:`X`

Delete the selected strip(s).


.. _bpy.ops.sequencer.scene_frame_range_update:

Update Scene Frame Range
========================

.. reference::

   :Menu:      :menuselection:`Strip --> Update Scene Frame Range`

For Scene strips only -- Updates the strip's :ref:`sequencer-strips-properties-time`
properties to match the referenced scene's frame range.
This operator should be used when the referenced scene's length is extended or shortened.


.. _bpy.ops.sequencer.images_separate:

Separate Images
===============

.. reference::

   :Menu:      :menuselection:`Strip --> Separate Images`
   :Shortcut:  :kbd:`Y`

For images sequence only -- Converts the strip into multiple strips, one strip for each frame.
Useful for slide shows and other cases where you want to bring in a set on non-continuous images.

Length
   You have to specify the duration you want the resulting strips will be.


Movie Strip
===========

.. _bpy.ops.sequencer.rendersize:

Set Render Size
---------------

.. reference::

   :Menu:      :menuselection:`Strip --> Set Render Size`

Sets the render resolution and aspect to match the strip's resolution.


.. _bpy.ops.sequencer.deinterlace_selected_movies:

Deinterlace Movies
------------------

.. reference::

   :Menu:      :menuselection:`Strip --> Deinterlace Movies`

Converts interlaced video into progressive video.


.. _sequencer-edit-change:

Effect Strip
============

.. _bpy.ops.sequencer.change_effect_type:

Change Effect Type
------------------

.. reference::

   :Menu:      :menuselection:`Strip --> Effect Strip --> Change Effect Type`

Replaces the selected effect strip with another effect type that requires the same number of inputs.

This operator preserves existing input strips and settings where possible,
making it quicker to experiment with different effects without manually recreating the setup.

For example, you can switch between effects like *Cross*, *Gamma Cross*, and *Wipe*, since they all use two inputs.


.. _bpy.ops.sequencer.reassign_inputs:

Reassign Inputs
---------------

.. reference::

   :Menu:      :menuselection:`Strip --> Effect Strip --> Reassign Inputs`
   :Shortcut:  :kbd:`R`

This tool can be used to assign (reconnect) effect strips in a different way.
Select three arbitrary strips and press :kbd:`R`.
If you don't create a cycle, those will be connected to a new effect chain.


.. _bpy.ops.sequencer.swap_inputs:

Swap Inputs
-----------

.. reference::

   :Menu:      :menuselection:`Strip --> Effect Strip --> Swap Inputs`
   :Shortcut:  :kbd:`Alt-S`

Swaps the first two inputs for the effect strip.


Lock/Mute
=========

.. _bpy.ops.sequencer.lock:

Lock Strips :kbd:`Ctrl-H`
   Disables the strip from being transformed.

.. _bpy.ops.sequencer.unlock:

Unlock Strips :kbd:`Ctrl-Alt-H`
   Enables disabled strips allowing them to be transformed.

.. _bpy.ops.sequencer.mute:
.. _bpy.ops.sequencer.unmute:

Mute/Unmute Strips :kbd:`H`, :kbd:`Alt-H`
   Mute or unmute the selected strips.

Mute/Unmute Deselected Strips :kbd:`Shift-H`, :kbd:`Shift-Alt-H`
   Mute or unmute all strips but the selected.


Inputs
======

.. _bpy.ops.sequencer.reload:

Reload Strips :kbd:`Alt-R`
   Reloads the strips from their external saved location.
Reload Strips and Adjust Length :kbd:`Shift-Alt-R`
   Reloads the strips from their external saved location and re-adjusts the strip duration.

.. _bpy.ops.sequencer.change_path:

Change Path/Files
   Changes the source file contained in a selected strip.

.. _bpy.ops.sequencer.swap_data:

Swap Data
   Swaps two sequence strips.


Image Menu
==========

.. _bpy.ops.sequencer.strip_transform_clear:

Clear
-----

Position
^^^^^^^^

.. reference::

   :Menu:      :menuselection:`Image --> Clear --> Position`

Resets the strips :ref:`Position Transforms <bpy.types.StripTransform.rotation>` to a value of zero.


Scale
^^^^^

.. reference::

   :Menu:      :menuselection:`Image --> Clear --> Scale`

Resets the strips :ref:`Scale Transforms <bpy.types.StripTransform.scale>` to a value of one.


Rotation
^^^^^^^^

.. reference::

   :Menu:      :menuselection:`Image --> Clear --> Rotation`

Resets the strips :ref:`Rotation Transform <bpy.types.StripTransform.rotation>` to a value of zero.


All Transforms
^^^^^^^^^^^^^^

.. reference::

   :Menu:      :menuselection:`Strip --> Clear --> All Transforms`

Resets the strips position, scale, and rotation :ref:`Transforms <bpy.types.StripTransform>` to
their default values.


.. _bpy.ops.sequencer.strip_transform_fit:

Apply
-----

Scale to Fit
^^^^^^^^^^^^

.. reference::

   :Menu:      :menuselection:`Strip --> Image Transform --> Scale to Fit`

Adjusts the strips :ref:`Scale Transforms <bpy.types.StripTransform.scale>`
so the visual contents of the strip to fit exactly within the project's
:ref:`Resolution <bpy.types.RenderSettings.resolution_x>`
while maintaining the original aspect ratio.

This may mean that the transparent areas may be added
along the content's border to fit the content in the rendered area.


Scale to Fill
^^^^^^^^^^^^^

.. reference::

   :Menu:      :menuselection:`Strip --> Image Transform --> Scale to Fill`

Adjusts the strips :ref:`Scale Transforms <bpy.types.StripTransform.scale>`
so the visual contents of the strip to span the project's
:ref:`Resolution <bpy.types.RenderSettings.resolution_x>`
while maintaining the original aspect ratio.

This may mean that portions of the original image no longer fit the content inside the rendered area.


Stretch to Fill
^^^^^^^^^^^^^^^

.. reference::

   :Menu:      :menuselection:`Strip --> Image Transform --> Stretch to Fill`

Adjusts the strips :ref:`Scale Transforms <bpy.types.StripTransform.scale>`
so the visual contents of the strip to fill the project's
:ref:`Resolution <bpy.types.RenderSettings.resolution_x>`.
Note, unlike the other two methods described above, *Stretch to Fill* does not maintaining the original aspect ratio.

This may mean that the original image becomes distorted to fit the content inside the rendered area.


Context Menu
============

You can activate context menu by clicking :kbd:`RMB` in the Sequencer's timeline.
In this menu you can quickly access some commonly used tools.


Fades
=====

.. reference::

   :Menu:      :menuselection:`Add --> Fades`

This submenu contains tools to add or remove fades to strips.
In case of visual strips the tools will animate the opacity or volume in case of audio strips.

Clear Fades
   Removes fade animation from selected sequences.
Fade In and Out
   Fade selected strips in and out.
Fade In
   Fade in selected strips.
Fade Out
   Fade out selected strips.
From Current Frame
   Fade from the current frame to the end of overlapping sequences.
To Current Frame
   Fade from the start of sequences under the Playhead to the current frame.
