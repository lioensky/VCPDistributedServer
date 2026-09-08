.. index:: Compositor Nodes; Translate
.. _bpy.types.CompositorNodeTranslate:

**************
Translate Node
**************

.. figure:: /images/node-types_CompositorNodeTranslate.webp
   :align: right
   :alt: Translate Node.

The Translate node moves an image.

Could also be used to add a 2D camera shake.


Inputs
======

Image
   Standard color input.
X, Y
   Used to move the input image horizontally and vertically.


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
