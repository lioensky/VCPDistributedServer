
***********
Performance
***********

.. reference::

   :Panel:     :menuselection:`Properties --> Render --> Performance`

.. _bpy.types.RenderSettings.use_high_quality_normals:

High Quality Normals
   Uses higher precision normals and tangents which can improve
   visual quality for dense meshes with high frequency textures at the cost of memory.


Memory
======

.. _bpy.types.SceneEEVEE.shadow_pool_size:

Shadow Pool
   A bigger pool size allows for more shadows in the scene
   but might not fit into GPU memory and decreases performance.
   Increasing the size might fix the *Shadow buffer full* error.

   .. seealso::
      :ref:`Shadow documentation <bpy.types.Light.shadow>`

.. _bpy.types.SceneEEVEE.gi_irradiance_pool_size:

Light Probes Volume Pool
   A bigger pool size allows for more irradiance grids in the scene
   but might not fit into GPU memory and decreases performance.


Viewport
========

.. _bpy.types.RenderSettings.preview_pixel_size:

Pixel Size
   Option to control the resolution for viewport rendering.
   Allows you to speed up viewport rendering, which is especially useful for displays with high DPI.


Compositor
==========

.. Editor's Note: This section gets copied into:
.. - :doc:`</render/cycles/render_settings/performance>`
.. - :doc:`</compositing/sidebar>`
.. These bpy types cannot be added below the copy line as it causes build warnings.

.. _bpy.types.RenderSettings.compositor_device:
.. _bpy.types.RenderSettings.compositor_precision:
.. _bpy.types.RenderSettings.compositor_denoise_device:
.. _bpy.types.RenderSettings.compositor_denoise_preview_quality:
.. _bpy.types.RenderSettings.compositor_denoise_final_quality:

.. --- copy below this line ---

Device
   The device used for compositing.

   :CPU: Use the CPU for compositing.
   :GPU: Use the GPU for compositing.

Precision :guilabel:`GPU`
   The precision of compositor intermediate result.

   :Auto: Use full precision for final renders, half precision otherwise.
   :Full: Use full precision for final renders and viewport.

.. --- end copy above this line - compositor sidebar ---

Denoise Nodes
^^^^^^^^^^^^^

Denoising Device
   The device to use to process :doc:`Denoise nodes </compositing/types/filter/denoise>` in the compositor.

   :Auto: Use the same device used by the compositor to process the denoise node.
   :CPU: Use the CPU to process the denoise node.
   :GPU: Use the GPU to process the denoise node if available, otherwise fallback to CPU.

Preview Quality
   The quality used by :doc:`Denoise nodes </compositing/types/filter/denoise>` during viewport
   and interactive compositing of a render if their quality is set to *Follow Scene*.

   :High:
      Produces the highest quality output at the cost of long processing times.
   :Balanced:
      Balanced between performance and quality, typically processing in half the time as *High*,
      while retaining most of the quality.
   :Fast:
      Produces an output quickly at a noticeable cost of quality.

Final Quality
   The quality used by :doc:`Denoise nodes </compositing/types/filter/denoise>` during the final
   render if their quality is set to *Follow Scene*.

   :High:
      Produces the highest quality output at the cost of long processing times.
   :Balanced:
      Balanced between performance and quality, typically processing in half the time as *High*,
      while retaining most of the quality.
   :Fast:
      Produces an output quickly at a noticeable cost of quality.

.. --- end copy above this line - compositor performance ---
