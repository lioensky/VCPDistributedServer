GPU Platform Utilities (gpu.platform)
=====================================

.. module:: gpu.platform

This module provides access to GPU Platform definitions.

.. function:: backend_type_get()

   Get active GPU backend.

   :return: Backend type ('OPENGL', 'VULKAN', 'METAL', 'NONE', 'UNKNOWN').
   :rtype: str


.. function:: device_type_get()

   Get GPU device type.

   :return: Device type ('APPLE', 'NVIDIA', 'AMD', 'INTEL', 'SOFTWARE', 'QUALCOMM', 'UNKNOWN').
   :rtype: str


.. function:: renderer_get()

   Get GPU to be used for rendering.

   :return: GPU name.
   :rtype: str


.. function:: vendor_get()

   Get GPU vendor.

   :return: Vendor name.
   :rtype: str


.. function:: version_get()

   Get GPU driver version.

   :return: Driver version.
   :rtype: str


