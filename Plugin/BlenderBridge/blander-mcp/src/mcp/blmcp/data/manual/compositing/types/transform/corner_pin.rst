.. index:: Compositor Nodes; Corner Pin
.. _bpy.types.CompositorNodeCornerPin:

***************
Corner Pin Node
***************

.. figure:: /images/node-types_CompositorNodeCornerPin.webp
   :align: right
   :alt: Corner Pin Node.

The Corner Pin node uses explicit corner values for a plane warp transformation.
It works like the :doc:`Plane Track Deform </compositing/types/tracking/plane_track_deform>` node,
but without using "plane track" data from the Movie Clip Editor.

The transformation of the input Image is applied before distortion, this consequently means that
translations will introduce clipping.


Inputs
======

Image
   Standard color input.
Corners
   Four vector inputs to define the plane warping.


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


Outputs
=======

Image
   Standard color output. (The image after distorting.)
Plane
   A black-and-white alpha mask of the plane.


Example
=======

.. figure:: /images/compositing_types_distort_corner-pin_example.png

   An example of the Corner Pin node.

.. figure:: /images/compositing_types_distort_corner-pin_example-result.jpg

   An example of the distorted image.

In the example above, the image of the bird is distorted by the vectors specified by the Corner Pin node.
