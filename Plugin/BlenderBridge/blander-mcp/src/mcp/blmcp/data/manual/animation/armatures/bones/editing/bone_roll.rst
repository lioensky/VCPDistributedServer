.. _armature-bone-roll:

*********
Bone Roll
*********

The bone roll is a part of a bone's :term:`rest pose` defining its default rotation around the bone's length. 
You can control the bone roll in *Edit Mode*.

.. _bpy.ops.armature.calculate_roll:

Recalculate Roll
================

.. reference::

   :Mode:      Edit Mode
   :Menu:      :menuselection:`Armature --> Bone Roll --> Recalculate Roll`
   :Shortcut:  :kbd:`Shift-N`

Automatically align the roll of all selected bones to various points of reference.

Axis Orientation
   Local (X, Z, -X, -Z) Tangent
      Align the roll of the selected bones relative to the axis defined by the bones and their parent.
      If a bone has no parent, use the first child as a point of reference instead, 
      even if that child is not connected and another one is.
      For bones with no parent and no children, this option does nothing.

   Global (X, Y, Z, -X, -Y, -Z) Axis
      Align the roll of the selected bones such that their Z axis points towards the chosen global axis.
   Active Bone
      Align the roll of the selected bones such that their Z axis points where the active bone's Z axis is currently
      pointing.
   View Axis
      Align the roll of the selected bones such that their Z axis points at the viewport's forward/backward axis,
      basically the user's eyes.
   Cursor
      Align the roll of the selected bones such that their Z axis points at the 3D cursor.
Flip Axis
   Change the result by 180°.
Shortest Rotation
   Change the result by 180° when needed in order to force the absolute roll value below 90°.
   For example, for an initial result of 160°, this option will instead flip that to -20°.

.. _tool-bone-roll:

Set Roll
========

.. reference::

   :Mode:      Edit Mode
   :Menu:      :menuselection:`Armature --> Bone Roll --> Set Roll`
   :Shortcut:  :kbd:`Ctrl-R`

Tweak the roll of all selected bones.

.. _bpy.ops.armature.roll_clear:

Clear Roll
==========

.. reference::

   :Mode:      Edit Mode
   :Menu:      :menuselection:`Armature --> Bone Roll --> Clear Roll`
   :Shortcut:  :kbd:`Alt-R`

Set the roll of all selected bones to 0°.