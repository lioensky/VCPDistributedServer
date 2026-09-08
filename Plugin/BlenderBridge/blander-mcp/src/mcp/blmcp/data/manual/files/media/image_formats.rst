.. _bpy.types.Image:
.. _bpy.ops.image:

**************************
Supported Graphics Formats
**************************

.. _files-media-image_formats:

Image Formats
=============

This is the list of image file formats supported internally by Blender:

.. |tick|  unicode:: U+2713
.. |cross| unicode:: U+2717

.. list-table::
   :header-rows: 1
   :class: valign
   :widths: 25 25 10 10 10 20

   * - Format
     - Channel Depth
     - Alpha
     - :doc:`Metadata </render/output/properties/metadata>`
     - :term:`DPI`
     - Extensions
   * - JPEG
     - 8bit
     - |cross|
     - |tick|
     - |tick|
     - ``.jpg`` ``.jpeg``
   * - `OpenEXR`_
     - float 16, 32bit
     - |tick|
     - |tick|
     - |tick|
     - ``.exr``
   * - PNG
     - 8, 16bit
     - |tick|
     - |tick|
     - |tick|
     - ``.png``
   * - WebP
     - 8bit
     - |tick|
     - |tick|
     - |cross|
     - ``.webp``
   * - AVIF
     - 8, 10, 12bit
     - |tick|
     - |tick|
     - |cross|
     - ``.avif``
   * - BMP
     - 8bit
     - |tick|
     - |cross|
     - |tick|
     - ``.bmp``
   * - :ref:`Cineon <file-media-cineon_dpx>`
     - 8, 10, 12, 16bit
     - |tick|
     - |cross|
     - |cross|
     - ``.cin``
   * - :ref:`DPX <file-media-cineon_dpx>`
     - 8, 10, 12, 16bit
     - |tick|
     - |cross|
     - |cross|
     - ``.dpx``
   * - Iris
     - 8, 16bit
     - |tick|
     - |cross|
     - |cross|
     - ``.sgi`` ``.rgb`` ``.bw``
   * - JPEG 2000
     - 8, 12, 16bit
     - |tick|
     - |cross|
     - |cross|
     - ``.jp2`` ``.jp2`` ``.j2c``
   * - `Radiance HDR`_
     - float
     - |tick|
     - |cross|
     - |cross|
     - ``.hdr``
   * - Targa
     - 8bit
     - |tick|
     - |cross|
     - |cross|
     - ``.tga``
   * - Targa Raw
     - 8bit
     - |tick|
     - |cross|
     - |cross|
     - ``.tga``
   * - TIFF
     - 8, 16bit
     - |tick|
     - |cross|
     - |tick|
     - ``.tif`` ``.tiff``

.. hint::

   If you are not interested in technical details,
   a good rule of thumb for selecting output formats for your project is:

   Use OpenEXR
      if you intend to do compositing or color grading on these images.
   Use PNG
      if you intend on-screen output or encoding into multiple video formats.
   Use JPEG
      for on-screen output where file size is a concern and quality loss is acceptable.

   *All these formats support compression which can be important when rendering out animations.*

.. hint::

   Bit depths for image formats represent the following numbers of tonal levels per channel:

   :8: 256 levels
   :10: 1024 levels
   :12: 4096 levels
   :16: 65536 levels


Opening Images
==============

Relative Path
   Sets the file path to be relative to the currently opened blend-file.

   See :ref:`files-blend-relative_paths`.
Detect Sequences
   Automatically looks for image sequences in the selected images (based on the file name).
   Disable this when you do want to get single images that are part of a sequence.
   See :ref:`image-formats-open-sequence` for more information.
Detect UDIMs
   Automatically looks for :doc:`UDIM </modeling/meshes/uv/workflows/udims>`
   tiles in the directory of the selected image; if matches are found they are loaded into Blender as UDIMs.
   This works by detecting if the filename has a ``.xxxx`` (four digit number) before the file extension.


.. _image-formats-open-sequence:

