.. index:: Compositor Nodes; Unsharp Mask
.. _bpy.types.CompositorNodeUnsharpMask:

*****************
Unsharp Mask Node
*****************

.. figure:: /images/node-types_CompositorNodeUnsharpMask.webp
   :align: right
   :alt: Unsharp Mask Node.

The *Unsharp Mask* node enhances the apparent sharpness of an image by increasing edge contrast.
Despite its name, it does not blur the image; instead, it sharpens details by subtracting a
blurred (unsharp) version of the image from the original and emphasizing the resulting edges.

This technique is commonly used in photography, printing, and digital compositing
to improve clarity and definition.


Inputs
======

Image
   Standard color input image.

Radius
   Controls how much surrounding area is sampled when detecting edges.
   Larger values affect broader regions and can enhance larger features,
   while smaller values focus on fine detail.

Factor
   Controls the intensity of the sharpening effect.
   Higher values produce stronger edge contrast but can lead to halos or artifacts if overused.

Threshold
   Defines how different a pixel must be from its surrounding area before sharpening is applied.
   Higher values limit sharpening to more distinct edges, reducing noise enhancement.


Outputs
=======

Result
   The sharpened image with enhanced edge contrast.
