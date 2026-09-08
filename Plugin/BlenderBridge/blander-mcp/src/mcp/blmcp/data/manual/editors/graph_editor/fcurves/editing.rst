****************
Editing F-Curves
****************

Transform
=========

.. reference::

   :Mode:      Edit Mode
   :Menu:      :menuselection:`Key --> Transform`

An F-Curve can be edited by transforming the locations of its keyframes.

Move, Rotate, Scale
   Like other elements in Blender, keyframes can be
   moved, rotated, and scaled as described in
   :doc:`Basic Transformations </scene_layout/object/editing/transform/introduction>`.
Extend :kbd:`E`
   Lets you quickly move the selected keyframes that are on a certain side of the Playhead.
   This is handy if you need to, say, move all the keyframes after a certain time point to
   the right to make space for new ones.

   To use this operator, first select some or all keyframes and place your mouse cursor to
   the left or right of the Playhead. Then, press :kbd:`E`, move the mouse to move (only)
   the keyframes on that side of the Playhead, and press :kbd:`LMB` to confirm
   (or :kbd:`RMB` to cancel).

.. tip::

   You can also change the *Key Frame* and *Value* properties in
   :menuselection:`Sidebar --> F-Curve --> Active Keyframe` if you want to specify exact numbers.

While transforming keyframes, you can hold :kbd:`Shift` to move them more slowly for
better precision, or :kbd:`Ctrl` to move them in coarse increments.

.. _bpy.ops.graph.snap:

Snap
====

.. reference::

   :Menu:      :menuselection:`Key --> Snap`
   :Shortcut:  :kbd:`Shift-S`

Apart from using the snapping operators in this menu, you can also turn on
:ref:`snapping <bpy.types.ToolSettings.use_snap_anim>` in the header.

Selection to Current Frame
   Set the selected keyframes' time to the current frame.
Selection to Cursor Value
   Set the selected keyframes' value to that of the :ref:`2D Cursor <graph_editor-2d-cursor>`.
Selection to Nearest Frame
   Round the time of each keyframe to the nearest frame.
Selection to Nearest Second
   Round the time of each keyframe to the nearest second.
   You can use :ref:`Use Timecode <bpy.types.SpaceGraphEditor.show_seconds>`
   to show seconds instead of frames at the top of the editor.
Selection to Nearest Marker
   Set the time of each keyframe to that of the nearest :doc:`marker </animation/markers>`.
Flatten Handles
   Flatten the *Bézier* handles for the selected keyframes.

   .. list-table:: Flatten Handles snapping example.

      * - .. figure:: /images/editors_graph-editor_fcurves_editing_flatten-handles-1.png

             Before Flatten Handles.

        - .. figure:: /images/editors_graph-editor_fcurves_editing_flatten-handles-2.png

             After Flatten Handles.

.. _bpy.ops.graph.equalize_handles:

Equalize Handles
   Ensure selected keyframes' handles have equal length.

   Side
      Which handles to affect (left, right, or both).
   Handle Length
      Length to make selected keyframes' Bézier handles.
   Flatten
      Make the values of the handles the same as their respective keyframes.

Cursor to Selected :kbd:`Ctrl-G`
   Changes the time and value of the 2D Cursor to the average time and value of the selected keyframes.

.. _bpy.ops.graph.snap_cursor_value:

Cursor Value to Selection
   Changes the value of the 2D Cursor to the average value of the selected keyframes.


.. _bpy.ops.graph.mirror:

Mirror
======

.. reference::

   :Menu:      :menuselection:`Key --> Mirror`
   :Shortcut:  :kbd:`Ctrl-M`

Mirrors the selected keyframes across a reference point.

By Times over Current Frame
   Mirror horizontally across the current frame.
By Values over Cursor Value
   Mirror vertically across the 2D Cursor's value.
By Times over Zero Time
   Mirror horizontally across frame 0.
By Values over Zero Value
   Mirror vertically across value 0.
By Times over First Selected Marker
   Mirror horizontally across the first selected marker.


.. _bpy.ops.graph.frame_jump:

Jump to Selected
================

