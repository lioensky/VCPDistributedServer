
****************
Editing Channels
****************

.. _bpy.ops.anim.channels_delete:

Delete Channels
===============

.. reference::

   :Menu:      :menuselection:`Channel --> Delete Channels`
   :Shortcut:  :kbd:`Delete`, :kbd:`X`

Removes the selected channels from the current :doc:`action </animation/actions>`.

.. warning::

   Make sure the mouse cursor is hovering over the channel region before using
   the keyboard shortcuts. If it's hovering over the main region, you'll only
   delete the selected keyframes, not the full channels.


.. _bpy.ops.anim.channels_group:
.. _bpy.ops.anim.channels_ungroup:

Un/Group Channels
=================

.. reference::

   :Menu:      :menuselection:`Channel --> Un/Group Channels`
   :Shortcut:  :kbd:`Ctrl-Alt-G`, :kbd:`Ctrl-G`

Un/Groups the selected channels into a collection that can be renamed by double-clicking its name.
Grouping channels helps keep the view more organized.


.. _bpy.ops.anim.channels_setting_toggle:
.. _bpy.ops.anim.channels_setting_enable:
.. _bpy.ops.anim.channels_setting_disable:

Toggle/Enable/Disable Channel Settings
======================================

.. reference::

   :Menu:      :menuselection:`Channel --> Toggle/Enable/Disable Channel Settings`
   :Shortcut:  :kbd:`Shift-W`, :kbd:`Shift-Ctrl-W`, :kbd:`Alt-W`

Toggles, enables, or disables a certain setting for the selected channels:

Protect
   When a channel is protected (closed padlock icon), it can't be edited.
   Instead of pressing :kbd:`Shift-W` and selecting *Toggle*,
   you can also simply press :kbd:`Tab`.
Mute
   When a channel is muted (empty checkbox), it doesn't affect the animation.


.. _bpy.ops.anim.channels_editable_toggle:

Toggle Channel Editability
==========================

.. reference::

   :Menu:      :menuselection:`Channel --> Toggle Channel Editability`
   :Shortcut:  :kbd:`Tab`

Locks or unlocks a channel for editing.


.. _editors-graph-fcurves-settings-extrapolation:
.. _bpy.ops.graph.extrapolation_type:

Extrapolation Mode
==================

.. reference::

   :Menu:      :menuselection:`Channel --> Extrapolation Mode`
   :Shortcut:  :kbd:`Shift-E`

Changes how the curve behaves before its first keyframe and after its last keyframe.

:Constant:
   .. figure:: /images/editors_graph-editor_fcurves_introduction_extrapolate1.png
      :align: right
      :width: 300px

      Constant extrapolation.

   Continue in a straight line, keeping the same value as the first/last keyframe.
   This is the default.

:Linear:
   .. figure:: /images/editors_graph-editor_fcurves_introduction_extrapolate2.png
      :align: right
      :width: 300px

      Linear extrapolation.

   Continue in a straight line, keeping the same slope as on the first/last keyframe.

:Make Cyclic:
   Repeat the whole curve. This works by adding a :ref:`Cycles modifier <bpy.types.FModifierCycles>`.

:Clear Cyclic:
   Remove the above modifier, making the curve non-repeating again.

.. _bpy.ops.graph.fmodifier_add:

Add F-Curve Modifier
====================

.. reference::

   :Menu:      :menuselection:`Channel --> Add F-Curve Modifier`
   :Shortcut:  :kbd:`Shift-Ctrl-M`

Shows a submenu from where you can add a :doc:`modifier </editors/graph_editor/fcurves/modifiers>`
to the active curve. Settings for these modifiers can be found in :menuselection:`Sidebar --> Modifiers`.


.. _bpy.ops.graph.hide:
.. _bpy.ops.graph.reveal:

Show/Hide
=========

Hide Selected Curves :kbd:`H`
   Hides the selected curves.
Hide Unselected :kbd:`Shift-H`
   Hides all curves except the selected ones.
Reveal Curves :kbd:`Alt-H`
   Shows all previous hidden curves.


.. _bpy.ops.anim.channels_expand:
.. _bpy.ops.anim.channels_collapse:

Expand/Collapse Channels
========================

