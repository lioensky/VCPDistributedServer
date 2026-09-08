*************
GPU Rendering
*************

:abbr:`GPU (Graphics Processing Unit)` rendering makes it possible to use your
graphics card for rendering, instead of the :abbr:`CPU (Central Processing Unit)`. This can speed up rendering
because modern GPUs are designed to do quite a lot of number crunching.
On the other hand, they also have some limitations in rendering complex scenes, due to more limited memory,
and issues with interactivity when using the same graphics card for display and rendering.

To enable GPU rendering:

#. Select either *CUDA*, *OptiX*, *HIP*, *oneAPI*, or *Metal*
   in the :ref:`Cycles Render Devices <editors_preferences_cycles>` user preference.
#. Enable the available devices for the chosen backend.
#. Configure each scene to use the *GPU Compute* :ref:`Device <bpy.types.CyclesRenderSettings.device>`.


Rendering Technologies
======================

Blender supports different technologies to render on the GPU depending on the particular GPU manufacturer
and operating system.

CUDA -- NVIDIA
--------------

:abbr:`CUDA (Compute Unified Device Architecture)` is supported on Windows and Linux and requires a
NVIDIA graphics cards with compute capability 5.0 and higher. To make sure your GPU is supported,
see the `list of NVIDIA graphics cards <https://developer.nvidia.com/cuda-gpus#compute>`__
with the compute capabilities and supported graphics cards.


.. _render-cycles-gpu-optix:

OptiX -- NVIDIA
---------------

OptiX is supported on Windows and Linux and requires a NVIDIA graphics cards with compute capability 5.0 and higher
and a driver version of at least 535. To make sure your GPU is supported,
see the `list of NVIDIA graphics cards <https://developer.nvidia.com/cuda-gpus#compute>`__.

OptiX takes advantage of hardware ray-tracing acceleration in RTX graphics cards, for improved performance.

GPU acceleration for OpenImageDenoise is available for compute capability 7.0 and higher, which includes
all NVIDIA RTX cards.


HIP -- AMD
----------

:abbr:`HIP (Heterogeneous-compute Interface for Portability)` is supported on Windows and Linux and requires a
AMD graphics card with the RDNA1 architecture or newer. Both discrete GPUs and APUs are supported.

Supported GPUs include:

- `Radeon RX 5000 Series <https://en.wikipedia.org/wiki/Radeon_RX_5000_series>`__
- `Radeon RX 6000 Series <https://en.wikipedia.org/wiki/Radeon_RX_6000_series>`__ and `Radeon Pro W6000 Series <https://en.wikipedia.org/wiki/Radeon_Pro#Radeon_Pro_W6000/W6000M_series>`__
- `Radeon RX 7000 Series <https://en.wikipedia.org/wiki/Radeon_RX_7000_series>`__ and `Radeon Pro W7000 Series <https://en.wikipedia.org/wiki/Radeon_Pro#Radeon_Pro_W7000_series>`__
- `Radeon RX 9000 Series <https://en.wikipedia.org/wiki/Radeon_RX_9000_series>`__

Minimum driver versions:

- Windows: Radeon Software 24.9.1 or Radeon PRO Software 24.Q4
- Linux: Radeon Software 23.40 or `ROCm HIP Runtime 6.0 <https://rocm.docs.amd.com/projects/install-on-linux/en/latest/install/quick-start.html>`__

Please refer to `AMD's website <https://www.amd.com/en/products/specifications.html>`__ for more
information about AMD graphics cards and their architectures.

Hardware ray-tracing support is available with the most recent drivers.
This can be enabled in the preferences, and is supported on Radeon RX 6000 and newer.

GPU accelerated denoising is available on discrete Radeon RX 6000 and newer.


oneAPI -- Intel
---------------

oneAPI is a computation library that is supported on Windows and Linux and requires an
`Intel® Arc™ graphics card <https://en.wikipedia.org/wiki/Intel_Arc>`__
with the Xe HPG architecture.
Hardware acceleration for ray-tracing and denoising is supported.

Supported GPUs include:

- Intel® Arc™ A-Series
- Intel® Arc™ B-Series

Minimum driver versions:

- Windows: Intel Graphics Driver XX.X.101.5518
- Linux: ``intel-level-zero-gpu`` package 1.3.27642,
  typically available through the ``intel-compute-runtime`` package XX.XX.34666.3

Please refer to `Intel's website <https://www.intel.com/content/www/us/en/products/details/discrete-gpus.html>`__
for more information about Intel graphics cards and their architectures.

GPU accelerated denoising is available on all supported GPUs.


Metal -- Apple (macOS)
----------------------

Metal for GPU acceleration is supported on Apple computers with `Apple Silicon <https://en.wikipedia.org/wiki/Apple_silicon>`__.
macOS 13.0 or newer is required to support all features.

GPU accelerated ray-tracing and denoising is available on Apple Silicon.


Limitations
===========