.. reference::

   :Menu:      :menuselection:`Key --> Jump to Selected`
   :Shortcut:  :kbd:`Ctrl-G`

Places the 2D Cursor at the average time and value of the selected keyframes.


.. _bpy.ops.graph.keyframe_insert:

Insert
======

.. reference::

   :Menu:      :menuselection:`Key --> Insert`
   :Shortcut:  :kbd:`I`

Adds new keyframes and selects them. Previously selected keyframes stay selected too.

All Channels
   Insert a keyframe on all visible and editable F-Curves using each curve's current value.
Only Selected Channels
   Insert a keyframe on the selected F-Curves using each curve's current value.
Only Active F-Curve
   Insert a keyframe on the active F-Curve using the curve's current value.
Active Channels at Cursor
   Insert a keyframe on the active F-Curve at the 2D Cursor's value.
Selected Channels at Cursor
   Insert a keyframe on the selected F-Curves at the 2D Cursor's value.


.. _bpy.ops.graph.copy:
.. _bpy.ops.graph.paste:

Copy/Paste
==========

.. reference::

   :Menu:      :menuselection:`Key --> Copy`, :menuselection:`Key --> Paste`
   :Shortcut:  :kbd:`Ctrl-C`, :kbd:`Ctrl-V`

Use :kbd:`Ctrl-C` to copy the selected keyframes and :kbd:`Ctrl-V` to paste them.
After pasting, the :ref:`bpy.ops.screen.redo_last` panel provides some extra options:

Frame Offset
   Offsets the pasted keyframes horizontally so that...

   Frame Start
      ...the first one lands on the current frame.
   Frame End
      ...the last one lands on the current frame.
   Frame Relative
      ...they land at the same distance from the current frame as when they were copied.
   No Offset
      ...they stay at their original frames.

Value Offset
   Offsets the pasted keyframes vertically so that...

   Left Key
      ...the first one has the value of the existing keyframe to the left of the Playhead.
   Right Key
      ...the last one has the value of the existing keyframe to the right of the Playhead.
   Current Frame Value
      ...the first one has the value of the curve at the current frame.
   Cursor Value
      ...the first one has the value of the :ref:`2D Cursor <graph_editor-2d-cursor>`.
   No Offset
      ...they keep their original values.

Type
   Mix
      Integrates the pasted keyframes with existing ones, only overwriting those that share a frame.
   Overwrite All
      Removes all previous keyframes in the target F-Curves.
   Overwrite Range
      Within each F-Curve, remove the existing keyframes that are in the range of the keyframes
      pasted into it.
   Overwrite Entire Range
      Within each F-Curve, remove the existing keyframes that are in the range of all pasted
      keyframes combined.

Flipped
   If you copied keyframes from one or more pairs of
   :doc:`symmetrically opposite bones </animation/armatures/bones/editing/naming>`,
   enabling this option will paste the keyframes of the left bones into the curves of the right ones
   and vice versa. In addition, the values are inverted, effectively mirroring the animation.


.. _bpy.ops.graph.duplicate_move:

Duplicate
=========

.. reference::

   :Menu:      :menuselection:`Key --> Duplicate`
   :Shortcut:  :kbd:`Shift-D`

Duplicates the selected keyframes. You can reposition them by moving the mouse.


.. _bpy.ops.graph.delete:

Delete
======

.. reference::

   :Menu:      :menuselection:`Key --> Delete`
   :Shortcut:  :kbd:`X`, :kbd:`Delete`

Pressing :kbd:`X` or :kbd:`Delete` opens a pop-up menu from where you can delete the selected keyframes.


.. _bpy.ops.graph.handle_type:

Handle Type
===========

.. reference::

   :Menu:      :menuselection:`Key --> Handle Type`
   :Shortcut:  :kbd:`V`

Sets the :ref:`handle type <editors-graph-fcurves-settings-handles>` of the selected keyframes.


.. _bpy.ops.graph.interpolation_type:

Interpolation Mode
==================

.. reference::

   :Menu:      :menuselection:`Key --> Interpolation Mode`
   :Shortcut:  :kbd:`T`

