.. _bpy.ops.armature.symmetrize:

**********
Symmetrize
**********

.. reference::

   :Mode:      Edit Mode
   :Menu:      :menuselection:`Armature --> Symmetrize`

The Symmetrize operator mirrors selected bones along the X axis using Blender's bone
:ref:`naming convention <armature-editing-naming-conventions>` for symmetrical armatures.
Bones can be mirrored from left to right or right to left, depending on the selection.

- If matching bones are selected on both sides, mirroring happens from right to left.
- Bones with opposite names that don't exist are created, and existing ones are overwritten.
- Bones that cannot be determined as left or right are ignored.

Symmetrized bone and constraint properties are adjusted to mirror their behaviors.
For bones with :doc:`Action Constraints </animation/constraints/relationship/action>`,
keyframes are added to the target Action, ensuring symmetrical motion when the Action is activated.

.. note::

   Bone or constraint drivers are not created or affected during symmetrization.


.. rubric:: Bone Collections

Bone collection assignments are also symmetrized. Collections that follow the
:ref:`naming convention <armature-editing-naming-conventions>` are mirrored.
If a collection does not exist, it is created and parented to the same collection as the original.

.. note::

   Blender does not prevent left bones from being assigned to right collections.
   During symmetrization, the resulting right bone will be assigned to the left collection.
