.. index:: Compositor Nodes; Difference Key
.. _bpy.types.CompositorNodeDiffMatte:

*******************
Difference Key Node
*******************

.. figure:: /images/node-types_CompositorNodeDiffMatte.webp
   :align: right
   :alt: Difference Key Node.

This node produces a matte that isolates foreground content by comparing it with a reference background image.


Inputs
======

Image 1
   Contains foreground content against the background that is to be removed.
Image 2
   The reference background image.
Tolerance
   Where pixels match the reference background to within the specified threshold, the matte is made transparent.
Falloff
   Increase to make nearby pixels partially transparent producing a smoother blend along the edges.


Outputs
=======

Image
   Image with its alpha channel adjusted for the keyed selection.
Matte
   A black-and-white alpha mask of the key.
