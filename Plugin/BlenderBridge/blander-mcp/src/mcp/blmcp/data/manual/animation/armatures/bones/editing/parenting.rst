.. _bpy.ops.armature.parent_set:
.. _bpy.ops.armature.parent_clear:

*********
Parenting
*********

.. reference::

   :Mode:      Edit Mode
   :Menu:      :menuselection:`Armature --> Parent`
   :Panel:     :menuselection:`Properties --> Bones --> Relations`
   :Shortcut:  :kbd:`Ctrl-P`, :kbd:`Alt-P`

You can edit the relationships between bones (and hence create/modify the chains of bones)
both from the 3D Viewport and the Properties. Whatever method you prefer,
it's always a matter of deciding, for each bone, if it has to be parented to another one,
and if so, if it should be connected to it.

To parent and/or connect bones, you can:

In the *3D Viewport*, select the bone and *then* its future parent, and press :kbd:`Ctrl-P`
(or :menuselection:`Armature --> Parent --> Make Parent...`).
In the small *Make Parent* menu that pops up, choose *Connected*
if you want the child to be connected to its parent, else click on *Keep Offset*.
If you have selected more than two bones, they will all be parented to the last selected one.
If you only select one already-parented bone, or all selected bones are already parented to the last selected one,
your only choice is to connect them, if not already done.
If you select only one non-parented bone, you will get the *Need selected bone(s)* error message...

.. note::

   With this method, the newly-children bones will not be scaled nor rotated --
   they will just be moved if you choose to connect them to their parent's tip.

In the *Properties*, Bones tab, for each selected bone,
you can select its parent in the *Parent* data ID to the upper right corner of its Relations panel.
If you want them to be connected, just enable the checkbox to the right of the list.

.. note::

   With this method, the tip of the child bone will never be moved --
   so if *Connected* is enabled, the child bone will be completely transformed by the operation.

.. list-table:: Parenting example.

   * - .. figure:: /images/animation_armatures_bones_editing_parenting_start.png

          The starting armature, with Bone.005 parented and connected to Bone.004.

     - .. figure:: /images/animation_armatures_bones_editing_parenting_unconnected.png

          Bone.005 re-parented to Bone.002, but not connected to it
          (same result, using either :kbd:`Ctrl-P 2` in 3D Viewport, or the Bones tab settings).

   * - .. figure:: /images/animation_armatures_bones_editing_parenting_connected.png

          Bone.005 parented and connected to Bone.002, using :kbd:`Ctrl-P 1` in 3D Viewport.

     - .. figure:: /images/animation_armatures_bones_editing_parenting_data-id.png

          Bone.005 parented and connected to Bone.002.

          Using the Parent data ID of Bone.005 Relations panel.

To disconnect and/or free bones, you can:

- In a 3D Viewport, select the desired bones, and press :kbd:`Alt-P`
  (or :menuselection:`Armature --> Parent --> Clear Parent...`).
  In the small *Clear Parent* menu that pops up, choose *Clear Parent* to completely free all selected bones,
  or *Disconnect Bone* if you just want to break their connections.
- In the Properties, *Bones* tab, for each selected bone, you can select no parent
  in the *Parent* data ID of its Relations panel, to free it completely.
  If you just want to disconnect it from its parent, disable the *Connected* checkbox.

Note that relationships with non-selected children are never modified.


.. _bpy.ops.armature.assign_to_collection:

Bone Collections
================

.. reference::

   :Mode:      Edit Mode, Pose Mode
   :Menu:      :menuselection:`Armature --> Bone Collections`, :menuselection:`Pose --> Bone Collections`

Manages the :ref:`bpy.types.BoneCollection` the bone is assigned to.

Move to Collection :kbd:`M`
   Move bones to a collection.

Assign to Collection :kbd:`Shift-M`
   Assign all selected bones to a collection, or unassign them,
   depending on whether the active bone is already assigned or not.

----------

.. _bpy.ops.armature.collection_show_all:

Show All :kbd:`Ctrl-AccentGrave`
   Unhides any hidden bone collections.

.. _bpy.ops.armature.collection_create_and_assign:

Assign to new Collection
   Assigns the selected bones to a new collection named "New Collection".
   This collection can be renamed in the :ref:`bpy.types.BoneCollection` panel of the Armature properties.
