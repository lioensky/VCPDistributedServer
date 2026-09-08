.. _bpy.types.LineStyleGeometryModifier_PerlinNoise1D:

***************
Perlin Noise 1D
***************

The *Perlin Noise 1D* modifier adds one-dimensional Perlin noise to the stroke.
The curvilinear abscissa (value between 0 and 1 determined by a point's position
relative to the first and last point of a stroke) is used as the input to
the noise function to generate noisy displacements.

This means that this modifier will give an identical result for two strokes
with the same length and sampling interval.

Frequency
   How dense the noise is (kind of a scale factor along the stroke).
Amplitude
   How much the noise distorts the stroke in the *Angle* direction.
Seed
   The seed of the random generator (the same seed over a stroke will always give the same result).
Octaves
   The "level of detail" of the noise.
Angle
   In which direction the noise is applied (0.0 is fully horizontal).
