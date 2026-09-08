.. _bpy.types.CyclesRenderSettings:

###################
  Render Settings
###################

.. reference::

   :Panel:     :menuselection:`Render`

.. _bpy.types.CyclesRenderSettings.device:

Device
   Specifies the compute device used for rendering in Cycles.
   The choice of device can significantly affect render performance, *GPU Compute* is often faster .

   :CPU:
      Render using the system's central processing unit. This mode is compatible with all Cycles features.
      The number of CPU threads used can be changed in the
      :doc:`Performance Properties </render/cycles/render_settings/performance>`.
   :GPU Compute:
      Render using one or more graphics processing units (GPUs) through the compute backend
      and devices selected in the :ref:`editors_preferences_cycles`.
      Depending on the backend, it may be possible to use both CPU and GPU devices simultaneously.

      For more details, including setup instructions, device compatibility, and known limitations,
      see :doc:`/render/cycles/gpu_rendering`.

   .. note::

      GPU rendering may have limitations compared to CPU rendering, depending on the backend.

   .. seealso::

      :ref:`Denoising <bpy.types.cyclesrendersettings.denoising_use_gpu>`
      and :ref:`Compositing <bpy.types.RenderSettings.compositor_device>` have their own device selection.

.. _bpy.types.CyclesRenderSettings.shading_system:

Open Shading Language
   Enables the use of :doc:`/render/cycles/osl/index` which allows custom shading using shader scripts.
   When OSL is enabled, you can:

   - Use OSL shader nodes in materials using the :doc:`Script Node </render/shader_nodes/utilities/script>`.
   - Write custom shading logic that is not possible with built-in Cycles nodes.

   Limitations:

   - OSL is supported only when rendering with the *CPU* or with the
     :ref:`OptiX <render-cycles-gpu-optix>` GPU Compute backend.
   - Rendering performance is typically slower than with built-in nodes due to shader compilation and interpretation.
   - Some features, such as baking and certain volume shaders, may not work with OSL.

.. toctree::
   :maxdepth: 2

   sampling.rst
   light_paths.rst
   volumes.rst
   subdivision.rst
   hair.rst
   simplify.rst
   motion_blur.rst
   film.rst
   performance.rst
   grease_pencil.rst
