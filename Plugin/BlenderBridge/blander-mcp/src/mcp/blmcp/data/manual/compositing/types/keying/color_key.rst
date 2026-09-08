.. index:: Compositor Nodes; Color Key
.. _bpy.types.CompositorNodeColorMatte:

**************
Color Key Node
**************

.. figure:: /images/node-types_CompositorNodeColorMatte.webp
   :align: right
   :alt: Color Key node.

The *Color Key* node is used for chroma keying—removing parts of an image based on color.
It is commonly used to remove backgrounds like green screens or blue screens from footage,
creating a matte where selected colors become transparent.


Inputs
======

Image
   Standard color input.
Key Color
   The target color to be keyed out (made transparent).
   This is typically the background color, such as pure green or blue.
Hue
   The tolerance for hue difference from the key color.
   A wider range will key out more colors with similar hues.
Saturation
   The tolerance for saturation difference from the key color.
   Helps avoid removing unintended desaturated areas like skin tones or clothing.
Value
   The tolerance for brightness difference from the key color.
   Useful when lighting is uneven or background luminance varies.


Outputs
=======

Image
   Image with its alpha channel adjusted for the keyed selection.
Matte
   A black-and-white alpha mask of the key.
