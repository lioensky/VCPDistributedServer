.. index:: Geometry Nodes; Image Info
.. _bpy.types.GeometryNodeImageInfo:

***************
Image Info Node
***************

.. figure:: /images/node-types_GeometryNodeImageInfo.webp
   :align: right
   :alt: Image Info node.
   :width: 300px


The *Image Info* node gets information from image and animation.
This can be useful to generate parameters in the geometry node for arbitrary images. Image information can be either
general or frame-specific.

Inputs
======

Image
   Source image to get parameters from.

Frame
   Frame index for frame-specific outputs.


Outputs
=======

Width
   The number of pixels along the X axis. Specific to each frame.

Height
   The number of pixels along the Y axis. Specific to each frame.

Has Alpha
   Whether the transparency channel be different from 1 for the pixels of this image frame. Specific to each frame.

Frame Count
   The number of frames in an image or video frame sequence. For a static image, always 1.

FPS
   The number of frames per second. For static image is always 0.
