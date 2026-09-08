.. index:: Compositor Nodes; Dilate/Erode
.. _bpy.types.CompositorNodeDilateErode:

*****************
Dilate/Erode Node
*****************

.. figure:: /images/node-types_CompositorNodeDilateErode.webp
   :align: right
   :alt: Dilate/Erode Node.

Expands or shrinks a mask using a morphological operator.


Inputs
======

Mask
   A grayscale image.
Size
   The size of the surrounding area to look at for each pixel; or in other words, how much to
   dilate (for positive values) or erode (for negative values) the mask.
Type
   :Steps:
      Sets each pixel to the maximum (for dilation) or minimum (for erosion) value that's found
      within a square surrounding it. This approach keeps the original gray levels and is best
      suited for masks that contain sharp corners; rounded shapes such as circles will look more
      square-like in the output.

      Despite the name, this is not an iterative process; the dilation/erosion is only performed
      once regardless of the chosen *Size*.
   :Threshold:
      Makes all the pixels fully black or white depending on whether they're darker or brighter
      than 50% gray. Then, sets each pixel to the maximum (for dilation) or minimum
      (for erosion) value that's found within a circle surrounding it. This approach loses the
      original gray levels. Shape wise, it's well-suited for masks that contain rounded corners;
      sharp ones will be rounded off.
   :Distance:
      Sets each pixel to the maximum (for dilation) or minimum (for erosion) value that's found
      within a circle surrounding it. This approach preserves the original gray levels and
      is well-suited for masks that contain rounded corners.
   :Feather:
      Blurs the image.
Falloff Size :guilabel:`Threshold`
   Determines how much to blur the edges after dilation/erosion.
Falloff :guilabel:`Feather`
   Determines the brightness curve of the blurred edges.


Outputs
=======

Mask
   The resulting mask.


Example
=======

In the image below, notice that:

- The light gray disk has turned white and the dark gray rectangle has turned black
  because of the *Mode*.
- The shapes have become thicker -- dilated because of the positive *Size*.
- The shapes appear blurred because of the positive *Falloff Size*.

.. figure:: /images/compositing_types_filter_dilate-erode_example.png
