.. index:: Compositor Nodes; Levels
.. _bpy.types.CompositorNodeLevels:

***********
Levels Node
***********

.. figure:: /images/node-types_CompositorNodeLevels.webp
   :align: right
   :alt: Levels Node.

The Levels Node read the input color channels and outputs analytical values.
The output is one-dimensional meaning the visualization will be a uniform gray color.


Inputs
======

Image
   Standard color input.
Channel
   Selects which color values are used to calculate analytics.

   :Combined: Calculate values based on the red, green, and blue channels.
   :Red: Calculate values based on the red channel.
   :Green: Calculate values based on the green channel.
   :Blue: Calculate values based on the blue channel.
   :Luminance: Calculate values based on the :term:`Luminance` of the image.


Outputs
=======

Mean
   The mean is the average value of all image pixels in specified channel.
   It represents the overall brightness of the image and can be used as such
   for setups that depend on how "bright" or "dark" the input is.
Standard Deviation
   How much pixel values differ from the mean.
   A low standard deviation indicates that the pixel values tend to be very close to the mean.
   A high standard deviation indicates that the values are spread out over a large range of values.
