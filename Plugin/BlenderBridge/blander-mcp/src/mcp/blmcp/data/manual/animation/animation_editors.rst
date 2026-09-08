
*****************
Animation Editors
*****************

Blender provides a set of editors designed for creating, editing, and refining animation.
These editors let you work with keyframes, curves, non-linear actions, drivers,
video sequencing, and motion tracking as part of the animation pipeline.

Each editor serves a different purpose:

- The :doc:`Dope Sheet </editors/dope_sheet/introduction>` organizes and manipulates keyframes
  across multiple objects and data-blocks.
- The :doc:`Graph Editor </editors/graph_editor/introduction>` provides fine control over F-Curves
  to refine motion and interpolation.
- The :doc:`Nonlinear Animation (NLA) Editor </editors/nla/introduction>` arranges and layers animation
  actions for complex sequencing.
- The :doc:`Drivers Editor </editors/drivers_editor>` links properties with expressions
  for procedural animation.
- The :doc:`Movie Clip Editor </editors/clip/introduction>` supports motion tracking, mask editing,
  and stabilization, which can be integrated into animation and compositing workflows.
- The :doc:`Video Sequence Editor </editors/video_sequencer/introduction>` (VSE) combines
  rendered animations, image sequences, audio, and effects into a final movie edit.

Together, these editors form the backbone of Blender's animation system --
from quick keyframe adjustments to advanced rigging, motion editing, visual effects integration,
and final shot assembly.

This page describes features that are shared across the different animation focused editors.


.. _playhead:

Playhead
========

.. figure:: /images/editors_timeline_cursor.png
   :align: right

   Playhead.

The *Playhead* is the blue vertical line showing the current frame number.

It can be moved to a new position by clicking or
dragging :kbd:`LMB` in the scrubbing area at the top or by
click and drag :kbd:`Shift-RMB` anywhere in the timeline.

While dragging it can snap to elements of the editor in which it is dragged.
- Seconds
- Frames
- Markers
- Strips
- Keys

It is only possible to snap to elements that are visible in the editor in which the playhead is dragged.
For example having "Strips" enabled but dragging in the Graph Editor will do nothing.
Snapping can be toggled during scrubbing by holding down :kbd:`Ctrl`.

Snapping to seconds or frames can have a custom increment for example snapping to every third frame.
This is always relative to the first frame of the scene and ignores the preview range.
In contrast to the other snapping options, seconds and frames will always snap to the closest position,
regardless of the snap distance set. When mixing options, the system will first try to snap to
elements that are snapped by distance. Only if no element is close enough will it snap to seconds or frames.

You can also move it in single-frame increments by pressing :kbd:`Left` or :kbd:`Right` or :kbd:`Alt-Wheel`.
To jump to the beginning or end frame (of the ends of the preview range if that is active)
press :kbd:`Shift-Left` or :kbd:`Shift-Right`.


.. _playhead-snapping:

Snapping
--------

.. reference::

   :Menu:      :menuselection:`Header --> Snapping`

Playhead snapping helps you position the playhead precisely when scrubbing the timeline
by snapping it to specific elements like frames, markers, or keyframes.

.. _bpy.types.ToolSettings.use_snap_playhead:

Use Snapping
   Enables or disables snapping behavior when moving the playhead.

.. _bpy.types.ToolSettings.playhead_snap_distance:

Snap Distance
   The maximum distance (in pixels) the playhead can be from a target before snapping to it.

.. _bpy.types.ToolSettings.snap_playhead_element:

Snap Target
   Specifies which elements the playhead can snap to:

   :Frames: Snap to frame intervals.
   :Seconds: Snap to second intervals.
   :Markers: Snap to timeline markers.
   :Keyframes: Snap to animation keyframes.
   :Strips: Snap to the start and end points of strips (e.g. in the Video Sequencer).

.. _bpy.types.ToolSettings.snap_playhead_frame_step:

Frame Step :guilabel:`Frames`
   The interval in frames between each snap point when using the *Frames* target.

.. _bpy.types.ToolSettings.snap_playhead_second_step:

Second Step :guilabel:`Seconds`
   The interval in seconds between each snap point when using the *Seconds* target.



.. _animation-editors-footer:

Playback Controls
=================

The Playback Controls region of the animation editors (such as the Timeline, Dope Sheet, Graph Editor, and NLA Editor)
contains controls and options related to playback, keying, auto keyframing, and transport.

