PreferencesSystem(bpy_struct)
=============================

.. currentmodule:: bpy.types

base class --- :class:`bpy_struct`

.. class:: PreferencesSystem(bpy_struct)

   Graphics driver and operating system settings

   .. attribute:: anisotropic_filter

      Quality of anisotropic filtering (default ``'FILTER_2'``)

      :type: Literal['FILTER_0', 'FILTER_2', 'FILTER_4', 'FILTER_8', 'FILTER_16']

   .. attribute:: audio_channels

      Audio channel count (default ``'STEREO'``)

      - ``MONO``
        Mono -- Set audio channels to mono.
      - ``STEREO``
        Stereo -- Set audio channels to stereo.
      - ``SURROUND4``
        4 Channels -- Set audio channels to 4 channels.
      - ``SURROUND51``
        5.1 Surround -- Set audio channels to 5.1 surround sound.
      - ``SURROUND71``
        7.1 Surround -- Set audio channels to 7.1 surround sound.

      :type: Literal['MONO', 'STEREO', 'SURROUND4', 'SURROUND51', 'SURROUND71']

   .. attribute:: audio_device

      Audio output device (default ``'None'``)

      - ``None``
        None -- No device - there will be no audio output.

      :type: Literal['None']

   .. attribute:: audio_mixing_buffer

      Number of samples used by the audio mixing buffer (default ``'SAMPLES_2048'``)

      - ``SAMPLES_256``
        256 Samples -- Set audio mixing buffer size to 256 samples.
      - ``SAMPLES_512``
        512 Samples -- Set audio mixing buffer size to 512 samples.
      - ``SAMPLES_1024``
        1024 Samples -- Set audio mixing buffer size to 1024 samples.
      - ``SAMPLES_2048``
        2048 Samples -- Set audio mixing buffer size to 2048 samples.
      - ``SAMPLES_4096``
        4096 Samples -- Set audio mixing buffer size to 4096 samples.
      - ``SAMPLES_8192``
        8192 Samples -- Set audio mixing buffer size to 8192 samples.
      - ``SAMPLES_16384``
        16384 Samples -- Set audio mixing buffer size to 16384 samples.
      - ``SAMPLES_32768``
        32768 Samples -- Set audio mixing buffer size to 32768 samples.

      :type: Literal['SAMPLES_256', 'SAMPLES_512', 'SAMPLES_1024', 'SAMPLES_2048', 'SAMPLES_4096', 'SAMPLES_8192', 'SAMPLES_16384', 'SAMPLES_32768']

   .. attribute:: audio_sample_format

      Audio sample format (default ``'FLOAT'``)

      - ``U8``
        8-bit Unsigned -- Set audio sample format to 8-bit unsigned integer.
      - ``S16``
        16-bit Signed -- Set audio sample format to 16-bit signed integer.
      - ``S24``
        24-bit Signed -- Set audio sample format to 24-bit signed integer.
      - ``S32``
        32-bit Signed -- Set audio sample format to 32-bit signed integer.
      - ``FLOAT``
        32-bit Float -- Set audio sample format to 32-bit float.
      - ``DOUBLE``
        64-bit Float -- Set audio sample format to 64-bit float.

      :type: Literal['U8', 'S16', 'S24', 'S32', 'FLOAT', 'DOUBLE']

   .. attribute:: audio_sample_rate

      Audio sample rate (default ``'RATE_48000'``)

      - ``RATE_44100``
        44.1 kHz -- Set audio sampling rate to 44100 samples per second.
      - ``RATE_48000``
        48 kHz -- Set audio sampling rate to 48000 samples per second.
      - ``RATE_96000``
        96 kHz -- Set audio sampling rate to 96000 samples per second.
      - ``RATE_192000``
        192 kHz -- Set audio sampling rate to 192000 samples per second.

      :type: Literal['RATE_44100', 'RATE_48000', 'RATE_96000', 'RATE_192000']

   .. data:: dpi

      (in [-inf, inf], default 0, readonly)

      :type: int

   .. attribute:: gl_clip_alpha

      Clip alpha below this threshold in the 3D textured view (in [0, 1], default 0.004)

      :type: float

   .. attribute:: gl_texture_limit

      Limit the texture size to save graphics memory (default ``'CLAMP_OFF'``)

      :type: Literal['CLAMP_OFF', 'CLAMP_8192', 'CLAMP_4096', 'CLAMP_2048', 'CLAMP_1024', 'CLAMP_512', 'CLAMP_256', 'CLAMP_128']

   .. attribute:: gpu_backend

      GPU backend to use (requires restarting Blender for changes to take effect) (default ``'OPENGL'``)

      - ``OPENGL``
        OpenGL -- Use OpenGL backend.
      - ``METAL``
        Metal -- Use Metal backend.
      - ``VULKAN``
        Vulkan -- Use Vulkan backend.

      :type: Literal['OPENGL', 'METAL', 'VULKAN']

   .. attribute:: gpu_preferred_device

      Preferred device to select during detection (requires restarting Blender for changes to take effect) (default ``'AUTO'``)

      - ``AUTO``
        Auto -- Auto detect best GPU for running Blender.

      :type: Literal['AUTO']

   .. attribute:: gpu_shader_workers

      Number of shader compilation threads or subprocesses, clamped at the max threads supported by the CPU (requires restarting Blender for changes to take effect). A higher number increases the RAM usage while reducing compilation time. A value of 0 will use automatic configuration. (OpenGL only) (in [0, 32], default 0)

      :type: int

   .. attribute:: image_draw_method

      Method used for displaying images on the screen (default ``'AUTO'``)

      - ``AUTO``
        Automatic -- Automatically choose method based on GPU and image.
      - ``2DTEXTURE``
        2D Texture -- Use CPU for display transform and display image with 2D texture.
      - ``GLSL``
        GLSL -- Use GLSL shaders for display transform and display image with 2D texture.

      :type: Literal['AUTO', '2DTEXTURE', 'GLSL']

   .. data:: is_microsoft_store_install

      Whether this blender installation is a sandboxed Microsoft Store version (default False, readonly)

      :type: bool

   .. attribute:: light_ambient

      Color of the ambient light that uniformly lit the scene (array of 3 items, in [0, inf], default (0.0, 0.0, 0.0))

      :type: :class:`mathutils.Color`

   .. attribute:: memory_cache_limit

      Memory cache limit (in megabytes) (in [0, inf], default 4096)

      :type: int

   .. attribute:: network_connection_limit

      Limit the number of simultaneous internet connections online operations may make at once. Zero disables the limit. (in [0, 255], default 0)

      :type: int

   .. attribute:: network_timeout

      The time in seconds to wait for online operations before a connection may fail with a time-out error. Zero uses the systems default. (in [0, 255], default 0)

      :type: int

   .. data:: pixel_size

      (in [-inf, inf], default 1.0, readonly)

      :type: float

   .. attribute:: register_all_users

      Make this Blender version open blend files for all users. Requires elevated privileges. (default False)

      :type: bool

   .. attribute:: scrollback

      Maximum number of lines to store for the console buffer (in [32, 32768], default 256)

      :type: int

   .. attribute:: sequencer_proxy_setup

      When and how proxies are created (default ``'AUTOMATIC'``)

      - ``MANUAL``
        Manual -- Set up proxies manually.
      - ``AUTOMATIC``
        Automatic -- Build proxies for added movie and image strips in each preview size.

      :type: Literal['MANUAL', 'AUTOMATIC']

   .. attribute:: shader_compilation_method

      Compilation method used for compiling shaders in parallel. Subprocess requires a lot more RAM for each worker but might compile shaders faster on some systems. Requires restarting Blender for changes to take effect. (OpenGL only) (default ``'THREAD'``)

      - ``THREAD``
        Thread -- Use threads for compiling shaders.
      - ``SUBPROCESS``
        Subprocess -- Use subprocesses for compiling shaders.

      :type: Literal['THREAD', 'SUBPROCESS']

   .. data:: solid_lights

      Lights used to display objects in solid shading mode (default None, readonly)

      :type: :class:`bpy_prop_collection`\ [:class:`UserSolidLight`]

   .. attribute:: texture_collection_rate

      Number of seconds between each run of the GL texture garbage collector (in [1, 3600], default 60)

      :type: int

   .. attribute:: texture_time_out

      Time since last access of a GL texture in seconds after which it is freed (set to 0 to keep textures allocated) (in [0, 3600], default 120)

      :type: int

   .. data:: ui_line_width

      Suggested line thickness and point size in pixels, for add-ons displaying custom user interface elements, based on operating system settings and Blender UI scale (in [-inf, inf], default 1.0, readonly)

      :type: float

   .. data:: ui_scale

      Size multiplier to use when displaying custom user interface elements, so that they are scaled correctly on screens with different DPI. This value is based on operating system DPI settings and Blender display scale. (in [-inf, inf], default 0.0, readonly)

      :type: float

   .. attribute:: use_edit_mode_smooth_wire

      Enable edit mode edge smoothing, reducing aliasing (requires restart) (default True)

      :type: bool

   .. attribute:: use_gpu_subdivision

      Enable GPU acceleration for evaluating the last subdivision surface modifiers in the stack (default True)

      :type: bool

   .. attribute:: use_online_access

      Allow Blender to access the internet. Add-ons that follow this setting will only connect to the internet if enabled. However, Blender cannot prevent third-party add-ons from violating this rule. (default False)

      :type: bool

   .. attribute:: use_overlay_smooth_wire

      Enable overlay smooth wires, reducing aliasing (default True)

      :type: bool

   .. attribute:: use_region_overlap

      Display tool/property regions over the main region (default True)

      :type: bool

   .. attribute:: use_studio_light_edit

      View the result of the studio light editor in the viewport (default False)

      :type: bool

   .. attribute:: vbo_collection_rate

      Number of seconds between each run of the GL vertex buffer object garbage collector (in [1, 3600], default 60)

      :type: int

   .. attribute:: vbo_time_out

      Time since last access of a GL vertex buffer object in seconds after which it is freed (set to 0 to keep VBO allocated) (in [0, 3600], default 120)

      :type: int

   .. attribute:: viewport_aa

      Method of anti-aliasing in 3d viewport (default ``'8'``)

      - ``OFF``
        No Anti-Aliasing -- Scene will be rendering without any anti-aliasing.
      - ``FXAA``
        Single Pass Anti-Aliasing -- Scene will be rendered using a single pass anti-aliasing method (FXAA).
      - ``5``
        5 Samples -- Scene will be rendered using 5 anti-aliasing samples.
      - ``8``
        8 Samples -- Scene will be rendered using 8 anti-aliasing samples.
      - ``11``
        11 Samples -- Scene will be rendered using 11 anti-aliasing samples.
      - ``16``
        16 Samples -- Scene will be rendered using 16 anti-aliasing samples.
      - ``32``
        32 Samples -- Scene will be rendered using 32 anti-aliasing samples.

      :type: Literal['OFF', 'FXAA', '5', '8', '11', '16', '32']

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

   - :class:`Preferences.system`