.. reference::

   :Menu:      :menuselection:`Channel --> Expand/Collapse Channels`
   :Shortcut:  :kbd:`NumpadPlus`, :kbd:`NumpadMinus`

Expands or collapses the selected headers.


.. _bpy.ops.anim.channels_move:

Move
====

.. reference::

   :Menu:      :menuselection:`Channel --> Move...`

Lets you reorder the selected channels or slots in the list:

- To the top :kbd:`Shift-PageUp`
- Up one line :kbd:`PageUp`
- Down one line :kbd:`PageDown`
- To the bottom :kbd:`Shift-PageDown`


.. _bpy.ops.anim.channels_fcurves_enable:

Revive Disabled F-Curves
========================

.. reference::

   :Menu:      :menuselection:`Channel --> Revive Disabled F-Curves`

Clears the "disabled" tag from all F-Curves to get broken F-Curves working again.
(A curve is broken if it references a property that doesn't exist.)

.. _bpy.ops.graph.keys_to_samples:

Keys to Samples
===============

.. reference::

   :Menu:      :menuselection:`Channel --> Keys to Samples`
   :Shortcut:  :kbd:`Alt-C`

Switches the selected curves from interpolating between a set of keyframes to using
a sampled value at each full frame.
**This is a destructive process that removes the ability to edit the curve.**
It's mainly used to reduce the file size with large datasets, as samples take up
less space than keyframes.

Between samples (on subframes), the curve interpolates linearly.


.. _bpy.ops.graph.samples_to_keys:

Samples to Keys
===============

.. reference::

   :Menu:      :menuselection:`Channel --> Samples to Keys`

Switches the selected curves from using samples to using keyframes, making them editable.
Note that this creates a keyframe on every frame.


.. _bpy.ops.graph.sound_to_samples:

Sound to Samples
================

.. reference::

   :Menu:      :menuselection:`Channel --> Sound to Samples`

Creates a sampled curve based on a sound file. Use *Samples to Keys* if you need to edit it.

Lowest Frequency
   Cutoff frequency of a high-pass filter that is applied to the audio data.
Highest Frequency
   Cutoff frequency of a low-pass filter that is applied to the audio data.
Attack Time
   Value for the hull curve calculation that tells how fast the hull curve can rise.
   The lower the value, the steeper it can rise.
Release Time
   Value for the hull curve calculation that tells how fast the hull curve can fall.
   The lower the value, the steeper it can fall.
Threshold
   Minimum amplitude value needed to influence the hull curve.

Accumulate
   Only the positive differences of the hull curve amplitudes are summarized to produce the output.
Additive
   The amplitudes of the hull curve are summarized. If *Accumulate* is enabled,
   both positive and negative differences are accumulated.
Square
   Gives the output as a square curve.
   Negative values always result in -1, and positive ones in 1.

   Square Threshold
      All values lower than this threshold result in 0.


.. _bpy.ops.graph.channels_bake:

Bake Channels
=============

.. reference::

   :Menu:      :menuselection:`Channel --> Bake Channels`

Generates new keyframes for the selected curves.

Frame Range
   The range that will be baked. Defaults to the scene range or preview range.
Frame Step
   Distance between keyframes. Can be used to create a keyframe every 10 frames or even every half frame.
Remove Outside Range
   Removes existing keys outside the specified baking range.
Interpolation Type
   The :ref:`interpolation type <editors-graph-fcurves-settings-interpolation>` for the new keys.
Bake Modifiers
   If enabled, the new keyframes are based on the modified curve, and the modifiers get deleted.

   If disabled, the new keyframes are based on the original curve, and the modifiers stay applied.

.. _bpy.ops.graph.euler_filter:

Discontinuity (Euler) Filter
============================

.. reference::

   :Menu:      :menuselection:`Channel --> Discontinuity (Euler) Filter`

Cleans up Euler rotation channels that suffer from :term:`Gimbal Lock`.
The channels of all three euler rotation axes need to be selected for this to work.

.. _bpy.ops.anim.channels_view_selected:

Frame Selected Channels
=======================

.. reference::

   :Menu:      :menuselection:`Channel --> Frame Selected Channels`
   :Shortcut:  :kbd:`NumpadPeriod`

Pans and zooms the view to show all keyframes of the selected curves.
You can also click a channel with :kbd:`Alt-MMB`.
