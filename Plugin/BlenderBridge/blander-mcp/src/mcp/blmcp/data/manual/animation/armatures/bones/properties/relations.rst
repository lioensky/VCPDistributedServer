.. _properties_data_bone_relations:

*********
Relations
*********

.. reference::

   :Mode:      All Modes
   :Panel:     :menuselection:`Bone --> Relations`

.. figure:: /images/animation_armatures_bones_properties_relations_panel.png

   Bone Relations panel.

In this panel you can manage the relationship of this bone with its parent bone.
It also shows the bone collections the bone is assigned to.


Parenting
=========

.. _bpy.types.EditBone.parent:

Parent
   A :ref:`ui-data-id` to select the bone to set as a parent.

.. _bpy.types.Bone.use_relative_parent:

Relative Parenting :guilabel:`Pose Mode Only`
   Changes how transformation of the bone is applied to its child Objects.

.. _bpy.types.EditBone.use_connect:

Connected
   The *Connected* checkbox set the head of the bone to be connected with its parent tail.


Transformations
---------------

Bones relationships have effects on transformations behavior.

By default, children bones inherit:

- Their parent position, with their own offset of course.
- Their parent rotation (i.e. they keep a constant rotation relatively to their parent).
- Their parent scale, here again with their own offset.

.. list-table:: Examples of transforming parented/connected bones.

   * - .. figure:: /images/animation_armatures_bones_properties_relations_rest.png
          :width: 200px

          The armature in its rest position.

     - .. figure:: /images/animation_armatures_bones_properties_relations_root-rotation.png
          :width: 200px

          Rotation of a root bone.

     - .. figure:: /images/animation_armatures_bones_properties_relations_root-scale.png
          :width: 200px

          Scaling of a root bone.

Exactly like standard children objects. You can modify this behavior on a per-bone basis,
using the Relations panel in the *Bones* tab:

.. _bpy.types.EditBone.use_local_location:

Local Location
   When disabled, the location transform property is evaluated in the parent bone's local space,
   rather than using the bone's own *rest pose* local space orientation.

.. _bpy.types.EditBone.use_inherit_rotation:

Inherit Rotation
   When disabled, this will "break" the rotation relationship to the bone's parent.
   This means that the child will keep its rotation in the armature object space when its parent is rotated.

.. _bpy.types.EditBone.inherit_scale:

Inherit Scale
   Specifies which effects of parent scaling the bone inherits:

   These inheriting behaviors propagate along the bones' hierarchy.
   So when you scale down a bone, all its descendants are by default scaled down accordingly.
   However, if you disable one bone's *Inherit Scale* or *Inherit Rotation*
   property in this "family", this will break the scaling propagation,
   i.e. this bone *and all its descendants* will no longer be affected when you scale one of its ancestors.

   :Full:
      The bone inherits all effects of parent scaling and shear.
   :Fix Shear:
      Full parent effects are applied to the rest state of the child, after which any shear is
      removed in a way that preserves the bone direction, length and volume, and minimally affects
      roll on average. The result is combined with the local transformation of the child.

      If the inherited scale is non-uniform, this does not prevent shear from reappearing due to
      local rotation of the child bone, or of its children.
   :Aligned:
      Parent scaling is inherited as if the child was oriented the same as the parent, always
      applying parent X scale over child X scale, and so on.
   :Average:
      Inherits a uniform scaling factor that is the total change in the volume of the parent.
   :None:
      Ignores all scaling and shear of the parent.
   :None (Legacy):
      Ignores all scaling, provided the parent is not sheared. If it is, there are no guarantees.

      This choice replicates the behavior of the old Inherit Scale checkbox, and may be removed in a future release.

   .. tip::

      The various *Inherit Scale* options are provided as tools in avoiding shear that is caused
      by non-uniform scaling combined with parenting and rotation. There is no obvious best way
      to achieve that, so different options are useful for different situations.

      - **None** --
        Useful for gaining full control over the scaling of the child in order
        to e.g. manually overwrite it with constraints.
      - **Average** --
        Useful to block squash and stretch propagation between sub-rigs, while
        allowing uniform changes in the size and volume to pass through.
      - **Aligned** --
        Can be used within bone chains, e.g. tentacles, in order to propagate
        lengthwise scaling as lengthwise, and sideways as sideways, no matter
        how the tentacle bends. Similar to using *None* with
        :doc:`Copy Scale </animation/constraints/transform/copy_scale>` from parent.
      - **Fix Shear** --
        May be useful at the base of an appendage in order to reallocate squash and stretch
        between axes based on the difference in rest pose orientations of the parent and child.
        It behaves closest to *Full* while suppressing shear.

   .. list-table:: Examples of transforming parented/connected bones with Inherit Rotation disabled.

      * - .. figure:: /images/animation_armatures_bones_properties_relations_inherit-rot-disabled.png

             The yellow outlined Inherit Rotation disabled bone in the armature.

        - .. figure:: /images/animation_armatures_bones_properties_relations_inherit-rot-disabled-descendant.png

             Rotation of a bone with an Inherit Rotation disabled bone among its descendants.

        - .. figure:: /images/animation_armatures_bones_properties_relations_inherit-rot-disabled-scale.png

             Scaling of a bone with an Inherit Rotation disabled bone among its descendants.

