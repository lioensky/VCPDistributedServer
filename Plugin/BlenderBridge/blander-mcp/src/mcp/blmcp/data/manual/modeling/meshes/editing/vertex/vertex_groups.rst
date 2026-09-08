
*************
Vertex Groups
*************

.. _bpy.ops.object.vertex_group_assign_new:

Assign to New Group
===================

.. reference::

   :Mode:      Edit Mode
   :Menu:      :menuselection:`Vertex --> Vertex Groups --> Assign to New Group`
   :Shortcut:  :kbd:`Ctrl-G`

Creates a new :doc:`Vertex Group </modeling/meshes/properties/vertex_groups/introduction>`
and assigns the selected vertices to it, with the *Weight* that's currently set
in the :doc:`/modeling/meshes/properties/vertex_groups/vertex_groups`.


Assign to Active Group
======================

.. reference::

   :Mode:      Edit Mode
   :Menu:      :menuselection:`Vertex --> Vertex Groups --> Assign to Active Group`
   :Shortcut:  :kbd:`Ctrl-G`

Assigns the selected vertices to the vertex group that's selected in the Vertex Groups panel,
with the *Weight* that's currently set in that panel.

This is the same as clicking the *Assign* button in the panel itself.


Remove from Active Group
========================

.. reference::

   :Mode:      Edit Mode
   :Menu:      :menuselection:`Vertex --> Vertex Groups --> Remove from Active Group`
   :Shortcut:  :kbd:`Ctrl-G`

Removes the selected vertices from the vertex group that's selected in the Vertex Groups panel.
This is the same as clicking the *Remove* button in the panel itself.


Remove from All
===============

.. reference::

   :Mode:      Edit Mode
   :Menu:      :menuselection:`Vertex --> Vertex Groups --> Remove from All`
   :Shortcut:  :kbd:`Ctrl-G`

Removes the selected vertices from all vertex groups.


.. _bpy.ops.object.vertex_group_set_active:

Set Active Group
================

.. reference::

   :Mode:      Edit Mode
   :Menu:      :menuselection:`Vertex --> Vertex Groups --> Set Active Group`
   :Shortcut:  :kbd:`Ctrl-G`

Sets a specific vertex group (chosen from the menu) as the active one.
This is the same as selecting the group in the Vertex Groups panel.


Remove Active Group
===================

.. reference::

   :Mode:      Edit Mode
   :Menu:      :menuselection:`Vertex --> Vertex Groups --> Remove Active Group`
   :Shortcut:  :kbd:`Ctrl-G`

Deletes the vertex group that's currently selected in the Vertex Groups panel.
This is the same as clicking the :bl-icon:`remove` button in the panel.


Remove All Groups
=================

.. reference::

   :Mode:      Edit Mode
   :Menu:      :menuselection:`Vertex --> Vertex Groups --> Remove All Groups`
   :Shortcut:  :kbd:`Ctrl-G`

Deletes all vertex groups of the mesh. This can also be done by clicking the
:bl-icon:`downarrow_hlt` button in the Vertex Groups panel and selecting
*Delete All Groups* in the popover menu.
