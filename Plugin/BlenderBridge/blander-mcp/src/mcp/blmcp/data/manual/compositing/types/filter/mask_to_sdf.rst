.. index:: Compositor Nodes; Mask To SDF
.. _bpy.types.CompositorNodeMaskToSDF:

****************
Mask To SDF Node
****************

.. figure:: /images/node-types_CompositorNodeMaskToSDF.webp
   :align: right
   :alt: Mask To SDF node.

The *Mask To SDF* node computes a signed distance field (SDF) from a mask.
A signed distance field stores, for each pixel, the distance to the nearest
boundary of the mask, with the sign indicating whether the pixel lies inside
or outside the masked region.

This representation is useful for effects such as soft edges, outlines,
glows, erosion/dilation, or procedural distance-based compositing operations.


Inputs
======

Mask
   The input mask used to generate the signed distance field.
   Pixels inside the mask are considered interior, while pixels outside are considered exterior.


Outputs
=======

SDF
   Signed distance to the nearest pixel on the mask boundary, measured in pixels.
   Distances are negative inside the mask and positive outside the mask.

Nearest Pixel
   The integer pixel coordinates of the nearest boundary pixel of the mask.
   This can be used for advanced effects that require knowledge of the closest edge position.
