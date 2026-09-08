.. index:: Compositor Nodes; Anti-Aliasing
.. _bpy.types.CompositorNodeAntiAliasing:

******************
Anti-Aliasing Node
******************

.. figure:: /images/node-types_CompositorNodeAntiAliasing.webp
   :align: right
   :alt: Anti-Aliasing Node.

The Anti-Aliasing node smooths away jagged edges.


Inputs
======

Image
   Standard color input.

Threshold
   Controls edge detection sensitivity across the whole image.

Contrast Limit
   Controls contrast level to consider when detecting edges.

   The human eye does not perceive all edges equally. For instance,
   it tends to mask low contrast edges in the presence of much higher contrasts in the surrounding area.
   Therefore, applying anti-aliasing to unperceived edges will produce artifacts.
   This option quantifies the difference between low contrast and high contrast neighboring edges.

Corner Rounding
   Detect corners to help preserve the original shape.
   Setting *Corner Rounding* to 0 means no corner detection and no corner rounding will take place.
   The higher the value the better corners will be preserved, i.e. resemble original image.


Outputs
=======

Image
   Standard color output.


Examples
========

.. list-table:: The Anti-Aliasing node has three properties shown here.

   * - .. figure:: /images/compositing_types_filter_antialiasing-node_example-1-threshold.gif
          :align: center

          Changing threshold affects all edges.

     - .. figure:: /images/compositing_types_filter_antialiasing-node_example-2-contrast_limit.gif
          :align: center

          Changing contrast limit affects neighboring edges below contrast limit.

.. list-table:: The effect of corner rounding.

   * - .. figure:: /images/compositing_types_filter_antialiasing-node_example-3-corner_rounding-off.png

          Corner detection and rounding off (set to 0).
          Notice how corners are smoothed because they are treated as artifacts.

     - .. figure:: /images/compositing_types_filter_antialiasing-node_example-3-corner_rounding-on.png

          Full corner detection and rounding preserves the sharp edges around the corner.
