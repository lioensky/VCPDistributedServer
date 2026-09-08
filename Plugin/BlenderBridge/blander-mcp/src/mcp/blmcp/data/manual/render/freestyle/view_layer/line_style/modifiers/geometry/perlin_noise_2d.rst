.. _bpy.types.LineStyleGeometryModifier_PerlinNoise2D:

***************
Perlin Noise 2D
***************

The *Perlin Noise 2D* modifier adds one-dimensional Perlin noise to the stroke. The modifier generates
noisy displacements using 2D coordinates of stroke vertices as the input of the noise generator.

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
