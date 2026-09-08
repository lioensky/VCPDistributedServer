.. index:: Compositor Nodes; Image Coordinates
.. _bpy.types.CompositorNodeImageCoordinates:

**********************
Image Coordinates Node
**********************

.. figure:: /images/node-types_CompositorNodeImageCoordinates.webp
   :align: right
   :alt: Image Coordinates Node.

The *Image Coordinates* node outputs various coordinate fields for an input image.
These outputs provide information about each pixel's location in different coordinate spaces,
which can be useful for procedural texturing, compositing effects, or image-based masking.

The coordinate outputs are calculated per pixel based on the image resolution and placement
within the compositor's virtual space.


Inputs
======

Image
   The input image used to determine dimensions and placement for the coordinate outputs.


Outputs
=======

Uniform
   Normalized coordinates centered at zero, scaled based on the image's largest dimension.
   This is useful for procedural effects that need aspect-ratio-independent coordinates,
   similar to *Object* coordinates in shader nodes.

Normalized
   Normalized coordinates ranging from 0 to 1 across the image dimensions,
   with half-pixel offsets to align with pixel centers.

Pixel
   Pixel-space coordinates representing the center position of each pixel.
   These are integer-based coordinates with a half-pixel offset applied.
