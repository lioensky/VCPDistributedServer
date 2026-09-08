.. index:: Geometry Nodes; Hair Curves Noise

*****************
Hair Curves Noise
*****************

The *Hair Curves Noise* node adds procedural noise-based deformation to hair curves,
creating natural-looking randomness or turbulence.
This can be used to simulate effects such as wind disturbance, curly or wavy hair,
or subtle irregularities in a groom.

.. peertube:: eWCeePgTsA75Q8QhKQ6Qh9


Inputs
======

Geometry
   The input geometry containing the hair curves to deform.

Cumulative Offset
   When enabled, each point's offset is influenced by the displacement of the preceding points
   along the curve.
   This produces smoother and more continuous bending rather than independent point motion.

Factor
   Controls the overall intensity of the noise deformation.
   A value of 0.0 disables the effect, while 1.0 applies the full displacement.

Distance
   Multiplies the amplitude of the noise displacement.
   Higher values increase how far the hair is moved from its original shape.

Shape
   Defines the variation of the effect along the curve length.
   A value of 0.0 applies a constant deformation, while 0.5 produces a linear falloff from root to tip.

Scale
   Adjusts the scale of the noise texture based on the root position of each curve.
   Smaller values create larger, smoother waves, while higher values produce finer detail.

Scale along Curve
   Defines the frequency of the noise along each individual curve.
   Higher values create tighter, more frequent variations along the hair strands.

Offset per Curve
   Adds a random offset to the noise pattern for each curve.
   This ensures that each hair receives a unique noise variation.

Seed
   Sets the random seed used to initialize the noise pattern.
   Changing this value produces different random results while maintaining the same parameters.

Preserve Length
   When enabled, maintains the original length of each curve segment during deformation.
   When disabled, noise deformation may stretch or compress the curve slightly.


Outputs
=======

Geometry
   The resulting geometry with the noise deformation applied to the hair curves.

Offset Vector
   The vector field indicating the displacement applied to each point along the curves.
