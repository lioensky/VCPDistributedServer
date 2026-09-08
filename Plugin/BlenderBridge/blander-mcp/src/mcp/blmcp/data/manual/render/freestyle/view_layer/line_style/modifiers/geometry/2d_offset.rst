.. _bpy.types.LineStyleGeometryModifier_2DOffset:

*********
2D Offset
*********

The *2D Offset* modifier adds some two-dimensional offsets to the stroke backbone geometry.
It has two sets of independent options/effects:

Start, End
   These two options add the given amount of offset to the start (or end) point of the stroke,
   along the (2D) normal at those points. The effect is blended over the whole stroke, if you for example,
   set only *Start* to 50, the start of the stroke is offset 50 pixels along its normal,
   the middle of the stroke, 25 pixels along its own normal, and the end point is not moved.
X, Y
   These two options simply add a constant horizontal and/or vertical offset to the whole stroke.
