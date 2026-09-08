.. _bpy.types.AddStrip:

*********
Add Strip
*********

The Add effect strip adds the colors of two strips together.
Use this effect with a base image strip, and a modifier strip.
The modifier strip is either a solid color or a black-and-white mask,
or another image entirely.

You can use this effect to increase the brightness of an image, or if you use a BW mask,
selectively increase the brightness of certain areas of the image. The Mix node, in Add mode,
does exactly the same thing as the Add SFX strip here,
and is controlled the same way by feeding the Factor input.

.. Red and Cyan (Green and Blue) make White. Red and Blue make Magenta. Red and Green make Yellow.

The :ref:`example <fig-sequencer-strips-effects-add>` shows what happens when you add gray to an image.
The image gets bright because we are adding gray
RGB(0.5, 0.5, 0.5) to say, a blue color RGB(0.1, 0.1, 0.5) resulting in RGB(0.6, 0.6, 1.0)
which retains the original hue (relationship between the colors) but is much brighter
(has a higher value). When applied to the whole image like this, it seems to flash.


Options
=======

This strip has no options.


Example
=======

.. _fig-sequencer-strips-effects-add:

.. figure:: /images/video-editing_sequencer_strips_effects_add_example.png

   Add Effect.
