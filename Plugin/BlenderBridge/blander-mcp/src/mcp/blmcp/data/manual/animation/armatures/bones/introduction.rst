
************
Introduction
************

Much like in real-life skeletons, Bones are the building blocks of Armatures.
Each bone has a resting position, orientation, and length -- and all of these
can be changed while posing or animating.

You can change the way bones are displayed in the armature's
:doc:`/animation/armatures/properties/display` settings.


Classification
==============

Bones can be classified into two types depending on their
:doc:`/animation/armatures/bones/properties/deform` setting:


Deforming Bones
---------------

Bones that have the *Deform* setting enabled will drag vertices along with them.
For example, you could have a bone in a character's upper arm and another in
the lower arm, and then rotate and flex the arm by transforming these bones.


Control Bones
-------------

Bones that have the *Deform* setting disabled do not drag any vertices along.
Instead, they're typically used to control other bones.

A common use case is
:doc:`inverse kinematics </animation/armatures/posing/bone_constraints/inverse_kinematics/introduction>`:
rotating the above two arm bones manually is a bit of a pain, so instead,
you can add a control bone and configure the arm bones to automatically orient
themselves towards it. This way, you can simply position the control bone
where the character's hand should be, which is much easier.
