******************
Displays and Views
******************

.. _render-post-color-management:

Overview
========

To display an image, it must be converted from
:ref:`scene linear <color-management-linear-space>` to a display color space.
This involves both technical and artistic choices.

The technical choice of :ref:`display color space <bpy.types.ColorManagedDisplaySettings.display_device>`
depends on the target display device and its capabilities. sRGB works for all
computer displays, but different choices may be made for digital cinema, HD TVs,
and computers with wide gamut or HDR support.

Because display devices cannot display the full spectrum of colors and only have
limited brightness, colors must be fitted to the gamut of the device. Blender
includes a choice of :ref:`views <bpy.types.ColorManagedViewSettings.view_transform>`,
each resulting in a different look.

Further artistic choices can be made with color management settings like exposure and
white balance, and color grading in the compositor.
.

.. figure:: /images/render_color-management_linear-display-space.svg
   :width: 100%
   :align: center

   Conversion from linear to display device space.

.. _bpy.types.ColorManagedDisplaySettings:
.. _bpy.types.ColorManagedDisplaySettings.display_device:

Displays
========

The color space of the display that images and video are being created for.

Regular compute displays support sRGB, and most images and videos are
stored in this color space. However moderns displays often support a wider
gamut and high dynamic range content.

Standard Dynamic Range (SDR)
   :sRGB: Basic display supported everywhere.
   :Display P3: Wide gamut for Apple devices and other modern displays.
   :Rec.1886: Used by many older TVs.
   :Rec.2020: Even wider gamut than P3 supported by some displays.
High Dynamic Range (HDR)
   :Rec.2100 PQ: For HDR displays with Rec.2020 wide gamut, up to 10000 nits.
   :Rec.2100 HLG: For HDR TVs with Rec.2020 wide gamut, up to 1000 nits.


Wide Gamut
----------

Select the "Display P3" or "Rec.2020" display to view wide gamut colors.

This should be used in conjunction with the "ACEScg" or "Linear Rec.2020" working space
for materials, lights, rendering and compositing.

Requirements:

* A P3 or Rec.2020 capable monitor.
* macOS: Any Apple Silicon device.
* Linux: Use Wayland, and set the Vulkan backend in the Blender system preferences.
* Windows: Enable "Automatically manage color for apps" in the Windows display settings,
  and set the Vulkan backend in the Blender system preferences.

High Dynamic Range
------------------

Select the "Rec.2100 PQ" or "Rec.21000 HLG" display to view high dynamic range (HDR) colors.

With standard dynamic range (SDR), views must significantly lower bright colors to fit within the range.
With high dynamic range it is possible to go beyond and more accurately display the scene. HDR displays have limits
too, and there are separate views for 500, 1000, 2000 and 4000 nits to target displays with different maximum
luminance.

In Blender, HDR content automatically scales up and down along with display brightness. Seeing the full range often
requires lowering the display brightness, to make enough headroom above SDR white.

Requirements:

* A HDR capable monitor.
* macOS: Any Apple Silicon device.
* Linux: Use Wayland, and set the Vulkan backend in the Blender system preferences.
* Windows: Enable "Use HDR" in the Windows display settings, and set the Vulkan backend in the Blender system
  preferences.

.. _bpy.types.ColorManagedDisplaySettings.emulation:

Display Emulation
-----------------

:Automatic:
   Display images consistent with most other applications, to preview images and video
   for export. A best effort is made to emulate the chosen display on the actual
   display device.
:Off:
   Directly output image as produced by OpenColorIO. This is not correct in general,
   but may be used when the system configuration and actual display device is known
   to match the chosen display.

Emulation is not supported with older :ref:`OpenColorIO configurations <ocio-config>`.


.. _bpy.types.ColorManagedViewSettings.view_transform:

Views
=====

These are different ways to view the image on the same display.

:Standard:
   Does no extra conversion besides the conversion for the display. Often used for
   non-photorealistic results or video editing where a specific look is already baked into
   the input video.
:ACES 1.3:
   `ACES <https://www.oscars.org/science-technology/sci-tech-projects/aces>`__ view transforms,
   a widely used standard in film and TV production. Suitable for photorealistic results.
:ACES 2.0:
   Version 2.0 of the ACES view transform, with a more neutral look. It features a less
   aggressive tone scale with reduced mid-tone contrast and gentler highlight rolloff,
   and improve gamut mapping.
:Khronos PBR Neutral:
   A tone mapping transform designed specifically for PBR color accuracy,
   to get sRGB colors in the output render that match as faithfully as possible
   the input sRGB base color in materials, under gray-scale lighting.
   This is aimed toward product photography use cases, where the scene
   is well-exposed and HDR color values are mostly restricted to small specular highlights.
