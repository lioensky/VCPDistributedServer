.. index:: Geometry Nodes; Rotate Hair Curves

******************
Rotate Hair Curves
******************

The *Rotate Hair Curves* node twists or rotates each hair curve around a chosen axis,
allowing for effects such as gentle twisting, spiral motion, or directional flow in grooms.
It can be used to add subtle styling variation or create complex twisting deformations.

.. peertube:: dLEJ6ZgP1t9ksxfB3zHrsj


Inputs
======

Geometry
   The input geometry containing the hair curves to be rotated.

Factor
   Controls the overall strength of the rotation.
   A value of 0.0 disables the effect, while 1.0 applies the full rotation angle.

Axis
   Defines the axis around which each curve is rotated.
   By default, the tangent direction at the root of each curve is used.

Angle
   Specifies the amount of rotation applied around the chosen axis, in radians.
   Positive values rotate in one direction, negative values in the opposite.

Random Offset
   Adds a random offset to the rotation angle for each curve, introducing natural variation
   and avoiding a uniform appearance.

Lock Ends
   When enabled, constrains the deformation to preserve the relative position between
   the root and tip of each curve.
   This helps maintain the overall direction and placement of the hair strands.

Seed
   Sets the random seed used for generating the random offsets.
   Changing this value produces different randomized rotation patterns while keeping the same parameters.


Outputs
=======

Geometry
   The resulting geometry with rotated hair curves.
