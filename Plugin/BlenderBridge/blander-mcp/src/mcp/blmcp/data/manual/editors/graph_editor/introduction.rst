.. index:: Editors; Graph Editor

************
Introduction
************

The Graph Editor lets you edit animation curves, which determine how properties change over time.

.. figure:: /images/editors_graph-editor_introduction_example.png

   The Graph Editor.


Main Region
===========

The curve view allows you to view and edit :doc:`F-Curves </editors/graph_editor/fcurves/introduction>`.
An F-Curve has several key parts:

Curve
   The curve describes how the value of a property (Y axis) evolves over time (X axis).
:doc:`Keyframes </animation/keyframes/index>`
   Keyframes are user-defined values on certain frames and are represented
   by little black discs that become orange when selected.
   The values on the other frames are calculated automatically by interpolating
   between these keyframes.
:ref:`Handles <editors-graph-fcurves-settings-handles>`
   Each keyframe has two handles -- points that can be dragged around to influence
   the shape of the curve around it.

.. figure:: /images/editors_graph-editor_introduction_f-curve-example.png

   A simple curve. The discs are keyframes, and the circles are their handles.

.. seealso::

   See :doc:`F-Curves </editors/graph_editor/fcurves/introduction>` for more info.


Navigation
----------

As with most editors, you can:

Pan
   Pan the view by dragging with :kbd:`MMB`.
Zoom
   Zoom in and out with the mouse :kbd:`Wheel`.
Scale View
   Scale the view horizontally or vertically by dragging with :kbd:`Ctrl-MMB`.

You can also use the scrollbars.

.. tip::

   You can focus the view on the curve of an animated property by right clicking it and choosing
   :menuselection:`View in Graph Editor`. If you want to set up a hotkey for this, you need to open
   the :doc:`/editors/preferences/keymap` preferences, open the *User Interface* category,
   click *Add New*, fill in the operator name ``anim.view_curve_in_graph_editor``, and finally choose
   a shortcut. Normally this can be done more easily by right clicking the context menu item and
   choosing *Assign Shortcut*, but in this case, the shortcut would be added to the wrong category
   and not work.


.. _graph_editor-2d-cursor:
.. _bpy.types.SpaceGraphEditor.cursor:

Playhead & 2D Cursor
--------------------

.. figure:: /images/editors_graph-editor_introduction_2dcursor.png
   :align: right

   Graph Editor 2D Cursor.

The current frame is represented by a vertical blue line called the *Playhead*.
Like other :doc:`/animation/animation_editors`,
you can move it by clicking or dragging with :kbd:`LMB` in the scrubbing area at the top.

Combined with the horizontal blue line, the Playhead forms the *2D Cursor*
which can be used as a :doc:`pivot point </editors/3dview/controls/pivot_point/index>`
for rotating and scaling. You can disable the horizontal line using
:menuselection:`View --> Show Cursor` or :menuselection:`Sidebar --> View --> Show Cursor`.

The 2D Cursor can be moved by clicking or dragging with :kbd:`Shift-RMB`
or by adjusting its coordinates in the :ref:`View tab <graph_editor-view-properties>` of the Sidebar.


Header
======

.. _graph-view-menu:

View Menu
---------

Sidebar :kbd:`N`
   Shows or hides the :ref:`Sidebar Region <ui-region-sidebar>`.
Adjust Last Operation
   Displays a pop-up panel to alter properties of the last
   completed operation. See :ref:`bpy.ops.screen.redo_last`.
Channels
   Shows or hides the :ref:`Channels Region <editors-graph_editor-channels_region>`.
Playback Controls
   Show or hide the :ref:`Playback Controls <animation-editors-footer>`.

----------

Frame Selected :kbd:`NumpadPeriod`
   Pans and zooms the view to focus on the selected keyframes.
Frame All :kbd:`Home`
   Pans and zooms the view to show all keyframes.
Frame Scene/Preview Range
   Reset the horizontal view to the current scene frame range,
   taking the preview range into account if it is active.
Go to Current Frame :kbd:`Numpad0`
   Centers the area to the Playhead.

----------

Realtime Updates
   Whether to update other views (such as the 3D Viewport) while you're moving keyframes around.
   If disabled, the other views only get updated once you finish the move.

.. figure:: /images/animation_keyframes_introduction_sliders.png
   :align: right

   Sliders.

Show Sliders
   Shows a value slider next to each channel. Adjusting such a slider automatically creates a keyframe.
Auto-Merge Keyframes
   Automatically merge keyframes that end up on the same frame after transformation.

.. _bpy.types.SpaceGraphEditor.use_auto_lock_translation_axis:

Auto-Lock Key Axis
   Automatically locks the movement of keyframes to the axis that best matches the direction
   of the mouse cursor.

----------

