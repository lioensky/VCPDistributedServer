.. _bpy.types.ShaderNodeVectorTransform:

*********************
Vector Transform Node
*********************

.. figure:: /images/node-types_ShaderNodeVectorTransform.webp
   :align: right
   :alt: Vector Transform node.

The *Vector Transform* node allows converting a vector, point, or normal between
world and camera and object coordinate space.


Inputs
======

Vector Input
   Standard vector input.


Properties
==========

Type
   Specifies the input/output type.

   Vector, Point, Normal.
Convert From
   Coordinate Space to convert from:

   World, Object, Camera.
Convert To
   Coordinate Space to convert to:

   World, Object, Camera.


Outputs
=======

Vector Output
   The transformed output vector.
