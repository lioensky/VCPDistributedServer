
*********
Animation
*********

The *Animation* section lets you manage settings related to :doc:`Animation </animation/index>`.
This includes how editors look and also some different tools properties.

.. figure:: /images/editors_preferences_section_animation.webp

   Blender Preferences Animation section.


Timeline
========

.. _bpy.types.PreferencesEdit.use_negative_frames:

Allow Negative Frame
   Playback and animations can occur during negative frame ranges.

.. _bpy.types.PreferencesView.view2d_grid_spacing_min:

Minimum Grid Spacing
   The minimum number of pixels between grid lines.

.. _bpy.types.PreferencesView.timecode_style:

Timecode Style
   Format of timecodes displayed when not displaying timing in terms of frames.

   :Minimal Info:
      Most compact representation, uses '+' as separator for sub-second frame numbers,
      with left and right truncation of the timecode as necessary.
   :SMPTE (Full): Full SMPTE timecode (format is HH:MM:SS:FF).
   :SMPTE (Compact):
      SMPTE timecode showing minutes, seconds, and frames only
      -- hours are also shown if necessary, but not by default.
   :Compact with Decimals:
      Similar to SMPTE (Compact), except that the decimal part of the second is shown instead of frames.
   :Only Seconds: Direct conversion of frame numbers to seconds.

.. _bpy.types.PreferencesView.view_frame_type:

Zoom to Frame Type
   Defines what time range (around the cursor) will be displayed
   when the *View Frame* :kbd:`Numpad0` is performed.

   :Keep Range:
      The currently displayed time range is preserved.
   :Seconds:
      The number of seconds specified in the *Zoom Seconds* field will be shown around the cursor.
   :Keyframes:
      The number of animation keyframes defined in the *Zoom Keyframes* field will be shown around the cursor.


Keyframes
=========

These settings control :doc:`Keyframes </animation/keyframes/index>`
which are the building blocks for animations.

.. _bpy.types.PreferencesEdit.key_insert_channels:

Default Key Channels
   Which channels to insert keys at when no keying set is active.

   :Location: Inset keyframes for an object's :ref:`Location <bpy.types.Object.location>`.
   :Rotation: Inset keyframes for an object's :ref:`Rotation <bpy.types.Object.rotation>`.
   :Scale: Inset keyframes for an object's :ref:`Scale <bpy.types.Object.scale>`.
   :Rotation Mode: Inset keyframes for an object's :ref:`Rotation Mode <bpy.types.Object.rotation_mode>`.
   :Custom Properties: Inset keyframes for :doc:`/files/custom_properties`.

.. _bpy.types.PreferencesEdit.use_keyframe_insert_needed:
.. _bpy.types.PreferencesEdit.use_auto_keyframe_insert_needed:

Only Insert Needed
   This will only insert keyframes if the value of the property is different.

   :Manual: When keying manually, skip inserting keys that don't affect the animation.
   :Auto: Auto-Keying will skip inserting keys that don't affect the animation.

.. _bpy.types.PreferencesEdit.use_visual_keying:

Keyframing -- Visual Keying
   When an object is using constraints, the object property value does not actually change.
   *Visual Keying* will add keyframes to the object property,
   with a value based on the visual transformation from the constraint.

.. _bpy.types.PreferencesEdit.use_auto_keying:

Auto-Keyframing
   Enable in New Scenes
      Enables *Auto Keyframe* by default for new scenes.

   .. _bpy.types.PreferencesEdit.use_auto_keying_warning:

   Show Warning
      Displays a warning at the top right of the *3D Viewport*, when moving objects, if *Auto Keyframe* is on.

   .. _bpy.types.PreferencesEdit.use_keyframe_insert_available:

   Only Insert Available
      This will only add keyframes to channels of F-Curves that already exist.

   .. seealso::

      Learn more about :ref:`Auto-Keyframing <bpy.types.ToolSettings.use_keyframe_insert_auto>`.


F-Curves
========

These settings control how :doc:`F-Curves </editors/graph_editor/fcurves/index>`
look and their default behavior.

.. _bpy.types.PreferencesEdit.fcurve_unselected_alpha:

Unselected Opacity
   Controls the opacity of unselected :doc:`F-Curves </editors/graph_editor/fcurves/index>` against
   the background of the Graph Editor.

.. _bpy.types.PreferencesEdit.fcurve_new_auto_smoothing:

Default Smoothing Mode
   Controls the behavior of :ref:`automatic curve handles <editors-graph-fcurves-settings-handles>`
   for newly created F-Curves.

.. _bpy.types.PreferencesEdit.keyframe_new_interpolation_type:

Default Interpolation
   Controls the default :ref:`Interpolation <editors-graph-fcurves-settings-interpolation>`
   for newly created keyframes.

.. _bpy.types.PreferencesEdit.keyframe_new_handle_type:

Default Handles
   Controls the default :ref:`Handle <editors-graph-fcurves-settings-handles>` for newly created F-Curves.

.. _bpy.types.PreferencesEdit.use_insertkey_xyz_to_rgb:

XYZ to RGB
   Color for X, Y, or Z animation curves (location, scale or rotation)
   is the same as the color for the X, Y, and Z axis.

.. _bpy.types.PreferencesEdit.use_anim_channel_group_colors:

Channel Group Colors
   Display groups and channels with colors matching their corresponding groups.

.. _bpy.types.PreferencesEdit.show_only_selected_curve_keyframes:

Only Show Selected F-Curve Keyframes
   Only shows the keyframes markers on the selected curves.

.. _bpy.types.PreferencesEdit.use_fcurve_high_quality_drawing:

F-Curve High Quality Drawing
   Display F-Curves using :term:`Anti-Aliasing` and other effects (disable for a better performance).
