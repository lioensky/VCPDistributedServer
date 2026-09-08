.. _bpy.types.BoneCollection:

****************
Bone Collections
****************

.. note::

   Bone Collections were introduced in Blender 4.0 as replacement of Armature
   Layers and Bone Groups. :ref:`Bone colors <bpy.types.Bone.color>` are now
   managed directly on the bone.

.. reference::

   :Mode:      Object, Pose, and Edit Modes
   :Panel:     :menuselection:`Properties --> Armature --> Bone Collections`

.. figure:: /images/animation_armatures_properties_bonecollections_panel.png

   The Bone Collections panel in the Armature properties.

This panel contains a Tree View to manage :doc:`Bone Collection </animation/armatures/bones/bone_collections>`
From this panel, Bone Collections can be created, deleted, re-arranged, and more.

Collections can be renamed by double clicking on the name, or right clinking and selecting *Rename*.
To nest a collection inside an existing collection, click and drag the name onto another collection's name.
Child collection can also be made by :kbd:`RMB` and selecting "Add Child Collection".

To the right of the name gives a few controls of the collection:

.. _bpy.types.BoneCollection.is_visible:

Visible (Eye)
   Bones in this collection will be visible in the 3D Viewport.

.. _bpy.types.BoneCollection.is_solo:

Solo (Star)
   Show only this bone collection, and others also marked as "solo".

Further more, collection that are not empty will have a dot to indicate the collection has bones assigned to it.

.. tip::

   The Bone Properties panel gives a slightly different view on the bone's collections. See
   :doc:`Bone Relations </animation/armatures/bones/properties/relations>`.


Specials
========

Show All
   Unhides any hidden bone collections.

.. _bpy.ops.armature.collection_unsolo_all:

Un-Solo All
   Clear the 'solo' setting on all bone collections

.. _bpy.ops.armature.collection_remove_unused:

Remove Unused
   Remove all bone collections that have neither bones nor children.
   This is done recursively, so bone collections that only have unused children are also removed.


Assign & Select
===============

.. reference::

   :Mode:      Pose, and Edit Modes
   :Panel:     :menuselection:`Properties --> Armature --> Bone Collections`
   :Menu:      :menuselection:`Pose --> Bone Collections --> ...`

.. _bpy.ops.armature.collection_assign:

Assign
   Assigns the selected bones to the active bone collection.

.. _bpy.ops.armature.collection_unassign:

Remove
   Removes the selected bones from the active bone collection.

.. _bpy.ops.armature.collection_select:

Select
   Selects the bones in the active bone collection.

.. _bpy.ops.armature.collection_deselect:

Deselect
   Deselects the bones in the active bone collection.

.. note::

   Individual bones can also be unassigned from their collections via the
   :ref:`Bone Relations panel <bpy.types.PoseBone.collections>`.

.. tip::

   For setting up custom selection sets of bones, take a look at the *Selection
   Sets* add-on. It is bundled with Blender.


.. _moving_bones_between_collections:

Moving Bones between Collections
================================

Blender should be in *Edit Mode* or *Pose Mode* to move bones between collections.
Note that as with objects, bones can be assigned to in several collections at once.

.. _bpy.ops.armature.move_to_collection:

Move to Bone Collection
   Shows a list of the Armature's *editable* bone collections. Choosing a bone
   collection unassign the selected bones from all other bone collections, then
   assigns them to the chosen one.

   Available as :menuselection:`Pose --> Move to Collection` (*Pose Mode*)
   :menuselection:`Armature --> Move to Collection` (*Edit Mode*), and :kbd:`M` (either mode).

Bone Collections
   Shows a list of the Armature's *editable* bone collections. The collections
   that the active bone is assigned to are prefixed with a ``-``, and choosing
   those will unassign all selected bones from that collection. Similarly,
   choosing a bone collection prefixed with a ``+`` will assign all selected bones
   to that collection.

   Available as :menuselection:`Pose --> Bone Collections` (*Pose Mode*)
   :menuselection:`Armature --> Bone Collections` (*Edit Mode*), and :kbd:`Shift-M` (either mode).

.. note::

   The above operators will only show the *editable* bone collections. When the
   Armature is linked, its bone collections will be *read-only*. New bone
   collections can still be added via library overrides; only those will be
   editable.

   See :ref:`Library Overrides of Bone Collections <bone_collections_library_overrides>`.


Custom Properties
=================

Create and manage your own properties to store data in the Bone Collection's data-block.
See the :ref:`Custom Properties <files-data_blocks-custom-properties>` page for more information.