:AgX:
   A tone mapping transform that improves on *Filmic*, giving more photorealistic results.
   AgX offers 16.5 stops of dynamic range and desaturates highly
   exposed colors to mimic film's natural response to light.
:Filmic:
   A tone mapping transform designed to handle high dynamic range colors.
   Filmic is deprecated and is superseded by AgX which improves handling of saturated colors.
:Filmic Log:
   Converts to Filmic log color space. This can be used for export to color grading applications,
   or to inspect the image by flattening out very dark and light areas.
:False Color:
   Shows a heat map of image intensities, to visualize the dynamic range, and help properly expose an image.

   Below is a table that represents how normalized linear color data is represented with False Color.

   .. list-table::
      :header-rows: 1

      * - Luminance Value
        - Color
      * - Low Clip
        - Black
      * - 0.0001% to 0.05%
        - Blue
      * - 0.05% to 0.5%
        - Blue-Cyan
      * - 0.5% to 5%
        - Cyan
      * - 5% to 16%
        - Green-Cyan
      * - 16% to 22%
        - Gray
      * - 22% to 35%
        - Green-Yellow
      * - 35% to 55%
        - Yellow
      * - 55% to 80%
        - Orange
      * - 80% to 97%
        - Red
      * - High Clip
        - White

:Raw:
   Intended for inspecting the image but not for final export.
   Raw gives the image without any color space conversion.

.. _bpy.types.ColorManagedViewSettings.look:

Look
----

Choose an artistic effect from a set of measured film response data
which roughly emulates the look of certain film types. Applied before color space conversion.

.. _bpy.types.ColorManagedViewSettings.exposure:

Exposure
--------

Used to control the image brightness (in stops) applied before color space conversion.
It is calculated as follows: :math:`output\_value = render\_value × 2^{(exposure)}`

.. _bpy.types.ColorManagedViewSettings.gamma:

Gamma
-----

Extra gamma correction applied after color space conversion.
Note that the default display transforms already perform the appropriate conversion,
so this mainly acts as an additional effect for artistic tweaks.

.. _bpy.types.ColorManagedViewSettings.use_curve_mapping:

Curves
------

Adjust RGB Curves to control the image colors before the color space conversion.
Read more about using the :ref:`ui-curve-widget`.


.. _bpy.types.ColorManagedViewSettings.use_white_balance:
.. _bpy.types.ColorManagedViewSettings.white_balance:

White Balance
-------------

Adjusts colors so that a given white point (expressed in color temperature and tint) ends up as white on the display.

As an alternative to manually specifying the values, there's also a color picker.
When a color is selected, temperature and tint are set such that this color ends up being balanced to white.
This only works if the color is close enough to a blackbody emitter.

White balancing can also be accomplished as part of the compositing
pipeline by using the :doc:`/compositing/types/color/adjust/color_balance`

Temperature
   The blackbody temperature of the primary illuminant. By default a D65 white point is used.
Tint
   The amount of green/magenta shift of the blackbody curve.

.. figure:: /images/render_color-management_white-balance-curve.png
   :align: center

   Blackbody temperature curve.

Images
======

Display
-------

By default, only renders are displayed and saved with the render *View* applied.
These images are the "Render Result" and "Viewer" image data-blocks,
and the files saved directly to disk with the Render Animation operator.
However, when loading a render saved to an intermediate OpenEXR file,
Blender cannot detect automatically that this is a render
(it could be e.g. an image texture or displacement map).
We need to specify that this is a render and that we want the transformations
applied, with the following settings.

View as Render
   Display the image data-block (not only renders) with view, exposure, gamma, RGB curves applied.
   Useful for viewing rendered frames in linear OpenEXR files the same as when rendering them directly.

Output
------

For file saving an equivalent option exists.

Save as Render
   Option in the image save operator to apply the view, exposure, gamma, RGB curves.
   This is useful for saving linear OpenEXR to e.g. PNG or JPEG files in display space.

Wide gamut images can be written in the following file formats: PNG, JPEG, WebP, AVIF, TIFF and JPEG 2000.

HDR images can be written as AVIF or PNG files. They are written with 203 nits diffuse
white to match the convention in most browsers and image viewers.

Video
=====

Output
------

Videos can be rendered with both wide gamut and HDR color spaces. They use the scene display
by default, but can also be assigned a different color space by overriding the color management
settings in the output properties.

Saving HDR videos has a few additional requirements:

* Set color management display to Rec.2100 PQ or HLG
* Set codec to H.265 or AV1
* Set bit depth to 10 or 12

Video players and devices have different levels of support for HDR video.
Bit depth 10 with PQ encoding is a good default choice to maximize compatibility.

HDR videos are written with 100 nits diffuse white, to match the convention in most video
players and browsers.
