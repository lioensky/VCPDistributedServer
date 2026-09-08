.. index:: Grease Pencil Visual Effects; Blur Visual Effect
.. _bpy.types.ShaderFxBlur:

******************
Blur Visual Effect
******************

The *Blur* Visual Effect applies a Gaussian blur to the object.


Options
=======

.. figure:: /images/grease-pencil_visual-effects_blur_panel.png
   :align: right

   Blur Visual Effect.

Samples
   Number of blur samples (0 disabled the blur effect).

Use Depth of Field
   When enabled, the blur effect uses the focal plane distance of the actual camera to
   calculate the object blur. Only available in camera view.

Size X, Y
   Control the blur scale in pixels on the X and Y axis.

Rotation
   Control the Rotation of the blur.


Example
=======

.. list-table:: Blur Effect samples (Samples: 8).

   * - .. figure:: /images/grease-pencil_visual-effects_blur_factor-0.png
          :width: 200px

          Original Model.

     - .. figure:: /images/grease-pencil_visual-effects_blur_factor-10.png
          :width: 200px

          Factor: 10, 10.

     - .. figure:: /images/grease-pencil_visual-effects_blur_factor-50.png
          :width: 200px

          Factor: 50, 50.

     - .. figure:: /images/grease-pencil_visual-effects_blur_factor-100.png
          :width: 200px

          Factor: 100, 100.
