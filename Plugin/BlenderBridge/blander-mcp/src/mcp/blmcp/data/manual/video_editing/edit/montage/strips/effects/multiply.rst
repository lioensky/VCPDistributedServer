.. _bpy.types.MultiplyStrip:

**************
Multiply Strip
**************

The *Multiply* effect multiplies two colors.
Blender uses values between (0.0 to 1.0) for the colors.
This operation does not have to be normalized, the multiplication of two terms
between (0.0 to 1.0) always gives a result between (0.0 to 1.0).

(With the "traditional" representation of three bytes, like RGB(124, 255, 56),
the multiplications give far too high results, like RGB(7316, 46410, 1848),
that have to be normalized (brought back) by dividing them by 256
to fit in the range of (0 to 255)...)

This effect has two main usages:


.. rubric:: With a Mask

A mask is a black-and-white picture which, after multiplication with a "normal" image,
only show this one in the white areas of the mask (everything else is black).

The opening title sequence to James Bond movies,
where the camera is facing down the barrel of a gun at James, is a good example of this effect.


.. rubric:: With Uniform Colors

Multiplying a color with a "normal" image allows you to soften some hues of this one
(and so -- symmetrically -- to enhance the others).

For example, if you have a brown pixel RGB(0.50, 0.29, 0.05), and
you multiply it with a cyan filter (uniform color RGB(0.0, 1.0, 1.0)), you will get a color RGB(0.0, 0.29, 0.05).
Visually, the result is to zero the reds and bring up (by "symmetry" -- the real values remain unchanged!)
the blues and greens. Physically, it is the same effect as shining a cyan light onto a chocolate bar. Emotionally,
vegetation becomes more lush, water becomes more Caribbean and inviting, skies become friendlier.

.. note::

   This effect reduces the global luminosity of the picture
   (the result will always be smaller than the smallest operand).
   If one of the images is all white, the result is the other picture;
   if one of the images is all black, the result is all black!


Options
=======

This strip has no options.


Example
=======

.. figure:: /images/video-editing_sequencer_strips_effects_multiply_example.png

   Multiply Effect.
