.. index:: Compositor Nodes; Filter
.. _bpy.types.CompositorNodeFilter:

***********
Filter Node
***********

.. figure:: /images/node-types_CompositorNodeFilter.webp
   :align: right
   :alt: Filter Node.

The Filter node implements various common image enhancement filters.


Inputs
======

Image
   Standard color input.
Factor
   Controls the amount of influence the node exerts on the output image.
Type
   The Soften, Laplace, Sobel, Prewitt and Kirsch all perform edge detection
   (in slightly different ways) based on vector calculus and set theory equations.

   :Soften: Slightly blurs the image.
   :Box Sharpen: Increases the contrast, especially at edges.
   :Diamond Sharpen: Less aggressive than box sharpen, reducing sharpening artifacts.
   :Laplace: Edge highlighting filter susceptible to highlighting visual noise.
   :Sobel: Creates a negative image that highlights edges.
   :Prewitt: Produces a similar results to Sobel.
   :Kirsch: Gives better blending than Sobel or Prewitt, when approaching an edge.
   :Shadow: Performs a relief, emboss effect, darkening outside edges.


Outputs
=======

Image
   Standard color output.


Example
=======

.. list-table:: The Filter node has eight modes, shown here.

   * - .. figure:: /images/compositing_types_filter_filter-node_example-1-original.png

          Original image.

     - .. figure:: /images/compositing_types_filter_filter-node_example-2-soften.png

          Soften.

   * - .. figure:: /images/compositing_types_filter_filter-node_example-3-box-sharpen.png

          Box Sharpen.

     - .. figure:: /images/compositing_types_filter_filter-node_example-4-diamond-sharpen.png

          Diamond Sharpen.

   * - .. figure:: /images/compositing_types_filter_filter-node_example-5-laplace.png

          Laplace.

     - .. figure:: /images/compositing_types_filter_filter-node_example-6-sobel.png

          Sobel.

   * - .. figure:: /images/compositing_types_filter_filter-node_example-7-prewitt.png

          Prewitt.

     - .. figure:: /images/compositing_types_filter_filter-node_example-8-kirsch.png

          Kirsch.

   * - .. figure:: /images/compositing_types_filter_filter-node_example-9-shadow.png

          Shadow.

     -
