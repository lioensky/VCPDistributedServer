***********
OpenColorIO
***********

.. _ocio-config:

Blender comes with a standard OpenColorIO configuration that
contains a number of useful display devices and view transforms.

However, OpenColorIO is also designed to give a consistent user experience across
`multiple applications <https://opencolorio.org/#supported_apps>`__,
and for this, a single shared configuration file can be used.
Blender will use the standard ``OCIO`` environment variable to read an OpenColorIO configuration
other than the default Blender one. More information about how to set up such a workflow
can be found on the `OpenColorIO website <https://opencolorio.org/>`__.

There is also a ``BLENDER_OCIO`` environment variable to change the configuration
for Blender only. It is recommended to use ``OCIO`` when possible for compatibility
with other software and pipelines that may not be aware of ``BLENDER_OCIO``. However
sometimes there are incompatibilities in configuration files that make it difficult
to share them across applications.

ACES
====

The standard Blender configuration includes essential support for
`ACES <https://www.oscars.org/science-technology/sci-tech-projects/aces>`_ workflows
with the ACEScg working space, ACES 2.0 view transform and OpenEXR images saved in
the ACES2065-1 and ACEScg color spaces.

This covers most needs for working in an ACES pipeline. However for more complete
support, the
`official ACES configurations <https://github.com/AcademySoftwareFoundation/OpenColorIO-Config-ACES/releases>`_
can be manually installed and set through the ``OCIO`` environment variable.

Roles
=====

``scene_linear``
   Color space used for rendering, compositing, and storing all float precision images in memory.
``data``
   Color space for non-color data.
``aces_interchange``
   ACES2065-1 color space. Used to derive chromaticities of the *scene_linear* color space, for
   effects such as blackbody emission.
``cie_xyz_d65_interchange``
   Intermediate display linear color space, to connected view transforms to display color spaces.
``color_picking``
   Defines the distribution of colors in color pickers. It is expected to
   be approximately perceptually linear, have the same gamut as the *scene_linear* color space,
   map 0..1 values to 0..1 values in the scene linear color space for predictable editing of materials' albedo.
``default_sequencer``
   Default color space for the Sequencer, *scene_linear* if not specified.
``default_byte``
   Default color space for byte precision images and files, *texture_paint* if not specified.
``default_float``
   Default color space for float precision images and files, *scene_linear* if not specified.

Writing Configurations for Blender
==================================

OpenColorIO configurations do not strictly specify all information needed for Blender to work optimally.
These guidelines help ensure a configuration works well:

* Use OpenColorIO v2 ``display_colorspaces`` and ``view_transforms`` with ``cie_xyz_d65_interchange``
  intermediate display linear space. This is used to emulate the chosen display on the actual display.
  In older configs without this, display emulation will be disabled and wide gamut and HDR display will
  not work well. Saving colorspace metadata for images and video also depends on this.
* For every display, include a view transform without tone mapping. Blender will look for a view
  transform named ``Standard`` or ``Un-tone-mapped`` or the config wide ``default_view_transform``.
  If not found, the first view transform of the display will be used. This is more important
  for OpenColorIO v1 configs without ``display_colorspaces``, to determine the color space of an image
  after applying a view transform.
* Include the interop ID from the `Color Interop Forum <https://github.com/AcademySoftwareFoundation/ColorInterop>`__
  for every color space and display color space that you can. This helps save image and video
  with correct colorspace information. Add the interop ID as an alias of the colorspace. For
  OpenColor 2.5 configs, additionally set the native ``interop_id`` attribute where possible.
* The ``icc_profile_name`` interchange attribute is supported, to embed ICC profiles when saving images.
* Mark HDR displays by setting ``encoding: hdr-video`` on the corresponding colorspace.
* For HDR view transforms, use ``HDR 500 nits``, ``HDR 1000 nits``, ``HDR 2000 nits`` or ``HDR 4000 nits``
  as part of the name to automatically determine maximum luminance for mastering display metadata.
