
************
Introduction
************

.. figure:: /images/render_materials_legacy-textures_introduction_menu.png
   :width: 230px

   The Texture Type list in the Texture panel of the Texture buttons.

Procedural textures are textures that are defined mathematically.
They are generally relatively simple to use,
because they do not need to be mapped in a special way.
This does not mean that procedural textures cannot become very complex.

These types of textures are 'real' 3D. By that we mean that they fit together perfectly at
the edges and continue to look like what they are meant to look like even when they are cut;
as if a block of wood had really been cut in two.
Procedural textures are not filtered or anti-aliased. This is hardly ever a problem:
the user can easily keep the specified frequencies within acceptable limits.


Common Options
==============

Noise Basis
-----------

Each noise-based Blender texture (except Voronoi and Simple Noise) has
a *Noise Basis* setting that allows the user to select
which algorithm is used to generate the texture.
This list includes the original Blender noise algorithm.
The *Noise Basis* settings makes the procedural textures extremely flexible (especially *Musgrave*).

The *Noise Basis* governs the structural appearance of the texture:

.. list-table::

   * - .. figure:: /images/render_materials_legacy-textures_introduction_noise-basis-blender-original.jpg
          :width: 160px

          Blender Original.

     - .. figure:: /images/render_materials_legacy-textures_introduction_noise-basis-voronoi-f1.jpg
          :width: 160px

          Voronoi F1.

     - .. figure:: /images/render_materials_legacy-textures_introduction_noise-basis-voronoi-f2-f1.jpg
          :width: 160px

          Voronoi F2-F1.

   * - .. figure:: /images/render_materials_legacy-textures_introduction_noise-basis-original-perlin.jpg
          :width: 160px

          Original Perlin.

     - .. figure:: /images/render_materials_legacy-textures_introduction_noise-basis-voronoi-f2.jpg
          :width: 160px

          Voronoi F2.

     - .. figure:: /images/render_materials_legacy-textures_introduction_noise-basis-voronoi-crackle.jpg
          :width: 160px

          Voronoi Crackle.

   * - .. figure:: /images/render_materials_legacy-textures_introduction_noise-basis-improved-perlin.jpg
          :width: 160px

          Improved Perlin.

     - .. figure:: /images/render_materials_legacy-textures_introduction_noise-basis-voronoi-f3.jpg
          :width: 160px

          Voronoi F3.

     - .. figure:: /images/render_materials_legacy-textures_introduction_noise-basis-cell-noise.jpg
          :width: 160px

          Cell Noise.

   * - .. figure:: /images/render_materials_legacy-textures_introduction_noise-basis-voronoi-f4.jpg
          :width: 160px

          Voronoi F4.

     - ..

     - ..

There are two more possible settings for *Noise Basis*, which are relatively similar to *Blender Original*:
Improved Perlin and Original Perlin.


Nabla
-----

Almost all procedural textures in Blender use derivatives for calculating normals for texture mapping
(except *Blend* and *Magic*). This is important for Normal and Displacement Maps.
The strength of the effect is controlled with the *Nabla* number field.


Hints
=====

Procedural textures can either produce colored textures, intensity only textures,
textures with alpha values and normal textures.
If intensity only ones are used the result is a black-and-white texture,
which can be greatly enhanced by the use of ramps.
If on the other hand you use ramps and need an intensity value,
you have to switch on *No RGB* in the *Mapping* panel.
