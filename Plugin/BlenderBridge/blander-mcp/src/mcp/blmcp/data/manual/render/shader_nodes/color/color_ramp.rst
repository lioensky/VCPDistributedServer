.. index:: Shader Nodes; Color Ramp
.. _bpy.types.ShaderNodeValToRGB:
.. Editors Note: This page gets copied into:
.. - :doc:`/compositing/types/color/color_ramp`
.. - :doc:`/modeling/geometry_nodes/color/color_ramp`
.. - :doc:`/editors/texture_node/types/converter`
.. --- copy below this line ---

***************
Color Ramp Node
***************

.. figure:: /images/node-types_ShaderNodeValToRGB.webp
   :align: right
   :alt: Color Ramp Node.

The Color Ramp Node is used for mapping values to colors using a gradient.


Inputs
======

Factor
   The value to map. 0.0 results in the leftmost color, while 1.0 results in the rightmost.


Properties
==========

Color Ramp
   See :ref:`ui-color-ramp-widget`.


Outputs
=======

Image/Color
   Standard color output.
Alpha
   Standard alpha output.


Examples
========

Creating an Alpha Mask
----------------------

An often overlooked use case of the Color Ramp is to turn a black-and-white image
into a colored image with transparency.

.. figure:: /images/compositing_types_converter_color-ramp_create-alpha-mask.png
   :width: 600px

In the example above, a black-and-white swirl image, which is lacking an alpha channel,
is fed into the Color Ramp node as a *Factor*.

The Color Ramp node is set to a purely transparent color on the left end of the gradient,
and a fully red color on the right. As you can see in the Viewer node,
the Color Ramp node outputs an image that is transparent where the input is black,
and opaque where the input is white.


Colorizing an Image
-------------------

In this example, multiple colors are added to the color gradient,
converting a black-and-white image into a flaming swirl.

.. figure:: /images/compositing_types_converter_color-ramp_colorizing-image.png
   :width: 600px

The shades of gray in the input image are mapped to three colors:
blue, yellow, and red, all fully opaque. Where the image is black,
the Color Ramp substitutes blue (the first color stop). Where it is some shade of gray,
the Color Ramp outputs a corresponding color from the gradient (bluish, yellow, to reddish).
Where the image is fully white, the Color Ramp outputs red.
