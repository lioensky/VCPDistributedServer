.. index:: Geometry Nodes; Trim Hair Curves

****************
Trim Hair Curves
****************

The *Trim Hair Curves* node shortens or scales hair curves based on a specified length or length factor.
It can be used to precisely control the overall length of hair, create varied or randomized trims,
or adjust groom density and layering.

.. peertube:: qfXRAqbL8MKus8YKMkUpE5


Inputs
======

Geometry
   The input geometry containing the hair curves to trim.

Scale Uniform
   When enabled, each curve is scaled uniformly to reach the target length.
   When disabled, trimming is applied progressively from root to tip.

Length Factor
   Multiplies the original curve length by this factor.
   A value of 1.0 keeps the hair at its original length, while 0.5 halves it.

Replace Length
   When enabled, the *Length* input fully replaces the original curve length
   instead of scaling it by the *Length Factor*.

Length
   The target length for the operation.
   Used when *Replace Length* is enabled.

Mask
   A per-curve mask that modulates the overall trimming effect.
   A value of 0.0 disables trimming for that curve, while 1.0 applies the full effect.

Random Offset
   Adds random variation to the trimmed length of each curve,
   creating more natural-looking hair variation.

Pin at Parameter
   Specifies a parameter along each curve to act as a pivot or anchor point during trimming.
   The trimming operation is performed relative to this point.

Seed
   Sets the random seed used for the random offset.
   Changing this value produces different trimming variations while maintaining the same parameters.


Outputs
=======

Geometry
   The resulting geometry with trimmed or scaled hair curves.
