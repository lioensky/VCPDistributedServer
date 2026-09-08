.. index:: Geometry Nodes; Restore Curve Segment Length

****************************
Restore Curve Segment Length
****************************

The *Restore Curve Segment Length* node restores the original length of each curve segment
based on a reference position, typically from a pre-deformation state.
It is useful for correcting unwanted stretching or compression that occurs after
curve deformations, simulations, or procedural modifications.

.. peertube:: vCkQDxPe65KBTEHwfHUivN


Inputs
======

Curves
   The input geometry containing the curves whose segment lengths should be restored.

Selection
   A boolean field selecting which points or segments are affected.
   Unselected elements remain unchanged.

Factor
   Controls the overall influence of the length restoration.
   A value of 0.0 leaves the curves as they are, while 1.0 fully restores the original segment lengths.

Reference Position
   The reference position of the curve points before deformation.
   This is used to compute the original segment lengths that the node will attempt to restore.

Pin at Parameter
   Specifies a parameter along each curve to act as a fixed anchor point during restoration.
   The operation adjusts other points relative to this pinned location, preventing unwanted shifting.


Outputs
=======

Curves
   The resulting geometry with restored per-segment lengths, based on the provided reference positions.