Show Markers
   Shows the marker region. When disabled, the `Marker Menu`_ is also hidden
   and marker operators are not available in this editor.
Show Cursor
   Toggles the visibility of the horizontal blue line (see `Playhead & 2D Cursor`_).

.. _bpy.types.SpaceGraphEditor.show_seconds:

Use Timecode :kbd:`Ctrl-T`
   Show timing in seconds instead of frames.
   As an example, the timestamp ``01:03+02`` means "1 minute, 3 seconds, 2 frames."
Sync Visible Range
   Synchronizes the horizontal panning and scale of the editor
   with other time-based editors that also have this option enabled.
   That way, they always show the same section of time.

----------

.. _bpy.types.SpaceGraphEditor.show_extrapolation:

Show Extrapolation
   Toggles the visibility of the :ref:`extrapolated <editors-graph-fcurves-settings-extrapolation>`
   portion of curves.
Show Handles :kbd:`Ctrl-H`
   Toggles the display of keyframe handles.
Only Selected Keyframes Handles
   Only shows the handles for the selected keyframes.

----------

.. _graph-preview-range:
.. _bpy.ops.anim.previewrange_set:

Set Preview Range :kbd:`P`
   Lets you drag a box to define a time range for previewing. As long as this range is active,
   playback will be limited to it, letting you repeatedly view a segment of the animation without
   having to manually rewind each time.

   You can change the start or end frame using the corresponding button in the
   Timeline editor's :ref:`Playback <animation-editors-playback>` popover.
   Alternatively, you can simply run *Set Preview Range* again.
Clear Preview Range :kbd:`Alt-P`
   Clears the preview range.
Set Preview Range to Selected :kbd:`Ctrl-Alt-P`
   Applies a preview range that encompasses the selected keyframes.


----------

Toggle Dope Sheet
   Changes the area's editor to the :doc:`Dope Sheet Editor </editors/dope_sheet/introduction>`.

----------

Area
   Area controls. See the :doc:`user interface </interface/window_system/areas>`
   documentation for more information.


Select Menu
-----------

.. _bpy.ops.graph.select_all:

All :kbd:`A`
   Selects all keyframes and handles.
None :kbd:`Alt-A`
   Clears the selection.
Invert :kbd:`Ctrl-I`
   Inverts the selection.

----------

.. _bpy.ops.graph.select_box:

:ref:`Box Select <bpy.ops.*.select_box>` :kbd:`B`
   Lets you drag a box and selects the keyframes and handles inside it.
Box Select (Axis Range) :kbd:`Alt-B`
   Lets you drag a box and selects the keyframes and handles inside the corresponding time range,
   even if they're above or below the box.
Box Select (Include Handles)
   Selects keyframes and their handles inside the defined box.
:ref:`Circle Select <bpy.ops.*.select_circle>` :kbd:`C`
   Displays a circle around the cursor, which you can drag over keyframes and handles to select them.
:ref:`Lasso Select <bpy.ops.*.select_lasso>` :kbd:`Ctrl-RMB`
   Lets you draw a freehand shape and selects the keyframes and handles inside it.

----------

.. _bpy.ops.graph.select_column:

Columns on Selected Keys :kbd:`K`
   Selects keys that are on the same frame as a key that's already selected.
Column on Current Frame :kbd:`Ctrl-K`
   Selects all the keys that are on the current frame.
Columns on Selected Markers :kbd:`Shift-K`
   Selects keys that are on the same frame as a selected :doc:`marker </animation/markers>`.
Between Selected Markers :kbd:`Alt-K`
   Selects keys that lie between the leftmost and rightmost selected markers.

----------

.. _bpy.ops.graph.select_leftright:

Before Current Frame :kbd:`[`
   Select the keys that lie before (or on) the current frame.
   You can also click :kbd:`Shift-Ctrl-LMB` anywhere to the left of the Playhead.
After Current Frame :kbd:`]`
   Select the keys that lie after (or on) the current frame.
   You can also click :kbd:`Shift-Ctrl-LMB` anywhere to the right of the Playhead.

----------

.. _bpy.ops.graph.select_key_handles:

Select Handles
   Selects the handles of the currently selected keyframes.
Select Keys
   Selects the keyframes of the currently selected handles.

----------

.. _bpy.ops.graph.select_more:
.. _bpy.ops.graph.select_less:

Select More :kbd:`Ctrl-NumpadPlus`
   Expands the selection to include the neighbors (in time) of the currently selected keys.
Select Less :kbd:`Ctrl-NumpadMinus`
   Deselects keyframes with fewer than two selected neighbors.

----------

.. _bpy.ops.graph.select_linked:

Select Linked
   Selects keys that are on the same curve as a key that's already selected.


Marker Menu
-----------

:doc:`Markers </animation/markers>` are used to denote frames with key points or significant events
within an animation. Like with most animation editors, they're shown at the bottom.

