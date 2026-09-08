.. index:: Geometry Nodes; Frizz Hair Curves

*****************
Frizz Hair Curves
*****************

The *Frizz Hair Curves* node introduces small random displacements along hair curves to create
a frizzy or irregular look.
It is commonly used to add natural variation to grooms by breaking up overly smooth or uniform
strand shapes.

.. peertube:: jdiMkR9aQnCm1QXc71Fz5h


Inputs
======

Geometry
   The input geometry containing the hair curves to modify.

Cumulative Offset
   When enabled, each point's offset depends on the displacement of previous points along the curve.
   This results in more natural and continuous bending.

Factor
   Controls the overall blending strength of the effect.
   A value of 0.0 applies no frizz, while 1.0 applies the full random displacement.

Distance
   Scales the magnitude of the random displacement applied to the curve points.

Shape
   Determines how the displacement strength changes along the length of each curve.
   A value of 0.0 applies a constant effect, while 0.5 results in a linear falloff from root to tip.

Seed
   Defines the random seed used to generate unique displacement patterns.
   Changing this value alters the random variation between curves.

Preserve Length
   When enabled, maintains the original length of each curve during deformation.
   When disabled, curves may stretch or shrink slightly as a result of the frizz.


Outputs
=======

Geometry
   The resulting geometry with frizzed hair curves.

Offset Vector
   The vector field describing the per-point displacement applied to each curve.
