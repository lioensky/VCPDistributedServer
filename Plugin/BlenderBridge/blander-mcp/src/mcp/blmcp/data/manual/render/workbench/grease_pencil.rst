
*************
Grease Pencil
*************

.. reference::

   :Panel:     :menuselection:`Render --> Grease Pencil`

This panel contains settings that control the rendering of :doc:`Grease Pencil lines </grease_pencil/index>`.


Viewport
========

SMAA Threshold
   Threshold for the edge detection algorithm used to correct aliasing for the 3D Viewport,
   Higher values may result in loss of detail due to excessive blurring.


Render
======

SMAA Threshold
   Threshold for the edge detection algorithm used to correct aliasing for the final render,
   Higher values may result in loss of detail due to excessive blurring.

SSAA Samples
   Number of samples used for super-sampling anti-aliasing in the final render.
   Higher values produce smoother lines but increase render time.

Motion Blur Steps
   Controls accuracy of :term:`motion blur <Motion Blur>`, more steps result in longer render time.
   Only used when :ref:`Motion Blur <bpy.types.RenderSettings.use_motion_blur>` is enabled.
   Set to 0 to disable motion blur for Grease Pencil objects.
