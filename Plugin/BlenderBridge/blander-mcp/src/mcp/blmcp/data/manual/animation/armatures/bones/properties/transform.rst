
*********
Transform
*********

.. reference::

   :Mode:      Edit Mode and Pose Mode
   :Panel:     :menuselection:`Bone --> Transform`

.. list-table::

   * - .. figure:: /images/animation_armatures_bones_properties_transform_panel-edit.png

          The Transform panel (Edit Mode).

     - .. figure:: /images/animation_armatures_bones_properties_transform_panel-pose.png

          The Transform panel (Pose Mode).

When in *Edit Mode* you can use this panel to control position and roll of individual bones.
Whereas in *Pose Mode* you can only set location for the main bone, and you can now set rotation and scale.

In addition, in *Pose Mode* it is possible to restrict changes in position,
rotation and scale by axis on each bone in the armature.

.. _bpy.types.EditBone.head:

Head X, Y, Z
   Location of head end of the bone.

.. _bpy.types.EditBone.tail:

Tail X, Y, Z
   Location of tail end of the bone.

.. _bpy.types.EditBone.roll:

Roll
   Bone rotation around head-tail axis.

.. _bpy.types.EditBone.length:

Length
   The distance from the bone's head to it's tail. Changing the length moves the tail end.

.. _bpy.types.EditBone.lock:

Lock
   Bone is not able to be transformed when in Edit Mode.
