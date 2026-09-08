
*******************
Vertex Groups Panel
*******************

.. reference::

   :Mode:      All Modes
   :Panel:     :menuselection:`Object Data tab --> Vertex Groups`

.. figure:: /images/modeling_meshes_properties_vertex-groups_introduction_panel.png
   :align: right

   The Vertex Group panel.

Vertex groups are maintained within the *Object Data* Properties, in the *Vertex Groups* panel.

.. _bpy.ops.object.vertex_group_add:
.. _bpy.ops.object.vertex_group_sort:
.. _bpy.ops.object.vertex_group_copy:
.. _bpy.ops.object.vertex_group_copy_to_selected:
.. _bpy.ops.object.vertex_group_remove:
.. _bpy.ops.object.vertex_group_move:
.. _bpy.types.VertexGroups.active_index:

Active Vertex Group
   A :ref:`List view <ui-list-view>`.

   Lock
      Locks the group from being editable. You can only rename or delete the group.

:bl-icon:`add` Add Vertex Group
   Create an empty vertex group.
:bl-icon:`remove` Remove Vertex Group
   Deletes the active vertex group.

:bl-icon:`downarrow_hlt` Vertex Group Specials
   Sort by Name
      Sorts vertex groups alphabetically.
   Sort by Bone Hierarchy
      .. todo:: Add this information.
   Duplicate Vertex Group
      Add a copy of the active vertex group as a new group.
      The new group will be named like the original group with "_copy" appended at the end of its name.
      And it will contain associations to exactly the same vertices
      with the exact same weights as in the source vertex group.
   Copy Vertex Group to Selected
      Copy all vertex groups to other selected objects provided they have matching indices
      (typically this is true for copies of the mesh which are only deformed and not otherwise edited).

   Mirror Vertex Group
      Mirrors weights and/or flips group names.
      See :ref:`Mirror Vertex Group <bpy.ops.object.vertex_group_mirror>` for more information.
   Mirror Vertex Group (Topology)
      Performs the *Mirror Vertex Group* with :ref:`bpy.types.Mesh.use_mirror_topology` enabled.

   Remove from All Groups
      Unassigns the selected vertices from all (even locked) groups.
      After this operation has been performed, the vertices will no longer be contained in any vertex group.
      (Not available for locked groups.)
   Clear Active Group
      Remove all assigned vertices from the active group. The group is made empty.
      Note that the vertices may still be assigned to other vertex groups of the object.
      (Not available for locked groups.)
   Delete All Unlocked Groups
      Remove all vertex groups from the object that are *not* locked.
   Delete All Groups
      Remove all vertex groups from the object.

   Lock All
      Lock all groups.
   Unlock All
      Unlock all groups.
   Lock Invert All
      Invert group locks.


Editing Vertex Groups
=====================

.. reference::

   :Mode:      Edit Mode
   :Panel:     :menuselection:`Object Data tab --> Vertex Groups`
   :Menu:      :menuselection:`Vertex --> Vertex Groups`
   :Shortcut:  :kbd:`Ctrl-G`

.. figure:: /images/modeling_meshes_properties_vertex-groups_vertex-groups_panel-edit.png
   :align: right

   Vertex Group panel in Edit or Weight Paint Mode.

When you switch either to Edit Mode or to Weight Paint Mode, vertex weights can be edited.
The same operations are available in the 3D Viewport's
:menuselection:`Vertex --> Vertex Groups` menu or :kbd:`Ctrl-G`.

.. _bpy.ops.object.vertex_group_assign:

Assign
   To assign the selected vertices to the active group with the weight as defined in the *Weight* (see below).

.. _bpy.ops.object.vertex_group_remove_from:

Remove
   To remove the selected vertices from the active group (and thus also delete their weight values).
Select
   To select all vertices contained in the group.
Deselect
   To deselect all vertices contained in the group.

.. _bpy.types.ToolSettings.vertex_group_weight:

Weight
   The weight value that gets assigned to the selected vertices.

Auto Normalize
   Ensure all bone-deforming vertex groups add up to 1.0 while weight painting or assigning to vertices.
