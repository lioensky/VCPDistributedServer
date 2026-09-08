.. |copy-paste| image:: /images/animation_armatures_posing_editing_copy-paste_buttons.png
.. _bpy.ops.pose.copy:
.. _bpy.ops.pose.paste:

***************
Copy/Paste Pose
***************

.. reference::

   :Mode:      Pose Mode
   :Menu:      :menuselection:`Pose --> Copy Pose`,
               :menuselection:`Pose --> Paste Pose`,
               :menuselection:`Pose --> Paste Pose Flipped`
   :Shortcut:  :kbd:`Ctrl-C`,
               :kbd:`Ctrl-V`,
               :kbd:`Shift-Ctrl-V`

Blender allows you to copy and paste a pose, either through the *Pose* menu, or
by using hotkeys.

Copy Pose
   Copy the current pose of selected bones into the pose buffer.
Paste Pose
   Paste the buffered pose to the currently posed armature.
Paste Pose Flipped
   Paste the *X axis mirrored* buffered pose to the currently posed armature.

Here are important points:

- This tool works at the :term:`Blender session` level, which means you can use it across
  armatures, scenes, and even files. However, the pose buffer is not saved, so you lose it when you
  close Blender.
- There is only one pose buffer.
- Only the selected bones are taken into account during copying (i.e. you copy only selected bones' pose).
- During pasting, on the other hand, bone selection has no importance.
  The copied pose is applied on a per-name basis
  (i.e. if you had a ``forearm`` bone selected when you copied the pose,
  the ``forearm`` bone of the current posed armature will get its pose when you paste it --
  and if there is no such named bone, nothing will happen...).
- What is copied and pasted is in fact the position, rotation or scale of each bone, in its own space.
  This means that the resulting pasted pose might be very different from the originally copied one, depending on:

  - The rest position of the bones.
  - And the current pose of their parents.

.. list-table::

   * - .. figure:: /images/animation_armatures_posing_editing_copy-paste_examples-1.png

          The rest position of the original armature.

     - .. figure:: /images/animation_armatures_posing_editing_copy-paste_examples-2.png

          The rest position of the destination armature.

.. list-table:: Examples of pose copy/paste.

   * - .. figure:: /images/animation_armatures_posing_editing_copy-paste_examples-3.png

          The first copied pose (note that only two bones are selected and hence copied).

     - .. figure:: /images/animation_armatures_posing_editing_copy-paste_examples-4.png

          The pose pasted on the destination armature.

     - .. figure:: /images/animation_armatures_posing_editing_copy-paste_examples-5.png

          The pose mirror-pasted on the destination armature.

   * - .. figure:: /images/animation_armatures_posing_editing_copy-paste_examples-6.png

          The same pose as above is copied, but this time with all bones selected.

     - .. figure:: /images/animation_armatures_posing_editing_copy-paste_examples-7.png

          The pose pasted on the destination armature.

     - .. figure:: /images/animation_armatures_posing_editing_copy-paste_examples-8.png

          The pose mirror-pasted on the destination armature.