These settings allow you to:

- Control how animations are previewed and synchronized with audio.
- Insert and manage keyframes through keying sets and auto keying.
- Navigate the timeline using playback and transport controls.
- Adjust frame ranges and preview specific segments of the animation.

The footer is shared across animation editors to provide a consistent workflow for animators,
whether they are editing keyframes, adjusting curves, or sequencing actions.

.. figure:: /images/editors_playback_controls.png

.. _animation-editors-playback:

Playback
--------

Properties for how animations are played.

.. figure:: /images/editors_timeline_playback.png

.. _bpy.types.Scene.sync_mode:

Sync
   .. figure:: /images/editors_timeline_red-fps.png
      :figwidth: 109px
      :align: right

      3D Viewport red FPS.

   If animation playback can't keep up with the desired :ref:`Frame Rate <bpy.types.RenderSettings.fps>`,
   the actual frame rate (shown in the top left corner of the 3D Viewport) will turn red,
   and the *Sync* option determines how the situation should be handled.

   :Play Every Frame:
      Play every frame, even if this results in the animation playing slower than intended.
   :Frame Dropping:
      Drop frames if playback becomes slower than the scene's frame rate.
   :Sync to Audio:
      Drop frames if playback becomes too slow to remain synced with audio.

Audio -- Scrubbing
   Play bits of the sound in the animation (if there is any) while you drag the Playhead around.
Audio -- Play Audio
   Uncheck to mute all sound.

Playback -- Limit to Frame Range
   Don't allow moving the Playhead outside of the Frame Range using the mouse.

.. _bpy.types.Screen.use_follow:

Playback -- Follow Current Frame
   Automatically pan the view to catch up when the Playhead goes off screen.

.. _bpy.types.Screen.use_play:

Play In
   Which editors to update on each animation frame. If an editor is unchecked,
   it'll only be updated once playback stops (with some exceptions where it'll
   update on each frame anyway). When starting playback in either the
   :doc:`Graph Editor </editors/graph_editor/introduction>`,
   :doc:`Dope Sheet </editors/dope_sheet/introduction>` or the
   :doc:`NLA Editor</editors/nla/introduction>`,
   all editors will play back regardless of the settings.
   This is a feature requested by animators to easily play back all views.

.. _bpy.types.Scene.show_subframe:

Show -- Subframes
   Display and allow setting fractional frame values for the current frame.

Set Start/End Frame
   Set the scene's start/end frame to the current frame.
   If the Preview Range is active (see `Frame Controls`_), that one is changed instead.


.. _animation-editors-keying:

Keying
------

The *Keying* popover contains options that affect keyframe insertion.

.. note::

   The name of this popover will change depending on the active keying set.

.. figure:: /images/editors_timeline_keying.png

.. _bpy.types.KeyingSetsAll.active:

Active Keying Set
   .. figure:: /images/editors_timeline_keying-sets.png
      :align: right

      Timeline Keying Sets.

   A *Keying Set* is a named collection of animatable properties. If you select
   one and then press :kbd:`I` while not hovering over any input field,
   Blender will create keyframes for the properties in that keying set.

   If you don't have a keying set selected, you'll get keyframes on a default
   set of properties instead (e.g. Location/Rotation/Scale for objects).

   There are a number of predefined keying sets, but you can also create your own
   in the :ref:`Keying Sets <bpy.types.KeyingSets>` panel.

   Insert Keyframes :bl-icon:`key_hlt` :kbd:`I`
      Insert keyframes on the current frame.
   Delete Keyframes :bl-icon:`key_dehlt` :kbd:`Alt-I`
      Delete keyframes on the current frame.

.. _bpy.types.ToolSettings.keyframe_type:

New Keyframe Type
   The :ref:`keyframe type <keyframe-type>` for newly created keyframes.

.. _bpy.types.ToolSettings.use_keyframe_cycle_aware:

Cycle-Aware Keying
   When inserting keyframes into :ref:`trivially cyclic curves <bpy.types.FModifierCycles>`,
   special handling is applied to preserve the cycle integrity (most useful while tweaking an established cycle):

   - If a key insertion is attempted outside of the main time range of the cycle,
     it is remapped back inside the range.
   - When overwriting one of the end keys, the other one is updated accordingly.

   In addition, when adding a new curve into an action with a
   :ref:`Manual Frame Range <bpy.types.Action.use_frame_range>`
   and *Cyclic Animation* enabled, the curve is automatically made cyclic with the period matching the frame range.
   For convenience, this check and conversion is also done before adding the second keyframe to such a curve.


