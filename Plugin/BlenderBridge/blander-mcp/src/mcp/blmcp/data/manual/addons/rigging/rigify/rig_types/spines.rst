
******
Spines
******

These rigs are used to generate spine structures, including the head and tail.


.. _rigify.rigs.spines.super_spine:

spines.super_spine
==================

Will create a complete bendy and stretchy b-bones spine system based on bone numbers of
your bone chain and user defined options.

This is a composite wrapper of `spines.basic_spine`_, `spines.super_head`_ and `spines.basic_tail`_.
Note that for the tail, the direction of the bones is reversed compared to the separate rig.

Requirement: A chain of at least three connected bones (base system).

.. figure:: /images/addons_rigging_rigify_rig-types_spines-required.png

   Spine required bones.

Pivot Position (integer)
   Defines the pivot position for torso and hips.
Head (Boolean)
   When checked neck and head systems will be added to your spine rig.

   Neck Position (integer)
      Defines the bone where the neck system starts. The last bone will always be the head system.
      If neck position is the last bone of the chain, then only the head system will be created ignoring the neck.
Tail (Boolean)
   When checked tail system will be added to your spine rig.

   Tail Position (integer)
      Defines the bone where the tail system starts. The next bone will always be the hips system.
X, Y, Z (Boolean)
   When generating a tail, specifies which local axis rotations should be replicated along the chain.
Assign Tweak Layers
   If enabled, allows placing the Tweak controls in different bone collections from the IK bones.

.. figure:: /images/addons_rigging_rigify_rig-types_spines-default.png

   Spine default bones.

.. figure:: /images/addons_rigging_rigify_rig-types_spines-example.png

   Spine with tail bones.


.. _rigify.rigs.spines.basic_spine:

spines.basic_spine
==================

Defines a bendy and stretchy b-bones spine.

Pivot Position (integer)
   Defines the pivot position for torso and hips.
Assign Tweak Layers
   If enabled, allows placing the Tweak controls in different bone collections from the IK bones.
FK Controls
   Specifies whether to generate an FK control chain.
Assign FK Layers
   If enabled, allows placing the FK chain in different bone collections from the IK bones.


.. _rigify.rigs.spines.basic_tail:

spines.basic_tail
=================

Defines a bendy and stretchy b-bones tail.

X, Y, Z (Boolean)
   Specifies which local axis rotations should be replicated along the chain from each control
   bone to the following one.
Assign Tweak Layers
   If enabled, allows placing the Tweak controls in different bone collections from the IK bones.


.. _rigify.rigs.spines.super_head:

spines.super_head
=================

Defines a head rig with follow torso controls.

Assign Tweak Layers
   If enabled, allows placing the Tweak controls in different bone collections from the IK bones.
