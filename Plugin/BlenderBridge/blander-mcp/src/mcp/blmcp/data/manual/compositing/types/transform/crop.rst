.. index:: Compositor Nodes; Crop
.. _bpy.types.CompositorNodeCrop:

*********
Crop Node
*********

.. figure:: /images/node-types_CompositorNodeCrop.webp
   :align: right
   :alt: Crop Node.

The Crop node crops an input image to a selected region
by either making the cropped area transparent or by resizing the input image.


Inputs
======

Image
   Standard color input. If no image is selected, an image filled with the selected color is used.
   You can use and crop this image in combination with another background image.
X
   The X position of the lower left corner of the crop region.
Y
   The Y position of the lower left corner of the crop region.
Width
   The width of the crop region.
Height
   The height of the crop region.
Alpha Crop
   Sets the areas outside of the crop region to be transparent instead of actually cropping the size of the image.


Outputs
=======

Image
   Standard color output.
