
*****
Limbs
*****

These rig types handle generation of different kind of limbs and their features, like fingers.


.. _rigify.rigs.limbs.simple_tentacle:

limbs.simple_tentacle
=====================

Will create a simple bendy and stretchy b-bones tentacle chain, which can optionally replicate local rotation
from preceding bones to the subsequent ones for use in cases like fingers.

Requirement: A chain of at least two connected bones.

Automation Axis (X, Y, Z, None)
   Enables the automation on the selected axis. Multiple axis or none can be selected holding :kbd:`Shift-LMB`.
   When enabled the subsequent control bones will copy the local rotations from the previous ones.
   The option is accessible in the controls of the final rig as a Copy Rotation constraint and
   can be disabled even after rig is generated, or at animation time.
Assign Tweak Layers
   If enabled, allows placing the Tweak controls in different bone collections from the main controls.


.. _rigify.rigs.limbs.super_finger:

limbs.super_finger
==================

Will create a bendy and stretchy finger chain with a master control bone that controls the rotation of
all joints through its scale.

Requirement: A chain of at least two connected bones.

Bend Rotation Axis (Automatic, X, Y, Z, -X, -Y, -Z)
   Defines the automatic rotation axis to be linked to the scale of the master bone.
B-Bone Segments (integer)
   Defines the number of b-bone segments each tweak control will be split into.
IK Control
   Generates a very simple IK mechanism with only one control.

   IK starts its work with the shape of the finger defined by FK controls and adjusts it
   to make the fingertip touch the IK control. It is designed as a tool to temporarily keep
   the fingertip locked to a surface it touches, rather than a fully featured posing system.

   To improve performance, the switchable parent for the IK control contains only one option beside None.
   Thus it is advised to add a 'held object' control using the :ref:`basic.raw_copy <rigify.rigs.basic.pivot>`
   rig to act as the common parent for the fingers with a fully functional parent switch.
IK Local Location
   Specifies the value of the Local Location option for IK controls, which decides if the location
   channels are aligned to the local control orientation or world.
Assign Tweak Layers
   If enabled, allows placing the Tweak controls in different bone collections from the main controls.
Assign Extra IK Layers
   If enabled, allows placing the extra IK control in different bone collections from the main controls.

.. note::

   Rotation Axis (Bend Rotation Axis in the case of `limbs.super_finger`_)
   affects the :doc:`roll </animation/armatures/bones/editing/bone_roll>` of the generated bones.
   Automatic mode recalculates the generated bones roll while
   any of the Manual modes copy the roll of the meta-rig bones.


.. _rigify.rigs.limbs.super_limb:

limbs.super_limb
================

A backwards compatibility wrapper around `limbs.arm`_, `limbs.leg`_ and `limbs.paw`_.


.. _rigify.rigs.limbs.arm:

limbs.arm
=========

Will create a fully featured bendy and stretchy arm depending on the user-defined options.

Requirement: A chain of three connected bones (upper_arm, forearm, hand).

.. figure:: /images/addons_rigging_rigify_rig-types_limbs_arm-required.png

   Arm required bones.

IK Wrist Pivot
   Generates an extra child of the hand IK control that rotates around the tail of the hand bone.

Rotation Axis (Automatic, X, Z)
   Defines the bend axis for the IK chain. FK chains will have a totally free degree of rotation on all axes.
Limb Segments (integer)
   Defines the number of additional tweak controls each limb bone will have on the final rig.
B-Bone Segments (integer)
   Defines the number of b-bone segments each tweak control will be split into.
Custom IK Pivot
   Generates an extra control for the end of the IK limb that allows rotating it around an arbitrarily placed pivot.
Assign FK Layers
   If enabled, allows placing the FK chain in different bone collections from the IK bones.
Assign Tweak Layers
   If enabled, allows placing the Tweak controls in different bone collections from the IK bones.


.. _rigify.rigs.limbs.leg:

limbs.leg
=========

Will create a fully featured bendy and stretchy leg depending on the user-defined options.

Requirement: A chain of four connected bones (thigh, shin, foot, toe) with one unconnected
child of the foot to be used as the heel pivot.

.. figure:: /images/addons_rigging_rigify_rig-types_limbs_leg-required.png

   Leg required bones.

Foot Pivot (Ankle, Toe, Ankle & Toe)
   Specifies where to put the pivot location of the main IK control, or whether to generate an additional
   pivot control at the base of the toe.

Separate IK Toe
   Specifies that two separate toe controls should be generated for IK and FK instead of sharing one bone.
   This is necessary to get fully correct IK-FK snapping in all possible poses.

Toe Tip Roll
   Generates a slider to switch the heel control to pivot on the tip rather than the base of the toe
   (for roll this obviously only applies on forward roll).

Rotation Axis (Automatic, X, Z)
   Defines the bend axis for the IK chain. FK chains will have a totally free degree of rotation on all axes.
