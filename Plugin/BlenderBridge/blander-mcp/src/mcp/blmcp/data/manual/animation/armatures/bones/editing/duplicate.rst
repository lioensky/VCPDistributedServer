.. _bpy.ops.armature.duplicate_move:

*********
Duplicate
*********

.. reference::

   :Mode:      Edit Mode
   :Menu:      :menuselection:`Armature --> Duplicate`
   :Shortcut:  :kbd:`Shift-D`

.. note::

   This tool works on selected bones; selected joints are ignored.

As in mesh editing, by pressing :kbd:`Shift-D` the selected bones will be duplicated.
The duplicates become the selected elements and they are placed in select mode,
so you can move them wherever you like.

If you select part of a chain, by duplicating it you will get a copy of the selected chain,
so the copied bones are interconnected exactly like the original ones.

The duplicate of a bone which is parented to another bone will also be parented to the same
bone, even if the root bone is not selected for the duplication. Be aware, though,
that if a bone is parented **and** connected to an unselected bone,
its copy will be parented, but **not** connected to the unselected bone
(see Fig. :ref:`fig-rig-bone-duplication`).

.. _fig-rig-bone-duplication:

.. list-table:: Duplication example.

   * - .. figure:: /images/animation_armatures_bones_editing_duplicate_example-1.png

          An armature with three selected bones and a selected single root.

     - .. figure:: /images/animation_armatures_bones_editing_duplicate_example-2.png

          The three duplicated bones. Note that the selected chain is preserved in the copy,
          and that Bone.006 is parented but not connected to Bone.001, as indicated by the black dashed line.
          Similarly, Bone.007 is parented but not connected to Bone.003.
