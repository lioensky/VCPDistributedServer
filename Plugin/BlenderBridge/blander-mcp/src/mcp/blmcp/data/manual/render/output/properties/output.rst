
******
Output
******

.. figure:: /images/render_output_properties_output_panel.png

   Output panel.

This panel provides options for setting the location of rendered frames for animations,
and the quality of the saved images.

.. _bpy.types.RenderSettings.filepath:

File Path
   Choose the location to save rendered frames.

   When rendering an animation,
   the frame number is appended at the end of the file name with four padded zeros (e.g. ``image0001.png``).
   You can set a custom padding size by adding the appropriate number of ``#`` anywhere in the file name
   (e.g. ``image_##_test.png`` translates to ``image_01_test.png``).

   This setting expands :ref:`files-blend-relative_paths`
   where a ``//`` prefix represents the directory of the current blend-file.

.. _bpy.types.RenderSettings.use_file_extension:

Saving -- File Extensions
      Adds the correct file extensions per file type to the output files.

.. _bpy.types.RenderSettings.use_render_cache:

Saving -- Cache Result
      Saves the rendered view layers and their :doc:`passes </render/layers/passes>` to a multi-layer OpenEXR image.
      The Compositor can then use this file to improve performance, especially for heavy compositing.

      The image is stored in the *Render Cache* folder as specified in the
      :doc:`File Paths Preferences </editors/preferences/file_paths>`.
      You can also load it back into the Image Editor's Render Result, even after closing
      and reopening Blender; see :ref:`Open Cached Render <bpy.ops.image.read_viewlayers>`.

.. _bpy.types.ImageFormatSettings.media_type:

Media Type
   The type of media to save.

   :Image:
      Saves each input as a separate image file.
      Each input can use its own image format settings.
   :Multi-Layer EXR:
      Saves all inputs together in a single multi-layer OpenEXR file.
   :Video:
      Encodes each frame into a video container.
      Encoding options can be found in the `Encoding`_ panel.

.. _bpy.types.ImageFormatSettings.file_format:

File Format :guilabel:`Image`
   Choose the image file format to save to. Based on which format is used,
   other options such as channels, bit depth and compression level are available.
   See :ref:`saving images <bpy.types.ImageFormatSettings>` for list of image encoding options.

.. _bpy.types.ImageFormatSettings.color_mode:

Color :guilabel:`Image` :guilabel:`Multi-Layer EXR`
   The color format to save the image or video to.
   This setting is used by some formats to optimize how much data is written to the file.
   Note, *RGBA* is not available for all image formats, check the list above for details.

   :BW: Saves the image using grayscale colors.
   :RGB: Saves red, green and blue channels
   :RGBA: Saves red, green, blue and alpha channels.

.. _bpy.types.RenderSettings.use_overwrite:

Image Sequence -- Overwrite :guilabel:`Image` :guilabel:`Multi-Layer EXR`
   Overwrite existing files when rendering.

.. _bpy.types.RenderSettings.use_placeholder:

Image Sequence -- Overwrite :guilabel:`Image` :guilabel:`Multi-Layer EXR`
   Create empty placeholder frames while rendering.

.. hint:: Primitive Render Farm

   An easy way to get multiple machines to share the rendering workload is to:

   - Set up a shared directory over a network file system.
   - Disable *Overwrite*, enable *Placeholders* in the Render *Output* panel.
   - Start as many machines as you wish rendering to that directory.


.. _render-output-color-management-panel:

Color Management
================

This panel controls how :doc:`/render/color_management/index` is applied when saving images.

.. _bpy.types.ImageFormatSettings.color_management:

:Follow Scene:
   Uses the same color management settings defined by the active Scene.
   These properties are defined in the Render Settings
:Override:
   Uses custom color management settings defined by the properties below in the panel;
   disregarding any color management settings set at the Scene level.

For a detailed description of color management properties,
see the :ref:`Color Management <render-post-color-management>` page.


.. _render-output-pixel-density-panel:
.. _bpy.types.RenderSettings.ppm_base:
.. _bpy.types.RenderSettings.ppm_factor:

Pixel Density
=============

The pixel density (often called :term:`PPI` or :term:`DPI`) controls the intended physical size for an image.
This is often used for printing or the physical size when loaded into desktop publishing software.

The X/Y density is calculated using the render X/Y aspect,
making these values useful for storing the aspect ratio of non-square pixels.

The pixel-density is meta-data which doesn't impact the quality of the image.

.. seealso::

   :ref:`Pixel Density support for image formats <files-media-image_formats>`


.. _render-output-video-encoding-panel:
.. _bpy.types.FFmpegSettings:

Encoding
========

.. reference::

   :Panel:     :menuselection:`Properties --> Output --> Encoding`

.. figure:: /images/render_output_properties_output_video-encoding-panel.png

   Encoding panel.

Here you choose which video container, codec, and compression settings you want to use.
With all of these compression choices, there is a trade-off between file size,
compatibility across platforms, and playback quality.
In the header, you can use the presets, which choose optimum settings for you for that type of output.

.. tip::

   When you view the :doc:`System Console </advanced/command_line/index>`,
   you can see some of the output of the encoding process.
   You will see even more output if you execute Blender as ``blender -d``.

.. _bpy.types.FFmpegSettings.format:

Container
   Video container or file type. For a list of all available options, see
   :doc:`video formats </files/media/video_formats>`.

.. _bpy.types.FFmpegSettings.use_autosplit:

Autosplit Output
   If your video is huge and exceeds 2GiB, enable Autosplit Output.
   This will automatically split the output into multiple files after the first file is 2GiB in size.


Video
-----

.. _bpy.types.FFmpegSettings.codec:

Video Codec
   Chooses the method of compression and encoding.
   For a list of all available options see :doc:`video formats </files/media/video_formats>`.

   .. note:: Standards

      Some containers and codecs are not compatible with each other,
      so if you are getting errors check that your container and codec are compatible.
      Like containers and codecs are sometimes not compatible with each other, some codecs
      do not work with arbitrary dimensions. So, try to stick with common dimensions
      or research the limitations of the codec you are trying to use.

Color Depth
   The exponent value (with base two) for how many colors can be represented within a single color channel.
   A higher bit depth will allow more possible colors, reducing banding, and increasing precision.
   Yet a higher bit depth will increase memory usage exponentially.

   Note, not all file formats support every color depth configuration.

   :8:
      Allows 256 levels per channel, resulting in approximately 16.7 million total colors (RGB).
      This is the most common format for on-screen graphics and standard video.
   :10:
      Allows 1,024 levels per channel, resulting in over 1 billion total colors (RGB).

      *Available for H.264, H.265, and AV1 codecs.*
   :12:
      Allows 4,096 levels per channel, resulting in over 68 billion total colors (RGB).

      *Available for H.265 and AV1 codecs.*

.. _bpy.types.FFmpegSettings.ffmpeg_prores_profile:

Profile :guilabel:`ProRes`
   Determines the quality, compression, and data rate of the encoded video.

   :ProRes 422 Proxy:
      Lowest data rate and quality.
      Useful for offline editing or situations where storage and speed are critical.
   :ProRes 422 LT:
      Lower data rate than standard ProRes 422 with reasonable quality.
      Suitable for editing and draft reviews.
   :ProRes 422:
      Standard quality with good balance between image fidelity and file size.
      Recommended for general workflows.
   :ProRes 422 HQ:
      Higher quality and data rate than standard ProRes 422.
      Preferred for broadcast and high-end post-production.
   :ProRes 4444:
      Supports full-resolution RGB and alpha channels.
      Suitable for compositing and visual effects pipelines.
   :ProRes 4444 XQ:
      Highest quality ProRes format.
      Maintains maximum color detail and dynamic range, ideal for color grading and VFX.

.. _bpy.types.FFmpegSettings.constant_rate_factor:

Output Quality
   These are preset `Rate`_.

.. _bpy.types.FFmpegSettings.custom_constant_rate_factor:

CRF :guilabel:`Custom Quality`
   Constant Rate Factor (CRF). A smaller CRF results in better video quality but larger file size.
   The range of allowed CRF values is dependent on the codec.
   They are: 0-51 for AV1, H.264 and H.265/HEVC; 0-63 for WebP/VP9 and 1-31 for MPEG-4/DivX.
   CRF values outside the allowed range are clamped to the nearest allowed value.
   A CRF value of 0 results in lossless encoding.

.. _bpy.types.FFmpegSettings.ffmpeg_preset:

Encoding Speed
   Presets to change between a fast encode (bigger file size) and more compression (smaller file size).

.. _bpy.types.FFmpegSettings.gopsize:

Keyframe Interval
   The number of pictures per `Group of Pictures <https://en.wikipedia.org/wiki/Group_of_pictures>`__.
   Set to 0 for "intra_only", which disables `inter-frame <https://en.wikipedia.org/wiki/Inter-frame>`__ video.
   A higher number generally leads to a smaller file but needs a higher-powered device to replay it.

.. _bpy.types.FFmpegSettings.use_max_b_frames:

Max B-frames
   Enables the use of :term:`B-frames <Frame Types>`.

   .. _bpy.types.FFmpegSettings.max_b_frames:

   Interval
      The maximum number of :term:`B-frames <Frame Types>` between non-B-frames.


Rate
^^^^

.. _bpy.types.FFmpegSettings.video_bitrate:

Bitrate
   Sets the average `bit rate <https://en.wikipedia.org/wiki/Bit_rate>`__ (quality),
   which is the count of binary digits per frame.
   See also: `FFmpeg -b:v <https://ffmpeg.org/ffmpeg.html#Description>`__.

.. _bpy.types.FFmpegSettings.minrate:
.. _bpy.types.FFmpegSettings.maxrate:

Minimum / Maximum
   Video files can use what is called variable bit rate (VBR).
   This is used to give some segments of the video less compressing to frames that need more data
   and less to frames with less data. This can be controlled by the *Minimum* and *Maximum* values.

.. _bpy.types.FFmpegSettings.buffersize:

Buffer
   The `decoder bitstream buffer <https://en.wikipedia.org/wiki/Video_buffering_verifier>`__ size.

.. _bpy.types.FFmpegSettings.muxrate:

Mux Rate
   Maximum bit rate of the multiplexed stream.
   `Multiplexing <https://www.afterdawn.com/glossary/term.cfm/multiplexing>`__
   is the process of combining separate video and audio streams into a single file,
   similar to packing a video file and MP3 audio file in a zip-file.

.. _bpy.types.FFmpegSettings.packetsize:

Mux Packet Size
   Reduces data fragmentation or muxer overhead depending on the source.


.. _render-output-video-encoding-audio:

Audio
-----

These settings change how sound is exported while rendering.
To control how sound is played back from within Blender, see the audio settings
in the :ref:`Preferences <prefs-system-sound>`.

.. _bpy.types.FFmpegSettings.audio_codec:

Audio Codec
   Audio format to use. For a list of all available options, see
   :doc:`video formats </files/media/video_formats>`.

.. _bpy.types.FFmpegSettings.audio_channels:

Audio Channels
   The number of audio source "locations" to encode.

   :Mono: Output a single audio channel.
   :Stereo: Output two audio channels; typically a left and right channel.
   :4 Channels: Output a four audio channels.
   :5.1 Surround:  Output a five audio channels with one :abbr:`LFE (low-frequency effects)` channel.
   :7.1 Surround: Output a seven audio channels with one :abbr:`LFE (low-frequency effects)` channel.

.. _bpy.types.FFmpegSettings.audio_mixrate:

Sample Rate
   Sets the audio `sampling rate <https://en.wikipedia.org/wiki/Sampling_(signal_processing)#Sampling_rate>`__.

.. _bpy.types.FFmpegSettings.audio_bitrate:

Bitrate
   For each codec, you can control the bit rate (quality) of the sound in the movie.
   Higher bit rates are bigger files that stream worse but sound better.
   Use powers of 2 for compatibility.

.. _bpy.types.FFmpegSettings.audio_volume:

Volume
   Sets the output volume of the audio.


Tips
----

.. tip::

   The choice of video format depends on what you are planning to do.

   It's not recommended to render directly to a video format in the first instance.
   If a problem occurs while rendering, the file might become unplayable and you will
   have to re-render all frames from the beginning. If you first render out a set
   of static images such as the default PNG format or the higher-quality OpenEXR
   (which can retain HDR pixel data), you can combine them as
   an :doc:`Image Strip </video_editing/edit/montage/strips/image>`
   in the Video Sequencer. This way, you can easily:

   - Restart the rendering from the place (the frame) where any problem occurred.
   - Try out different video encoding options in seconds,
     rather than minutes or hours as encoding is usually much faster than rendering the 3D scene.
   - Enjoy the rest of the features of the Video Sequencer, such as adding
     :doc:`Image Strips </video_editing/edit/montage/strips/image>`
     from previous renders, audio, video clips, etc.

.. tip::

   You shouldn't post-process a lossy-compressed file as the compression artifacts may become visible.
   Lossy compression should be reserved as a final 'delivery format'.