Limb Segments (integer)
   Defines the number of additional tweak controls each limb bone will have on the final rig.
B-Bone Segments (integer)
   Defines the number of b-bone segments each tweak control will be split into.
Custom IK Pivot
   Generates an extra control for the end of the IK limb that allows rotating it around an arbitrarily placed pivot.
Assign FK Layers
   If enabled, allows placing the FK chain in different bone collections from the IK bones.
Assign Tweak Layers
   If enabled, allows placing the Tweak controls in different bone collections from the IK bones.


.. _rigify.rigs.limbs.paw:

limbs.paw
=========

Will create a fully featured bendy and stretchy paw depending on the user-defined options.

Requirement: A chain of four or five connected bones (thigh, shin, paw, *optional* digit, toe).

.. figure:: /images/addons_rigging_rigify_rig-types_limbs_paw-required.png

   Front/Rear paw required bones.

Rotation Axis (Automatic, X, Z)
   Defines the bend axis for the IK chain. FK chains will have a totally free degree of rotation on all axes.
Limb Segments (integer)
   Defines the number of additional tweak controls each limb bone will have on the final rig.
B-Bone Segments (integer)
   Defines the number of b-bone segments each tweak control will be split into.
Custom IK Pivot
   Generates an extra control for the end of the IK limb that allows rotating it around an arbitrarily placed pivot.
Assign FK Layers
   If enabled, allows placing the FK chain in different bone collections from the IK bones.
Assign Tweak Layers
   If enabled, allows placing the Tweak controls in different bone collections from the IK bones.


.. _rigify.rigs.limbs.front_paw:

limbs.front_paw
===============

Derivative of `limbs.paw`_ with extended IK suitable for use in front paws.
The additional IK limits the degree of change in the angle between shin and
paw bones (2nd and 3rd) as the main IK control moves and rotates.

For best results, the shin bone should not be parallel to either thigh or paw in rest pose,
i.e. there should be some degree of bend in all joints of the paw.

Heel IK Influence
   Influence of the extended IK. At full rotating the main IK control or digit bone would
   not affect the rotation of the paw bone, while lower values provide some blending.


.. _rigify.rigs.limbs.rear_paw:

limbs.rear_paw
==============

Derivative of `limbs.paw`_ with extended IK suitable for use in rear paws.
The additional IK tries to maintain thigh and paw bones (1st and 3rd) in a nearly parallel orientation
as the main IK control moves and rotates.

For best results, thigh and paw bones should start nearly parallel in the rest pose.


.. _rigify.rigs.limbs.super_palm:

limbs.super_palm
================

Will create a palm system based on the distance between palm bones.

Requirement: At least two bones child of the same parent.
The property has to be set on the inner palm bones (think it as index's metacarpus),
the rig control will appear on the last palm bone (think it as pinky's metacarpus).

Both Sides
   Generates controls on both sides of the palm, with influence on inner bones blended between them.

Primary Rotation Axis (X, Z)
   Defines the automatic rotation axis to be used on the palm bones.


.. _rigify.rigs.limbs.spline_tentacle:

limbs.spline_tentacle
=====================

This rig type implements a flexible tentacle with an IK system using the Spline IK constraint. The control bones
define control points of a Bezier curve, and the bone chain follows the curve.

The curve control points are sorted into three groups: start, middle and end. The middle controls are always
visible and active, while the other two types can be shown and hidden dynamically using properties; when enabled
they appear next to the corresponding permanent start/end control and can be moved from there.

Extra Start Controls
   Specifies the number of optional start controls to generate.
Middle Controls
   Specifies the number of middle controls to generate.
Extra End Controls
   Specifies the number of optional end controls to generate.
Tip Control:
   Specifies how the curve stretching and the final control bone work:

   Stretch To Fit
      Stretches the whole bone chain to fit the length of the curve defined by the controls.

      An end twist control is generated to control the twist along the chain.
   Direct Tip Control
      Generates an IK end control, which directly controls the final bone of the chain similar to how
      regular IK works for limbs, as well as controlling the end of the bezier curve. The middle bones of
      the chain stretch to follow the curve and cover the gap.

      The rig automatically deduces twist of up to 180 degrees based on the orientation of the end control.
      Higher amounts of twist have to be dialed in through an End Twist Estimate slider to avoid flipping.
   Manual Squash & Stretch
      This mode allows full manual control over the chain scaling, while the chain covers as much of the curve
      as it can given its current length.

      The start control of the chain manages its uniform squash & stretch scale, while the end twist control
      manages both the twist of the chain, as well as its scale at the tip (blended gradually along the length).
Radius Scaling
   Allows scaling the controls to control the thickness of the chain through the curve.
Maximum Radius
   Specifies the maximum scale allowed by the Radius Scaling feature.
FK Controls
   Generates an FK control chain and IK-FK snapping.
Assign FK Layers
   If enabled, allows placing the FK chain in different bone collections from the IK bones.
