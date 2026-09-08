
************
Introduction
************

Once an armature is :doc:`skinned </animation/armatures/skinning/index>` by the needed object(s),
you need a way to configure the armature into positions known as poses.
Basically, by transforming the bones, you deform or transform the skinned object(s).
However, you will notice that you cannot do this in *Edit Mode* --
remember that *Edit Mode* is used to edit the default, base, or "rest" position of an armature.
You may also notice that you cannot use *Object Mode* either, as here you can only transform whole objects.

So, armatures have a third mode dedicated to the process of posing known as *Pose Mode*.
In rest position (as edited in *Edit Mode*), each bone has its own position/rotation/scale to neutral values
(i.e. 0.0 for position and rotation, and 1.0 for scale). Hence, when you edit a bone in *Pose Mode*,
you create an offset in the transform properties, from its rest position.
This may seem quite similar if you have worked with :doc:`relative shape keys </animation/shape_keys/index>`
or :ref:`Delta Transformations <bpy.types.Object.delta>`.

Even though it might be used for completely static purposes,
posing is heavily connected with animation features and techniques.
So if you are not familiar at all with animation in Blender,
it might be a good idea to read the :doc:`animation chapter </animation/index>` first,
and then come back here.


Visualization
=============

Bone State Colors
-----------------

The color of the bones are based on their state.
There are six different color codes, ordered here by precedence
(i.e. the bone will be of the color of the bottom-most valid state):

.. hue rotation based on the bone solid.

- Gray: Default.
- Blue wire-frame: in Pose Mode.
- Green: with Constraint.
- Yellow: with :doc:`IK Solver constraint </animation/constraints/tracking/ik_solver>`.
- Orange: with Targetless Solver constraint.

.. note::

   When :ref:`bone colors <bpy.types.BoneColor>` are enabled,
   the state colors will be overridden.
