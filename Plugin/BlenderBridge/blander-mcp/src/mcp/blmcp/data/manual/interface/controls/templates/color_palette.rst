.. _bpy.ops.palette:
.. _bpy.types.PaletteColor:

*************
Color Palette
*************

.. figure:: /images/interface_controls_templates_color-palette_ui.png
   :align: right

   Color Palette.

Color Palettes are a way of storing a brush's color so that it can be used at a later time.
This is useful when working with several colors at once.

Palette
   A :ref:`ui-data-block` to select a palette.

:bl-icon:`add` (New Pallet Color)
   Adds the current brush's primary *Color* to the palette.

:bl-icon:`remove` (Delete Pallet Color)
   Removes the currently selected color from the palette.

:bl-icon:`tria_up`/:bl-icon:`tria_down` (Move Pallet Color)
   Moves the selected color up/down one position.

:bl-icon:`sortsize` (Sort By)
   Sort Colors by Hue, Saturation, Value, Luminance.

.. _bpy.types.PaletteColor.color:

Color List
   Each color that belongs to the palette is presented in a list.
   Clicking on a color will change the brush's primary *Color* to that color.


Shortcuts
=========

- :kbd:`Ctrl-LMB` open the color picker to change color. See :ref:`ui-color-picker`.
- :kbd:`Backspace` reset the value.
