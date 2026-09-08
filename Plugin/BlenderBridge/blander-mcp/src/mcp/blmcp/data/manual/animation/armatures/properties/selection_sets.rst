.. _bpy.types.SelectionSet:

**************
Selection Sets
**************

.. reference::

   :Mode:      Pose Mode
   :Panel:     :menuselection:`Armature --> Selection Sets`

Selection Sets are a feature that allows the definition of sets of bones for easy selection while animating.
The sets can be created in local and linked armature overrides.

.. _bpy.types.Object.active_selection_set:

Selection Set
   A :ref:`ui-list-view` listing all selection sets for the selected armature.
   Here, selection sets can be renamed by double clicking on the name.

   .. _bpy.types.SelectionSet.is_selected:

   To the right of the name is a check box to include that selection set when copying to the clipboard.

.. rubric:: Specials

.. _bpy.ops.pose.selection_set_delete_all:

Delete All Sets
   Removes all selection sets from the list.

.. _bpy.ops.pose.selection_set_remove_bones:

Remove Selected Bones from All Sets
   Removes the selected bones from all selection sets.

.. _bpy.ops.pose.selection_set_copy:

Copy Selected Set(s)
   Copies the selected set to Blender's clipboard.

.. _bpy.ops.pose.selection_set_paste:

Paste Selected Set(s)
   Pastes a selection set from Blender's clipboard.

-----

.. _bpy.ops.pose.selection_set_assign:

Assign
   Assigns the selected bones to the active selection set.

.. _bpy.ops.pose.selection_set_unassign:

Remove
   Removes the selected bones to the active selection set.

.. _bpy.ops.pose.selection_set_select:

Select
   Selects all the bones in the active selection set.

.. _bpy.ops.pose.selection_set_deselect:

Deselect
   Deselects all the bones in the active selection set.
