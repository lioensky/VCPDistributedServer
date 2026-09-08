
*******************************
Alpha Over & Alpha Under Strips
*******************************

Using the alpha (transparency channel),
this effect composites a result based on transparent areas of the dominant image.
If you use a Scene strip, the areas of the image where there is not anything solid are transparent;
they have an alpha value of 0. If you use a Movie strip, that movie has an alpha value of 1 (completely opaque).

So, you can use the *Alpha Over* / *Alpha Under* effect to composite the CGI Scene on top of your movie.
The result is your model doing whatever as if it was part of the movie.
The :menuselection:`Adjust --> Compositing --> Opacity` controls how much
the foreground is mixed over the background, fading in the foreground on top of the background.
The colors of transparent foreground image areas are ignored and do not change the color of the background.


.. _bpy.types.AlphaOverStrip:

Alpha Over
==========

With *Alpha Over*, the strips are layered up in the order selected; the first strip selected is the background,
and the second one goes *over* the first one selected.
The *Opacity* controls the transparency of the *foreground*, i.e. *Opacity* of 0.0;
will only show the background, and an *Opacity* of 1.0 will completely override the background with the foreground
(except in the transparent areas of this one, of course!)

.. warning::

   By clicking the *Premultiply Alpha* button in the Sidebar of the foreground strip,
   the alpha values of the two strips are not multiplied or added together.
   Use this effect when adding a foreground strip that has a variable alpha channel
   (some opaque areas, some transparent, some in between) over a strip that has a flat opaque
   (alpha=1.0 or greater) channel. If you notice a glow around your foreground objects,
   or strange transparent areas of your foreground object when using *Alpha Over*,
   enable *Premultiply*.

.. figure:: /images/video-editing_sequencer_strips_effects_alpha-over-under-overdrop_example.png

   Alpha Over Effect.


.. _bpy.types.AlphaUnderStrip:

Alpha Under
===========

With *Alpha Under*, this is the contrary:
The first strip selected is the foreground, and the second one, the background.
Moreover, the *Opacity* controls the transparency of the *background*, i.e. an *Opacity* of 0.0;
will only show the foreground (the background is completely transparent),
and an *Opacity* of 1.0 will give the same results as with *Alpha Over*.
