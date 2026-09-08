.. _bpy.ops.pose.ik_add:

**************
Add IK to Bone
**************

.. reference::

   :Mode:      Pose Mode
   :Menu:      :menuselection:`Pose --> Inverse Kinematics --> Add IK to Bone`
   :Shortcut:  :kbd:`Shift-I`

Adds an :doc:`/animation/constraints/tracking/ik_solver` to the active bone.
The operator shows a menu for selecting the target of the constraint:

Without Target
   Creates the constraint without a *Target*. Only available when no other bone
   or object is selected.
Target New Empty Object
   Creates an :doc:`Empty </modeling/empties>` at the bone's tail and uses it
   as the constraint target. Only available when no other bone or object is
   selected.
Target Selected Bone
   Sets the target to the selected bone (that's not active).
Target Selected Object
   Sets the target to the selected object (that's not active). Either select
   the object before selecting the Armature and entering Pose Mode,
   or select it in the :doc:`Outliner </editors/outliner/introduction>` when
   already in Pose Mode.


.. _bpy.ops.pose.ik_clear:

*********
Remove IK
*********

.. reference::

   :Mode:      Pose Mode
   :Menu:      :menuselection:`Pose --> Inverse Kinematics --> Remove IK`
   :Shortcut:  :kbd:`Ctrl-Alt-I`

Removes the :doc:`/animation/constraints/tracking/ik_solver` from the selected bones.
