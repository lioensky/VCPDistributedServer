.. index:: Compositor Nodes; Flip
.. _bpy.types.CompositorNodeFlip:

*********
Flip Node
*********

.. figure:: /images/node-types_CompositorNodeFlip.webp
   :align: right
   :alt: Flip Node.

The *Flip* node flips the input image horizontally, vertically, or both, based on the inputs provided.

This node can be used to mirror an image or as part of a compositing setup that blends the original
image with a flipped version to achieve symmetry effects.


Inputs
======

Image
   Standard color input to be flipped.
Flip X
   Flips the image horizontally (left to right).
Flip Y
   Flips the image vertically (top to bottom).


Outputs
=======

Image
   The resulting flipped image.
