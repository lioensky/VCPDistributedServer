********
Sampling
********

.. reference::

   :Panel:     :menuselection:`Render --> Sampling`

Sampling is the process of tracing rays from the camera into the scene and
bouncing them around until they reach a light source such as a Light object,
an emissive mesh, or the world background. The algorithm for this is known
as the integrator.

.. _bpy.types.CyclesRenderSettings.preview_samples:

Viewport (Max) Samples
   The number of paths to trace per pixel in the 3D Viewport
   (when using the *Rendered* :doc:`shading mode </editors/3dview/display/shading>`).
   Setting this value to zero enables indefinite sampling.

.. _bpy.types.CyclesRenderSettings.samples:

Render (Max) Samples
   The number of paths to trace per pixel in the final render.
   A higher number results in a cleaner image at the cost of a longer render time.

.. _bpy.types.CyclesRenderSettings.time_limit:

Time Limit
   Stops rendering if the time exceeds the limit, even if the desired sample count
   hasn't been reached yet. Setting this value to zero disables the limit.

   .. note:: The time limit does not include pre-render processing time, only render time.


.. _bpy.types.CyclesRenderSettings.use_adaptive_sampling:

Adaptive Sampling
=================

If the *Noise Threshold* checkbox is enabled, Cycles will use adaptive sampling,
cutting short the sampling process in areas that have become less noisy than the
specified threshold value -- in other words, not wasting time further refining
areas that already look good enough. For example, hair on a character may need many samples,
but the background may only need few.

.. _bpy.types.CyclesRenderSettings.adaptive_threshold:
.. _bpy.types.CyclesRenderSettings.preview_adaptive_threshold:

Noise Threshold
   The threshold to decide whether to continue sampling a pixel.
   Typical values are in the range from 0.1 to 0.001, with lower values meaning better
   quality but longer render times.
   Setting this to 0 makes Cycles guess an automatic value based on the total sample count.

.. _bpy.types.CyclesRenderSettings.adaptive_min_samples:
.. _bpy.types.CyclesRenderSettings.preview_adaptive_min_samples:

Min Samples
   The minimum number of samples a pixel receives before adaptive sampling is applied.
   When set to 0 (default), Cycles automatically picks a value determined by the *Noise Threshold*.


.. _render-cycles-settings-viewport-denoising:

Denoising
=========

Denoising uses a specialized algorithm to get a less noisy image without requiring more samples.

.. seealso::

   If you enable the *Denoising Data* :doc:`render pass </render/layers/passes>`, you can
   alternatively denoise in the compositing step using the :doc:`/compositing/types/filter/denoise`.

.. _bpy.types.CyclesRenderSettings.use_preview_denoising:

Denoise (Viewport)
   Whether to perform denoising for the 3D Viewport in the *Rendered* shading mode.

.. _bpy.types.CyclesRenderSettings.use_denoising:

Denoise (Render)
   Whether to perform denoising for the final rendered image.

.. _bpy.types.CyclesRenderSettings.preview_denoiser:
.. _bpy.types.CyclesRenderSettings.denoiser:

Denoiser
   The algorithm to use.

   :Automatic:
      Uses GPU accelerated denoising if supported, for best performance.
      Prefers OpenImageDenoise over OptiX.
   :OpenImageDenoise:
      Uses Intel's `Open Image Denoise <https://www.openimagedenoise.org/>`__,
      an AI denoiser. Typically provides the highest quality.
   :OptiX:
      Uses NVIDIA's OptiX AI denoiser.
      Supports GPU acceleration on some older NVIDIA GPUs where OpenImageDenoise does not.

      Only available on NVIDIA GPUs when configured in the :ref:`editors_preferences_cycles` user preferences.

.. _bpy.types.CyclesRenderSettings.preview_denoising_input_passes:
.. _bpy.types.CyclesRenderSettings.denoising_input_passes:

Passes
   Controls which :doc:`Render Passes </render/layers/passes>` the denoiser should use as input.
   Generally, the more passes the denoiser has access to, the better the result.
   It is recommended to use at least *Albedo* as *None* can blur out details,
   especially at lower sample counts.

   :None: Denoises the image using color data.
   :Albedo: Denoises the image using color and albedo data.
   :Albedo + Normal: Denoises the image using color, albedo, and normal pass data.

