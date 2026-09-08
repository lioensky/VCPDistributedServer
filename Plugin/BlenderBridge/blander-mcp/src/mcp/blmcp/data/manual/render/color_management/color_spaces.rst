************
Color Spaces
************

.. _color-management-linear-space:

Linear Workflow
===============

Different :term:`Color Spaces <Color Space>`
are needed for rendering, display and storage of images.

Rendering and compositing is best done in a *scene linear* color space,
which corresponds more closely to nature, and makes computations more physically accurate.
Blender primarily works with scene linear colors for materials, lighting, geometry and
compositing.

However, these values do not directly correspond to human perception or the way display devices
work. Image files are also often stored in different color spaces for more efficient compression.

For a correct linear workflow, it is important to assign the correct color spaces for images
and displays. Blender will then perform conversion to and from scene linear colors.

.. figure:: /images/render_color-management_linear-workflow.svg
   :width: 100%
   :align: center

   An example of a linear workflow.


Working Space
=============

.. reference::

   :Editor:    Properties
   :Panel:     :menuselection:`Render Properties --> Color Management --> Working Space`

.. _bpy.types.BlendFileColorspace.working_space:

File
  Color space used for all scene linear colors in this file, and for shader, compositing and geometry
  nodes processing. The default is Linear Rec.709, while Linear Rec.2020 and ACEScg are available for
  working with a wider gamut of colors and compatibility with ACES workflows.

  The working space affects the colors of all data-blocks in a file, and has a significant effect on
  rendering and compositing results. Generally the working space should be chosen at the start of a
  project and used for all blend files.

  Blender can convert between different working spaces, however this is only an approximation and
  manual fix-ups are typically needed. When linking and appending data-blocks, colors are
  automatically converted to match the current file.

.. _bpy.types.ColorManagedSequencerColorspaceSettings.name:

Sequencer
   The color space that the :doc:`Sequencer </editors/video_sequencer/index>` operates in.
   By default, the Sequencer operates in sRGB space,
   but it can also be set to work in Linear space like the Compositing nodes, or another color space.
   Different color spaces will give different results for color correction, crossfades, and other operations.

   The default supported color spaces are described in
   :ref:`Built-in Color Spaces <ocio-config-default-color-spaces>`.

Images and Video
================

When working with image and video files, Blender will automatically try to guess the right color space.
If this is not correct, the color space of the image file can be configured in the image settings.

A common situation where manual changes are needed is when working with or baking normal maps and
displacement maps. Such maps do not actually store colors, just data encoded as colors.
Those images should be marked as *Non-Color Data*.

For intermediate image files in production, it is recommended to use *OpenEXR* files.
These are always stored in scene linear color spaces, with high precision to avoid data loss.
That makes them suitable to store renders that can later be composited, color graded and
converted to different output formats.

.. _ocio-config-default-color-spaces:

Built-in Color Spaces
=====================

Blender's OCIO configuration file is equipped by default to read/write files in these color spaces


Display
-------

Color spaces for displays and image files.

:sRGB: Standard RGB display space using Rec. 709 chromaticities and a D65 white point.
:Rec.2020: BT.2020 2.4 Exponent EOTF Display.
:Rec.1886: BT.1886 2.4 Exponent EOTF Display, commonly used for TVs.
:Display P3: Apple's Display P3 with sRGB compound (piece-wise) encoding transfer function, common on Mac devices.
:Rec.2100 PQ: For high dynamic range images and video with Rec.2020 wide gamut, up to 10000 nits.
:Rec.2100 HLG: For high dynamic range images and video with Rec.2020 wide gamut, up to 1000 nits.


Linear
------

Color spaces commonly used for OpenEXR files.

:Working Space:
   The linear working space of the current blend file,
   that is used by default in compositing, shader and geometry nodes.
:Linear Rec.709: Linear BT.709 chromaticities with illuminant D65 white point.
:Linear Rec.2020: Linear BT.2020 with illuminant D65 white point.
:ACEScg:
   An ACES color space that is designed to be used for rendering and compositing.
   It uses the AP1 color primaries, a D60 white point, and a linear transfer function.
   The standard working space in ACES workflows.
:ACES2065-1:
   An ACES color space using the AP0 color primaries, a D60 white point and a linear transfer function.
   This color space is meant to store and transfer data, preserving the most information possible.
   Commonly used for delivery and archival in ACES workflows.
:Linear FilmLight E-Gamut: Linear E-Gamut with illuminant D65 white point.
:Linear DCI-P3 D65: Linear DCI-P3 with illuminant D65 white point.
:Linear CIE-XYZ E: 1931 CIE XYZ standard with assumed illuminant E white point.
:Linear CIE-XYZ D65: 1931 CIE XYZ with adapted illuminant D65 white point.


Other
-----

:Non-Color:
   Generic data that is not color, will not apply any color transform (e.g. normal maps or displacement maps).
:Working Space:
   Uses the :ref:`bpy.types.BlendFileColorspace.working_space`
   color space defined in the scene's color management settings.


Log
---

:ACEScc: ACES color correction space, using AP1 primaries.
:ACEScct: ACES color correction space with toe, using AP1 primaries.
:AgX Log: Intermediate log color space of AgX view transform.
:Filmic Log: Intermediate log color space of Filmic view transform.


Utilities
---------

Color spaces corresponding to view transforms. These color spaces can
be used for background images that should not be affected by the view
transform, while everything else in the scene is affected.

:ACES 1.3 sRGB: ACES 1.3 view transform
:ACES 2.0 sRGB: ACES 2.0 view transform
:AgX Base sRGB: AgX view transform
:Filmic sRGB: Filmic view transform
:Khronos PBR Neutral sRGB: Khronos PBR Neutral view transform
