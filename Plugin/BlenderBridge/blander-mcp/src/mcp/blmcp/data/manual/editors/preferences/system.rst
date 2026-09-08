.. _bpy.types.PreferencesSystem:

******
System
******

The *System* section allows you to set graphics card options, memory limits & sound settings.

If your hardware does not support some of the options described on this page,
then they will either not be displayed or be corrected on startup.

.. figure:: /images/editors_preferences_section_system.webp

   Preferences System section.


.. _editors_preferences_cycles:

Cycles Render Devices
=====================

Changes the :ref:`Computing Device <bpy.types.CyclesRenderSettings.device>`
the :doc:`Cycles </render/cycles/index>` render engine uses to render images.
Cycles can use either the CPU or certain GPUs to render images,
for more information see the :doc:`GPU Rendering </render/cycles/gpu_rendering>` page.

:None:
   When set to *None* or when the only option is *None*:
   the CPU will be used as the computing device for Cycles.
:CUDA:
   If the system has a compatible NVIDIA CUDA device, it will be available as an option for rendering with Cycles.
:OptiX:
   If the system has a compatible NVIDIA OptiX device, it will be available as an option for rendering with Cycles.
:HIP:
   If the system has a compatible AMD HIP device, it will be available as an option for rendering with Cycles.
:oneAPI:
   If the system has a compatible Intel oneAPI device, it will be available as an option for rendering with Cycles.
:Metal:
   If the system has a compatible Apple Metal device, it will be available as an option for rendering with Cycles.

.. _prefs-system-cycles-distributive-memory:

Distribute Memory Across Devices
   Allocates resources across multiple GPUs rather than duplicating data,
   effectively freeing up space for larger scenes. Note that in order for this option to be available,
   the GPUs must be connected together with a high bandwidth communication protocol.

   Currently only NVLink on NVIDIA GPUs is supported.

Embree on GPU
   Enables the use of hardware ray tracing on Intel GPUs, providing better overall performance.

   Only supported with oneAPI rendering devices.

HIP RT
   Speeds up rendering by enabling AMD hardware ray tracing on RDNA2 and above.

   This feature is only available when using a *HIP* render device.

MetalRT
   MetalRT for ray tracing uses less memory for scenes which use curves extensively,
   and can give better performance in specific cases.

   :Off: Disable MetalRT (uses BVH2 layout for intersection queries).
   :On: Enable MetalRT for intersection queries.
   :Auto: Automatically pick the fastest intersection method.


.. _editors_preferences_display_graphics:

Display Graphics
================

Settings that control how Blender draws its user interface and other display graphics.
These options can influence performance and compatibility.

.. _bpy.types.PreferencesSystem.gpu_backend:

Backend
   Selects the graphics API used for drawing the interface and rendering display content.

   Changing the backend requires restarting Blender for the change to take effect.

   :OpenGL:
      Uses the OpenGL backend.
      This is the traditional backend, compatible with a wide range of systems.
   :Vulkan:
      Uses the Vulkan backend. Vulkan may offer improved performance and better support for modern GPU features,
      but compatibility may vary depending on the system and drivers.

.. _bpy.types.PreferencesSystem.gpu_preferred_device:

Device :guilabel:`Vulkan`
   Specifies which GPU device to use for display drawing operations.

   This setting is useful for systems with multiple GPUs (e.g., integrated + discrete)
   where you want to force Blender to use a specific GPU for UI rendering.

   Changing the backend requires restarting Blender for the change to take effect.

   :Auto:
      Automatically selects the most appropriate GPU based on system configuration and driver support.


Operating System Settings
=========================

Make this installation your default Blender (MS-Windows & Linux only).

On Linux, if Blender is installed from a package manager such as Snap,
file association is handled by the package manager.

.. _bpy.ops.preferences.associate_blend:

Register
   Make the currently in use Blender installation the default
   for generating thumbnails and the default for opening blend-files.

.. _bpy.ops.preferences.unassociate_blend:

Unregister
   Remove file association & thumbnailer.

.. _bpy.types.PreferencesSystem.register_all_users:

For All Users
   Register Blender for all users, requires escalated privileges.

.. admonition:: Linux Registration
   :class: note

   Files are setup files under: ``/usr/local`` for all users, otherwise ``~/.local`` is used.

   - A desktop file & icon is installed so the application is available in launchers.
   - A file association for ``*.blend`` is setup.
   - The thumbnailer is installed so blend-file thumbnails will be shown in file managers (**For All Users** only).


Network
=======

.. _bpy.types.PreferencesSystem.use_online_access:

Allow Online Access
   Allow Blender to access the internet.

   Add-ons that follow this setting will only connect to the internet if enabled.
   However, Blender cannot prevent third-party add-ons from violating this rule.

.. _bpy.types.PreferencesSystem.network_timeout:

Time Out
   The time (in seconds) that online operations may wait before timing out.

   Use the systems default when zero.

.. _bpy.types.PreferencesSystem.network_connection_limit:

Connection Limit
   The maximum number of simultaneous connections an online operation may make.

   Do not limit the number of connections when zero.


.. _prefs-system-memory-and-limits:

Memory & Limits
===============

.. _bpy.types.PreferencesEdit.undo_steps:

Undo Steps
   Number of Undo steps available.

.. _bpy.types.PreferencesEdit.undo_memory_limit:

Undo Memory Limit
   Maximum memory usage in Mb (0 is unlimited).

.. _bpy.types.PreferencesEdit.use_global_undo:

