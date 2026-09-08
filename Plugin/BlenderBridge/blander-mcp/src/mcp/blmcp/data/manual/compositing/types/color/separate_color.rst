.. index:: Compositor Nodes; Separate Color
.. Editor's Note: This page gets copied into :doc:`</render/cycles/nodes/types/converter/combine_separate>`
.. _bpy.types.CompositorNodeSeparateColor:

*******************
Separate Color Node
*******************

.. figure:: /images/node-types_FunctionNodeSeparateColor.webp
   :align: right
   :alt: Separate Color Node.

The *Separate Color Node* splits an image into its composite color channels.
The node can output multiple :term:`Color Models <Color Model>` depending on the Mode property.


Inputs
======

Image
   Standard image input.


Properties
==========

Mode
   The color model to output.

   :RGB: Split the input image into it's three outputs: Red, Green, and Blue color channels.
   :HSV: Split the input image into it's three outputs: Hue, Saturation, and Value color channels.
   :HSL: Split the input image into it's three outputs: Hue, Saturation, and Lightness color channels.
   :YCbCrA:
       Split the input image into it's three outputs:
       Luminance, Chrominance Blue, and Chrominance Red color channels.

      Color Space
         ITU 601, ITU 709, JPEG
   :YUV:
      Split the input image into it's three outputs:
      Luminance, U chrominance, and V chrominance color channels.


Outputs
=======

The outputs of this node depends on the Mode property (see above).

Alpha
   The color channel that is responsible for the image's transparency.


Examples
========

Blur Alpha
----------

.. figure:: /images/compositing_types_converter_combine-separate_example-combine-rgba.png
   :width: 640px

   An example of blurring the alpha channel.

In this first example, we take the Alpha channel and blur it,
and then combine it back with the colors. When placed in a scene,
the edges of it will blend in, instead of having a hard edge.
This is almost like :term:`Anti-Aliasing` but in a three-dimensional sense.
Use this node setup, when adding CG elements to live action to remove any hard edges.
Animating this effect on a broader scale will make the object appear to "phase" in and out,
as an "out-of-phase" time-traveling sync effect.


Increase Luminance
------------------

.. figure:: /images/compositing_types_converter_math_multiply.png

   An example of the scaling the Luminance channel.

This example has a *Math (Multiply)* node increasing the luminance channel (Y)
of the image to make it brighter.

.. tip::

   If running these channels through a *Color Ramp* node to adjust value,
   use the Cardinal scale for accurate representation.
   Using the Exponential scale on the luminance channel gives a high-contrast effect.
