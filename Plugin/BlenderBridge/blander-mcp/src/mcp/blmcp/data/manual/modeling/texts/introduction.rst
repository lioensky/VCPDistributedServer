
************
Introduction
************

Text objects contain some text, and are in the same object type family as curves and surfaces ones,
as fonts are vector data (they are made of curves).

Blender uses a "Font System" to manage mapping letter codes to geometry representing them in the 3D Viewport.
This font system has its own *built-in* font, but it can use external fonts too,
including *PostScript Type 1*, *OpenType* and *TrueType* fonts.
And moreover, it can use any objects existing in the current blend-file as letters.

.. figure:: /images/modeling_texts_introduction_examples.jpg
   :width: 460px

   An example of an extruded text.

Text objects allow you to create and render 2D or 3D text,
with various advanced layout options, like justifying and frames.
By default, letters are just flat filled surfaces, exactly like any closed 2D curve.
But, just like curves, you can extrude them,
and apply :doc:`modifiers </modeling/modifiers/introduction>` to them
(e.g. to make them :doc:`follow a curve </modeling/modifiers/deform/curve>`).

Text in Blender can be laid out in some relatively advanced ways,
defining columns or blocks of text, using different alignments, and so on.

Those features are similar in concept to what you can find in :abbr:`DTP (DeskTop Publishing)` software
(like `Scribus <https://www.scribus.net/>`__), although at a very basic level currently.

.. tip::

   You can convert a text object, either to a curve, or directly to a mesh,
   using :ref:`object-convert-to` in Object Mode.

.. note::

   A maximum of 50,000 characters is allowed per text object. However,
   be forewarned that the more characters a single text object has,
   the slower the object will respond interactively.
