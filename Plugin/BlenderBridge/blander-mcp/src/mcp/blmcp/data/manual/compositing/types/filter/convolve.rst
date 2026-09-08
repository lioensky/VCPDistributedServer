.. index:: Compositor Nodes; Convolve
.. _bpy.types.CompositorNodeConvolve:

*************
Convolve Node
*************

.. figure:: /images/node-types_CompositorNodeConvolve.webp
   :align: right
   :alt: Convolve Node

The *Convolve* node performs a 2D convolution operation on an image
using a custom :doc:`Image Kernel </compositing/image_kernels>`.
This allows for a wide range of effects such as blurring, sharpening,
and edge detection, depending on the kernel values provided.

The node multiplies a neighborhood of pixels around each image pixel by the kernel values
and sums the results to compute the output pixel color.
This process is often used in image processing to emphasize or suppress certain spatial features.


Inputs
======

Image
   The image to be processed.

Kernel
   The convolution kernel used to modify the image.
   This can be provided as a constant value or an input image where pixel values define the kernel weights.

Normalize Kernel
   A factor that determines whether the kernel values should be automatically normalized
   (i.e., divided by their total sum) to maintain consistent brightness.


Properties
==========

Kernel Data Type
   Determines how the kernel is defined:

   :Float: A numeric kernel defined by the *Kernel* input socket.
   :Image: A full image used as the kernel, allowing for more complex filtering patterns.


Outputs
=======

Image
   The resulting image after applying the convolution operation.


Usage
=====

The *Convolve* node can be used for a variety of image processing effects:

- **Blurring** -- Use a kernel with evenly weighted positive values.
- **Sharpening** -- Use a kernel with a high central value and negative surrounding values.
- **Edge Detection** -- Use kernels such as Sobel or Laplacian to enhance image edges.

.. tip::

   When designing custom kernels, ensure the kernel size and values are balanced to avoid excessive brightening
   or darkening. Enabling *Normalize Kernel* is often recommended to keep overall image brightness consistent.
