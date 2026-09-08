
**********
Navigating
**********

As with most editors, you can:

- Pan the view vertically (channels) and horizontally (time) by dragging :kbd:`MMB`.
- Zoom in and out by rolling :kbd:`Wheel` or dragging :kbd:`Ctrl-MMB`.

You can also use the scrollbars for this.


.. _dope-sheet-view-menu:

View Menu
=========

Sidebar :kbd:`N`
   Shows or hides the :ref:`Sidebar Region <ui-region-sidebar>`.
Adjust Last Operation
   Displays a pop-up panel to alter the properties of the last
   completed operation. See :ref:`bpy.ops.screen.redo_last`.
Channels
   Shows or hides the Channels region (the list of animated property names on the left).
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
   Pans the view so the Playhead is in the center.

----------

Multi-Word Match Search
   Lets you filter by multiple search terms instead of just one (in the search textbox above the
   channel list and in the :ref:`Filters popover <bpy.types.DopeSheet.filter_fcurve_name>`).
   The terms are space-separated, so you can for example type "loc rot" to find all channels that
   have "loc" or "rot" in their name. If this option were disabled, the list would only show
   channels containing the text "loc rot", of which there are likely none.

----------

Realtime Updates
   Whether to update other views (such as the 3D Viewport) while you're moving keyframes around.
   If disabled, the other views only get updated once you finish the move.

.. figure:: /images/animation_keyframes_introduction_sliders.png
   :align: right

   Sliders.

Show Sliders
   Shows a value slider next to each channel. Adjusting such a slider automatically creates a keyframe.

.. figure:: /images/animation_keyframes_introduction_interpolation.png
   :align: right

   Handle types.

Show Handles and Interpolation
   Displays keyframes using shapes that represent their Bézier handle type.
   In addition, if a keyframe uses a non-default interpolation type for the curve segment
   that comes after it, this is indicated by a green line.

   See :ref:`Handles & Interpolation Display <keyframe-handle-display>`.

.. figure:: /images/editors_dope-sheet_introduction_extremes.png
   :align: right

   Extreme markers.

Show Curve Extremes
   Detects keys where the curve changes direction, and marks them by displaying an arrow inside their shape.
   Local maxima (hills) are shown as up arrows, while local minima (valleys) are shown as down arrows.

   A keyframe may show both arrows, namely when it's part of a summary row containing a channel with a
   maximum and one with a minimum.

Auto-Merge Keyframes
   Automatically merge keyframes that end up on the same frame after transformation.

----------

Show Markers
   Shows the marker region (provided any markers have been defined).
   When disabled, the :ref:`Marker menu <dopesheet-marker-menu>` is also hidden and marker operators are
   not available in this editor.
Use Timecode :kbd:`Ctrl-T`
   Shows timing in seconds instead of frames.
Sync Visible Range
   Synchronizes the horizontal panning and scale of the editor
   with other time-based editors that also have this option enabled.
   That way, they always show the same section of time.

----------

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

Toggle Graph Editor :kbd:`Ctrl-Tab`
   Changes the area's editor to the :doc:`/editors/graph_editor/index`.

----------

.. _bpy.types.SpaceDopeSheetEditor.show_cache:

Cache
   Which simulation caches to show on the timeline.

   Baked simulations will be shown as fully opaque, cached simulations will be slightly transparent,
   and invalid caches will be slightly transparent with dark diagonal stripes.

   .. figure:: /images/editors_timeline_cache.png

      Timeline Cache.

----------

Area
   Area controls. See the :doc:`user interface </interface/window_system/areas>`
   documentation for more information.


Filters
=======

These filters are available in the funnel dropdown button in the header.

.. _bpy.types.DopeSheet.show_summary:

Summary
   Toggles the "Summary" row at the top of the Channels region.
   This row shows the union of all keyframes across all channels.

.. _bpy.types.DopeSheet.show_only_selected:

Only Show Selected
   Only show keyframes belonging to objects/bones/... that are selected.

.. note::
   If this option is enabled, the Dope Sheet may not show all :doc:`material </render/materials/introduction>`
   keyframes of the selected objects. Instead, it only shows the keyframes belonging to the selected nodes
   in the :doc:`/editors/shader_editor`.

Show Hidden
   Show keyframes from objects/bones/... that are hidden.
Only Show Errors
   Only show channels that have errors (for example, because they try to animate a property that doesn't
   exist on the object).

.. _bpy.types.DopeSheet.filter_fcurve_name:

Search
   Filters the channel list by a search term (or multiple search terms if *Multi-Word Match Search*
   is enabled).

Filtering Collection
   Select a collection to only show keyframes from objects in that collection.

Filter by Type
   Filter curves by property type.

Sort Data-Blocks
   Sorts data-blocks alphabetically to make them easier to find.

   If your playback speed suffers because of this
   (should only really be an issue when working with lots of objects),
   you can turn it off.


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
