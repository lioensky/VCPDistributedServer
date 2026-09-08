.. index:: Geometry Nodes; Roll Hair Curves

****************
Roll Hair Curves
****************

The *Roll Hair Curves* node coils or curls the tips of hair curves, rolling them inward or outward
based on configurable geometric parameters.
This node can be used to create spiral or curled hairstyles, simulate rolled fur, or stylize hair motion.

.. peertube:: 5jrgEkcWH88fmL1MEsqQN2


Inputs
======

Geometry
   The input geometry containing the hair curves to be deformed.

Factor
   Controls the overall strength of the rolling effect.
   A value of 0.0 disables the effect, while 1.0 applies the full roll.

Subdivision
   Defines how finely each curve is subdivided before deformation.
   Higher values produce smoother and more detailed rolls but increase computational cost.

Variation Level
   Introduces variation along the roll path by smoothing or distorting its shape.
   Higher values produce more natural and uneven rolls.

Roll Length
   Specifies the portion of each curve (measured from the tip) that is rolled.
   Increasing this value extends the length of the coiled section.

Roll Radius
   Determines the radius of the roll, controlling how tightly each curve is coiled.

Roll Depth
   Adds an offset along the roll axis, producing a stretched or compressed spiral shape.

Roll Taper
   Controls how the roll radius decreases toward the tip, tapering the spiral.

Retain Overall Shape
   When enabled, offsets the roll along the curve's original path to better preserve the initial flow and shape
   of the hair.

Roll Direction
   Defines the axis around which the roll is performed (e.g., X, Y, or Z).
   This determines the orientation of the curls.

Random Orientation
   Introduces randomization to the direction of the roll, helping to avoid uniform patterns
   and adding a more natural appearance.

Seed
   Sets the random seed for the orientation randomization.
   Changing the value alters the distribution of curl directions while keeping the same parameters.

Preserve Length
   When enabled, maintains the total length of each curve after deformation.
   When disabled, the curves may stretch or compress slightly as a result of rolling.


Outputs
=======

Geometry
   The resulting geometry with the rolled hair curves applied.
