.. _bpy.types.VoronoiTexture:

*******
Voronoi
*******

The Voronoi texture is used to generate very convincing Metal,
especially the "Hammered" effect. Organic shaders (e.g. scales, veins in skin).

.. figure:: /images/render_materials_legacy-textures_types_voronoi_panel.png

   Voronoi Texture panels.


Options
=======

Distance Metric
   This procedural texture has seven Distance Metric options.
   These determine the algorithm to find the distance between cells of the texture. These options are:

   - Minkowski
   - Minkowski 4
   - Minkowski 1/2
   - Chebychev
   - Manhattan
   - Distance Squared
   - Actual Distance

   The *Minkowski* setting has a user definable value (the *Exponent* button)
   which determines the Minkowski exponent *e* of the distance function:

      (*x*\ :sup:`e` + *y*\ :sup:`e` + *z*\ :sup:`e`)\ :sup:`1/e`

   A value of one produces the *Manhattan* distance metric, a value less than one produces stars
   (at 0.5, it gives a *Minkowski 1/2*), and higher values produce square cells
   (at 4.0, it gives a *Minkowski 4*, at 10.0, a *Chebychev*).
   So nearly all Distance Settings are basically the same -- a variation of *Minkowski*.

   You can get irregularly-shaped rounded cells with
   the *Actual Distance* / *Distance Squared* options.

.. list-table::

   * - .. figure:: /images/render_materials_legacy-textures_types_voronoi_minkowski0-5.jpg
          :width: 200px

          Minkowski Exponent: 0.5 (Minkowski 1/2).

     - .. figure:: /images/render_materials_legacy-textures_types_voronoi_minkowski1.jpg
          :width: 200px

          Minkowski Exponent: 1 (Manhattan).

     - .. figure:: /images/render_materials_legacy-textures_types_voronoi_minkowski2.jpg
          :width: 200px

          Minkowski Exponent: 2 (Actual Distance).

   * - .. figure:: /images/render_materials_legacy-textures_types_voronoi_minkowski4.jpg
          :width: 200px

          Minkowski Exponent: 4 (Minkowski 4).

     - .. figure:: /images/render_materials_legacy-textures_types_voronoi_minkowski10.jpg
          :width: 200px

          Minkowski Exponent: 10 (Chebychev).

     - .. figure:: /images/render_materials_legacy-textures_types_voronoi_distancesquared.jpg
          :width: 200px

          Distance Squared (more contrast than Actual Distance).

Feature Weights
   These four sliders at the bottom of the Voronoi panel represent the values of the four Worley constants,
   which are used to calculate the distances between each cell in the texture based on the distance metric.
   Adjusting these values can have some interesting effects on the end result...

.. (no gallery yet) Check the Samples Gallery for some examples of these settings and what textures they produce.

Coloring
   Four settings (*Intensity*, *Position*, *Position and Outline*, and *Position, Outline, and Intensity*)
   that can use four different noise basis as methods to calculate color and intensity of the texture output.
   This gives the Voronoi texture you create with the "Worley Sliders"
   a completely different appearance and is the equivalent of the noise basis setting found on the other textures.