.. _bpy.types.ToolSettings.use_keyframe_insert_auto:

Auto Keying
-----------

.. figure:: /images/editors_timeline_keyframes-auto.png
   :align: right

   Auto Keying button.

When the record button (:bl-icon:`rec`) is enabled, Blender will automatically create keyframes on the current
frame whenever you transform an object or bone in the 3D Viewport (or change one of its transform properties
in the :doc:`Properties Editor </editors/properties_editor>`).

One special use case is to record a camera path as you fly through the scene.
See :ref:`Fly/Walk Navigation <3dview-fly-walk>`.

.. note::

   Auto Keying only works for transform properties (Location, Rotation, Scale).
   It won't create a keyframe if you change, say, the color of a material --
   you still have to do that manually.

.. _bpy.types.ToolSettings.auto_keying_mode:

Mode
   :Add & Replace: Add or replace keyframes as needed.
   :Replace: Only replace existing keyframes.

.. _bpy.types.ToolSettings.use_keyframe_insert_keyingset:

Only Active Keying Set
   By default, Auto Keying will create keyframes even for properties that are not in the
   :ref:`active keying set <bpy.types.KeyingSetsAll.active>`. Use this checkbox to change that.

.. _bpy.types.ToolSettings.use_record_with_nla:

Layered Recording
   Adds a new :doc:`NLA Track </editors/nla/tracks>` for every pass made over the animation
   to allow non-destructive tweaking.


.. _bpy.ops.screen.frame_jump:
.. _bpy.ops.screen.keyframe_jump:
.. _bpy.ops.screen.animation_play:

.. _animation-editors-controls:

Transport Controls
------------------

These buttons are used to set the current frame and control playback.

.. figure:: /images/editors_timeline_player-controls.png
   :align: right

   Transport controls.

:bl-icon:`rew` Jump to Start :kbd:`Shift-Left`
   Sets the Playhead to the start of the frame range.
:bl-icon:`prev_keyframe` Jump to Previous Keyframe :kbd:`Up`
   Moves the Playhead to the previous keyframe.
:bl-icon:`play_reverse`  Rewind :kbd:`Shift-Ctrl-Spacebar`
   Starts playing the animation in reverse.
:bl-icon:`play` Play :kbd:`Spacebar`
   Starts playing the animation.
:bl-icon:`pause` Pause :kbd:`Spacebar`
   Stops playing the animation.
:bl-icon:`next_keyframe` Jump to Next Keyframe :kbd:`Down`
   Moves the Playhead to the next keyframe.
:bl-icon:`ff` Jump to End :kbd:`Shift-Right`
   Sets the Playhead to the end of the frame range.

.. _bpy.ops.screen.time_jump:

:bl-icon:`frame_prev` Jump Backward by Delta :kbd:`Ctrl-Left`
   Jumps the playhead backwards by a user-configured delta.
:bl-icon:`frame_next` Jump Forward by Delta :kbd:`Ctrl-Right`
   Jumps the playhead forward by a user-configured delta.

Additionally, there is a menu accessible to the right of the Jump by Delta buttons where their delta can be set:

.. figure:: /images/editors_timeline_player-jump_delta_panel.png

.. _animation-editors-frame_controls:

Frame Controls
--------------

.. _bpy.types.Scene.frame_current:

Current Frame :kbd:`Alt-Wheel`
   The number of the frame that's currently being displayed in the 3D Viewport.
   This is also the location of the Playhead.

.. _bpy.types.Scene.use_preview_range:

:bl-icon:`preview_range` Use Preview Range
   The Preview Range is an alternative Frame Range that you can use for focusing on a
   particular part of the animation. It lets you repeatedly play a short segment without
   having to manually rewind or change the frame range of the entire scene.

   This range only affects the preview in the 3D Viewport; it doesn't affect rendering.

   The boundaries of the Preview Range are shown in dark orange. You can quickly configure
   and enable it by pressing :kbd:`P` and dragging a box. To disable it,
   you can press :kbd:`Alt-P`.

Start, End
   The start/end frame of the scene (or the preview range, if active).
