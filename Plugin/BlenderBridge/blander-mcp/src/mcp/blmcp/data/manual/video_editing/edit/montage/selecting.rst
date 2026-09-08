
****************
Selecting Strips
****************

The active sequence strip is displayed with a light outline.
The *entire* strip could be selected by clicking :kbd:`LMB` in the middle of the strip.


Select Menu
===========

The Select menu lets you select strips in different ways.

.. _bpy.ops.sequencer.select_all:

All :kbd:`A`
   Selects all the strips in the timeline.

None :kbd:`Alt-A`
   Deselects all the strips in the timeline.

Invert :kbd:`Ctrl-I`
   Inverts the current selection.

.. _bpy.ops.sequencer.select_box:

Box Select :kbd:`B`
   See :ref:`Box Select <bpy.ops.*.select_box>`.

Box Select (Include Handles) :kbd:`Ctrl-B`
   Works like *Box Select*, but also selects any strip handles inside the box. If a strip has only
   one handle selected, dragging it will change the strip's length. (If both handles are selected,
   the complete strip moves instead.)

.. _bpy.ops.sequencer.select_grouped:

Select Grouped :kbd:`Shift-G`
   Select strips that are similar to the active strip. By default, unsimilar strips are
   deselected, but this can be changed in the :ref:`Adjust Last Operation <bpy.ops.screen.redo_last>`
   region.

   Type
      Select strips that have the same specific type as the active strip. For example,
      if the active strip is a Movie strip, this selects all Movie strips.
   Global Type
      Select strips that have the same general type (graphics or audio) as the active strip.
   Effect Type
      If the active strip is an effect strip, selects all effect strips. Otherwise,
      selects all non-effect strips. (Despite the name, this operator does not check
      the effect type.)
   Data
      Select strips that use the same source (file, scene, movie clip or mask) as the active strip.
   Effect
      Find the effect types that are applied to the active strip, and select all strips that have
      any of the same effect types applied to them. For example, if the active strip has a
      Gaussian Blur effect on it, this will select all other strips that are also blurred.
   Effect/Linked
      Select strips that are on a lower channel than a selected strip and overlap it in time;
      then, effect strips linked to the selected content strips; and finally, content strips
      linked to the selected effect strips.
   Overlap
      Select strips that partially or completely overlap the active strip in time.

.. _bpy.ops.sequencer.select_more:
.. _bpy.ops.sequencer.select_less:
.. _bpy.ops.sequencer.select_linked:

Select Linked
   All :kbd:`Ctrl-L` / Less :kbd:`Ctrl-NumpadMinus` / More :kbd:`Ctrl-NumpadPlus`
      Add/remove neighboring strips to/from the selection.

.. _bpy.ops.sequencer.select_side_of_frame:

Side of Frame
   Left/Right :kbd:`[`/:kbd:`]`
      Select the strips that lie completely to the left or right of the current frame.
   Current
      Select the strips that intersect the current frame.

.. _bpy.ops.sequencer.select_handles:

Handle
   Both, Left, Right
      Select the left, right, or both handles of the selected strips.
   Both/Left/Right Neighbor
      Select the handle of the neighboring strip to the left, right, or on both sides of the selected strips.

.. _bpy.ops.sequencer.select_side:

Channel
   Select all the strips that are in the same channels as the currently selected strips.
