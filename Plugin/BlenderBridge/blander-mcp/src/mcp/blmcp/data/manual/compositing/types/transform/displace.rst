.. index:: Compositor Nodes; Displace
.. _bpy.types.CompositorNodeDisplace:

*************
Displace Node
*************

.. figure:: /images/node-types_CompositorNodeDisplace.webp
   :align: right
   :alt: Displace Node.

The *Displace Node* displaces the pixel position based on an input vector.

This node could be used to model phenomena, like hot air distortion,
refractions of uneven glass or for surreal video effects.


Inputs
======

Image
   Standard color input.
Displacement
   Input of the displacement map.
   If the input is color it's implicitly converted in the vector input,
   the first channel (red) value determines displacement along X axis.
   The second channel (green) the displacement along Y axis.
   If the input is a grayscale image, where both the channel values are equal,
   the input image will be displaced equally in both X and Y directions.


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

   .. note::

      This option is not available for the *Anisotropic* *Interpolation* mode.


Outputs
=======

Image
   Standard color output.
