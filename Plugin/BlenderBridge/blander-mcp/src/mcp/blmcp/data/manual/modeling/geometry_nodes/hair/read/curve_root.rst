.. index:: Geometry Nodes; Curve Root

**********
Curve Root
**********

The *Curve Root* node outputs information related to the root point of each curve.
It is commonly used in hair grooming and procedural setups to anchor deformations,
apply transformations relative to the curve base, or isolate operations affecting
only the roots.

.. peertube:: mMFF7YU4uJ7SXtJR7BdV5Q


Inputs
======

This node has no inputs.


Outputs
=======

Root Selection
   A boolean selection that is ``true`` only for the root points of curves.
   This is useful for applying operations exclusively at the curve base.

Root Position
   The position of each curve's root point in 3D space.
   This can be used for aligning objects, sampling data from a surface, or generating root-based effects.

Root Direction
   A normalized vector representing the direction of the first segment of the curve,
   pointing away from the root toward the next control point.
   This is useful for orienting instances or determining the initial growth direction of the curve.

Root Index
   The index of the root point for each curve.
   This is typically 0 for every curve, but it can be used to identify root points
   when processing multiple curves together.
