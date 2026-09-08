
*********
Thickness
*********

Controls the thickness of the Freestyle strokes.

.. figure:: /images/render_freestyle_parameter-editor_line-style_thickness_tab.png
   :align: center
   :width: 50%

   Line Style: Thickness.

Base Thickness
   The base thickness for this line style.

Thickness Position
   Control the position of stroke thickness from the original (backbone) stroke geometry. There are four choices:

   :Center:
      The thickness is evenly split to the left and right side of the stroke geometry.
   :Inside:
      The strokes are drawn within object boundary.
   :Outside:
      The strokes are drawn outside the object boundary.
   :Relative:
      Specifies the relative position by a number between 0.0 (inside) and 1.0 (outside),
      in the *Thickness Ratio* number field just below.

   .. note::

      The thickness position options are applied only to strokes of edge types
      *Silhouette* and *Border*,
      since these are the only edge types defined in terms of the object boundary.
      Strokes of other edge types are always drawn using the *Center* option.


Modifiers
=========

Common Options
--------------

Mix
   The modifier output can be mixed with the base property using the usual methods
   (see for example the :doc:`Mix compositing node </compositing/types/color/mix_color>`).
Influence
   How much the result of this modifier affects the current property.


Types
-----

- :doc:`/render/freestyle/view_layer/line_style/modifiers/thickness/along_stroke`
- :doc:`/render/freestyle/view_layer/line_style/modifiers/thickness/calligraphy`
- :doc:`/render/freestyle/view_layer/line_style/modifiers/thickness/crease_angle`
- :doc:`/render/freestyle/view_layer/line_style/modifiers/thickness/curvature_3d`
- :doc:`/render/freestyle/view_layer/line_style/modifiers/thickness/distance_from_camera`
- :doc:`/render/freestyle/view_layer/line_style/modifiers/thickness/distance_from_object`
- :doc:`/render/freestyle/view_layer/line_style/modifiers/thickness/material`
- :doc:`/render/freestyle/view_layer/line_style/modifiers/thickness/noise`
- :doc:`/render/freestyle/view_layer/line_style/modifiers/thickness/tangent`
