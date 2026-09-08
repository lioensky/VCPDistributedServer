.. index:: Geometry Nodes; Star
.. _bpy.types.GeometryNodeCurveStar:

*********
Star Node
*********

.. figure:: /images/node-types_GeometryNodeCurveStar.webp
   :align: right
   :alt: Star Node.

The *Star* node generates a poly spline in a star pattern by connecting alternating points of two circles.
The points on the inner circle are offset by a rotation so that they lie in between the points on the outer circle.
This offset can be changed with the twist input.


Inputs
======

Points
   Number of points on each of the circles.

Inner Radius, Outer Radius
   Radii of the two circles on which to place the control points.
   The inner radius can be larger than the outer radius.

Twist
   Angle offset of the inner circle.
   The twist value rotates the points on the circle corresponding with the inner radius
   counterclockwise by the given angle.


Outputs
=======

Curve
   Poly spline generated from the inputs.

Outer Points
   A boolean attribute field with a selection of the points on the *Outer Radius*, which is every
   other point.
