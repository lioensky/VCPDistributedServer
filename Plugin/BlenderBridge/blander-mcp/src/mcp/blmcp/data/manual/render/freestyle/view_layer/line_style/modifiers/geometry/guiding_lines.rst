.. _bpy.types.LineStyleGeometryModifier_GuidingLines:

*************
Guiding Lines
*************

The *Guiding Lines* modifier replaces a stroke by a straight line connecting both of its ends.

Offset
   Offset the start and end points along the original stroke, before generating the new straight one.

This modifier will produce reasonable results when strokes are short enough,
because shorter strokes are more likely to be well approximated by straight lines.
Therefore, it is recommended to use this modifier together with one of the splitting options
(by 2D angle or by 2D length) from the *Strokes* panel.

.. figure:: /images/render_freestyle_parameter-editor_line-style_modifiers_geometry_guiding-lines_example.png
   :width: 50%
   :align: center

   Guiding Lines modifier Demo by T.K.
   (`blend-file <https://archive.blender.org/wiki/2015/index.php/File:Toycar_Guiding_Line.zip>`__).
