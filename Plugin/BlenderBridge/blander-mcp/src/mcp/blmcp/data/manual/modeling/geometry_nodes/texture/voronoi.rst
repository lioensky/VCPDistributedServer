.. index:: Geometry Nodes; Voronoi Texture

********************
Voronoi Texture Node
********************

.. note::

   This node is ported from shader nodes. The manual and images are
   referencing the shader version of the node.
   This node accepts field inputs and outputs.
   When not connected the Vector input has an implicit ``position`` attribute value.

.. figure:: /images/node-types_ShaderNodeTexVoronoi.webp
   :align: right
   :alt: Voronoi Texture Node.

The *Voronoi Texture* node evaluates a `Worley Noise <https://en.wikipedia.org/wiki/Worley_noise>`__ at
the input texture coordinates.


Inputs
======

The inputs are dynamic, they become available if needed depending on the node properties.

Vector
   Texture coordinate to evaluate the noise at;
   defaults to *Generated* texture coordinates if the socket is left unconnected.
W
   Texture coordinate to evaluate the noise at.
Scale
   Scale of the noise.
Detail
   Number of noise octaves.
   The fractional part of the input is multiplied by the magnitude of the highest octave.
   Higher number of octaves corresponds to a higher evaluation time.
Roughness
   Blend between a smoother noise pattern, and rougher with sharper peaks.
Lacunarity
   The difference between the scale of each two consecutive octaves.
   Larger values corresponds to larger scale for higher octaves.
Smoothness
   The smoothness of the noise.

   .. list-table::

      * - .. figure:: /images/render_shader-nodes_textures_voronoi_smoothness-distance-zero.png

             Smoothness: 0.0.

        - .. figure:: /images/render_shader-nodes_textures_voronoi_smoothness-distance-quarter.png

             Smoothness: 0.25.

        - .. figure:: /images/render_shader-nodes_textures_voronoi_smoothness-distance-half.png

             Smoothness: 0.5.

        - .. figure:: /images/render_shader-nodes_textures_voronoi_smoothness-distance-one.png

             Smoothness: 1.0.

      * - .. figure:: /images/render_shader-nodes_textures_voronoi_smoothness-color-zero.png

             Smoothness: 0.0.

        - .. figure:: /images/render_shader-nodes_textures_voronoi_smoothness-color-quarter.png

             Smoothness: 0.25.

        - .. figure:: /images/render_shader-nodes_textures_voronoi_smoothness-color-half.png

             Smoothness: 0.5.

        - .. figure:: /images/render_shader-nodes_textures_voronoi_smoothness-color-one.png

             Smoothness: 1.0.

Exponent
   Exponent of the Minkowski distance metric.

   .. list-table::

      * - .. figure:: /images/render_shader-nodes_textures_voronoi_minkowski-half.png

             Exponent: 0.5.

        - .. figure:: /images/render_shader-nodes_textures_voronoi_minkowski-one.png

             Exponent: 1.0.

        - .. figure:: /images/render_shader-nodes_textures_voronoi_minkowski-two.png

             Exponent: 2.0.

        - .. figure:: /images/render_shader-nodes_textures_voronoi_minkowski-32.png

             Exponent: 32.0.

Randomness
   The randomness of the noise.

   .. list-table::

      * - .. figure:: /images/render_shader-nodes_textures_voronoi_randomness-one.png

             Randomness: 1.0.

        - .. figure:: /images/render_shader-nodes_textures_voronoi_randomness-half.png

             Randomness: 0.5.

        - .. figure:: /images/render_shader-nodes_textures_voronoi_randomness-quarter.png

             Randomness: 0.25.

        - .. figure:: /images/render_shader-nodes_textures_voronoi_randomness-zero.png

             Randomness: 0.0.


Properties
==========

Dimensions
   The dimensions of the space to evaluate the noise in.

   :1D: Evaluate the noise in 1D space at the input W.
   :2D: Evaluate the noise in 2D space at the input Vector. The Z component is ignored.
   :3D: Evaluate the noise in 3D space at the input Vector.
   :4D: Evaluate the noise in 4D space at the input Vector and the input W as the fourth dimension.

   Higher dimensions corresponds to higher render time,
   so lower dimensions should be used unless higher dimensions are necessary.

