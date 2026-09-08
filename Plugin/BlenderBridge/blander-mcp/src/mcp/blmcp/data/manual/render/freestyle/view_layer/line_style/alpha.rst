
*****
Alpha
*****

In this tab you control the alpha (transparency) of your strokes.

.. figure:: /images/render_freestyle_parameter-editor_line-style_alpha_tab.png
   :align: center
   :width: 50%

   Line Style: Alpha.

.. _bpy.types.FreestyleLineStyle.alpha:

Base Transparency
   The base alpha for this line style.


.. _bpy.ops.scene.freestyle_alpha_modifier_add:

Modifiers
=========

Common Options
--------------

Mix
   The modifier output can be mixed with the base property using the usual methods
   (see for example the :doc:`Mix compositing node </compositing/types/color/mix_color>`).
Influence
   How much the result of this modifier affects the current property.
Mapping
   Either a linear progression (from 0.0 to 1.0),
   or a custom mapping :ref:`curve <ui-curve-widget>`.

   .. note::

      Note the linear non-inverted option is equivalent to "do nothing",
      as original values from materials are already in the (0.0 to 1.0) range.
      That is the case for: Crease Angle, Curvature 3D, Material, Noise, Tangent.

Invert
   Inverts the *Mapping*.


Types
-----

- :doc:`/render/freestyle/view_layer/line_style/modifiers/alpha/along_stroke`
- :doc:`/render/freestyle/view_layer/line_style/modifiers/alpha/crease_angle`
- :doc:`/render/freestyle/view_layer/line_style/modifiers/alpha/curvature_3d`
- :doc:`/render/freestyle/view_layer/line_style/modifiers/alpha/distance_from_camera`
- :doc:`/render/freestyle/view_layer/line_style/modifiers/alpha/distance_from_object`
- :doc:`/render/freestyle/view_layer/line_style/modifiers/alpha/material`
- :doc:`/render/freestyle/view_layer/line_style/modifiers/alpha/noise`
- :doc:`/render/freestyle/view_layer/line_style/modifiers/alpha/tangent`
