
******
Rename
******

.. _tools_rename-active:

Rename Active Item
==================

.. reference::

   :Menu:      :menuselection:`Edit --> Rename Active Item`
   :Shortcut:  :kbd:`F2`

The *Rename Active Item* operator renames the active
:doc:`Bone </animation/armatures/bones/index>`,
:doc:`Node </interface/controls/nodes/index>`,
:doc:`Object </scene_layout/object/index>` and
:doc:`Sequence Strip </video_editing/edit/montage/strips/index>`.

When the operator is executed, a pop-up dialog appears.
The text field shows the name of the current item and can be overwritten to rename the item.
:kbd:`Return` confirms the name while :kbd:`Esc` cancels the operator.


.. _bpy.ops.wm.batch_rename:

Batch Rename
============

.. reference::

   :Menu:      :menuselection:`Edit --> Batch Rename`
   :Shortcut:  :kbd:`Ctrl-F2`

The *Batch Rename* operator can rename many data-block names at once.
This uses a pop-up dialog with operations and their options to change the name.
These actions are applied in order, from first to last.

Data Source
   Where to look for the data-blocks that are intended to be renamed.

   :Selected: Operates on the currently selected objects.
   :All: Operates on all data in the blend file.

Data Type
   The :ref:`data-block type <data-system-datablock-types>` to perform the batch rename operations on.


Operations
----------

The *Batch Rename* has several sub Operations to change the data names.
The default operation is *Find/Replace* however, other operations can be added
to change the data names further.
Below all the operations gives a message in the status bar on how many data-blocks were renamed.


Find/Replace
^^^^^^^^^^^^

*Find/Replace* searches for a particular text in the names and optionally replaces it with a new text.
`Regular Expressions <https://en.wikipedia.org/wiki/Regular_expression>`__
can be used as a powerful way to tailor the *Find*/*Replace* texts
and can be enabled using the icon to the right of the text fields.

Find
   The text to search for in names.
Replace
   The text to replace for in matching names found from the *Find* text.
Case Sensitive
   Search results must exactly match the case of the *Find* text.


Set Name
^^^^^^^^

*Set Name* works the most similar to `Rename Active Item`_
by renaming the current data-block without having to do a find and replace operation.

Method
   :New:
      Disregards the current name replacing it with the "new" name.
   :Prefix:
      Adds text to the beginning of the current name.
      This is useful for tools that look for special text in the prefix of a data-block name.
   :Suffix:
      Adds text to the end of the current name.
      This is useful for tools that look for special text in the suffix of a data-block name.
Name
   Defines the new name or the text to add as a prefix/suffix.


Strip Characters
^^^^^^^^^^^^^^^^

*Strip Characters* cleans up names by removing certain
character types from either the beginning or the end of the name.

Characters
   :Spaces:
      Strips any space characters from the name, e.g. "Living Room   " becomes "Living Room".
   :Digits:
      Strips any numerical characters from the name, e.g. ``cube.001`` becomes ``cube.``.
   :Punctuation:
      Strips any punctuation characters (``,.?!:;`` etc.) from the name, e.g. ``cube?`` becomes ``cube``.

   .. tip::

      Multiple character types can be removed at once by :kbd:`Shift-LMB` on the types.

Strip From
   :Start: Strips any leading characters in the name.
   :End: Strips any trailing characters in the name.


Change Case
^^^^^^^^^^^

*Change Case* modifies the case of names to be one of the following:

Convert To
   :Upper Case: Changes all text to be in upper case, e.g. ``cube.001`` becomes ``CUBE.001``.
   :Lower Case: Changes all text to be in lower case, e.g. ``CUBE.001`` becomes ``cube.001``.
   :Title Case: Changes all text to be in title case, e.g. ``living room`` becomes ``Living Room``.
