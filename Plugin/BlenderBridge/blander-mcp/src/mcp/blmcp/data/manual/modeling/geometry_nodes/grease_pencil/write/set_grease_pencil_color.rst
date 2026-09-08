.. index:: Geometry Nodes; Set Grease Pencil Color
.. _bpy.types.GeometryNodeSetGreasePencilColor:

****************************
Set Grease Pencil Color Node
****************************

.. figure:: /images/node-types_GeometryNodeSetGreasePencilColor.webp
   :align: right
   :alt: Set Grease Pencil Color Node.

The *Set Grease Pencil Color* node sets the color and opacity attributes
of strokes and fills on Grease Pencil geometry.


Inputs
======

Grease Pencil
   The input Grease Pencil geometry.

Selection
   A boolean field to determine which elements to affect.
   Elements with a value of true will be modified.

Color
   The new color to apply.

Opacity
   The opacity value to apply.


Properties
==========

Mode
   Determines which component of the stroke is affected:

   :Stroke: Apply the color and opacity to stroke points.
   :Fill: Apply the color and opacity to stroke fills.


Outputs
=======

Grease Pencil
   The modified Grease Pencil geometry.
