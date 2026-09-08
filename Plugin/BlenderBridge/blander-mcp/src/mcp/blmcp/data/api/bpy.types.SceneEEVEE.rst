SceneEEVEE(bpy_struct)
======================

.. currentmodule:: bpy.types

base class --- :class:`bpy_struct`

.. class:: SceneEEVEE(bpy_struct)

   Scene display settings for 3D viewport

   .. attribute:: bokeh_max_size

      Max size of the bokeh shape for the depth of field (lower is faster) (in [0, 2000], default 100.0)

      :type: float

   .. attribute:: bokeh_neighbor_max

      Maximum brightness to consider when rejecting bokeh sprites based on neighborhood (lower is faster) (in [0, 100000], default 10.0)

      :type: float

   .. attribute:: bokeh_overblur

      Apply blur to each jittered sample to reduce under-sampling artifacts (in [0, 100], default 5.0)

      :type: float

   .. attribute:: bokeh_threshold

      Brightness threshold for using sprite base depth of field (in [0, 100000], default 1.0)

      :type: float

   .. attribute:: clamp_surface_direct

      If non-zero, the maximum value for lights contribution on a surface. Higher values will be scaled down to avoid too much noise and slow convergence at the cost of accuracy. Used by light objects. (in [0, inf], default 0.0)

      :type: float

   .. attribute:: clamp_surface_indirect

      If non-zero, the maximum value for indirect lighting on surface. Higher values will be scaled down to avoid too much noise and slow convergence at the cost of accuracy. Used by ray-tracing and light-probes. (in [0, inf], default 10.0)

      :type: float

   .. attribute:: clamp_volume_direct

      If non-zero, the maximum value for lights contribution in volumes. Higher values will be scaled down to avoid too much noise and slow convergence at the cost of accuracy. Used by light objects. (in [0, inf], default 0.0)

      :type: float

   .. attribute:: clamp_volume_indirect

      If non-zero, the maximum value for indirect lighting in volumes. Higher values will be scaled down to avoid too much noise and slow convergence at the cost of accuracy. Used by light-probes. (in [0, inf], default 0.0)

      :type: float

   .. attribute:: direct_light_intensity

      Scale the contribution of direct lighting (in [0, inf], default 1.0)

      :type: float

   .. attribute:: fast_gi_bias

      Bias the shading normal to reduce self intersection artifacts (in [0, 1], default 0.05)

      :type: float

   .. attribute:: fast_gi_distance

      If non-zero, the maximum distance at which other surfaces will contribute to the fast GI approximation (in [0, 100000], default 0.0)

      :type: float

   .. attribute:: fast_gi_method

      Fast GI approximation method (default ``'GLOBAL_ILLUMINATION'``)

      - ``AMBIENT_OCCLUSION_ONLY``
        Ambient Occlusion -- Use ambient occlusion instead of full global illumination.
      - ``GLOBAL_ILLUMINATION``
        Global Illumination -- Compute global illumination taking into account light bouncing off surrounding objects.

      :type: Literal['AMBIENT_OCCLUSION_ONLY', 'GLOBAL_ILLUMINATION']

   .. attribute:: fast_gi_quality

      Precision of the fast GI ray marching (in [0, 1], default 0.25)

      :type: float

   .. attribute:: fast_gi_ray_count

      Amount of GI ray to trace for each pixel (in [1, 16], default 2)

      :type: int

   .. attribute:: fast_gi_resolution

      Control the quality of the fast GI lighting. Higher resolution uses more memory. (default ``'2'``)

      - ``1``
        1:1 -- Full resolution.
      - ``2``
        1:2 -- Render this effect at 50% render resolution.
      - ``4``
        1:4 -- Render this effect at 25% render resolution.
      - ``8``
        1:8 -- Render this effect at 12.5% render resolution.
      - ``16``
        1:16 -- Render this effect at 6.25% render resolution.

      :type: Literal['1', '2', '4', '8', '16']

   .. attribute:: fast_gi_step_count

      Amount of screen sample per GI ray (in [1, 64], default 8)

      :type: int

   .. attribute:: fast_gi_thickness_far

      Angular thickness of the surfaces when computing fast GI and ambient occlusion. Reduces energy loss and missing occlusion of far geometry. (in [0.0174533, 3.14159], default 0.785398)

      :type: float

   .. attribute:: fast_gi_thickness_near

      Geometric thickness of the surfaces when computing fast GI and ambient occlusion. Reduces light leaking and missing contact occlusion. (in [0, 100000], default 0.25)

      :type: float

   .. attribute:: gi_cubemap_resolution

      Size of every cubemaps (default ``'512'``)

      :type: Literal['128', '256', '512', '1024', '2048', '4096']

   .. attribute:: gi_diffuse_bounces

      Number of times the light is reinjected inside light grids, 0 disable indirect diffuse light (in [0, inf], default 3)

      :type: int

   .. attribute:: gi_glossy_clamp

      Clamp pixel intensity to reduce noise inside glossy reflections from reflection cubemaps (0 to disable) (in [0, inf], default 0.0)

      :type: float

   .. attribute:: gi_irradiance_pool_size

      Size of the irradiance pool, a bigger pool size allows for more irradiance grid in the scene but might not fit into GPU memory and decrease performance (default ``'16'``)

      :type: Literal['16', '32', '64', '128', '256', '512', '1024']

   .. attribute:: gi_visibility_resolution

      Size of the shadow map applied to each irradiance sample (default ``'32'``)

      :type: Literal['8', '16', '32', '64']

   .. attribute:: indirect_light_intensity

      Scale the contribution of indirect lighting (in [0, inf], default 1.0)

      :type: float

   .. attribute:: light_threshold

      Minimum light intensity for a light to contribute to the lighting (in [0, inf], default 0.01)

      :type: float

   .. attribute:: motion_blur_depth_scale

      Lower values will reduce background bleeding onto foreground elements (in [0, inf], default 100.0)

      :type: float

   .. attribute:: motion_blur_max

      Maximum blur distance a pixel can spread over (in [0, 2048], default 32)

      :type: int

   .. attribute:: motion_blur_steps

      Controls accuracy of motion blur, more steps means longer render time (in [1, inf], default 1)

      :type: int

   .. attribute:: overscan_size

      Percentage of render size to add as overscan to the internal render buffers (in [0, 50], default 3.0)

      :type: float

   .. attribute:: ray_tracing_method

      Select the tracing method used to find scene-ray intersections (default ``'SCREEN'``)

      - ``PROBE``
        Light Probe -- Use light probes to find scene intersection.
      - ``SCREEN``
        Screen-Trace -- Raytrace against the depth buffer. Fallback to light probes for invalid rays..

      :type: Literal['PROBE', 'SCREEN']

   .. data:: ray_tracing_options

      EEVEE settings for tracing reflections (readonly)

      :type: :class:`RaytraceEEVEE` | None

   .. attribute:: shadow_pool_size

      Size of the shadow pool, a bigger pool size allows for more shadows in the scene but might not fit into GPU memory (default ``'512'``)

      :type: Literal['16', '32', '64', '128', '256', '512', '1024']

   .. attribute:: shadow_ray_count

      Amount of shadow ray to trace for each light (in [1, 4], default 1)

      :type: int

   .. attribute:: shadow_resolution_scale

      Resolution percentage of shadow maps (in [0, 1], default 1.0)

      :type: float

   .. attribute:: shadow_step_count

      Amount of shadow map sample per shadow ray (in [1, 16], default 6)

      :type: int

   .. attribute:: taa_render_samples

      Number of samples per pixel for rendering (in [1, inf], default 64)

      :type: int

   .. attribute:: taa_samples

      Number of samples, unlimited if 0 (in [0, inf], default 16)

      :type: int

   .. attribute:: use_bokeh_jittered

      Jitter camera position to create accurate blurring using render samples (only for final render) (default False)

      :type: bool

   .. attribute:: use_fast_gi

      Use faster global illumination technique for high roughness surfaces (default False)

      :type: bool

   .. attribute:: use_overscan

      Internally render past the image border to avoid screen-space effects disappearing (default False)

      :type: bool

   .. attribute:: use_raytracing

      Enable the ray-tracing module (default False)

      :type: bool

   .. attribute:: use_shadow_jitter_viewport

      Enable jittered shadows on the viewport. (Jittered shadows are always enabled for final renders). (default False)

      :type: bool

   .. attribute:: use_shadows

      Enable shadow casting from lights (default True)

      :type: bool

   .. attribute:: use_taa_reprojection

      Denoise image using temporal reprojection (can leave some ghosting) (default True)

      :type: bool

   .. attribute:: use_volume_custom_range

      Enable custom start and end clip distances for volume computation (default False)

      :type: bool

   .. attribute:: use_volumetric_shadows

      Cast shadows from volumetric materials onto volumetric materials (Very expensive) (default False)

      :type: bool

   .. attribute:: volumetric_end

      End distance of the volumetric effect (in [1e-06, inf], default 100.0)

      :type: float

   .. attribute:: volumetric_light_clamp

      Maximum light contribution, reducing noise (in [0, inf], default 0.0)

      :type: float

   .. attribute:: volumetric_ray_depth

      Maximum surface intersection count used by the accurate volume intersection method. Will create artifact if it is exceeded. Higher count increases VRAM usage. (in [1, 16], default 16)

      :type: int

   .. attribute:: volumetric_sample_distribution

      Distribute more samples closer to the camera (in [0, 1], default 0.8)

      :type: float

   .. attribute:: volumetric_samples

      Number of steps to compute volumetric effects. Higher step count increase VRAM usage and quality. (in [1, 256], default 64)

      :type: int

   .. attribute:: volumetric_shadow_samples

      Number of samples to compute volumetric shadowing (in [1, 128], default 16)

      :type: int

   .. attribute:: volumetric_start

      Start distance of the volumetric effect (in [1e-06, inf], default 0.1)

      :type: float

   .. attribute:: volumetric_tile_size

      Control the quality of the volumetric effects. Higher resolution uses more memory. (default ``'8'``)

      - ``1``
        1:1 -- Full resolution.
      - ``2``
        1:2 -- Render this effect at 50% render resolution.
      - ``4``
        1:4 -- Render this effect at 25% render resolution.
      - ``8``
        1:8 -- Render this effect at 12.5% render resolution.
      - ``16``
        1:16 -- Render this effect at 6.25% render resolution.

      :type: Literal['1', '2', '4', '8', '16']

   .. classmethod:: bl_rna_get_subclass(id, default=None, /)
   
      :param id: The RNA type identifier.
      :type id: str
      :param default: The value to return when not found.
      :type default: :class:`bpy.types.Struct` | None
      :return: The RNA type or default when not found.
      :rtype: :class:`bpy.types.Struct`


   .. classmethod:: bl_rna_get_subclass_py(id, default=None, /)
   
      :param id: The RNA type identifier.
      :type id: str
      :param default: The value to return when not found.
      :type default: type | None
      :return: The class or default when not found.
      :rtype: type


