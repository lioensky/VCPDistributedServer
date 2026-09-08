.. _bpy.types.FreestyleLineStyle:

##############
  Line Style
##############

In Freestyle, the line style settings define the appearance of a line set using five main aspects:
Stroke, Color, Alpha, Thickness, Geometry, and Texture with each on a separate tab.
These allow you to get many different styles of renders
(technical draw, rough sketch, cartoon, calligraphy, etc.).

You can create as many line styles as you wish, and reuse a given line style for several line
sets by selecting it from the select menu next to its name.

.. note::

   Unless otherwise specified, all lengths in line style settings are in pixels
   (either relative or absolute, as specified in the :doc:`core options </render/freestyle/render>`).

.. figure:: /images/render_freestyle_parameter-editor_line-style_introduction_line-style-example.png

   Line Style Example (`blend-file <https://archive.blender.org/wiki/2015/index.php/File:LineStyles.zip>`__).


Properties
==========

.. toctree::
   :maxdepth: 1

   strokes.rst
   color.rst
   alpha.rst
   thickness.rst
   geometry.rst
   texture.rst

.. toctree::
   :maxdepth: 2

   modifiers/index.rst
