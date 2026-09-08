.. index:: Compositor Nodes; Math
.. include:: /render/shader_nodes/utilities/math/math.rst
   :start-after: .. --- copy below this line ---

Examples
========

Manual Z-Mask
-------------

.. figure:: /images/compositing_types_converter_math_manual-z-mask.png

   Minimum and maximum function example.

The top *Render Layers* node has a cube that is about 10 units from the camera.
The bottom *Render Layers* node has a plane that covers the left half of the view
and is 7 units from the camera.
Both are fed through their respective *Map Value* nodes to multiply the depth value by
0.05 and clamp it to [0.0, 1.0], bringing it into a suitable range for displaying it as a color.

The Minimum node selects the smallest of the two depth values at each pixel. In the left half,
it chooses the plane (because it's closer than the cube), and in the right half,
it chooses the cube (because it's closer than the background, which is infinitely far away).

The Maximum node selects the largest of the two depth values at each pixel. In the left half,
it chooses the cube (because it's farther away than the plane), and in the right half,
it chooses the background (because it's farther away than the cube).


Using Sine Function to Pulsate
------------------------------

.. figure:: /images/compositing_types_converter_math_sine.png

   Using sine function example.

This example has a *Time* node putting out a linear sequence from 0 to 1 over the course of 101 frames.
At frame 25, the output value is 0.25.
That value is multiplied by 2 × pi (6.28) and converted to 1.0 by the Sine function,
since :math:`sin(2 × pi/ 4) = sin(pi/ 2) = +1.0`.

Since the sine function can output values between (-1.0 to 1.0),
the *Map Value* node scales that to 0.0 to 1.0 by taking the input (-1 to 1), adding 1
(making 0 to 2), and multiplying the result by 0.5 (thus scaling the output between 0 to 1).
The default *Color Ramp* converts those values to a gray-scale.
Thus, medium gray corresponds to a 0.0 output by the sine, black to -1.0,
and white to 1.0. As you can see, :math:`sin(pi/ 2) = 1.0`. Like having your own visual color calculator!
Animating this node setup provides a smooth cyclic sequence through the range of grays.

Use this function to vary, for example,
the alpha channel of an image to produce a fading in/out effect.
Alter the Z channel to move a scene in/out of focus.
Alter a color channel value to make a color "pulse".


Brightening (Scaling) a Channel
-------------------------------

.. figure:: /images/compositing_types_converter_math_multiply.png

   Scaling a channel example.

This example has a *Math (Multiply)* node increasing the luminance channel (Y)
of the image to make it brighter. Note that you should use a *Map Value node*
with min() and max() enabled to clamp the output to valid values.
With this approach, you could use a logarithmic function to make a high dynamic range image.
For this particular example,
there is also a *Brightness/Contrast node* that might give simpler control over brightness.