Inherited Properties
--------------------

.. hlist::
   :columns: 2

   - :class:`bpy_struct.id_data`

Inherited Functions
-------------------

.. hlist::
   :columns: 2

   - :class:`bpy_struct.as_pointer`
   - :class:`bpy_struct.driver_add`
   - :class:`bpy_struct.driver_remove`
   - :class:`bpy_struct.get`
   - :class:`bpy_struct.id_properties_clear`
   - :class:`bpy_struct.id_properties_ensure`
   - :class:`bpy_struct.id_properties_ui`
   - :class:`bpy_struct.is_property_hidden`
   - :class:`bpy_struct.is_property_overridable_library`
   - :class:`bpy_struct.is_property_readonly`
   - :class:`bpy_struct.is_property_set`
   - :class:`bpy_struct.items`
   - :class:`bpy_struct.keyframe_delete`
   - :class:`bpy_struct.keyframe_insert`
   - :class:`bpy_struct.keys`
   - :class:`bpy_struct.path_from_id`
   - :class:`bpy_struct.path_from_module`
   - :class:`bpy_struct.path_resolve`
   - :class:`bpy_struct.pop`
   - :class:`bpy_struct.property_overridable_library_set`
   - :class:`bpy_struct.property_unset`
   - :class:`bpy_struct.rna_ancestors`
   - :class:`bpy_struct.type_recast`
   - :class:`bpy_struct.values`

References
----------

.. hlist::
   :columns: 2

   - :class:`Scene.eevee`

