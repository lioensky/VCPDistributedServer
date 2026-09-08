.. _bpy.types.SceneEEVEE.bokeh:

**************
Depth of Field
**************

To render a scene, EEVEE uses a pinhole camera model which produces
a perfectly focused image of the scene. For an enhanced realism, EEVEE can simulate
the optical :term:`Depth of Field` using a post-process filter, and a sample-based method.
The optical settings are located in the :doc:`camera settings </render/cameras>` properties.
Whereas the quality of the effect can be controlled by the settings found in the present section.

.. note::

   In the 3D Viewport, depth of field only works while in Camera View.

The post-process method is computed in two passes.
The first pass is using a blur that fails to produce quality bokeh for highlights but works for the general case.
Followed by a second pass which is sprite-based and improves only the quality of very bright highlights.
That is because it is too slow to be applied on every part of the image.
So it just includes very bright isolated parts of the image such that are different from their surroundings.
Which pixels are being processed by second pass can be control with
the *Sprite Threshold* and *Neighbor Rejection* options.

Secondly the sample-based method works by randomizing the camera position for every sample.
It is more accurate but needs many samples to achieve a smooth result.
Accordingly the post-process blurring radius is scaled down to remove undersampling.
Yet some scenes might still need more post-process blur in order to remove the noticeable sample pattern.
This is exactly what the *Overblur* option does, but it will also reduce the bokeh shape sharpness.

.. reference::

   :Panel:     :menuselection:`Render --> Depth of Field`

Max Size
   Maximum size in pixels of the depth of field post-process effect (lower is faster).
   A value of 0 will disable the post-process effect but not the sample-based method.

Sprite Threshold
   Minimum brightness a pixel needs to have to be considered by the sprite-based depth of field.
   Higher values will improve the performance but will also reduce the quality of highlights.
   Brightness is in the scene's referred color space.

Neighbor Rejection
   Maximum intensity to consider when doing sprite neighborhood rejection.
   This should be set to a brightness value above which there is
   small visual differences to be noticeable after color management.
   Lower values will improve the performance but will also reduce the quality of highlights.
   Brightness is in the scene's referred color space.

.. _bpy.types.SceneEEVEE.use_bokeh_jittered:

Jitter Camera
   Randomize the camera position for every scene render sample to increase precision.
   Enabling this option can change the scene's actual sample count.

   .. note::

      Be aware that the actual sample count can grow quite rapidly.

   .. hint::

      The actual number of samples is computed by the following formula:

      .. math::

         sample\_count = (ring\_count^{2} + ring\_count) * 3 + 1

      where :math:`ring\_count` is the number of ring in the hexaweb pattern.
      The :math:`ring\_count` is chosen so that the entire pattern contains at least the number of
      samples set in the :doc:`Render Settings </render/eevee/render_settings/sampling>`.

Over-blur
   Scales the post-process depth of field radius to reduce artifacts. Higher values will soften the bokeh shape.

.. seealso:: :ref:`Limitations <eevee-limitations-dof>`.
