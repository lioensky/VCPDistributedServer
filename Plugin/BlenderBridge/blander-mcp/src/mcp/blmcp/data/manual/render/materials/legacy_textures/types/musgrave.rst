.. _bpy.types.MusgraveTexture:

********
Musgrave
********

The musgrave texture is used to generate organic materials,
but it is very flexible. You can do nearly everything with it.

.. figure:: /images/render_materials_legacy-textures_types_musgrave_panel.png

   Musgrave Texture panels.


Options
=======

Type
   This procedural texture has five noise types on which the resulting pattern can be based
   and they are selectable from a select menu at the top of the tab. The five types are:

   - Hetero Terrain
   - Fractal Brownian Motion (fBm)
   - Hybrid Multifractal
   - Ridged Multifractal
   - Multifractal

   These noise types determine the manner in which Blender layers successive copies of the same
   pattern on top of each other at varying contrasts and scales.

Examples with Basis: Voronoi: F1, Dimension: 0.5, Lacunarity: 0.15, Octave: 2.0.

.. list-table::

   * - .. figure:: /images/render_materials_legacy-textures_types_musgrave_heteroterrain.jpg
          :width: 120px

          Hetero Terrain.

     - .. figure:: /images/render_materials_legacy-textures_types_musgrave_fbm.jpg
          :width: 120px

          Fractal Brownian Motion.

     - .. figure:: /images/render_materials_legacy-textures_types_musgrave_hybridmultifractal.jpg
          :width: 120px

          Hybrid Multifractal.

     - .. figure:: /images/render_materials_legacy-textures_types_musgrave_ridgedmultifractal.jpg
          :width: 120px

          Ridged Multifractal.

     - .. figure:: /images/render_materials_legacy-textures_types_musgrave_multifractal.jpg
          :width: 120px

          Multifractal.

.. not implemented yet?
   In addition to the five noise types, Musgrave has a noise basis setting which determines
   the algorithm that generates the noise itself.
   These are the same noise basis options found in the other procedural textures.

The main noise types have four characteristics:

Dimension
   Fractal dimension controls the contrast of a layer relative to the previous layer in the texture.
   The higher the fractal dimension, the higher the contrast between each layer,
   and thus the more detail shows in the texture.
Lacunarity
   Lacunarity controls the scaling of each layer of the Musgrave texture,
   meaning that each additional layer will have a scale that is the inverse of the value which shows on the button.
   i.e. Lacunarity = 2 --> Scale = 1/2 original.
Octaves
   Octave controls the number of times the original noise pattern is overlaid on itself and
   scaled/contrasted with the fractal dimension and lacunarity settings.
Intensity
   Light intensity. Called *Offset* for *Hetero Terrain*.

The *Hybrid Multifractal* and *Ridged Multifractal* types have these additional settings:

Offset
   Both have a "Fractal Offset" button that serves as a "sea level"
   adjustment and indicates the base height of the resulting bump map.
   Bump values below this threshold will be returned as zero.
Gain
   Setting which determines the range of values created by the function.
   The higher the number, the greater the range.
   This is a fast way to bring out additional details in a texture where extremes are normally clipped off.
