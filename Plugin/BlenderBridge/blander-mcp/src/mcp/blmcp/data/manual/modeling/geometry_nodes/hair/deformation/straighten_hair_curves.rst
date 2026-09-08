.. index:: Geometry Nodes; Straighten Hair Curves

**********************
Straighten Hair Curves
**********************

The *Straighten Hair Curves* node aligns the points of each hair curve along a straight line
between its root and tip.
This can be used to relax curly or noisy hair, create stylized grooms, or prepare curves
for further deformation or simulation.

.. peertube:: grmo32udHpGWz2TwdEp9GD


Inputs
======

Geometry
   The input geometry containing the hair curves to straighten.

Amount
   Controls how much each curve is straightened.
   A value of 0.0 leaves the hair unchanged, while 1.0 fully aligns points along a straight line.
   Negative values exaggerate curve irregularities, causing crumpling or distortion.

Shape
   Defines how the straightening influence changes along the length of each curve.
   A value of 0.0 applies a constant effect, while 0.5 produces a linear falloff from root to tip.

Preserve Length
   When enabled, keeps the original length of each curve during deformation.
   When disabled, curves may shorten or stretch slightly as they are straightened.


Outputs
=======

Geometry
   The resulting geometry with straightened hair curves.
