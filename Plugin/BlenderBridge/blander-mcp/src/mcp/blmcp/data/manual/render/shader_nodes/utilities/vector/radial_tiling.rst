.. _bpy.types.ShaderNodeRadialTiling:

.. Editor's Note: This page gets copied into:
.. - :doc:`<//compositing/types/utilities/vector/radial_tiling>`
.. - :doc:`</modeling/geometry_nodes/utilities/vector/radial_tiling>`
.. --- copy below this line ---

******************
Radial Tiling Node
******************

.. figure:: /images/node-types_ShaderNodeRadialTiling.png
   :width: 240px
   :align: right
   :alt: Radial Tiling Node.

The *Radial Tiling Node* provides the ability to divide a 2D cartesian input coordinate system
into as many radial segments as specified by the *Sides* input.
Each segment has its own affinely transformed segment coordinate system,
which can be used to tile textures in a radially symmetric manner.


Inputs
======

Vector
   Vector of the input system that is to be divided into radial segments.

Sides
   Number of radial segments to divide the input coordinate system into.
   A non-integer value results in an irregular segment that is smaller than the regular segments.

   .. list-table::
      :widths: 25 25 25 25

      * - .. figure:: /images/render_shader-nodes_radial_tiling_segments-5_0.png

             Sides: 5.0.

        - .. figure:: /images/render_shader-nodes_radial_tiling_segments-5_25.png

             Sides: 5.25.

        - .. figure:: /images/render_shader-nodes_radial_tiling_segments-5_5.png

             Sides: 5.5.

        - .. figure:: /images/render_shader-nodes_radial_tiling_segments-6_0.png

             Sides: 6.0.

Roundness
   Roundness of the segment coordinate systems.

   .. list-table::
      :widths: 25 25 25 25

      * - .. figure:: /images/render_shader-nodes_radial_tiling_roundness-0_0.png

             Roundness: 0.0.

        - .. figure:: /images/render_shader-nodes_radial_tiling_roundness-0_25.png

             Roundness: 0.25.

        - .. figure:: /images/render_shader-nodes_radial_tiling_roundness-0_5.png

             Roundness: 0.5.

        - .. figure:: /images/render_shader-nodes_radial_tiling_roundness-1_0.png

             Roundness: 1.0.


Properties
==========

Normalize
   If enabled, the X-coordinates of the *Segment Coordinates* output are remapped into a 0.0 to 1.0 range
   and a constant value of 1.0 is added to the Y-coordinates which makes the output range non-negative.

   .. list-table::
      :widths: 50 50

      * - .. figure:: /images/render_shader-nodes_radial_tiling_normalize-disabled.png

             Normalize: Disabled.

        - .. figure:: /images/render_shader-nodes_radial_tiling_normalize-enabled.png

             Normalize: Enabled.


Outputs
=======

Segment Coordinates
   Segment coordinates for texture mapping within each radial segment.

Segment ID
   Unique ID for every radial segment startiing at 0 and increasing counterclockwise by 1 for every for each segment.

Segment Width
   Relative width of each radial segment. May be used to scale textures to fit into each segment.

Segment Rotation
   Counterclockwise rotation of each segment coordinate system. May be used to align the rotation of the textures of
   each segment.


Examples
========

The coordinates provided by the *Segment Coordinates* output can be used to tile textures in a radially symmetric
manner, which is demonstrated by radially tiling a heart texture in the following examples.

.. list-table::
   :widths: 50 50

   * - .. figure:: /images/render_shader-nodes_radial_tiling_example_segments-5_0-heart.png

             Sides: 5.0.

     - .. figure:: /images/render_shader-nodes_radial_tiling_example_segments-6_5-heart.png

             Sides: 6.5.

.. figure:: /images/render_shader-nodes_radial_tiling_example_segments-6_5-heart-nodetree.png

             Node tree for the shader above.

With an increasing number of segments the relative width of each segment decreases, eventually causing the textures to
overlap and clip, as seen on the example with *Sides* set to 6.5. Apart from that, the non-integer *Sides* value in
that example results in even more significant clipping due to the irregular segment that is smaller than the regular
segments. To avoid this clipping, the *Segment Width* output can be used to scale the textures according to the
relative width of each segment.

.. list-table::
   :widths: 50 50

   * - .. figure:: /images/render_shader-nodes_radial_tiling_example_segments-5_0-heart-scaled.png

             Sides: 5.0.

     - .. figure:: /images/render_shader-nodes_radial_tiling_example_segments-6_5-heart-scaled.png

             Sides: 6.5.

.. figure:: /images/render_shader-nodes_radial_tiling_example_segments-6_5-heart-scaled-nodetree.png

             Node tree for the shader above. The value 0.725 is an arbitrarily chosen texture scaling value and can be
             tweaked to change the size of the textures.

By default the segment coordinate systems are rotated to have their Y-axes intersect with the origin. The *Segment
Rotation* output can be used to align the rotation of the segment coordinate systems along a global direction instead.

.. list-table::
   :widths: 50 50

   * - .. figure:: /images/render_shader-nodes_radial_tiling_example_segments-5_0-heart-scaled-rotated.png

             Sides: 5.0.

     - .. figure:: /images/render_shader-nodes_radial_tiling_example_segments-6_5-heart-scaled-rotated.png

             Sides: 6.5.

.. figure:: /images/render_shader-nodes_radial_tiling_example_segments-6_5-heart-scaled-rotated-nodetree.png

             Node tree for the shader above. The value -1.571 is an arbitrarily chosen texture rotation value and can
             be tweaked to change the rotation of the textures.

When working with textures that span the entire UV space there is usually the issue of visible seams along segment
borders even if the original texture is seamless. The *Normalize* option eliminates these visible seams by ensuring
that the X-coordinates always only cover the entire 0 to 1 range. This also introduces a distortion effect, which
depending on whether or not it's desirable may need to be mitigated using additional nodes.

.. list-table::
   :widths: 50 50

   * - .. figure:: /images/render_shader-nodes_radial_tiling_example_normalize-disabled-pavement.png

             Normalize: Disabled.

     - .. figure:: /images/render_shader-nodes_radial_tiling_example_normalize-enabled-pavement.png

             Normalize: Enabled.

For some textures it may be useful to create a more rounded appearance in the vicinity of segment borders,
which can be done by setting the roundness of the segment coordinate systems using the *Roundness* input.

.. list-table::
   :widths: 25 25 25 25

   * - .. figure:: /images/render_shader-nodes_radial_tiling_example_roundness-0_0-pavement.png

          Roundness: 0.0.

     - .. figure:: /images/render_shader-nodes_radial_tiling_example_roundness-0_25-pavement.png

          Roundness: 0.25.

     - .. figure:: /images/render_shader-nodes_radial_tiling_example_roundness-0_5-pavement.png

          Roundness: 0.5.

     - .. figure:: /images/render_shader-nodes_radial_tiling_example_roundness-1_0-pavement.png

          Roundness: 1.0.
