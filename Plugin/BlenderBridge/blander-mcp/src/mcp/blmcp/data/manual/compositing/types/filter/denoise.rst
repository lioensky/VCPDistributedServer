.. index:: Compositor Nodes; Denoise
.. _bpy.types.CompositorNodeDenoise:

************
Denoise Node
************

.. figure:: /images/node-types_CompositorNodeDenoise.webp
   :align: right
   :alt: Denoise Node.

The Denoise node is used to denoise renders from :doc:`Cycles </render/cycles/index>`
and other ray tracing renderers. This helps to significantly reduce render time by
rendering with fewer samples.

It uses `Open Image Denoise <https://www.openimagedenoise.org/>`__,
which transforms noisy images into clean images with machine learning.


Inputs
======

Image
   Noisy image input.
Albedo
   Optional albedo render pass to better preserve detail.
   For Cycles, it is recommended to use the Denoising Albedo render pass,
   which is available when enabling the Denoising Data passes.
Normal
   Optional normal render pass to better preserve detail.
   For Cycles, it is recommended to use the Denoising Normal render pass,
   which is available when enabling the Denoising Data passes.
HDR
   Preserve colors outside the 0 to 1 range.
Prefilter
   :None:
      Does not apply any prefiltering to the input passes. This option retains the most detail and
      is the fastest, but assumes the input passes are noise free which may require a high sample
      count. If the input passes are not noise free, then noise will remain in the image after denoising.
   :Fast:
      Assumes the input passes are not noise free, yet does not apply prefiltering to the input passes.
      This option is faster than *Accurate* but produces a blurrier result.
   :Accurate:
      Prefilters the input passes before denoising to reduce noise. This option usually produces
      more detailed results than *Fast* with increased processing time.
Quality
   :Follow Scene:
      Use the :ref:`scene's quality setting <bpy.types.RenderSettings.compositor_denoise_preview_quality>`.
   :High:
      Produces the highest quality output at the cost of long processing times.
   :Balanced:
      Balanced between performance and quality, typically processing in half the time as *High*,
      while retaining most of the quality.
   :Fast:
      Produces an output quickly at a noticeable cost of quality.


Outputs
=======

Image
   Denoised image output.


Examples
========

.. figure:: /images/compositing_types_filter_denoise_example.jpg

   Render before and after denoising, with a very low number of samples as input.
   As more samples are used, the denoiser will be able to better preserve detail.