.. _bpy.types.CyclesRenderSettings.preview_denoising_prefilter:
.. _bpy.types.CyclesRenderSettings.denoising_prefilter:

Prefilter :guilabel:`OpenImageDenoise`
   Controls whether prefiltering is applied to the *Passes* before denoising.
   Visible only when using *OpenImageDenoise*.

   :None:
      Does not apply any prefiltering to the input passes. This option retains the most detail and
      is the fastest, but assumes the input passes are noise free which may require a high sample count.
      If the input passes aren't noise free, then noise will remain in the image after denoising.
   :Fast:
      Assumes the input passes are not noise free, yet does not apply prefiltering to the input passes.
      This option is faster than *Accurate* but produces a blurrier result.
   :Accurate:
      Prefilters the input passes before denoising to reduce noise. This option usually produces
      more detailed results than *Fast*, but with increased processing time.

.. _bpy.types.CyclesRenderSettings.preview_denoising_quality:
.. _bpy.types.CyclesRenderSettings.denoising_quality:

Quality :guilabel:`OpenImageDenoise`
   Overall denoising quality.
   Visible only when using *OpenImageDenoise*.

   :High: Produces the highest quality at the cost of time.
   :Balanced: Balanced between performance and quality.
   :Fast: Sacrifices quality for speed (ideal for viewport rendering).

.. _bpy.types.CyclesRenderSettings.preview_denoising_start_sample:

Start Sample
   Sample at which to start denoising in the 3D Viewport.

.. _bpy.types.CyclesRenderSettings.preview_denoising_use_gpu:
.. _bpy.types.CyclesRenderSettings.denoising_use_gpu:

Use GPU
   Perform denoising on the GPU.
   This is significantly faster than on CPU, but requires additional GPU memory.
   When large scenes need more GPU memory, this option can be disabled.

   See :doc:`GPU Rendering </render/cycles/gpu_rendering>` for details on supported GPUs.


.. _bpy.types.CyclesRenderSettings.use_guiding:

Path Guiding
============

Path guiding helps reduce noise in scenes where finding a path to a light source is difficult for
regular path tracing, for example when a room is lit through a small door opening.
Important light directions are learned over time, improving as more samples are taken.

.. note::

   - Path guiding is only available when rendering on a CPU.
   - While path guiding helps render caustics in some scenes, it is not designed for complex caustics
     as they are harder to learn and guide.

.. seealso::

   :ref:`render-cycles-lights-area-portals` to guide the path tracing manually.

.. _bpy.types.CyclesRenderSettings.guiding_training_samples:

Training Samples
   The maximum number of samples to use for training. A value of 0 will keep training until
   the end of the render. Usually 128 to 256 training samples is enough for accurate guiding.
   Higher values can lead to a minor increases in guiding quality but with increased render times.

.. _bpy.types.CyclesRenderSettings.use_surface_guiding:

Surface
   Enable path guiding for the diffuse and glossy components of surfaces.

.. _bpy.types.CyclesRenderSettings.use_volume_guiding:

Volume
   Enable path guiding inside volumes.


Lights
======

.. _bpy.types.CyclesRenderSettings.use_light_tree:

Light Tree
   Use a light tree to more effectively sample lights in the scene, taking into account
   distance and estimated intensity.
   This can significantly reduce noise, at the cost of a somewhat longer render time per sample.

   Certain lighting properties are not accounted for in the light tree. This includes custom
   falloff, ray visibility, and complex shader node setups including textures.
   This can result in an increase in noise in some scenes that make use of these features.

.. _bpy.types.CyclesRenderSettings.light_sampling_threshold:

Light Threshold
   Probabilistically terminates light samples when the light contribution is below the threshold.
   This avoids wasting time on lights that contribute little to the image.
   Zero disables the test.


Advanced
========

.. _bpy.types.CyclesRenderSettings.sampling_pattern:

