.. index:: Compositor Nodes; Hue/Saturation/Value
.. _bpy.types.CompositorNodeHueSat:
.. Editor's Note: This page gets copied into:
.. - :doc:`</render/shader_nodes/color/hue_saturation>`
.. - :doc:`</editors/texture_node/types/color/hue_saturation>`

.. --- copy below this line ---

*************************
Hue/Saturation/Value Node
*************************

.. figure:: /images/node-types_CompositorNodeHueSat.webp
   :align: right
   :alt: Hue/Saturation/Value Node.

The *Hue/Saturation/Value Node* applies a color transformation in the HSV :term:`Color Model`.


Inputs
======

Image/Color
   Standard color input.
Hue
   The hue rotation offset, from 0 (-180°) to 1 (+180°). Note that
   0 and 1 have the same result.
Saturation
   A value of 0 removes color from the image, making it black-and-white.
   A value greater than 1.0 increases saturation.
Value
   The value shift. 0 makes the color black, 1 keeps it the same, and higher
   values make it brighter.
Factor
   The amount of influence the node exerts on the image.


Outputs
=======

Image/Color
   Standard color output.


Hue/Saturation Tips
===================

Some things to keep in mind that might help you use this node better:

Hues are laid out on a circle
   If you apply a Hue offset of 1 (+180°) to a blue image, you get the diametrically opposite
   color, which is yellow. If you apply a Hue offset of 1 to that yellow image, you get blue again.
Grayscale images have no hue
   Trying to change the Hue or Saturation of a grayscale image has no effect. You can only brighten
   or darken it by adjusting the Value. To add color, use the Mix node instead.
Changing the effect over time
   The different values can be animated using a *Time Curve* node or by setting keyframes.


HSV Example
===========

.. figure:: /images/compositing_types_color_hue-saturation_example.jpg
   :width: 700px

   A basic example.

.. figure:: /images/compositing_types_input_mask_example.png
   :width: 700px

   An example of using the Factor input for masking.
