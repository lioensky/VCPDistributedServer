.. index:: Compositor Nodes; Scale
.. _bpy.types.CompositorNodeScale:

**********
Scale Node
**********

.. figure:: /images/node-types_CompositorNodeScale.webp
   :align: right
   :alt: Scale Node.

This node scales the size of an image.


Inputs
======

Image
   Standard color input.
Space
   Coordinate Space to scale relative to.

   :Relative:
      Percentage values relative to the dimensions of the image input.
   :Absolute:
      Size of an image by using absolute pixel values.
   :Scene Size:
      Sizes an image to the size of the final render resolution for the scene.
      For example, rendering a scene at the standard 1080p resolution but setting the render percentage at 50%,
      will produce a 1080p image with the scene scaled down 50% and leaving the rest of the image as alpha.
   :Render Size:
      Image dimensions set in the Render panel.
Frame Type :guilabel:`Render Size`
   How the image fits in the camera frame.

   :Stretch: Distorts the image so that it fits into the render size.
   :Fit: Scales the image until the bigger axis "fits" into the render size.
   :Crop: Cuts the image so that it is the same aspect ratio as the render size.
X, Y
   Scale in the axis directions, only available if *Space* is set to *Relative* or *Absolute*.


Sampling
--------

Interpolation
   Determines how pixel values are interpolated when scaling or transforming images.

   :Nearest:
      Uses the value of the closest pixel with no smoothing.
      This is the fastest method and is well-suited for pixel art or low-resolution images
      where sharp, blocky edges are desirable.
      In animations, motion appears in single-pixel steps, which can cause visible jittering.
   :Bilinear:
      Averages the values of surrounding pixels to create a smoother result than *Nearest*.
      Provides a good balance between performance and visual quality.
   :Bicubic:
      Computes a weighted average of a larger neighborhood of pixels for even smoother results.
      Ideal for photographic images or gradients where preserving fine detail is important.
   :Anisotropic:
      Adjusts interpolation based on the direction and scale of the transformation.
      Helps reduce blurring or aliasing when scaling at steep angles or uneven resolutions,
      especially useful in textures viewed at oblique angles or in detailed 3D projections.

Extension X/Y
   The extension mode applied to the X axis.

   :Clip: Areas outside of the image are filled with transparency.
   :Extend: Areas outside of the image are filled with the closest boundary pixel in the image.
   :Repeat: Areas outside of the image are filled with repetitions of the image.


Outputs
=======

Image
   Standard color output.


Examples
========

For instance X: 0.5 and Y: 0.5 would produce an image which width and
height would be half of what they used to be.

Use this node to match image sizes.
Most nodes produce an image that is the same size as the image input into their top image socket.
To uniformly combine two images of different size,
the second image has to be scaled up to match the resolution of the first.