Opening an Image Sequence
-------------------------

To load image sequence in any of the supported image file formats,
the filename of the images must contain a digit to indicate the frame order
(e.g. ``*-0001.jpg``, ``*-0002.jpg``, ``*-0003.jpg``, etc, of any image format), indicating the frame.

The sequence could be opened by the selection of the images with any of the following methods
by the confirmation with the *Open Image* button or :kbd:`Return`.

Range
   Navigate into the directory and :kbd:`LMB` click and drag over a range of names to highlight multiple files.
   You can page down and continue :kbd:`Shift-LMB` click-dragging to add more to the selection.
Batch
   :kbd:`Shift-LMB` click selected non-related stills for batch processing; each image will be one frame,
   in sort order, and can be a mix of file types (``jpg``, ``png``, ``exr``, etc.).
All
   Press :kbd:`A` to select/deselect all files in the directory.


.. _bpy.types.ImageFormatSettings:

Saving Images
=============

File Format
   Choose the image file format to save to. Based on which format is used,
   other options such as channels, bit depth and compression level are available.

Color
   The color format to save the image or video to.
   This setting is used by some formats to optimize how much data is written to the file.
   Note, *RGBA* is not available for all image formats, check the list above for details.

   :BW: Saves the image using grayscale colors.
   :RGB: Saves red, green and blue channels
   :RGBA: Saves red, green, blue and alpha channels.

.. _bpy.types.ImageFormatSettings.color_depth:

Color Depth
   Defines the bit depth per color channel, determining how many color values can be represented.

   Higher bit depths reduce color banding and improve precision but also increase file size and memory usage.
   Note, not all file formats support all color depths.

   :8:
      Most common for on-screen graphics, web, and standard video. Suitable for general-purpose use.
   :10, 12, 16:
      Used by formats focused on photography and digital cinema (e.g., DPX, JPEG 2000).
      Provides more tonal range and color detail than 8-bit.
   :32:
      32-bit floating point per channel. Provides the highest precision and dynamic range.
      Highest possible color depth, primarily used with OpenEXR for visual effects and compositing workflows.
   :Float (Half):
      16-bit floating point per channel. Offers high dynamic range with lower memory and storage usage.
      Only supported for OpenEXR files.
   :Float (Full):
      32-bit floating point per channel. Provides the highest precision and dynamic range.
      Only supported for OpenEXR files.

   .. note::

      Internally, Blender only operates in either 8-bit or 32-bit.

      Images with higher than 8-bit precision (e.g., 10-bit, 12-bit, 16-bit)
      are converted to 32-bit float when loaded into Blender.

Compression
   Used to reduce the size of the image file.
   How this is done may vary depending on the file format and settings used.

.. _bpy.types.ImageFormatSettings.quality:

Quality
   Controls the level of lossy compression applied to the image, expressed as a percentage.
   Lossy compression reduces file size by discarding some image data, which may result in a loss of detail.

   - **0%**: Maximum compression, producing the smallest file size but the most noticeable quality loss.
   - **100%**: No compression, preserving full image quality at the cost of a larger file size.
Save As Render
   Save image with render :doc:`color management </render/color_management/index>`.
   For display image formats like PNG, apply view and display transform.
   For intermediate image formats like OpenEXR, use the default render output color space.
Copy
   Defines if the data-block will reference the newly created file
   or the reference will be unchanged, maintaining it with the original one.

Color Space
   To specify the color space of the source file.

   The list of color spaces depends on the active :ref:`OCIO config <ocio-config>`.
   The default supported color spaces are described in detail here:
   :ref:`Default OpenColorIO Configuration <ocio-config-default-color-spaces>`

   .. note::

      Note, *Cineon*, *DPX*, *OpenEXR*, and *Radiance HDR*
      image types default to being saved in a linear color space.


Format Details
==============

.. _file-media-cineon_dpx:

Cineon & DPX
------------

