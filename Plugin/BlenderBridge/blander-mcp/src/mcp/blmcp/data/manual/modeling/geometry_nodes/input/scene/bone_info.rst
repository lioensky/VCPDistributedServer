.. index:: Geometry Nodes; Bone Info
.. _bpy.types.GeometryNodeBoneInfo:

****************
Bone Info Node
****************

.. figure:: /images/node-types_GeometryNodeBoneInfo.webp
   :align: right
   :alt: Bone Info node.

The *Bone Info* node gets bone transform properties from an armature object. This can be used to control geometry node
behavior with a rig or implement armature deformation using vertex group attributes.

.. note::

   A dependency cycle can occur if the *Bone Info* node uses one bone and another bone in the same armature in turn
   depends on the modified object, for example using a :doc:`/animation/constraints/relationship/geometry_attribute`.
   Inside an armature each bone can be referenced individually, but the geometry modifier node can only add a
   dependency on the entire armature. This is because the bone name is a generic string that does not generally point
   to a single bone.


Inputs
======

Armature
   Armature object to get bone poses from.

Bone Name
   Name of the bone to get the pose transforms from.


Properties
==========

Transform Space
   The space in which pose transforms are defined.

   :Original:
      Output the pose and rest pose relative to the armature object origin.
   :Relative:
      Bring the pose and rest pose into the modified object's space.


Outputs
=======

Pose
   Evaluated final transform of the bone.
Local Pose
   Difference between the pose and rest pose, relative to the parent bone. Not affected by the transform space.
Transform Pose
   Matrix representing the bone's location, rotation, and scale properties. Not affected by the transform space.
Rest Pose
   Original transform of the bone as defined in edit mode.
Rest Length
   Original length of the bone.