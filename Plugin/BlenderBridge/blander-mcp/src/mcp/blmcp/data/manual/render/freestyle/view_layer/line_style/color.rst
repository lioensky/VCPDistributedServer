
*****
Color
*****

In this tab you control the color of your strokes.

.. figure:: /images/render_freestyle_parameter-editor_line-style_color_tab.png
   :align: center
   :width: 50%

   Line Style: Color.

.. _bpy.types.FreestyleLineStyle.color:

Base Color
   The base color for this line style.


.. _bpy.ops.scene.freestyle_color_modifier_add:

Modifiers
=========

Common Options
--------------

Mix
   The modifier output can be mixed with the base property using the usual methods
   (see for example the :doc:`Mix compositing node </compositing/types/color/mix_color>`).
Influence
   How much the result of this modifier affects the current property.
Color Ramp
   Each modifier has :ref:`color ramp <ui-color-ramp-widget>` that maps the property to a stroke color.


Types
-----

- :doc:`/render/freestyle/view_layer/line_style/modifiers/color/along_stroke`
- :doc:`/render/freestyle/view_layer/line_style/modifiers/color/crease_angle`
- :doc:`/render/freestyle/view_layer/line_style/modifiers/color/curvature_3d`
- :doc:`/render/freestyle/view_layer/line_style/modifiers/color/distance_from_camera`
- :doc:`/render/freestyle/view_layer/line_style/modifiers/color/distance_from_object`
- :doc:`/render/freestyle/view_layer/line_style/modifiers/color/material`
- :doc:`/render/freestyle/view_layer/line_style/modifiers/color/noise`
- :doc:`/render/freestyle/view_layer/line_style/modifiers/color/tangent`
