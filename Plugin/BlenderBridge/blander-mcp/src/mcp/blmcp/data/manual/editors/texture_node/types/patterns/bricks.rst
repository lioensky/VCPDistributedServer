.. _bpy.types.TextureNodeBricks:

***********
Bricks Node
***********

.. figure:: /images/node-types_TextureNodeBricks.webp
   :align: right
   :alt: Bricks node.

The Bricks node creates a brick-like pattern.


Inputs
======

Bricks 1, Bricks 2
   Sets the color range of the bricks. Brick colors are chosen randomly between these two colors.
Mortar
   Sets the mortar color, in between the bricks.
Thickness
   Sets the thickness of the mortar.
Bias
   The bias of randomly chosen colors,
   between (-1 to 1). -1 Makes all bricks Color 1, and a value of 1 makes them all Color 2.
Brick Width
   Sets the horizontal size of all the bricks.
Row Height
   Sets the vertical size of all the bricks.


Properties
==========

Offset
   The relative offset of the next row of bricks.
Frequency
   Offset every N rows. The brick pattern offset repeats every N rows.
Squash
   Scales the bricks in every N rows by this amount.
Frequency
   Squash every N rows.


Outputs
=======

Color
   Standard color output.
