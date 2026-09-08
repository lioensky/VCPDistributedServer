.. index:: Compositor Nodes; Blur
.. _bpy.types.CompositorNodeBlur:

*********
Blur Node
*********

.. figure:: /images/node-types_CompositorNodeBlur.webp
   :align: right
   :alt: Blur Node.

The Blur node blurs an image, providing several blur modes.


Inputs
======

Image
   Standard color input.
Size
   The optional Size input will be multiplied with the X and Y blur radius values.
   It also accepts a value image, to control the blur radius with a mask.
   The values should be mapped between (0 to 1) for an optimal effect.
Type
   The difference between the types is in the way they handle sharp edges,
   smooth gradients and preserve the highs and the lows.

   :Flat: Simply blurs everything uniformly.
   :Tent: Preserves the high and the lows better by making a linear falloff.
   :Quadratic: Looks similar to *Gaussian* but can be a little faster but slightly worse looking.
   :Cubic: Preserve the highs, but give an almost out-of-focus blur while smoothing sharp edges.
   :Gaussian: Gives the best looking results but tends to be the slowest.
   :Fast Gaussian: An approximation of the Gaussian.
   :Catmull-Rom: Catmull-Rom keeps sharp contrast edges crisp.
   :Mitch: Preserve the highs, but give an almost out-of-focus blur while smoothing sharp edges.
Extend Bounds
   Allows the image, that is being blurred, to extend past its original dimension.
Separable
   Use faster approximation by blurring along the horizontal and vertical directions independently.


Outputs
=======

Image
   Standard color output.


Example
=======

.. list-table:: Blur node blur modes using 20% of image size as XY, no Bokeh/Gamma.

   * - .. figure:: /images/compositing_types_filter_blur-node_example-1-original.png

          Original image.

     - .. figure:: /images/compositing_types_filter_blur-node_example-2-flat.png

          Flat.

     - .. figure:: /images/compositing_types_filter_blur-node_example-3-tent.png

          Tent.

   * - .. figure:: /images/compositing_types_filter_blur-node_example-4-quadratic.png

          Quadratic.

     - .. figure:: /images/compositing_types_filter_blur-node_example-5-cubic.png

          Cubic.

     - .. figure:: /images/compositing_types_filter_blur-node_example-6-gaussian.png

          Gaussian.

   * - .. figure:: /images/compositing_types_filter_blur-node_example-7-fast-gaussian.png

          Fast Gaussian.

     - .. figure:: /images/compositing_types_filter_blur-node_example-8-catmull-rom.png

          Catmull-Rom.

     - .. figure:: /images/compositing_types_filter_blur-node_example-9-mitch.png

          Mitch.
