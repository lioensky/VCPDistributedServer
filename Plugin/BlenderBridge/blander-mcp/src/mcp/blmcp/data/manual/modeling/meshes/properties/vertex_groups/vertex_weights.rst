
**************
Vertex Weights
**************

.. reference::

   :Mode:      Edit and Weight Paint Modes
   :Panel:     :menuselection:`Sidebar region --> Vertex Weights`

.. figure:: /images/modeling_meshes_properties_vertex-groups_vertex-weights_panel-overview.png
   :width: 260px

   Vertex Weights panel.

A :doc:`vertex group </modeling/meshes/properties/vertex_groups/index>` assigns a weight
(a number between 0 and 1) to each vertex it contains. A group can have multiple vertices,
and each vertex can be part of multiple groups.

The *Vertex Weights* panel in the 3D Viewport's Sidebar shows the vertex groups for
the active vertex, and lets you see and edit the associated weights.
It's available in Edit Mode, as well as in Weight Paint Mode when Vertex Selection
is enabled in the header.

.. _bpy.types.ToolSettings.vertex_group_subset:

Vertex Group Categories
=======================

While all vertex groups are technically the same, we can still divide them into two types
depending on how they're used:

Deform Groups
   Also sometimes called "weight group" or "weight map," this type of vertex group determines
   which vertices are affected by a certain bone in the
   :doc:`Armature </animation/armatures/introduction>`. In other words, it defines which part
   of the mesh deforms when the bone moves around.

Other Groups
   The remaining vertex groups are used with shape keys, modifiers, and other areas.

The deform vertex groups are related to each other: the deformation weights of every vertex
typically need to add up to 1. For this reason, you can use the filter buttons at the top
of the panel to show only these vertex groups (or to exclude them).

Weight Table
============

The Weight Table shows all the weights associated with the *active vertex*, which is the
vertex that was selected last (and is highlighted in white). If there is no active vertex,
or it isn't part of any vertex group, the panel is not displayed.

Set the Active Group
--------------------

You can click the name of a vertex group to make it the active one.

.. figure:: /images/modeling_meshes_properties_vertex-groups_vertex-weights_editor-name.png
   :width: 260px

   Changing the active vertex group.

Display Weights in Edit Mode
----------------------------

.. figure:: /images/modeling_meshes_properties_vertex-groups_vertex-weights_show.png
   :align: right

   Enable display of weights in Edit Mode.

When you are in Edit Mode, you can make the weights of the active group visible on the mesh:
open the *Mesh Edit Mode Overlays* popover and enable the *Vertex Group Weights* option.

.. figure:: /images/modeling_meshes_properties_vertex-groups_vertex-weights_edit-mode.png
   :width: 260px

   Weights in Edit Mode.


Change a Weight
---------------

You can change the weight for a vertex group by either clicking the number and typing a new
one or by dragging left and right with :kbd:`LMB`. You can also click the arrows
(only shown when hovering) to change the weight in steps of 0.01.

.. figure:: /images/modeling_meshes_properties_vertex-groups_vertex-weights_editor-weight.png
   :width: 260px

   Changing a weight value.


.. _bpy.ops.object.vertex_weight_paste:

Copy a Weight
-------------

The *Paste Weight to Selected* button copies the weight from the active vertex to the other selected
vertices. Note that, even though it uses the word "paste," it doesn't interact with the *Copy* button
and in fact doesn't use the clipboard at all.

.. figure:: /images/modeling_meshes_properties_vertex-groups_vertex-weights_editor-paste.png
   :width: 260px

   Copying a weight.


.. _bpy.ops.object.vertex_weight_delete:

Delete a Weight
---------------

The *Delete Weight* button removes the active vertex from the vertex group,
making the row disappear from the list.

.. figure:: /images/modeling_meshes_properties_vertex-groups_vertex-weights_editor-delete.png
   :width: 260px

   Deleting a weight.


Operators
=========

.. figure:: /images/modeling_meshes_properties_vertex-groups_vertex-weights_editor-functions.png
   :width: 260px

   Vertex weight operators.

Normalize
   Recalculates the weights of the active vertex so that they add up to 1.0 while
   retaining their relative magnitude.

.. _bpy.ops.object.vertex_weight_copy:

Copy
   Copies all the weights from the active vertex to the other selected vertices.

.. tip::

   Both tools only work on the vertex groups that match the current filter setting.


Locking
=======

.. figure:: /images/modeling_meshes_properties_vertex-groups_vertex-weights_editor-locked.png
   :width: 260px

   Locked vertex group.

If a vertex group is locked, its weights become uneditable, and the buttons for copying
and normalizing weights become disabled.

.. tip::

   The *Normalize* and *Copy* buttons only become disabled if there's a locked vertex
   group in the current list. If (for example) only non-deforming vertex groups are locked,
   you can switch to the *Deform* filter and normalize the groups that way.
