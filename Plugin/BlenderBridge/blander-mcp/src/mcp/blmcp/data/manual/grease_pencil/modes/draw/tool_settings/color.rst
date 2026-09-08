.. _grease-pencil-draw-color:

*****
Color
*****

.. _bpy.types.GpPaint.color_mode:

Paint Mode
   Controls the source of the stroke color.
   The mode can be pinned to the brush by enabling the Pin icon in the Tool Settings header.

   :Material: Use the stroke/fill base color material.
   :Color Attribute: Use Color Attribute.

Color Picker
   Sets the primary brush color.

Color, Secondary Color
   The color of the brush. See :ref:`ui-color-picker`.

.. _bpy.types.BrushGpencilSettings.vertex_mode:

Mode
   The color transformation will be applied on the stroke and/or the fill color.

   :Stroke: Only paint over strokes.
   :Fill: Only paint over fill areas.
   :Stroke & Fill: Paint over strokes and fill areas.

.. _bpy.types.BrushGpencilSettings.vertex_color_factor:

Mix Factor
   Mixing factor between the selected color and the base material color.


Palette
-------

Active Color Palette. See :ref:`bpy.types.PaletteColor`.
