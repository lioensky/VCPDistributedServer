.. index:: Compositor Nodes; Chroma Key
.. _bpy.types.CompositorNodeChromaMatte:

***************
Chroma Key Node
***************

.. figure:: /images/node-types_CompositorNodeChromaMatte.webp
   :align: right
   :alt: Chroma Key Node.

The *Chroma Key* node determines if a pixel is a foreground or background
(and thereby should be transparent) based on its chroma values.

Use this, for example, to composite images that have been shot in front of a green or blue screen.


Inputs
======

Image
   Standard color input.
Key Color
   The background color usually selected using the color picker and the original image.
Minimum
   An angle on the color wheel that represents how tolerant the keying color is. Larger angles allow for larger
   variation in the keying color to be considered background pixels.
Maximum
   Controls the level that is considered the pure background. Higher cutoff levels mean more pixels will be
   100% transparent if they are within the angle tolerance.
Falloff
   Increase to make nearby pixels partially transparent producing a smoother blend along the edges.


Outputs
=======

Image
   Image with its alpha channel adjusted for the keyed selection.
Matte
   A black-and-white alpha mask of the key.
