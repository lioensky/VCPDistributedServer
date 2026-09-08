.. _bpy.types.LineStyleGeometryModifier_SpatialNoise:

*************
Spatial Noise
*************

The *Spatial Noise* modifier adds some spatial noise to the stroke.
Spatial noise displacements are added in the normal direction
(i.e. the direction perpendicular to the tangent line) evaluated at each stroke vertex.

Amplitude
   How much the noise distorts the stroke.
Scale
   How wide the noise is along the stroke.
Octaves
   The level of detail of the noise.
Smooth
   When enabled, apply some smoothing over the generated noise.
Pure Random
   When disabled, the next generated random value depends on the previous one;
   otherwise they are completely independent. Disabling this setting gives a more "consistent" noise along a stroke.
