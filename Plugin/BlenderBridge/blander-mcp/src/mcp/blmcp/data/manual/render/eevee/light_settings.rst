
**********************
Light Settings (EEVEE)
**********************

.. reference::

   :Panel:     :menuselection:`Properties --> Object Data`
               and :menuselection:`Shader Editor --> Sidebar --> Options`

Besides lighting from the background and materials with emission shaders,
lights are another way to add light into the scene.
The difference is that they are not directly visible in the rendered image,
and can be more easily managed as objects of their own type.

See :doc:`Light settings </render/lights/light_object>` for settings common to all renderers.


.. _bpy.types.Light.shadow:

Shadow
======

EEVEE uses a technique called *Virtual Shadow Mapping* along with *Shadow Map Raytracing*.
*Virtual Shadow Mapping* produces more accurate results than traditional shadow mapping by putting resolution
only where it is needed. It also includes a very efficient caching mechanism.
This technique offers better performance than ray tracing and is compatible
with any :ref:`Render Method <bpy.types.Material.surface_render_method>`.

.. tip::

   - The error message *Shadow buffer full* means that the system cannot allocate enough shadow memory.
     Increasing the :ref:`Shadow Pool Size <bpy.types.SceneEEVEE.shadow_pool_size>` or
     the :ref:`Resolution Limit <bpy.types.Light.shadow_maximum_resolution>` on some lights
     can fix the issue. Otherwise, the only workaround is to disable shadow casting on some lights.
   - *Shadow Map Raytracing* can be tweaked in the :ref:`Render Settings <bpy.types.SceneEEVEE.use_shadows>`.
   - Turning on :ref:`Jitter <bpy.types.Light.use_shadow_jitter>` can reduce the light leaking artifacts
     caused by large lights and *Shadow Map Raytracing*.

.. seealso:: :ref:`Limitations <eevee-limitations-shadows>`.

.. _bpy.types.Light.use_shadow_jitter:

Jitter
   Enable jittered soft shadows to increase shadow precision.
   Has a high performance impact as the shadow map cannot be cached and needs to be updated for each render sample.

   .. note::

      The effect isn't visible by default in the viewport.
      See :ref:`render settings <bpy.types.SceneEEVEE.use_shadow_jitter_viewport>`.

.. _bpy.types.Light.shadow_jitter_overblur:

Overblur
   Apply shadow tracing to each jittered sample to reduce under-sampling artifacts.

   .. note::

      Any value higher than zero will result in a blurrier shadow and is not physically correct.

.. _bpy.types.Light.shadow_filter_radius:

Filter
   Blur shadow aliasing using :abbr:`PCF (Percentage Closer Filtering)` with a circular kernel.
   The effective world scale of the filter depends on the shadow map resolution at the shadowed pixel position.

   .. note::

      Any value bigger than 1px will increase the chances of light leaking artifacts.

.. _bpy.types.Light.shadow_maximum_resolution:

Resolution Limit
   Minimum size of a shadow map pixel. Higher values use less memory at the cost of shadow quality.
   Higher values also speed-up rendering of heavy scenes.
   Each shadow is scaled depending on the shadowed pixel on screen. This can create very sharp shadows
   but also requires a lot of memory if the shadowed pixel is close to the camera.
   This property limits the maximum amount of detail that the shadow map can capture.

   .. note::

      Reducing the shadow map resolution will increase the chances of light leaking artifacts.

.. _bpy.types.Light.use_absolute_resolution:

Absolute Resolution Limit
   Limit the resolution at 1 unit from the light origin instead of relative to the shadowed pixel.
   This makes :ref:`Resolution Limit <bpy.types.Light.shadow_maximum_resolution>`
   act as a regular shadow map pixel size.

   .. hint::

      With this option enabled, the following equation can be used to set the *Resolution Limit*
      with a desired resolution:

      .. math::

         resolution\_limit = 2 * \sqrt{2} / resolution

      The :math:`2 * \sqrt{2}` refers to the unit cube diagonal and
      :math:`resolution` refers to the desired resolution (e.g. 1024px).

   .. note::

      The setting :ref:`Absolute Resolution Limit <bpy.types.Light.use_absolute_resolution>`
      does not exist for Sun Light.


Influence
=========

These parameters modulate the intensity of the light depending on the shader type.
These are meant for artistic control, and any value other than 1.0 breaks
:abbr:`PBR (Physically Based Rendering)` rules.

.. _bpy.types.Light.diffuse_factor:

Diffuse
   Diffuse reflection intensity multiplier.

.. _bpy.types.Light.specular_factor:

Glossy
   Glossy light intensity multiplier.

.. _bpy.types.Light.transmission_factor:

Transmission
   Transmission light intensity multiplier.

.. _bpy.types.Light.volume_factor:

Volume Scatter
   Volume light intensity multiplier.


.. _bpy.types.Light.use_custom_distance:

Custom Distance
===============

If enabled, uses :ref:`Distance <bpy.types.Light.cutoff_distance>` as the custom attenuation distance
instead of global Light Threshold. In order to avoid long setup times, this distance is first computed
automatically based on a light threshold.
The distance is computed at the light origin and using the inverse square falloff.

.. _bpy.types.Light.cutoff_distance:

Distance
   Specifies where light influence will be set to 0.

.. note::

   The setting :ref:`Custom Distance <bpy.types.Light.use_custom_distance>` does not exist for Sun Light.

.. seealso::

   Global :ref:`Light Threshold <bpy.types.SceneEEVEE.light_threshold>`.