Pattern
   The random sampling pattern used by the integrator.

   :Automatic:
      Use *Blue-Noise* (see below), but with a tweak for viewport rendering to get better quality in the
      first sample. This is useful for interactive changes (panning the view, moving an object...)
      where the render is constantly restarting.
   :Classic:
      Use pre-computed tables of Owen-scrambled Sobol for random sampling.
   :Blue-Noise:
      Use a blue-noise pattern, which optimizes the frequency distribution.
      If the full number of samples is rendered, the output typically appears smoother than *Classic*
      despite not actually reducing the overall noise.

.. _bpy.types.CyclesRenderSettings.seed:

Seed
   Seed value for integrator to get different noise patterns.

   .. _bpy.types.CyclesRenderSettings.use_animated_seed:

   :bl-icon:`time` Use Animated Seed
      Changes the seed for each frame. It is a good idea to enable this
      when rendering animations because a varying noise pattern is less noticeable.

Scrambling Distance
   A technique that reduces the randomness between pixels in an attempt to improve GPU rendering performance,
   at the cost of potential artifacts. Not compatible with the *Blue-Noise* sampling pattern.

   .. _bpy.types.CyclesRenderSettings.auto_scrambling_distance:

   Automatic
      Adapts the scrambling distance based on the sample count.

   .. _bpy.types.CyclesRenderSettings.preview_scrambling_distance:

   Viewport
      Uses the *Scrambling Distance* adjustment for viewport rendering.
      This will make rendering faster but may cause flickering.

   .. _bpy.types.CyclesRenderSettings.scrambling_distance:

   Multiplier
      A multiplier for the scrambling distance. Values below one will reduce the distance, having the potential
      to improve GPU rendering performance but increase the visibility of artifacts.

.. _bpy.types.CyclesRenderSettings.min_light_bounces:

Min Light Bounces
   Minimum number of light bounces for each path,
   after which the integrator uses Russian Roulette to terminate paths that contribute less to the image.
   Setting this higher gives less noise, but may also increase render time considerably. For a low number
   of :ref:`maximum bounces <bpy.types.CyclesRenderSettings.max_bounces>`, it is strongly recommended to
   set this minimum to the same value.

.. _bpy.types.CyclesRenderSettings.min_transparent_bounces:

Min Transparent Bounces
   Minimum number of :ref:`transparent <render-cycles-light-paths-transparency>` bounces
   (more specifically "passthroughs"). Setting this higher reduces noise in the first bounces,
   but can also be less efficient for more complex geometry like hair and volumes.

.. _bpy.types.CyclesRenderSettings.use_layer_samples:

Layer Samples
   If any view layers have :ref:`Sample Overrides <bpy.types.ViewLayer.samples>` configured,
   this option specifies how to use them.

   :Use: Allow view layers to override the scene-level sample count.
   :Bounded: Allow the overrides as long as they don't exceed the scene-level sample count.
   :Ignore: Ignore the overrides.

.. _bpy.types.CyclesRenderSettings.use_sample_subset:

Sample Subset
   Only render a subset of the samples. Multiple subset renders can be combined into a full
   one by running the following in the :doc:`Python Console </editors/python_console>`:

   ``bpy.ops.cycles.merge_images(input_filepath1=r"1.exr", input_filepath2=r"2.exr",
   output_filepath=r"combined.exr")``

   A typical use case is to distribute the rendering of a single frame over multiple machines.
   Say you want to render 2048 samples in total, but split this work over two machines because
   doing it on one would take too long:

   - On both machines, set the *(Max) Samples* to 2048, disable *Denoise*, and enable *Sample Subset*.
   - On the first machine, set *Offset* to 0 and *Length* to 1024.
   - On the second machine, set *Offset* to 1024 and *Length* to 1024.
   - Run the 1024-sample render on each machine, then combine the results as described above to get
     the equivalent of a single 2048-sample render.

   .. _bpy.types.CyclesRenderSettings.sample_offset:

   Offset
      The 0-based index of the first sample in the subset.

   .. _bpy.types.CyclesRenderSettings.sample_subset_length:

   Length
      The number of samples in the subset. While this overrides *(Max) Samples* in terms of the
      samples that will get rendered, it's still important to set *(Max) Samples* to the total number
      of samples that will be rendered across all subsets -- otherwise, the subsets will have
      incompatible noise and combining them will give a worse result.