Cineon is Kodak's standard for film scanning, 10 bits per channel and logarithmic.
DPX has been derived from Cineon as the ANSI/SMPTE industry standard.
DPX supports 16-bit colors/channels, linear as well as logarithmic.
DPX is currently a widely adopted standard used in the film hardware/software industry.

DPX as well as Cineon only stores and converts the "visible" color range of values between 0.0
and 1.0 (as a result of rendering or composite).


.. _files-images-openexr:

OpenEXR
-------

`ILM's OpenEXR <https://www.openexr.com/>`__ has become a software industry standard
for HDR image files, especially because of its flexible and expandable structure.

An OpenEXR file can store multiple layers and passes.
This means OpenEXR images can be loaded into a Compositor keeping render layers and passes intact.

.. note::

   When opening OpenEXR images, Blender will automatically set the
   :ref:`Color Space <ocio-config-default-color-spaces>` if it is detected as *Linear CIE-XYZ E* or *ACES2065-1*.


Output Options
^^^^^^^^^^^^^^

Available options for OpenEXR render output are:

Color Depth
   The exponent value (with base two) for how many colors can be represented within a single color channel.
   A higher bit depth will allow more possible colors, reducing banding, and increasing precision.
   Yet a higher bit depth will increase memory usage exponentially.

   :Float (Half):
      Saves images in a custom 16 bits per channel in a floating-point format.
      This reduces the actual "bit depth" to 10-bit, with a 5-bit power value and 1-bit sign.
   :Float (Full):
      Saves images using 32 bits per channel in a floating-point format.

.. _bpy.types.ImageFormatSettings.exr_codec:

Codec
   The type of compression to encode the EXR-file with.

   :None: Disables all compression for fastest encoding times but creates larger file sizes.
   :ZIP:
      Lossless compression using Zlib on 16 row image blocks.
   :PIZ:
      Lossless wavelet compression, effective for noisy/grainy images.
   :DWAA (lossy):
      JPEG-like lossy compression on 32 row image blocks.
   :DWAB (lossy):
      JPEG-like lossy compression on 256 row image blocks.
   :HTJ2K:
      Lossless compression based on high throughput JPEG 2000 encoding. It produces smaller
      files, but it is new and not widely supported by other software yet.
   :ZIPS:
      Lossless compression using Zlib, each image row compressed separately
   :RLE:
      Lossless run length encoding compression, works well when image rows have the same values.
   :Pxr24 (lossy):
      Converts 32-bit floats to 24 bits then uses deflate compression.
      Pxr24 is lossless for half and 32-bit integer data and slightly lossy for 32-bit float data.
   :B44 (lossy):
      Lossy compression for 16 bit float images, at fixed 2.3:1 ratio.
      B44 compresses uniformly regardless of image content.
   :B44A (lossy):
      Lossy compression for 16 bit float images, at fixed 2.3:1 ratio
      with further compression on areas of flat color are further compressed, such as alpha channels.

Quality :guilabel:`DWAA (lossy)` :guilabel:`DWAB (lossy)`
   Controls the level of lossy compression applied to the image, expressed as a percentage.
   Lossy compression reduces file size by discarding some image data, which may result in a loss of detail.

   - **0%**: Maximum compression, producing the smallest file size but the most noticeable quality loss.
   - **100%**: No compression, preserving full image quality at the cost of a larger file size.

.. _bpy.types.ImageFormatSettings.use_exr_interleave:

Interleave
   Use legacy interleaved storage of views, layers and passes for compatibility with
   applications that do not support more efficient multi-part OpenEXR files.

.. _bpy.types.ImageFormatSettings.use_preview:

Preview
   When rendering animations (or single frames via command line),
   save a JPEG copy of the image, for a quick preview.


Radiance HDR
------------

Radiance is a suite of tools for lighting simulation.
Since Radiance had the first (and for a long time the only) HDR image format,
this format is supported by many other software packages.

Radiance ``.hdr`` files store colors still in 8 bits per component,
but with an additional (shared) 8-bit exponent value, making it 32 bits per pixel.
