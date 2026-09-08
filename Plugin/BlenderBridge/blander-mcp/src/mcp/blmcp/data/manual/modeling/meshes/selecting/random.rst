.. _bpy.ops.mesh.select_random:

*************
Select Random
*************

.. reference::

   :Mode:      Object Mode and Edit Mode
   :Menu:      :menuselection:`Select --> Select Random`

Adds random items to the selection.

Options
=======

Ratio
   The ratio of items that should end up selected, e.g. 0.5 to select half of all items
   (that are not :doc:`hidden </scene_layout/object/editing/show_hide>`).

   Note that the existing selection is ignored: if half of the items are already selected,
   setting *Ratio* to 0.1 won't deselect anything, nor will it select 10% of the unselected
   items. Instead, it always picks 10% of *all* visible items and adds them to the selection.
Random Seed
   A number that influences which specific items get picked.
Action
   :Select: Add random items to the selection.
   :Deselect: Remove random items from the selection.
