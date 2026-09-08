.. _bpy.types.DistortedNoiseTexture:

***************
Distorted Noise
***************

*Distortion Noise* takes the option that you pick from *Noise Basis* and filters it, to create hybrid pattern.
It is often used for grunge but is also very complex and versatile.

.. figure:: /images/render_materials_legacy-textures_types_distorted-noise_panel.png

   Distorted Noise Texture panels.


Options
=======

Noise Basis
   The texture to be distorted.
Distortion
   The texture to use to distort another.
Amount
   The amount that *Distortion Noise* affects *Basis*.
Size
   The size of the noise generated.
Nabla
   Almost all procedural textures in Blender use derivatives for calculating normals for texture mapping
   (except *Blend* and *Magic*). This is important for Normal and Displacement Maps.
   The strength of the effect is controlled with the *Nabla* number field.