Feature
   The Voronoi feature that the node will compute.

   :F1:
      The distance to the closest feature point as well as its position and color.

      .. list-table::

         * - .. figure:: /images/render_shader-nodes_textures_voronoi_smoothness-distance-zero.png

                Distance.

           - .. figure:: /images/render_shader-nodes_textures_voronoi_smoothness-color-zero.png

                Color.

           - .. figure:: /images/render_shader-nodes_textures_voronoi_f1-position.png

                Position.

   :F2:
      The distance to the second closest feature point as well as its position and color.

      .. list-table::

         * - .. figure:: /images/render_shader-nodes_textures_voronoi_f2-distance.png

                Distance.

           - .. figure:: /images/render_shader-nodes_textures_voronoi_f2-color.png

                Color.

           - .. figure:: /images/render_shader-nodes_textures_voronoi_f2-position.png

                Position.

   :Smooth F1:
      A smooth version of F1.

      .. list-table::

         * - .. figure:: /images/render_shader-nodes_textures_voronoi_smoothness-distance-one.png

                Distance.

           - .. figure:: /images/render_shader-nodes_textures_voronoi_smoothness-color-one.png

                Color.

           - .. figure:: /images/render_shader-nodes_textures_voronoi_smooth-f1-position.png

                Position.

   :Distance to Edge:
      The distance to the edges of the Voronoi cells.

      .. list-table::

         * - .. figure:: /images/render_shader-nodes_textures_voronoi_distance-to-edge.png

                Distance.

           - .. figure:: /images/render_shader-nodes_textures_voronoi_distance-to-edge-less-than.png

                Distance smaller than 0.05.

   :N-Sphere Radius:
      The radius of the n-sphere inscribed in the Voronoi cells.
      In other words, it is half the distance between the closest feature point and the feature point closest to it.

      .. list-table::

         * - .. figure:: /images/render_shader-nodes_textures_voronoi_n-sphere-radius.png

                The n-sphere radius can be used to create tightly packed n-spheres.

           - .. figure:: /images/render_shader-nodes_textures_voronoi_n-sphere-radius-nodetree.png

                Node tree for the shader to the left.

Distance Metric
   The distance metric used to compute the texture.

   :Euclidean:
      Use the `Euclidean distance metric <https://en.wikipedia.org/wiki/Euclidean_distance>`__.
   :Manhattan:
      Use the `Manhattan distance metric <https://en.wikipedia.org/wiki/Taxicab_geometry>`__.
   :Chebychev:
      Use the `Chebychev distance metric <https://en.wikipedia.org/wiki/Chebyshev_distance>`__.
   :Minkowski:
      Use the `Minkowski distance metric <https://en.wikipedia.org/wiki/Minkowski_distance>`__.
      The Minkowski distance is a generalization of the aforementioned metrics with an *Exponent* as a parameter.
      Minkowski with an exponent of one is equivalent to the *Manhattan* distance metric.
      Minkowski with an exponent of two is equivalent to the *Euclidean* distance metric.
      Minkowski with an infinite exponent is equivalent to the *Chebychev* distance metric.

   .. list-table::

      * - .. figure:: /images/render_shader-nodes_textures_voronoi_minkowski-half.png

             Minkowski Exponent: 0.5 (Minkowski 1/2).

        - .. figure:: /images/render_shader-nodes_textures_voronoi_minkowski-one.png

             Minkowski Exponent: 1.0 (Manhattan).

        - .. figure:: /images/render_shader-nodes_textures_voronoi_minkowski-two.png

             Minkowski Exponent: 2.0 (Euclidean).

        - .. figure:: /images/render_shader-nodes_textures_voronoi_minkowski-32.png

             Minkowski Exponent: 32.0 (approximation of Chebychev).

Normalize
   If enabled, ensures that the output values stay in the range 0.0 to 1.0.
   In rare cases, the output value may be outside that range when *Feature* is *F2*.


Outputs
=======

Distance
   Distance.
Color
   Cell color. The color is arbitrary.
Position
   Position of feature point.
W
   Position of feature point.
Radius
   N-Sphere radius.


Notes
=====

In some configurations of the node, especially for low values of *Randomness*,
rendering artifacts may occur. This happens due to the same reasons described
in the :ref:`Notes section <shader-white-noise-notes>` in the White Noise Texture page
and can be fixed in a similar manner as described there.


Examples
========

.. figure:: /images/render_shader-nodes_textures_voronoi_example-beveled-cells.png

   The difference between *F1* and *Smooth F1* can be used to create beveled Voronoi cells.

.. figure:: /images/render_shader-nodes_textures_voronoi_example-hammered-metal.jpg

   Creating a hammered metal shader using the *Voronoi Texture* node.
