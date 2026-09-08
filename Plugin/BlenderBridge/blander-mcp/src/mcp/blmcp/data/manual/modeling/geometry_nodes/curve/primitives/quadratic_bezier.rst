.. index:: Geometry Nodes; Quadratic Bézier
.. _bpy.types.GeometryNodeCurveQuadraticBezier:

*********************
Quadratic Bézier Node
*********************

.. figure:: /images/node-types_GeometryNodeCurveQuadraticBezier.webp
   :align: right
   :alt: Quadratic Bézier Node.

The *Quadratic Bézier* node generates a poly spline curve from the given control points.
The generated shape is a parabola.


Inputs
======

Resolution
   The number of edges on the curve.

Start, Middle, End
   Positions of the three control points.
   The generated curve passes through the two end points, and is tangent to the lines between
   the middle point and the two end points.


Outputs
=======

Curve
   Poly spline generated from the inputs.
