
***************
Selecting Bones
***************

Selection in *Pose Mode* is very similar to the one in :doc:`Edit Mode </animation/armatures/bones/selecting>`,
with a few deviations:
You can only select *whole bones* in *Pose Mode*, not roots/tips...


.. _bpy.ops.pose.select_all:

All
===

.. reference::

   :Mode:      Pose Mode
   :Menu:      :menuselection:`Select --> All`
   :Shortcut:  :kbd:`A`

Select all selectable bones.


None
====

.. reference::

   :Mode:      Pose Mode
   :Menu:      :menuselection:`Select --> None`
   :Shortcut:  :kbd:`Alt-A`

Deselect all bones, but the active bone stays the same.


Invert
======

.. reference::

   :Mode:      Pose Mode
   :Menu:      :menuselection:`Select --> Invert`
   :Shortcut:  :kbd:`Ctrl-I`

Toggle the selection state of all visible bones.


Box Select
==========

.. reference::

   :Mode:      Pose Mode
   :Menu:      :menuselection:`Select --> Box Select`
   :Shortcut:  :kbd:`B`

Interactive :ref:`box selection <tool-select-box>`.


Circle Select
=============

.. reference::

   :Mode:      Pose Mode
   :Menu:      :menuselection:`Select --> Circle Select`
   :Shortcut:  :kbd:`C`

Interactive :ref:`circle selection <tool-select-circle>`.


Lasso Select
============

.. reference::

   :Mode:      Pose Mode
   :Menu:      :menuselection:`Select --> Lasso Select`
   :Shortcut:  :kbd:`Ctrl-Alt-LMB`

See :ref:`tool-select-lasso`.


.. _bpy.ops.pose.select_mirror:

Select Mirror
=============

.. reference::

   :Mode:      Pose Mode
   :Menu:      :menuselection:`Select --> Select Mirror`
   :Shortcut:  :kbd:`Shift-Ctrl-M`

Flip the selection from one side to another.


.. _bpy.ops.pose.select_hierarchy:

Select More/Less
================

.. reference::

   :Mode:      Pose Mode
   :Menu:      :menuselection:`Select --> More/Less`

Parent :kbd:`[`, Child :kbd:`]`
   You can deselect the active bone and select its immediate parent or one of its children.
Extend Parent :kbd:`Shift-[`, Extend Child :kbd:`Shift-]`
   Similar to *Parent*/*Child* but it keeps the active bone in the selection.


.. _bpy.ops.pose.select_grouped:

Select Grouped
==============

.. reference::

   :Mode:      Pose Mode
   :Menu:      :menuselection:`Select --> Select Grouped`
   :Shortcut:  :kbd:`Shift-G`

You can select bones, based on various properties, through the *Select Grouped* pop-up menu :kbd:`Shift-G`:

Collection
   Selects all bones that are share at least one bone collection with the active bone.
Color
   Selects all bones that have the same color as the active bone.
Keying Set
   All bones affected by active :doc:`Keying Set </animation/keyframes/keying_sets>`
Children
   Select all children of currently selected bones.
Immediate Children
   Select direct children of currently selected bones.
Parents
   Select the parents of currently selected bones.
Siblings
   Select all bones that have the same parent as currently selected bones.


.. _bpy.ops.pose.select_linked:

Select Linked
=============

.. reference::

   :Mode:      Pose Mode
   :Menu:      :menuselection:`Select --> Select Linked`
   :Shortcut:  :kbd:`Ctrl-L`

Selects all the bones in the chain which the active (last selected) bone belongs to.

All Forks
   Selects all bones connected to the active bone even if the branch off from the current bone.

.. list-table:: Linked bones selection.

   * - .. figure:: /images/animation_armatures_bones_selecting_single-bone.png
          :width: 320px

          A single selected bone.

     - .. figure:: /images/animation_armatures_bones_selecting_whole-chain.png
          :width: 320px

          Its whole chain selected with Linked.


Select Pattern
==============

.. reference::

   :Mode:      Pose Mode
   :Menu:      :menuselection:`Select --> Select Pattern...`

Selects all bones whose name matches a given pattern.
Supported wild-cards: \* matches everything, ? matches any single character,
[abc] matches characters in "abc", and [!abc] match any character not in "abc".
As an example \*house\* matches any name that contains "house",
while floor\* matches any name starting with "floor".

Case Sensitive
   The matching can be chosen to be case sensitive or not.
Extend
   When *Extend* checkbox is checked the selection is extended instead of generating a new one.


.. _bpy.ops.pose.select_constraint_target:

Constraint Target
=================

.. reference::

   :Mode:      Pose Mode
   :Menu:      :menuselection:`Select --> Constraint Target`

Select bones used as targets for the currently selected bones
