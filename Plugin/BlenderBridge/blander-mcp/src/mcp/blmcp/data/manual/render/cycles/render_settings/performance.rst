
***********
Performance
***********

.. reference::

   :Panel:     :menuselection:`Render --> Performance`

Properties that affect render speeds or memory consumption.
There are several presets available to help choose between different trade offs:

:Default: Balances memory saving and faster rendering settings.
:Faster Render: Uses settings to render faster at the cost of higher memory consumption.
:Lower Memory: Uses settings to decrease memory considered at the cost of slower renders.


Threads
=======

.. _bpy.types.RenderSettings.threads_mode:

Threads Mode
   Method to determine the maximum number of CPU cores to use while rendering.

   :Auto-Detect:
      Automatically chooses the amount of threads to match the number of logical processors on your computer.
   :Fixed:
      Manually choose the maximum number threads to use for rendering.
      This can be useful for example, if you want to use your computer while rendering,
      you can set the property to a thread count lower the amount of logical processors on your computer.

.. _bpy.types.RenderSettings.threads:

Threads
   The maximum number of CPU cores to use simultaneously while rendering.


Memory
======

.. _bpy.types.CyclesRenderSettings.tile_size:

Tile Size
   Render high resolution images in tiles of this size, to reduce memory usage.
   Tiles are cached to disk while rendering to save memory.

   .. note::

      In some cases changing the *Tile Size* can result in increased performance.
      For example when a small object renders slowly compared to other objects,
      using a small *Tiles Size* can lead to an increase in performance.


Acceleration Structure
======================

.. _bpy.types.CyclesRenderSettings.debug_use_spatial_splits:

Use Spatial Splits
   Spatial splits improve the rendering performance in scenes with a mix of large and small polygons.
   The downsides are longer BVH build times and slightly increased memory usage.

.. _bpy.types.CyclesRenderSettings.debug_use_hair_bvh:

Use Curves BVH
   Use a special type of :term:`BVH` for rendering curves.
   The bounding boxes are not axis aligned allowing a spatially closer fit to the curve geometry.
   Disabling this option will reduce memory, at the cost of increasing curve render time.

.. _bpy.types.CyclesRenderSettings.debug_bvh_time_steps:

BVH Time Steps
   Split BVH primitives by this number of time steps to speed up render time at the expense of memory.

Use Compact BVH
   Use a more compact BVH structure, which can reduce RAM usage but render slower.


Final Render
============

.. _bpy.types.RenderSettings.use_persistent_data:

Persistent Data
   Keep render data in memory after rendering for faster re-renders and animation renders
   at the cost of extra memory usage while performing other tasks in Blender.

   When using multiple :doc:`View Layers </render/layers/view_layer>`,
   only data from a single view layer is preserved to keep memory usage within bounds;
   however, objects shared between view layers are preserved.


Viewport
========

Pixel Size
   Option to control the resolution for viewport rendering.
   Allows you to speed up viewport rendering, which is especially useful for displays with high DPI.


Compositor
==========

.. include:: /render/eevee/render_settings/performance.rst
   :start-after: .. --- copy below this line ---
   :end-before: .. --- end copy above this line - compositor performance ---
