.. index:: Grease Pencil Modifiers; Hue/Saturation Modifier
.. _bpy.types.GreasePencilColorModifier:

***********************
Hue/Saturation Modifier
***********************

The *Hue/Saturation* Modifier applies a color transformation to the object output color.


Options
=======

.. figure:: /images/grease-pencil_modifiers_color_hue-saturation_panel.png
   :align: right

   Hue/Saturation Modifier.

Mode
   The color transformation will be applied on the stroke and/or the fill color.

   Stroke & Fill, Stroke, Fill

Hue
   Specifies the hue rotation of the image. 360° are mapped to (0 to 1).
   The hue shifts of 0 (-180°) and 1 (+180°) have the same result.
Saturation
   A saturation of 0 removes hues from the image, resulting in a grayscale image.
   A shift greater than 1.0 increases saturation.
Value
   Value is the overall brightness of the image.
   De/Increasing values shift an image darker/lighter.


Influence
---------

See :ref:`grease-pencil-modifier-influence-filters`.
