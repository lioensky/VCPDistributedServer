.. index:: Grease Pencil Visual Effects; Colorize Visual Effect
.. _bpy.types.ShaderFxColorize:

**********************
Colorize Visual Effect
**********************

The *Colorize* Visual Effect applies different preset colorizing effects to the object.


Options
=======

.. figure:: /images/grease-pencil_visual-effects_colorize_panel.png
   :align: right

   Blur Visual Effect.

Mode
   Grayscale
      Converts to a grayscale image.
   Sepia
      Converts to a sepia tone image.
   Duotone
      Converts to a posterize image with high contrast and brightness.

      Low Color
         Primary color.

      High Color
         Secondary color.
   Transparent
      Add color transparency.
   Custom
      Allows to define a tint custom color.

      Color
         Sets the tint color.

Factor
   Control the mix value.


Example
=======

.. list-table:: Colorize Effect samples.

   * - .. figure:: /images/grease-pencil_visual-effects_colorize_grayscale.png
          :width: 200px

          Mode: Grayscale.

     - .. figure:: /images/grease-pencil_visual-effects_colorize_sepia.png
          :width: 200px

          Mode: Sepia.

     - .. figure:: /images/grease-pencil_visual-effects_colorize_duotone.png
          :width: 200px

          Mode: Duotone.

     - .. figure:: /images/grease-pencil_visual-effects_colorize_transparent.png
          :width: 200px

          Mode: Transparent.
