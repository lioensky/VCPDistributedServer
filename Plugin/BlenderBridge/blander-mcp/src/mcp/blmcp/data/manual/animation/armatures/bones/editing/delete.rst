
******
Delete
******

.. _bpy.ops.armature.delete:

Bones
=====

.. reference::

   :Mode:      Edit Mode
   :Menu:      :menuselection:`Armature --> Delete --> Bones`
   :Shortcut:  :kbd:`X`

This tool delete selected bones, selected *joints* are ignored.

If you delete a bone in a chain, its child(ren)
will be automatically re-parented to its own parent, but **not** connected,
to avoid deforming the whole armature.

.. list-table:: Deletion example.

   * - .. figure:: /images/animation_armatures_bones_editing_delete_example-1.png

          An armature with two selected bones, just before deletion.

     - .. figure:: /images/animation_armatures_bones_editing_delete_example-2.png

          The two bones have been deleted. Note that Bone.002,
          previously connected to the deleted Bone.001, is now parented but not connected to Bone.


.. _bpy.ops.armature.dissolve:

Dissolve
========

.. reference::

   :Mode:      Edit Mode
   :Menu:      :menuselection:`Armature --> Delete --> Dissolve`
   :Shortcut:  :kbd:`Ctrl-X`

Todo 2.76.
