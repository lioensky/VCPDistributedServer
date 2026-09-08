.. index:: Grease Pencil Visual Effects; Glow Visual Effect
.. _bpy.types.ShaderFxGlow:

******************
Glow Visual Effect
******************

The *Glow* Visual Effect add a glowing rim around the object.


Options
=======

.. figure:: /images/grease-pencil_visual-effects_glow_panel.png
   :align: center

   Glow Visual Effect.

Mode
   Determines the mode for the glow effect.

   :Luminance:
      The glow light illuminates the entire object.
   :Color:
      The glow light only affect a single color.

      Select Color
         Allows to select a single color to apply the glow light.

Threshold
   Limits the colors affected by the glow light. (A value of 1 means no colors affected.)

Glow Color
   Defines the glow color.

Blend Mode
   The mask blending operation to perform. See :term:`Color Blend Modes`.

Opacity
   Control the Opacity of the glow over the object.

Size X, Y
   Control the glow scale in pixels on the X and Y axis.

Rotation
   Control the Rotation of the glow.

Samples
   Number of Blur samples (0 disabled the blur effect).

Glow Under
   When enabled, glow only affects alpha areas.


Example
=======

.. list-table:: Glow Effect samples.

   * - .. figure:: /images/grease-pencil_visual-effects_glow_original.png
          :width: 200px

          Original image.

     - .. figure:: /images/grease-pencil_visual-effects_glow_luminance.png
          :width: 200px

          Mode: Luminance.

     - .. figure:: /images/grease-pencil_visual-effects_glow_luminance-alpha.png
          :width: 200px

          Mode: Luminance (Glow Under).

     - .. figure:: /images/grease-pencil_visual-effects_glow_color.png
          :width: 200px

          Mode: Color (Black lines).
