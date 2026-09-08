.. _bpy.types.SceneEEVEE.motion_blur:

***********
Motion Blur
***********

.. reference::

   :Panel:     :menuselection:`Render --> Motion Blur`

Blender's animations are by default rendered as a sequence of *perfectly still* images.
While great for stop-motion and time-lapses, this is unrealistic, since fast-moving
objects do appear to be blurred in the direction of motion,
both in a movie frame and in a photograph from a real-world camera.

.. note::

   Motion blur is only visible in the viewport during animation playback and uses a simpler
   algorithm than final render. Same thing applies to :ref:`Viewport Renders <bpy.ops.render.opengl>`.

Position
   Controls at what point the shutter opens in relation to the current frame.

   :Start on Frame: Shutter is starting to open at the current frame.
   :Center on Frame: Shutter is fully opened at the current frame.
   :End on Frame: Shutter is fully closed at the current frame.

Shutter
   Time (in frames) taken between shutter open and close.

Bleeding Bias
   Used by the post-process blur to avoid blurring the background over the foreground.
   Lower values will reduce background bleeding onto foreground elements.

Max Blur
   Max Blur is intended to act as an optimization tool by
   limiting the number of pixels across which the blur is calculated.

Steps
   This controls the number of steps used by the accumulation blur and thus its accuracy.
   More steps means longer render time.

   .. note::

      When using multiple time steps, the render sample count is rounded up to the next multiple
      of steps to ensure even distribution of samples across steps.
      This can lower the quality of :ref:`jitter camera depth of field <bpy.types.SceneEEVEE.use_bokeh_jittered>`.
      Increasing the number of :ref:`viewport or render samples <bpy.types.SceneEEVEE.taa_samples>` will get the
      quality back.

   EEVEE splits the render into multiple time steps and accumulates the result
   which is known as Accumulation Motion Blur.
   This technique is precise but requires many steps for clean gradients.
   This is used in combination with the post-process blur to handle the inter-step gaps.
   Each step corresponds to a full scene re-evaluation and can add a lot of overhead to the render time.
   By adding more steps you can also reduce the *Max Blur* options because the post-process blur
   has to cover a smaller distance.

Shutter Curve
   Use a custom shutter curve.


Example
=======

.. _fig-render-motion-blur-properties-example:

.. list-table::

   * - .. figure:: /images/render_eevee_render-settings_motion-blur_1step-nofx.png
          :width: 310px

          No motion blur.

     - .. figure:: /images/render_eevee_render-settings_motion-blur_1step-fx.png
          :width: 310px

          Only post-process blur.

   * - .. figure:: /images/render_eevee_render-settings_motion-blur_4step-nofx.png
          :width: 310px

          4 time steps without post-process blur.

     - .. figure:: /images/render_eevee_render-settings_motion-blur_4step-fx.png
          :width: 310px

          4 time steps with post-process blur.

   * - .. figure:: /images/render_eevee_render-settings_motion-blur_32step-nofx.png
          :width: 310px

          32 time steps without post-process blur.

     - .. figure:: /images/render_eevee_render-settings_motion-blur_32step-fx.png
          :width: 310px

          32 time steps with post-process blur.
