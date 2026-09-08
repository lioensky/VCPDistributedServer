.. _bpy.types.LineStyle*Modifier_Noise:
.. Editor's Note: This page gets copied into:
   :doc:`</render/freestyle/view_layer/line_style/modifiers/alpha/noise>`
   :doc:`</render/freestyle/view_layer/line_style/modifiers/thickness/noise>`
.. --- copy below this line ---

*****
Noise
*****

The *Noise* modifier uses a pseudo-random number generator to variably distribute the property along the stroke.

Amplitude
   The maximum value of the noise. A higher amplitude means a less transparent (more solid) stroke.
Period
   The period of the noise. This means how quickly the property value can change.
   A higher value means a more smoothly changing color along the stroke.
Seed
   Seed used by the pseudo-random number generator.

Asymmetric :guilabel:`Thickness only`
   Allows the thickness to be distributed unevenly at every point.
   Internally, the stroke is represented as a backbone with a thickness to the right and left side.
   All other thickness shaders make sure that the left and right thickness values are equal.
   For the Noise shader however, a meaningful (and good-looking) result
   can be created by assigning different values to either side of the backbone.

.. figure:: /images/render_freestyle_parameter-editor_line-style_modifiers_color_noise_thickness-noise-example.png
   :align: center
   :width: 50%

   Effect generated with a noise thickness modifier using asymmetric thickness.