Sets the :ref:`interpolation mode <editors-graph-fcurves-settings-interpolation>` of the selected keyframes.
This determines the curve interpolation between each keyframe and the next.


.. _bpy.ops.graph.easing_type:

Easing Type
===========

.. reference::

   :Menu:      :menuselection:`Key --> Easing Type`
   :Shortcut:  :kbd:`Ctrl-E`

Sets the :ref:`easing mode <editors-graph-fcurves-settings-easing>` of the selected keyframes.
This determines whether easing is applied to the left side, right side, or both sides of the
curve segments between each keyframe and the next.


Density
=======

.. _bpy.ops.graph.decimate:

Decimate
--------

.. reference::

   :Menu:      :menuselection:`Key --> Density --> Decimate (Ratio)`
   :Menu:      :menuselection:`Key --> Density --> Decimate (Allowed Change)`

Simplifies an F-Curve by removing the keyframes that influence its shape the least.

Mode
   How to pick the number of keyframes to delete.

   Ratio
      Deletes a certain percentage of keyframes.

      Remove
         The percentage of keyframes to remove.

   Error Margin
      Deletes as many keyframes as possible while ensuring the F-Curve's shape changes
      no more than a certain amount.

      Max Error Margin
         How much the decimated curve may deviate from the original.


.. _bpy.ops.graph.bake_keys:

Bake Keyframes
--------------

.. reference::

   :Menu:      :menuselection:`Key --> Density --> Bake Keyframes`
   :Shortcut:  :kbd:`Shift-Alt-O`

Creates a keyframe at every frame.

.. seealso::
   :ref:`Bake Channels <bpy.ops.graph.channels_bake>`, which offers options on
   what range to bake and how.

.. list-table::

   * - .. figure:: /images/editors_graph-editor_fcurves_editing_sample.png

          F-Curve before baking.

     - .. figure:: /images/editors_graph-editor_fcurves_editing_sample2.png

          F-Curve after baking.


.. _bpy.ops.graph.clean:

Clean Keyframes
---------------

.. reference::

   :Menu:      :menuselection:`Key --> Density --> Clean Keyframes`
   :Shortcut:  :kbd:`X`

Finds redundant keyframes among the selected ones and deletes them. A keyframe is seen as
redundant if it has the same value as its neighbors -- even if the curve segments around it
aren't flat.

