
************
Introduction
************

The *Armature* tab in Properties contains various panels gathering the armature settings.

.. figure:: /images/animation_armatures_properties_introduction_properties-editor.png

   The Armature tab in the Properties.

Pose
====

.. reference::

   :Mode:      All Modes
   :Panel:     :menuselection:`Armature --> Pose`

.. _bpy.types.Armature.pose_position:

Pose Position
   A radio button to switch between Pose Position and Rest Position.

   In *Edit Mode*, you always see armatures in their rest position,
   in *Object Mode* and *Pose Mode*, by default, you see them in *Pose Position*
   (i.e. as it was transformed in the *Pose Mode*).
   If you want to see it in the rest position in all modes, select *Rest Position*.


Bone Collections
================

See :doc:`Bone Collections </animation/armatures/properties/bone_collections>`.


Motion Paths
============

.. reference::

   :Mode:      All Modes
   :Panel:     :menuselection:`Armature --> Motion Paths`

In the :doc:`Motion Paths </animation/motion_paths>` panel you can enable visualization
of the motion path your skeleton leaves when animated.


Inverse Kinematics
==================

.. reference::

   :Mode:      All Modes
   :Panel:     :menuselection:`Armature --> Inverse Kinematics`

.. figure:: /images/animation_armatures_posing_bone-constraints_inverse-kinematics_introduction_panel.png

   The Inverse Kinematics panel.

Defines the type of :doc:`IK solver </animation/armatures/posing/bone_constraints/inverse_kinematics/introduction>`
used in your animation.


Custom Properties
=================

.. reference::

   :Mode:      All Modes
   :Panel:     :menuselection:`Armature --> Custom Properties`

See the :ref:`Custom Properties <files-data_blocks-custom-properties>` page for more information.