- :ref:`Path Guiding <bpy.types.CyclesRenderSettings.use_guiding>` is not supported on any GPU.
- :doc:`/render/cycles/osl/index` is only supported for OptiX, with some limitations listed in the documentation.


Frequently Asked Questions
==========================

Why is Blender unresponsive during rendering?
---------------------------------------------

On older GPU generations, graphics cards can only either render or draw the user interface.
This can make Blender unresponsive while it is rendering.
Heavy scenes can also make Blender unresponsive on newer GPUs,
when using a lot of memory or executing expensive shaders, however this is generally less of a problem.

The only complete solution for this is to use a dedicated GPU for rendering, and another for display.


Why does a scene that renders on the CPU not render on the GPU?
---------------------------------------------------------------

There may be multiple causes,
but the most common one is that there is not enough memory on your graphics card.
Typically, the GPU can only use the amount of memory that is on the GPU
(see `Would multiple GPUs increase available memory?`_ for more information).
This is usually much smaller than the amount of system memory the CPU can access.
With CUDA, OptiX, HIP and Metal devices, if the GPU memory is full Blender will automatically
try to use system memory. This has a performance impact, but will usually still result in a faster render
than using CPU rendering.


Can multiple GPUs be used for rendering?
----------------------------------------

Yes, go to :menuselection:`Preferences --> System --> Compute Device Panel`, and configure it as you desire.


Would multiple GPUs increase available memory?
----------------------------------------------

Typically, no, each GPU can only access its own memory.

The exception is NVIDIA GPUs connected with NVLink, where multiple GPUs can share memory at a small performance cost.
This can be enabled with :ref:`Distributed Memory Across Devices <prefs-system-cycles-distributive-memory>`
in the preferences.


What renders faster?
--------------------

This varies depending on the hardware used. Different technologies also have different compute times
depending on the scene tested. For the most up to date information on the performance of different devices,
browse the `Blender Open Data <https://opendata.blender.org/>`__ resource.


Error Messages
==============

In case of problems, be sure to install the official graphics drivers from the GPU manufacturers website,
or through the package manager on Linux.
The graphics drivers provided by the computer manufacturer can sometimes be outdated or incomplete.


Error: Out of memory
--------------------

This usually means there is not enough memory to store the scene for use by the GPU.

.. note::

   One way to reduce memory usage is by using smaller resolution textures.
   For example, 8k, 4k, 2k, and 1k image textures take up respectively 256MB, 64MB, 16MB and 4MB of memory.


The NVIDIA OpenGL driver lost connection with the display driver
----------------------------------------------------------------

If a GPU is used for both display and rendering,
Windows has a limit on the time the GPU can do render computations.
If you have a particularly heavy scene, Cycles can take up too much GPU time.
Reducing Tile Size in the Performance panel may alleviate the issue,
but the only real solution is to use separate graphics cards for display and rendering.

Another solution can be to increase the time-out,
although this will make the user interface less responsive when rendering heavy scenes.
`Learn More Here <https://learn.microsoft.com/en-us/windows-hardware/drivers/display/timeout-detection-and-
recovery>`__.


Unsupported GNU version
-----------------------

On Linux, depending on your GCC version you might get this error.
See the `NVIDIA CUDA Installation Guide for Linux
<https://docs.nvidia.com/cuda/archive/10.2/cuda-installation-guide-linux/index.html>`__
for a list of supported GCC versions. There are two possible solutions to this error:

Use an alternate compiler
   If you have an older GCC installed that is compatible with the installed CUDA toolkit version,
   then you can use it instead of the default compiler.
   This is done by setting the ``CYCLES_CUDA_EXTRA_CFLAGS`` environment variable when starting Blender.

   Launch Blender from the command line as follows:

   .. code-block:: sh

      CYCLES_CUDA_EXTRA_CFLAGS="-ccbin gcc-x.x" blender

   (Substitute the name or path of the compatible GCC compiler).

Remove compatibility checks
   If the above is unsuccessful, delete the following line in
   ``/usr/local/cuda/include/host_config.h``:

   .. code-block:: c

      #error -- unsupported GNU version! gcc x.x and up are not supported!

   This will allow Cycles to successfully compile the CUDA rendering kernel the first time it
   attempts to use your GPU for rendering. Once the kernel is built successfully, you can
   launch Blender as you normally would and the CUDA kernel will still be used for rendering.


CUDA Error: Kernel compilation failed
-------------------------------------

This error may happen if you have a new NVIDIA graphics card that is not yet supported by
the Blender version and CUDA toolkit you have installed.
In this case Blender may try to dynamically build a kernel for your graphics card and fail.

In this case you can:

#. Check if the latest Blender version
   (official or `experimental builds <https://builder.blender.org/download/>`__)
   supports your graphics card.
#. If you build Blender yourself, try to download and install a newer CUDA developer toolkit.

Normally users do not need to install the CUDA toolkit as Blender comes with precompiled kernels.
