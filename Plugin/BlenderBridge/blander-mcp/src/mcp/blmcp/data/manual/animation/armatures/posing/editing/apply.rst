.. _bpy.ops.pose.armature_apply:

*****
Apply
*****

.. reference::

   :Mode:      Pose Mode
   :Menu:      :menuselection:`Pose --> Apply`
   :Shortcut:  :kbd:`Ctrl-A`

Pose as Rest Pose
   Conversely, you may define the current pose as the new rest pose
   (i.e. "apply" current transformations to the *Edit Mode*). When you do so,
   the skinned objects/geometry is **also** reset to its default,
   non-deformed state, which generally means you will have to skin it again.

Pose Selected as Rest Pose
   Same as *Pose as Rest Pose* but only applies to selected bones.

.. _bpy.ops.pose.visual_transform_apply:

Visual Transform to Pose
   Applies the position of the bone after :doc:`/animation/constraints/index`;
   allowing the constraints to be deleted and the bones will remain in their constrained positions.

.. _bpy.ops.object.assign_property_defaults:

Assign Custom Property Values as Default
   Assign the current values of custom properties as their defaults,
   for use as part of the rest pose state in NLA track mixing.
