.. index:: Geometry Nodes; Redistribute Curve Points

*************************
Redistribute Curve Points
*************************

The *Redistribute Curve Points* node repositions existing control points so they are
evenly spaced along each curve.
This helps improve uniformity, especially after deformations or procedural
operations that distort point spacing, ensuring consistent interpolation and smoother results.

.. peertube:: syFssvhthKJUo45B2dxw5W


Inputs
======

Curves
   The input geometry containing the curves whose control points will be redistributed.

Factor
   Controls the strength of the redistribution effect.
   A value of 0.0 leaves the curves unchanged, while 1.0 fully applies even spacing.

Feature Awareness
   Enables a simple feature-preserving algorithm that attempts to maintain
   local curve features and direction changes while redistributing points.
   This helps keep detailed areas or sharp bends more accurate.


Outputs
=======

Curves
   The resulting geometry with redistributed and evenly spaced curve control points.
