.. index:: Compositor Nodes; Directional Blur
.. _bpy.types.CompositorNodeDBlur:

*********************
Directional Blur Node
*********************

.. figure:: /images/node-types_CompositorNodeDBlur.webp
   :align: right
   :alt: Directional Blur Node.

Blurs an image along a specified direction. Can be used to fake motion blur.


Inputs
======

Image
   Standard color input.
Samples
   The number of samples used to compute the blur.
   The more samples the smoother the result, but at the expense of more compute time.
   The actual number of samples is two to the power of this input, so it increases exponentially.
Center
   The position at which the transformations pivot around.
   Defined in normalized coordinates, so 0 means lower left corner and 1 means upper right corner of the image.
Rotation
   The amount of rotation that the blur spans.
Scale
   The amount of scaling that the blur spans.


Translation
-----------

Amount
   The amount of translation that the blur spans in the specified direction relative to the size of the image.
   Negative values indicate translation in the opposite direction.
Direction
   The angle that defines the direction of the translation.


Outputs
=======

Image
   Standard color output.
