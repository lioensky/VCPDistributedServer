
**********************
Editing Dopesheet Data
**********************

.. _dopesheet-select-menu:

Select Menu
^^^^^^^^^^^

.. seealso::
   :doc:`/interface/selecting`.

.. _bpy.ops.action.select_all:

All :kbd:`A`
   Selects all keyframes.
None :kbd:`Alt-A`
   Deselects all keyframes.
Invert :kbd:`Ctrl-I`
   Inverts the selection.

----------

:ref:`Box Select <bpy.ops.*.select_box>` :kbd:`B`
   Lets you drag a box and selects the keyframes inside it.
Box Select (Axis Range) :kbd:`Alt-B`
   Lets you drag a box and selects the keyframes inside the corresponding time range,
   even if they're above or below the box.
:ref:`Circle Select <bpy.ops.*.select_circle>` :kbd:`C`
   Displays a circle around the cursor, which you can drag over keyframes to select them.
:ref:`Lasso Select <bpy.ops.*.select_lasso>` :kbd:`Ctrl-RMB`
   Lets you draw a freehand shape and selects the keyframes inside it.

----------

More :kbd:`Ctrl-NumpadPlus`
   Expand the selection to include the neighbors (in time) of the currently selected keys.
Less :kbd:`Ctrl-NumpadMinus`
   Deselect keyframes with fewer than two selected neighbors.

----------

Select Linked :kbd:`L`
   Select keys that are on the same channel as a key that's already selected.

----------

Columns on Selected Keys :kbd:`K`
   Selects keys that are on the same frame as a key that's already selected.
Column on Current Frame :kbd:`Ctrl-K`
   Selects all the keys that are on the current frame.
Columns on Selected Markers :kbd:`Shift-K`
   Selects keys that are on the same frame as a selected marker.
Between Selected Markers :kbd:`Alt-K`
   Selects keys that lie between the leftmost and rightmost selected markers.

----------

Before Current Frame :kbd:`[`
   Select the keys that lie before (or on) the current frame.
   You can also click :kbd:`Shift-Ctrl-LMB` anywhere to the left of the Playhead.
After Current Frame :kbd:`]`
   Select the keys that lie after (or on) the current frame.
   You can also click :kbd:`Shift-Ctrl-LMB` anywhere to the right of the Playhead.

.. _dopesheet-marker-menu:

Marker Menu
^^^^^^^^^^^

:doc:`Markers </animation/markers>` are used to denote frames with key points or significant events
within an animation. Like with most animation editors, they're shown at the bottom.

.. figure:: /images/editors_graph-editor_introduction_markers.png

   Markers in animation editor.

There are some options that are exclusive to the Dope Sheet editor:

Sync Markers
   Whether to also move the selected markers when moving the selected keyframes.
Show Pose Markers :guilabel:`Action Editor`
   Instead of showing the global scene markers, show the local pose markers (which only exist inside the action).
   While this option is active, the *Add Marker* menu item will also create pose markers instead of scene markers.
Make Markers Local :guilabel:`Action Editor`
   Converts the selected scene markers into pose markers,
   making them only visible inside the currently selected action.

For information about the other marker tools, see :ref:`Editing Markers <animation-markers-editing>`.


Channel Menu
^^^^^^^^^^^^

See :doc:`Graph Editor Channels </editors/graph_editor/channels/editing>`.

.. _dopesheet-key-menu:

Key Menu
^^^^^^^^

Most items in this menu are documented on the Graph Editor's :doc:`/editors/graph_editor/fcurves/editing` page.
One important difference is that scaling keyframes in the Dope Sheet Editor only moves them along the time axis
(with the Playhead serving as the pivot point); it doesn't change their values.

The Dope Sheet editor has the following additional menu items:

Slide :kbd:`Shift-T`
   Lets you stretch one set of keyframes across time while compressing an adjacent set to compensate,
   leaving the combined duration the same.

   To use this operator, first select a range of three or more keyframes, then place the mouse cursor
   somewhere in the middle and press :kbd:`Shift-T`. The range will be temporarily split in two
   at the location of the cursor, indicated by a dashed vertical line.
   If you now move the mouse, the two halves of the range will change in length,
   and the keyframes within them will move accordingly. Click :kbd:`LMB` to confirm or :kbd:`RMB` to cancel.

Keyframe Type :kbd:`R`
   Sets the :ref:`type <keyframe-type>` of the selected keyframes.

Snap
^^^^

The toggle button enables/disables automatic keyframe snapping.
The dropdown button shows a popover with the following options:

Snap To
   Type of element to snap to.

   :Frame: Snap to full frames.
   :Second: Snap to seconds.
   :Nearest Marker: Snap to the nearest :doc:`Marker </animation/markers>`.

Absolute Time Snap
   When disabled, keyframes will move in increments of *Snap To*.
   For example, if you selected *Second* and have a keyframe that's currently on
   0:06+5, dragging it to the right will snap it to 0:07+5. Its time
   increases by a second, and its subsecond offset of 5 frames remains the same.

   When enabled, keyframes will snap to multiples of *Snap To*.
   Taking the above example, the keyframe would snap to 0:07+0,
   removing the subsecond offset.


Proportional Editing
^^^^^^^^^^^^^^^^^^^^

See :doc:`Proportional Editing </editors/3dview/controls/proportional_editing>`.