.. tip::

   This operator is likely to change the shape of the affected curves, so it's best run after
   e.g. bulk keyframe insertion on all the bones of an armature (which creates useless keyframes
   on bones that haven't moved) and before tweaking the curves by hand.

Threshold
   Value threshold. By increasing this, you can also delete keyframes that *almost* have the
   same value as their neighbors.

Channels
   Cleans all the keyframes (even unselected ones) in the selected F-Curves.
   If a curve is left with only one keyframe, it's deleted entirely.

.. list-table::

   * - .. figure:: /images/editors_graph-editor_fcurves_editing_clean1.png

          F-Curve before cleaning.

     - .. figure:: /images/editors_graph-editor_fcurves_editing_clean2.png

          F-Curve after cleaning.


Blend
=====

.. reference::

   :Menu:      :menuselection:`Key --> Blend`
   :Shortcut:  :kbd:`Alt-D`

Adjusts the values of the selected keyframes by a certain percentage. Select a blending operator,
move the mouse left or right to adjust the factor, and click :kbd:`LMB` to confirm
(or :kbd:`RMB` to cancel).

Several blending operators work based on "neighboring keyframes." This means that they divide the
selected keyframes into contiguous groups, then reference the unselected keyframes immediately
before and after each group.

.. _bpy.ops.graph.breakdown:

Breakdown
---------

.. reference::

   :Menu:      :menuselection:`Key --> Blend --> Breakdown`

Sets the value of the selected keyframes to an interpolation of their neighbors.

Factor
   At -1, the keyframes are set to the value of the left neighbor.

   At 1, they're set to the value of the right neighbor.

   For other factors, they're set to an interpolation between the two neighbor values,
   with 0 being right in the middle.


.. _bpy.ops.graph.blend_to_neighbor:

Blend to Neighbor
-----------------

.. reference::

   :Menu:      :menuselection:`Key --> Blend --> Blend to Neighbor`

Moves each selected keyframe towards the value of the left or right neighbor by a certain percentage.

Blend
   When negative, each keyframe moves *Blend* percent to the value of the left neighbor.

   When positive, they move to the right neighbor.

   When zero, they keep their original values.


.. _bpy.ops.graph.blend_to_default:

Blend to Default Value
----------------------

.. reference::

   :Menu:      :menuselection:`Key --> Blend --> Blend to Default Value`

Moves the selected keyframes towards the property's default value by a certain percentage.

Factor
   How much to change the keyframes' values, going from 0 (no change) to 1 (reset to the default value).

.. seealso::

   The :ref:`Reset to Default <bpy.ops.ui.reset_default_button>` operator resets
   any property to its default value without the need of keyframing.


.. _bpy.ops.graph.ease:

Ease
----

.. reference::

   :Menu:      :menuselection:`Key --> Blend --> Ease`

Makes the selected keyframes follow an S-curve. While the slider is visible (so after activating
the operator but before confirming with :kbd:`LMB`), you can press :kbd:`Tab` to toggle which
of the following settings to edit:

Curve Bend
   A negative value gives more weight to the left side, while a positive value gives more weight
   to the right. A value of 0 results in a balanced curve.

Sharpness
   A low value results in an almost straight diagonal line, while a high value results in a steep
   rise/drop in the curve.

.. _bpy.ops.graph.blend_offset:

Blend Offset
------------

.. reference::

   :Menu:      :menuselection:`Key --> Blend --> Blend Offset`

Moves the selected keyframes up or down -- all by the same amount -- until the first/last one matches
the left/right neighbor.

Offset Factor
   At -1, the first selected key gets aligned to its left neighbor.

   At 1, the last selected key gets aligned to its right neighbor.

   At 0, nothing changes.


.. _bpy.ops.graph.blend_to_ease:

Blend to Ease
-------------

.. reference::

   :Menu:      :menuselection:`Key --> Blend --> Blend to Ease`

Blends the selected keys to either an "ease in" or an "ease out" curve.

Blend
   At -1, the keys will follow an "ease in" curve, with small value changes in the beginning
   and large changes towards the end.

   At 1, the keys will follow an "ease out" curve, with large value changes in the beginning
   and small changes towards the end.

   At 0, nothing changes.


.. _bpy.ops.graph.match_slope:

Match Slope
-----------

.. reference::

   :Menu:      :menuselection:`Key --> Blend --> Match Slope`

Blends the selected keys towards a straight line going through two keys just outside the current selection.

Factor
   Negative values use the two keys to the left of the selection.

   Positive values use the keys to the right.

   At zero, nothing changes.

.. _bpy.ops.graph.push_pull:

Push Pull
---------

.. reference::

   :Menu:      :menuselection:`Key --> Blend --> Push Pull`

Moves the selected keys towards, or away from, the straight line going through the first and last
selected key.

Factor
   At 0, the keys will lie on the straight line.

   At 1, they keep their original values.

   At 2, each key's value will be twice as far from the straight line as before.

.. _bpy.ops.graph.shear:

Shear Keys
----------

.. reference::

   :Menu:      :menuselection:`Key --> Blend --> Shear Keys`

Shears the selected keyframes -- that is, changes their value by an amount that increases
as they get further away in time from a reference keyframe. By default, this reference keyframe
is the leftmost selected one, but you can instead use the rightmost one by pressing :kbd:`D`.

Shear Factor
   How much to shear. Negative values move keyframes downwards, while positive ones move them up.
Direction
   Whether to use the leftmost or the rightmost selected keyframe as a reference.


.. _bpy.ops.graph.scale_average:

Scale Average
-------------

.. reference::

   :Menu:      :menuselection:`Key --> Blend --> Scale Average`

Scales the selected keyframes vertically, using their average value as the pivot.

Factor
   At 0, the keyframes will all have the average value.

   At 1, they keep their original values.

   At 2, each keyframe's value will be twice as far from the average as before.


.. _bpy.ops.graph.scale_from_neighbor:

Scale from Neighbor
-------------------

.. reference::

   :Menu:      :menuselection:`Key --> Blend --> Scale from Neighbor`

Scales the selected keyframes vertically, using a keyframe just outside the selection as
the pivot. By default, this is the neighbor to the left of the selection,
but you can instead use the right one by pressing :kbd:`D`.

Factor
   The scale factor to apply.
Reference Key
   Whether to use the left or right neighbor as the pivot.


.. _bpy.ops.graph.time_offset:

Time Offset
-----------

.. reference::

   :Menu:      :menuselection:`Key --> Blend --> Time Offset`

Shifts the values of the selected keyframes so that the resulting F-Curve appears to move in time.
Works best with dense keyframes.

As the curve leaves the selected keyframes' time range on one end, it wraps back in on the other,
offset vertically so that the ends connect and there is no jump.

Frame Offset
   By how many frames to shift the F-Curve. The slider is limited to the range -10 ... 10,
   but you can type larger numbers too.


Smooth
======

.. reference::

   :Menu:      :menuselection:`Key --> Smooth`
   :Shortcut:  :kbd:`Alt-S`

.. _bpy.ops.graph.gaussian_smooth:

Smooth (Gaussian)
-----------------

.. reference::

   :Menu:      :menuselection:`Key --> Smooth --> Smooth (Gaussian)`

Smooths the selected keyframes using a Gaussian kernel. Click the menu item, move the mouse left or right to
adjust the strength, and click :kbd:`LMB` to confirm (or :kbd:`RMB` to cancel).

Factor
   How strongly the smoothing should be applied.

Sigma
   The shape of the Gaussian distribution. Lower values mean a sharper curve, giving keys that are close to each
   other more weight. A high value behaves like a simple average filter.

Filter Width
   A wider filter looks at more keyframes, producing a smoother result.
   At a width of 1, the filter only looks at the keyframes to the immediate left and right for a weighted average.

.. figure:: /images/editors_graph-editor_gaussian_smooth.jpg

   F-Curve after applying the Gaussian Smooth with the original curve overlaid.


.. _bpy.ops.graph.smooth:

Smooth (Legacy)
---------------

.. reference::

   :Menu:      :menuselection:`Key --> Smooth --> Smooth (Legacy)`
   :Shortcut:  :kbd:`Alt-O`

There is also an option to smooth the selected curves, but beware: its algorithm seems to be
to halve the distance between each keyframe and the average linear value of the curve,
which gives quite a strong smoothing! Note that the first and last keys
seem to be never modified by this tool.

.. list-table::

   * - .. figure:: /images/editors_graph-editor_fcurves_editing_clean1.png

          F-Curve before smoothing.

     - .. figure:: /images/editors_graph-editor_fcurves_editing_smooth.png

          F-Curve after smoothing.


Butterworth Smooth
------------------

.. reference::

   :Menu:      :menuselection:`Key --> Smooth --> Butterworth Smooth`

Smooth the selected keyframes using a Butterworth filter. Click the menu item,
move the mouse left or right to adjust the frequency,
and click :kbd:`LMB` to confirm (or :kbd:`RMB` to cancel).

This filter is ideal for smoothing large amounts of data because it preserves the peaks
of the animation. The downside is that it can introduce a ripple effect when the key
values change rapidly.

Frequency Cutoff
   The lower the value, the smoother the curve. There is an implicit maximum at which
   the value no longer changes the curve, which is at half the sample rate. The sample
   rate in this case is the scene frame rate multiplied by the **Samples per Frame** of this operator.
Filter order
   Higher values mean the frequency cutoff is steeper.
Samples per Frame
   Before the filter is applied, the curve is resampled at this interval to avoid errors when there
   are uneven spaces between frames. If keys are on subframes, e.g. a 60fps file in a 30fps scene,
   increase this value to 2.
Blend
   A value between 0 and 1 for blending between the original curve and the smoothed one.
Blend In/Out
   The number of frames at the start and end for which to blend between the original and smoothed curve.
   This can help reduce jumps in the animation at the selection border. At value 1, it only locks the first and
   last frames of the selection to their original values.
