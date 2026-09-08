.. index:: Geometry Nodes; Curve Tip

*********
Curve Tip
*********

The *Curve Tip* node outputs information about the tip (end) point of each curve.
It is commonly used in hair grooming, deformation, and simulation setups to control
operations at the ends of curves, such as shaping, alignment, or applying tip-based effects.

.. peertube:: pcyUMH2SZ2DtwuDVF1bQio


Inputs
======

This node has no inputs.


Outputs
=======

Tip Selection
   A boolean selection that is true only for the tip points of curves.
   This can be used to isolate operations that affect only the curve ends.

Tip Position
   The position of each curve's tip point in 3D space.
   Useful for determining the end location of curves, placing instances, or measuring curve length.

Tip Direction
   A normalized vector representing the direction of the final segment of each curve,
   pointing toward the tip.
   This can be used for orienting instances or controlling effects based on curve direction.

Tip Index
   The index of the tip point for each curve.
   This corresponds to the last point in the curve's point list.
