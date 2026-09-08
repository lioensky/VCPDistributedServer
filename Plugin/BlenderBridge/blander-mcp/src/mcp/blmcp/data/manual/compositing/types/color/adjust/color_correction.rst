.. index:: Compositor Nodes; Color Correction
.. _bpy.types.CompositorNodeColorCorrection:

*********************
Color Correction Node
*********************

.. figure:: /images/node-types_CompositorNodeColorCorrection.webp
   :alt: Color Correction Node.

The Color Correction node adjusts the color of an image, separately in several tonal ranges
(highlights, midtones and shadows).


Inputs
======

Image
   Standard color input.
Mask
   Controls the amount of influence the node exerts on the output image.


Master
------

These settings target the entire tonal range.

Saturation
   Adjusts the image's saturation.
Contrast
   Adjust image contrast.
Gamma
   Exponential gamma correction, affecting the midtones of the image. (Works like Power in the Color Balance node.)
Gain
   Multiplier, stronger influence on the highlights. (Works like Slope in the Color Balance node.)
Offset
   This value (can be negative) will be added (+), linear lightens or darkens the image.


Highlights / Midtones / Shadows
-------------------------------

These settings target specific brightness ranges of the image.

Each tonal range (Highlights, Midtones, Shadows) supports the same controls as Master.


Tonal Ranges
------------

Midtones Start, Midtones End
   Defines the start and the end of midtones range, i.e.
   values where the whole tonal range is divided into the highlights, midtones and shadows
   (there is also a smooth transition between the ranges of width 0.2 units).


Channels
--------

Red, Green, Blue
   Specifies which RGB channels will be affected by the correction.


Outputs
=======

Color
   Standard color output.
