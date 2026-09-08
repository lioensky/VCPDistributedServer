.. index:: Geometry Nodes; Smooth Hair Curves

******************
Smooth Hair Curves
******************

The *Smooth Hair Curves* node relaxes and evens out the shape of hair curves by averaging
their control points over multiple iterations.
It is useful for reducing noise, smoothing deformation artifacts, or refining groomed hair shapes
after other operations such as frizz or noise deformation.

.. peertube:: 7fpUB2eRT6zjMyHRzJ2ZoJ


Inputs
======

Geometry
   The input geometry containing the hair curves to smooth.

Amount
   Controls the strength of the smoothing operation.
   Positive values smooth the curves by averaging point positions.
   Negative values exaggerate the differences between points, creating a crumpled or distorted effect.

Shape
   Defines how the smoothing influence changes along the curve length.
   A value of 0.0 applies a constant effect, while 0.5 results in a linear falloff from root to tip.

Iterations
   The number of smoothing steps applied.
   Increasing this value produces smoother results but may increase processing time.

Weight
   A per-point weighting factor that controls how much each point contributes to the smoothing.
   Values closer to 0 reduce smoothing influence at those points.

Lock Tips
   When enabled, the tips of the curves remain fixed, preventing them from moving during smoothing.

Preserve Length
   When enabled, maintains the original length of each curve during deformation.
   When disabled, smoothing may slightly shorten the curves.


Outputs
=======

Geometry
   The resulting geometry with smoothed hair curves.
