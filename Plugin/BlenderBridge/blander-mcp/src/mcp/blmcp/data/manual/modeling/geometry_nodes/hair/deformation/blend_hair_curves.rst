.. index:: Geometry Nodes; Blend Hair Curves

*****************
Blend Hair Curves
*****************

The *Blend Hair Curves* node smooths or blends the shape of hair curves by averaging
their positions with nearby curves within a specified radius.
This can be used to reduce noise, create more coherent flow in the groom, or
harmonize transitions between clumps of hair.

.. peertube:: kegHEYG8URADfPpBZ4jRUo


Inputs
======

Geometry
   The input geometry containing the hair curves to be blended.

Factor
   Controls the overall strength of the blending effect.
   A value of 0.0 applies no blending, while 1.0 fully averages the selected curves.

Blend Radius
   Defines the distance used to find neighboring curves that influence the blend.

Blend Neighbors
   Limits the number of neighboring curves considered during the blending process.
   Increasing this value can result in smoother results but slower performance.

Preserve Length
   When enabled, the length of each curve is maintained during blending.
   When disabled, curves may stretch or compress as a result of the averaging.


Outputs
=======

Geometry
   The modified geometry with blended hair curves.
