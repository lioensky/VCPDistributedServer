.. index:: Compositor Nodes; Alpha Over
.. _bpy.types.CompositorNodeAlphaOver:

***************
Alpha Over Node
***************

.. figure:: /images/node-types_CompositorNodeAlphaOver.webp
   :align: right
   :alt: Alpha Over Node

The *Alpha Over* node composites two images by layering the *Foreground* image over the *Background*,
using standard alpha blending operations.

This node is commonly used to combine rendered elements, overlays, or visual effects in a single image,
such as placing text, logos, or transparent effects over footage.


Inputs
======

Background
   The background image.
Foreground
   The foreground image to be placed over the background.
Factor
   Controls the opacity of the foreground image, from 0 (fully transparent) to 1 (fully opaque).
Type
   Determines the alpha compositing method:

   :Over:
      The standard alpha-over operation.
      The foreground is placed over the background based on its alpha channel.
   :Disjoint Over:
      Similar to *Over*, but assumes the background has been held out by the foreground,
      resulting in cleaner edges when compositing multiple layers.
   :Conjoint Over:
      Similar to *Over*, but assumes the foreground overlaps or extends into the background.
      Useful when the foreground is more opaque but not fully opaque.
Straight Alpha
   Specifies whether the foreground uses *straight* alpha (non-premultiplied) instead of *premultiplied* alpha.
   Most images in the compositor are premultiplied, so this should remain disabled in most cases.
   Enable it only if the foreground has been explicitly converted to straight alpha form.


Outputs
=======

Image
   The combined image after alpha compositing.


Examples
========

Disjoint / Conjoint / Over
--------------------------

The example below shows how different alpha compositing types affect the blending of multiple layers.
Four image layers are assembled using the *Disjoint*, *Conjoint*, and *Over* methods
to create depth between overlapping elements.

.. figure:: /images/compositing_types_color_alpha-over_example2.webp

   Assembling a composite image using Alpha Over.


Fade In
-------

This example uses a :doc:`/compositing/types/input/scene/time_curve`
to gradually animate the *Factor* input of the *Alpha Over* node from 0 to 1 over 30 frames.
The result is a smooth fade-in of text over a background image.

.. figure:: /images/compositing_types_color_alpha-over_example.png
   :width: 600px

   Animated fade-in effect using Alpha Over.