Global Undo
   This enables Blender to save actions done when you are **not** in *Edit Mode*.
   For example, duplicating objects, changing panel settings or switching between modes.

   .. warning::

      While disabling this option does save memory,
      it stops the :ref:`bpy.ops.screen.redo_last` panel from functioning,
      also preventing tool options from being changed in some cases.
      For typical usage, its best to keep this enabled.

.. seealso::

   :doc:`Read more about Undo and Redo options </interface/undo_redo>`.

.. _bpy.types.PreferencesSystem.scrollback:

Console Scroll-back Lines
   The number of lines, buffered in memory of the console window.
   Useful for debugging purposes and command-line rendering.

.. _bpy.types.PreferencesSystem.texture_time_out:

Texture Time Out
   Time since last access of a GL texture in seconds, after which it is freed.
   Set this to 0 to keep textures allocated.

   .. _bpy.types.PreferencesSystem.texture_collection_rate:

   Garbage Collection Rate
      Number of seconds between each run of the GL texture garbage collector.

.. _bpy.types.PreferencesSystem.vbo_time_out:

VBO Time Out
   Time since last access of a GL vertex buffer object (VBO) in seconds after which it is freed
   (set to 0 to keep VBO allocated).

   .. _bpy.types.PreferencesSystem.vbo_collection_rate:

   Garbage Collection Rate
      Number of seconds between each run of the GL vertex buffer object garbage collector.

.. _bpy.types.PreferencesSystem.shader_compilation_method:

Shader Compilation Method
   Defines the method used for compiling GPU shaders in parallel.

   - This option is not available on macOS and requires using OpenGL backend.
   - Changing this setting requires restarting Blender to take effect.

   :Thread:
      Uses multiple threads within a single process to compile shaders concurrently.
      This method is more memory-efficient but may be slower on some systems.
   :Subprocess:
      Uses multiple separate subprocesses to compile shaders in parallel.
      This can be faster, especially on systems with high core counts, but consumes significantly more RAM.

.. _bpy.types.PreferencesSystem.gpu_shader_workers:

Threads / Subprocesses
   The number of shader compilation threads or subprocesses to use.
   The maximum value is limited by the number of logical CPU cores on the system.

   Increasing the number can reduce shader compilation time at the cost of higher memory usage.
   A value of 0 lets Blender automatically choose a suitable number based on the system configuration.

   - This option is not available on macOS and requires using OpenGL backend.
   - Changing this setting requires restarting Blender to take effect.


.. _prefs-system-video-sequencer:

Video Sequencer
===============

.. _bpy.types.PreferencesSystem.memory_cache_limit:

Memory Cache Limit
   Upper limit of the Video Sequencer and Movie Clip Editor memory cache (in megabytes).
   For an optimal Clip editor and Sequencer performance, high values are recommended.

.. _bpy.types.PreferencesSystem.sequencer_proxy_setup:

Proxy Setup
   When and how :doc:`Proxies </editors/video_sequencer/sequencer/sidebar/proxy>` are created.

   :Automatic: Build proxies for added movie and image strips in each preview size.
   :Manual: Set up proxies manually.

.. seealso::

   :doc:`Sequencer Cache Properties </editors/video_sequencer/sequencer/sidebar/cache>`


.. _prefs-system-sound:

Sound
=====

This panel contains the sound settings for live playback
within Blender and are only available with a device other than *None*.
To control these settings for exporting sound
see the :ref:`Encoding Panel <render-output-video-encoding-panel>`
and :ref:`Audio Panel <data-scenes-audio>`.

.. _bpy.types.PreferencesSystem.audio_device:

Audio Device
   Sets the audio engine to use to process and output audio.

   :None:
      No audio playback support (audio strips can still be loaded and rendered normally).
   :CoreAudio:
      On macOS, CoreAudio is the native audio API.
      This is the default setting for macOS users and should be preferred.
   :PulseAudio:
      PulseAudio is the most commonly used sound server on modern Linux distributions.
      If PulseAudio is available, this should be the preferred setting on Linux.
   :WASAPI:
      On Windows, WASAPI is the native audio API introduced with Windows Vista.
      This is the default setting for Windows users and should be preferred.
   :Jack:
      High quality professional audio engine that needs a properly configured server running on your system.
      Supports accurate synchronization with other professional audio applications using Jack.
   :OpenAL:
      Available on all platforms in case the native engines do not work.
      The played back 3D audio might sound different than when rendered.
   :SDL:
      Uses Simple Direct Media Layer API from `libsdl.org <https://www.libsdl.org>`__
      which supports all platforms. Might be of lower quality and thus should only be used as backup.

.. _bpy.types.PreferencesSystem.audio_channels:

Channels
   The number of audio source "locations" to output.

   :Mono: Output a single audio channel.
   :Stereo: Output two audio channels; typically a left and right channel.
   :4 Channels: Output a four audio channels.
   :5.1 Surround:  Output a five audio channels with one :abbr:`LFE (low-frequency effects)` channel.
   :7.1 Surround: Output a seven audio channels with one :abbr:`LFE (low-frequency effects)` channel.

.. _bpy.types.PreferencesSystem.audio_mixing_buffer:

Mixing Buffer
   Sets the number of samples used by the audio mixing buffer.
   Higher buffer sizes can cause latency issues,
   but if you hear clicks or other problems, try to increase the size.

.. _bpy.types.PreferencesSystem.audio_sample_rate:

Sample Rate
   Sets the audio `sampling rate <https://en.wikipedia.org/wiki/Sampling_(signal_processing)#Sampling_rate>`__.

.. _bpy.types.PreferencesSystem.audio_sample_format:

Sample Format
   Sets the audio sample format.
