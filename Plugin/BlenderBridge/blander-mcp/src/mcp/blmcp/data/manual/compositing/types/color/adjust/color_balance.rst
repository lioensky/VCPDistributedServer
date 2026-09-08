.. index:: Compositor Nodes; Color Balance
.. _bpy.types.CompositorNodeColorBalance:

******************
Color Balance Node
******************

The Color Balance node adjusts the color and values of an image.

.. figure:: /images/node-types_CompositorNodeColorBalance.webp
   :alt: Color Balance Node.


Inputs
======

Image
   Standard color input.
Factor
   Controls the amount of influence the node exerts on the output image.
Type
   The mathematical method to adjust the image's colors.

   :Lift/Gamma/Gain:
      Adjusts the colors and tonal range of an image by controlling the shadows, midtones, and highlights separately.
   :Offset/Power/Slope (ASC-CDL):
      A standardized model for adjusting the colors and tonal range of an image.
      This allows the same values to be used across different application to yield the same result.
      See `Advanced`_ for more details on the underlying implementation.
   :White Point:
      Adjusts the color that should be considered white.
      The white point is specified as setting the inputs color temperature and then the desired output temperature.

.. rubric:: Lift/Gamma/Gain

Lift
   Adjusts the darkest areas of the image (the shadows).
Gamma
   Primarily affects the midtones, the middle range of brightness in the image.
Gain
   Controls the brightest parts of the image (the highlights).

.. rubric:: Offset/Power/Slope (ASC-CDL)

Offset
   Adjusts the darkest areas of the image (the shadows).
Basis
   Additional offset, allows to specify a negative offset value.
Power
   Primarily affects the midtones, the middle range of brightness in the image.
Slope
   Controls the brightest parts of the image (the highlights).


Input
-----

Temperature
   The blackbody temperature of the input's primary illuminant. By default a D65 white point is used.
Tint
   The amount of green/magenta shift of the input's white point (the default of 10 matches daylight)


Output
------

Temperature
   The blackbody temperature of the output's primary illuminant. By default a D65 white point is used.
Tint
   The amount of green/magenta shift of the output's white point (the default of 10 matches daylight)


Outputs
=======

Image
   Standard output image.


Advanced
========

The Offset/Power/Slope Formula
------------------------------

:math:`\text{out} = (i \times s + o)^p`

where:

- *out*: The color graded pixel code value.
- *i*: The input pixel code value (0 to 1) (black to white).
- *s*: Slope (any number 0 or greater, nominal value is 1.0).
- *o*: Offset (any number, the nominal value is 0).
- *p*: Power (any number greater than 0, nominal value is 1.0).