Connected bones have another specificity: they cannot be moved. Indeed,
as their root must be at their parent's tip, if you do not move the parent,
you cannot move the child's root, but only its tip, which leads to a child rotation.
This is exactly what happens, when you press :kbd:`G` with a connected bone selected,
Blender automatically switches to rotation operation.

Bones relationships also have important consequences on how selections of multiple bones
behave when transformed. There are many different situations which may not be included on this list,
however, this should give a good idea of the problem:

- Non-related selected bones are transformed independently, as usual.
- When several bones of the same "family" are selected,
  *only* the "most parent" ones are really transformed --
  the descendants are just handled through the parent relationship process, as if they were not selected
  (see Fig. :ref:`fig-rig-pose-edit-scale` the third tip bone,
  outlined in yellow, was only scaled down through the parent relationship,
  exactly as the unselected ones, even though it is selected and active.
  Otherwise, it should have been twice smaller!)

  .. _fig-rig-pose-edit-scale:

  .. figure:: /images/animation_armatures_bones_properties_relations_scale-related.png
     :align: center
     :width: 320px

     Scaling bones, some of them related.

- When connected and unconnected bones are selected,
  and you start a move operation, only the unconnected bones are affected.
- When a child connected hinge bone is in the selection,
  and the "most parent" selected one is connected, when you press :kbd:`G`,
  nothing happens, because Blender remains in move operation, which of course has no effect on a connected bone.

So, when posing a chain of bones, you should always edit its elements from the root bone to the tip bone.
This process is known as :term:`Forward Kinematics` (FK).
We will see in a :ref:`later page <bone-constraints-inverse-kinematics>`
that Blender features another pose method, called :term:`Inverse Kinematics` (IK),
which allows you to pose a whole chain just by moving its tip.

.. note::

   This feature is somewhat extended/completed by
   the :doc:`pose library </animation/armatures/posing/editing/pose_library>`.


.. _bpy.types.Bone.collections:
.. _bpy.types.EditBone.collections:
.. _bpy.types.PoseBone.collections:

Bone Collections
================

This list shows the :term:`bone collections <Bone Collection>` the bone is assigned to.
Press the eye icon to show or hide the entire bone collection.
Press the star icon to show only this bone collection, and others also marked as 'solo'
Press the X icon to remove the bone from that particular collection.

To assign the bone to other bone collections, either use the :kbd:`M` or :kbd:`Shift-M` shortcuts
(see :ref:`Moving Bones Between Collections <moving_bones_between_collections>`)
or go to the :ref:`Armature properties panel <bpy.types.BoneCollection>`.
