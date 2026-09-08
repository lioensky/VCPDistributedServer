.. _limitations:

***********
Limitations
***********


Hardware Limitations
====================

General hardware limitations apply when using the GPU compositor.
See also :ref:`Troubleshooting Graphics Hardware <troubleshooting-gpu-index>`.

Blender uses the same GPU resources for the UI as well as for the GPU compositor.
This have a number of consequences, each of which is described in one of the following sections.

UI Freezes
----------

Unlike rendering with Cycles, the UI might become irresponsive when using the GPU compositor for some slower GPUs.

TDR on Windows
--------------

Timeout Detection Recovery
(`TDR <https://learn.microsoft.com/en-us/windows-hardware/drivers/display/timeout-detection-and-recovery>`_)
resets the GPU driver if a GPU compositing task takes longer than the default 2 second limit.
This is especially common with older GPUs when using expensive nodes like
:ref:`Bokeh Blur <bpy.types.CompositorNodeBokehBlur>` node.
To prevent unexpected resets, it is recommended to increase the TDR timeout.
