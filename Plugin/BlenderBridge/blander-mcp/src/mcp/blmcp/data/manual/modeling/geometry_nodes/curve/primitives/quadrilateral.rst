.. index:: Geometry Nodes; Quadrilateral
.. _bpy.types.GeometryNodeCurvePrimitiveQuadrilateral:

******************
Quadrilateral Node
******************

.. figure:: /images/node-types_GeometryNodeCurvePrimitiveQuadrilateral.webp
   :alt: Quadrilateral Node.

The *Quadrilateral* node generates a polygon with four points, with different modes.


Inputs
======

Width / Bottom Width / Top Width
   The X axis size of the shape.

Height
   The Y axis size of the shape.

Bottom Height / Top Height
   The distance between the bottom or top point and the X axis, in *Kite* mode.

Offset
   In *Parallelogram* mode, the relative X difference between the top and bottom edge.
   In *Trapezoid* mode, the amount to move the top edge in the positive X axis.

Point 1 - 4
   Input vectors for the *Points* mode.


Properties
==========

Mode
   :Rectangle:
      Generate a rectangle-shaped curve with a width and a height.
   :Parallelogram:
      Generate a rectangle with an offset for the different X values of the top and bottom edges.
   :Trapezoid:
      Generate a trapezoid-shaped curve with a height, a width for the top and bottom, and an offset.
   :Kite:
      Generate a kite shape with a width, and the top and bottom points distance from the X axis.
   :Points:
      Generate a four point cyclic poly spline by inputting the position vectors directly.


Outputs
=======

Curve
   Poly spline generated from the inputs.
