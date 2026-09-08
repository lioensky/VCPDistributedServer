.. _bpy.types.CloudsTexture:

******
Clouds
******

Clouds represent Perlin noise. In addition, each noise-based Blender texture
(with the exception of Voronoi and simple noise) has a *Noise Basis* setting that allows
the user to select which algorithm is used to generate the texture. This is often used for
Clouds, Fire, Smoke. Well-suited to be used as a Bump map, giving an overall irregularity to the material.

.. figure:: /images/render_materials_legacy-textures_types_clouds_panel.png

   Clouds Texture panels.


Options
=======

Type
   *Soft* or *Hard*, changes contrast and sharpness.
Color
   :Grayscale: The standard noise, gives a floating-point intensity value.
   :Color: The noise gives an RGB value.
Size
   The dimension of the Noise table.
Depth
   The depth of the *Clouds* calculation.
   A higher number results in a long calculation time, but also in finer details.
Nabla 
   Size of the derivative offset used for calculating surface normals.
   Smaller values give more precision, larger values are smoother/faster.
   This is mostly relevant when the texture is used in displacement or bump channels.
