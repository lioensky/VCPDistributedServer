
********
Sampling
********

EEVEE uses a process called Temporal Anti-Aliasing (TAA) which reduces :term:`Aliasing`.
TAA is sample based so the more samples the more aliasing is reduced at the cost of performance.

.. reference::

   :Panel:     :menuselection:`Render --> Sampling`


Viewport
========

.. _bpy.types.SceneEEVEE.taa_samples:

Samples
   The number of samples to use in the 3D Viewport.
   When setting this to zero the viewport will be resampled continuously.

.. _bpy.types.SceneEEVEE.use_taa_reprojection:

Temporal Reprojection
   Reduces noise while moving the viewport or during animation playback. Can leave some ghosting.

.. _bpy.types.SceneEEVEE.use_shadow_jitter_viewport:

Jittered Shadows
   Enable jittered shadows on the viewport.
   Jittered shadows are always enabled for final renders.
   This also affects any transparent shadows.


Render
======

.. _bpy.types.SceneEEVEE.taa_render_samples:

Samples
   The number of samples to use in the final render.


.. _bpy.types.SceneEEVEE.use_shadows:

Shadows
=======

.. _bpy.types.SceneEEVEE.shadow_ray_count:

Rays
   Number of rays to trace for each light.
   Higher values reduces the noise caused by random shadow sampling.

.. _bpy.types.SceneEEVEE.shadow_step_count:

Steps
   Number of shadow map sample per shadow ray.
   Higher step count results in softer shadows but have a higher cost.

.. _bpy.types.SceneEEVEE.use_volumetric_shadows:

Volumetric Shadows
   Approximate light absorption of the surrounding volume objects. This makes the volumes more opaque to light.
   This is a very computationally expensive option and has limitations.

   .. _bpy.types.SceneEEVEE.volumetric_shadow_samples:

   Steps
      Number of steps to compute volumetric shadowing.

   .. seealso:: :ref:`Volume Limitations <eevee-limitations-volumetrics>`.

.. _bpy.types.SceneEEVEE.shadow_resolution_scale:

Resolution
   Resolution percentage of shadow maps.


Advanced
========

.. _bpy.types.SceneEEVEE.light_threshold:

Light Threshold
   Minimum light intensity for a light to contribute to the lighting.
   Used to compute the distance at which to cut-off lights influence.
   Lower values improve performance.

   .. seealso::

      :ref:`Custom Distance <bpy.types.Light.use_custom_distance>` overrides this setting.