.. figure:: /images/editors_graph-editor_introduction_markers.png

   Markers in animation editor.

For descriptions of the different marker tools, see :ref:`Editing Markers <animation-markers-editing>`.


Channel Menu
------------

See :doc:`Editing Channels </editors/graph_editor/channels/editing>`.


Key Menu
--------

See :doc:`Editing F-Curves </editors/graph_editor/fcurves/editing>`.


Normalize
---------

Scales the display of each curve so that they all (appear to) occupy the same value range,
going from -1 to 1. This can make editing easier when you're working with curves whose value
ranges are far apart.

When you enable this option, the view is zoomed accordingly and the area outside the normalized
value range is darkened.

If a preview range is defined, keyframes within the range are normalized,
while the others are scaled proportionally.

Auto Normalization
^^^^^^^^^^^^^^^^^^

Automatically recalculate curve normalization on every curve edit.


View Controls
-------------

.. figure:: /images/editors_graph-editor_introduction_header-view.png

   View controls.

Show Only Selected
   Only show curves belonging to objects/bones/... that are selected.
Show Hidden
   Show keyframes from objects/bones/... that are hidden.
Show Only Errors
   Only show channels that have errors (for example, because they try to animate a property that doesn't
   exist on the object).
Create Ghost Curves (framed F-Curve icon)
   Creates a snapshot of the current curves and shows it in the background
   so that you can use it as a reference. Click the button again to clear the snapshot.
Filter (funnel icon)
   Search
      Filters the channel list by a search term.

   Filtering Collection
      Select a collection to only show keyframes from objects in that collection.

   Filter by Type
      Filter curves by property type.

   Sort Data-Blocks
      Sorts data-blocks alphabetically to make them easier to find.

      If your playback speed suffers because of this
      (should only really be an issue when working with lots of objects),
      you can turn it off.


Transform Controls
------------------

.. figure:: /images/editors_graph-editor_introduction_header-edit.png

   Transform controls.

Pivot Point
   Pivot point for rotating and scaling.

   Bounding Box Center
      Center of the smallest possible box around the selected keyframes.
   2D Cursor
      The intersection between the Playhead and the horizontal Cursor line.
   Individual Centers
      Rotate/scale each handle around its keyframe.

.. _bpy.types.ToolSettings.use_snap_anim:

Snap
   The icon toggles snapping on or off. The dropdown offers the following options:

   .. _bpy.types.ToolSettings.snap_anim_element:

   Snap To
      Type of element to snap to.

      :Frame: Snap to full frames.
      :Second: Snap to seconds.
      :Nearest Marker: Snap to the nearest :doc:`Marker </animation/markers>`.

   .. _bpy.types.ToolSettings.use_snap_time_absolute:

   Absolute Time Snap
      When disabled, keyframes will move in increments of *Snap To*.
      For example, if you selected *Second* and have a keyframe that's currently on
      0:06+5, dragging it to the right will snap it to 0:07+5. Its time
      increases by a second, and its subsecond offset of 5 frames remains the same.

      When enabled, keyframes will snap to multiples of *Snap To*.
      Taking the above example, the keyframe would snap to 0:07+0,
      removing the subsecond offset.

Proportional Editing :kbd:`O`
   See :doc:`Proportional Editing </editors/3dview/controls/proportional_editing>`.


Playback Controls
=================

The Playback Controls region contains controls and options
related to playback, keying, auto keyframing, and transport.

These settings allow you to:

- Control how animations are previewed and synchronized with audio.
- Insert and manage keyframes through keying sets and auto keying.
- Navigate the timeline using playback and transport controls.
- Adjust frame ranges and preview specific segments of the animation.

.. seealso::

   For a detailed description of all properties and controls commonly found in the footer,
   see the :ref:`Playback Controls <animation-editors-footer>` documentation.


Sidebar Region
==============

.. _bpy.types.SpaceGraphEditor.show_cursor:
.. _graph_editor-view-properties:

View Tab
--------

.. figure:: /images/editors_graph-editor_introduction_view-panel.png
   :align: right

   View Tab.

Show Cursor
   Toggles the visibility of the :ref:`2D Cursor <graph_editor-2d-cursor>`'s horizontal line.
Cursor X, Y
   Shows, and lets you change, the X coordinate (current frame) and Y coordinate (value) of the 2D Cursor.
Cursor to Selection
   Places the 2D Cursor at the average time and value of the selected keyframes.
Cursor Value to Selection
   Places the 2D Cursor at the average value of the selected keyframes, leaving its time unchanged.


F-Curve Tab
-----------

See :doc:`F-Curve Properties </editors/graph_editor/fcurves/properties>`.


Modifiers Tab
-------------

See :doc:`F-Curve Modifiers </editors/graph_editor/fcurves/modifiers>`.
