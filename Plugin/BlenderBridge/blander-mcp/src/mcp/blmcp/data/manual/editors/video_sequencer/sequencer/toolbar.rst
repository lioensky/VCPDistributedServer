
###########
  Toolbar
###########

Selection tools
   :ref:`Tweak <tool-select-tweak>`
      Select or move.
   :ref:`Select Box <tool-select-box>`
      Select strips by dragging a box.
      All strips that intersect the box will be selected.
   :ref:`Select Circle <tool-select-circle>`
      Select strips by dragging a circle. All strips that intersect the path of
      the circle will be selected.
   :ref:`Select Lasso <tool-select-lasso>`
      Select strips by drawing a lasso.

.. _tool-blade:

Blade
   Cuts a strip in two. Specifically, it first shortens the strip so it only shows the content
   up to the cut point, then adds a second strip that shows the content after the cut point.

   The Blade tool supports both point-based cuts and a box gesture for quickly removing
   unwanted sections of strips.

   Splitting can be done in the following ways:

   - Select the tool in the Toolbar and click a strip at the time point where you want to split it.
   - Click and drag to draw a box. All strip content inside the box is cut out and removed.

   When using the box gesture, all strip content inside the box area is deleted.
   With *Remove Gaps* enabled, strips that follow the removed section are moved backward in time
   to close the gap (ripple behavior).

   When rippling, the behavior is applied to all channels that intersect the box area.
   Channels that are not covered by the box remain unchanged, allowing other strips
   to keep their relative timing if desired.

   If the box starts at the beginning or end of a strip, the amount of ripple is
   determined by the distance from the strip handle to the time-side of the box.
   When the box spans gaps between strips, those gaps can also be removed when
   rippling is enabled.

   .. rubric:: Tool Settings

   Type
      Split type for point-based cuts.

      :Soft:
         After splitting, it is still possible to restore the cut content in the new strips
         by dragging their handles.
      :Hard:
         After splitting, it is not possible to restore the cut content by dragging handles.
         However, the content can still be restored by adjusting the
         :ref:`Hold Offset <sequencer-duration-hard>` in the Sidebar.

   Remove Gaps
      In box blade mode, close gaps between cut strips, rippling later strips backward in time.
      Hold :kbd:`Shift` before dragging to temporarily disable this option and keep the gap.

   Ignore Selection
      In box blade mode, cut all strips inside the box, even if they are not selected.

   Ignore Connections
      Do not propagate the cut to connected strips, such as effect strips.

.. _tool-slip:

Slip
   Moves only the content of the strip. By default, the tool only allows the content to be moved within
   strip handles. If this limit applies, the strip outline is drawn in red color. By pressing :kbd:`C`
   the limiting is toggled on or off.
