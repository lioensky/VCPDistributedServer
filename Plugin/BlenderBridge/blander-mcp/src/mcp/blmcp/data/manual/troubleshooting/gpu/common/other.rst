:orphan:

Common Problems
===============

Unsupported Graphics Driver Error
---------------------------------

This means your graphics card and driver do not have the minimum required OpenGL 3.3 version needed by Blender.

Installing the latest version of the correct driver can help upgrade the OpenGL version, though some graphics cards
are simply too old to run the latest Blender. In such cases, using Blender 2.79 or earlier is the only option.
Starting with Blender 2.8 (which added EEVEE), there is less support for older graphics hardware.


Crash on Startup
----------------

Try running Blender from the :doc:`command line </advanced/command_line/index>`, to see if any helpful error messages
are printed.

On Windows, graphics drivers can sometimes get corrupted or incorrectly replaced by Windows Update. In this case, it
can help to uninstall all graphics drivers (there may be multiple sets installed from Intel, AMD and NVIDIA) and
perform a clean installation with drivers from the manufacturer's website.


Poor Performance
----------------

- Update your graphics drivers (see above).
- On laptops, make sure you are using a dedicated GPU (see above).
- Try lowering quality settings in :menuselection:`Preferences --> System --> Memory & Limits`.
- Try undoing settings in your graphics drivers, if you made any changes there.


Render Errors
-------------

See :doc:`EEVEE </render/eevee/limitations/index>` and :doc:`Cycles </render/cycles/gpu_rendering>` documentation
respectively.


Wrong Selection in 3D Viewport
------------------------------

See :ref:`Invalid Selection, Disable Anti-Aliasing <troubleshooting-3dview-invalid-selection>`.


Virtual Machines
----------------

Running Blender inside a virtual machine is known to have problems when OpenGL drawing calls are forwarded to the host
operating system.

To resolve this, configure the system to use PCI passthrough.

Some VM hosts may require turning on GPU paravirtualization. Some GPU vendors restrict this function to higher-priced
cards or models.


Information
===========

To find out which graphics card and driver Blender is using, use :menuselection:`Help --> Save System Info` inside
Blender. The OpenGL section will have information about your graphics card, vendor and driver version.
