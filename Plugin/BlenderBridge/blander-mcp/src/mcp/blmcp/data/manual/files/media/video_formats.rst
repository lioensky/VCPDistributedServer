
*******************************
Supported Video & Audio Formats
*******************************

Blender used `FFmpeg <https://ffmpeg.org/>`__ to handle video encoding/decoding various video formats.
These formats are primarily used for compressing rendered sequences into a playable movie.
Video formats are composed of a container, a codec, and sometimes audio which is stored using its own codec.
The roll of the container to encapsulate video and audio data that is compressed using a codec.

Codecs compress the channels of a video down to save space and enable continuous playback.
*Lossy* codecs make smaller files at the expense of image quality,
while *lossless* codecs compress as much as possible the video/audio, but without losing any existing data.

Some codecs, like H.264, are great for larger images. Codecs are used to encode and decode the movie,
and so must be present on both the encoding machine (Blender) and the target machine.
The results of the encoding are stored in a container file.

There are dozens, if not hundreds, of codecs, including Xvid, H.264, DivX, Microsoft,
and so on. Each has advantages and disadvantages, and compatibility with different players on
different operating systems.

.. note::

   Most codecs can only compress the RGB or YUV colors,
   but some support the Alpha channel as well. Codecs that support RGBA include:

   - `FFmpeg video codec #1 <https://en.wikipedia.org/wiki/FFV1>`__
   - `PNG <https://en.wikipedia.org/wiki/Portable_Network_Graphics>`__
   - QuickTime Animation
   - WebM/VP9 (although Blender will not import the alpha channel due to
     a `limitation of FFmpeg <https://trac.ffmpeg.org/ticket/8344>`__).


.. _files-video-containers:

FFmpeg Containers
=================

:`MPEG-4 <https://en.wikipedia.org/wiki/MPEG-4>`__:
   While being a :ref:`video codec <files-video-codecs>`, it is also a real container,
   in which you can store video and audio streams using various codecs.
   It is widely supported by many modern software and hardware players.

   File Extensions: ``.mp4``, ``.mpg``, ``.mpeg``
:`Matroska <https://en.wikipedia.org/wiki/Matroska>`__:
   A free open-standard container format, a file format that can hold an unlimited number of video,
   audio, picture or subtitle tracks in one file.

   File Extension: ``.mkv``
:`WebM <https://en.wikipedia.org/wiki/WebM>`__:
   A free open-standard container format, designed to be used for internet streaming.
   Note that this container can only hold a VP9 video codec, and Vorbis or Opus audio codecs.

   File Extension: ``.webm``

-----

:`AVI <https://en.wikipedia.org/wiki/Audio_Video_Interleave>`__:
   A derivative of the Resource Interchange File Format (RIFF).
   One of the first and most widely used video container format.

   File Extension: ``.avi``
:`DV <https://en.wikipedia.org/wiki/DV>`__:
   An intra-frame video compression scheme, used by many digital camcorders back in the days.
   It uses the discrete cosine transform (DCT, similar algorithm to JPEG)
   to compress video on a frame-by-frame basis.
   Audio is stored uncompressed.
   This container enforces the video codec, you can only define quality parameters.

   File extension: ``.dv``
:`Flash <https://en.wikipedia.org/wiki/Flash_Video>`__:
   A container file format used to deliver video over the internet using Adobe Flash Player.
   This container enforces the video codec, you can only define quality parameters.

   File Extension: ``.flv``
:`MPEG-1 <https://en.wikipedia.org/wiki/MPEG-1>`__:
   A standard for lossy compression of video and audio.
   It is designed to compress VHS-quality raw digital video and CD audio down to 1.5 Mbit/s.
   This container enforces the video codec, you can only define quality parameters, and the audio codec.

   File Extensions: ``.mpg``, ``.mpeg``
:`MPEG-2 <https://en.wikipedia.org/wiki/MPEG-2>`__:
   A standard for "the generic coding of moving pictures and associated audio information".
   It describes a combination of lossy video compression and lossy audio data compression
   methods which permit storage and transmission of movies using
   currently available storage media (notably DVDs) and transmission bandwidth.
   This container enforces the video codec, you can only define quality parameters, and the audio codec.

   File Extensions:  ``.dvd``, ``.vob``, ``.mpg``, ``.mpeg``
:`Ogg <https://en.wikipedia.org/wiki/Ogg>`__:
   A free open-standard container format, that can hold an unlimited number of video,
   audio, picture or subtitle tracks in one file.

   File Extensions:  ``.ogg``, ``.ogv``
:`QuickTime <https://en.wikipedia.org/wiki/.mov>`__:
   A multi-tracks format. QuickTime and MP4 container formats can use the same codecs.
   They are mostly interchangeable in a QuickTime-only environment.
   MP4, being an international standard, has more support.

   File Extension: ``.mov``


.. _files-video-codecs:

FFmpeg Video Codecs
===================

These options are not available with all :ref:`Containers <files-video-containers>`.

:No Video: For audio-only encoding.
:`AV1 <https://en.wikipedia.org/wiki/AV1>`__:
   A free open-standard lossy video compression format, designed as a successor to *VP9*.
   AV1 offers great compression rates and visual quality,
   *AV1* produces video files that are about 30% more space efficient than *VP9*
:`H.264 <https://en.wikipedia.org/wiki/Advanced_Video_Coding>`__:
   A modern variation of the MPEG-4 family, this lossy codec is very commonly used.
   It offers a very good compression/quality ratio.
:`H.265 / HEVC <https://en.wikipedia.org/wiki/High_Efficiency_Video_Coding>`__:
   An improved format of H.264 with improved compression efficiency, advanced motion compensation,
   larger coding blocks, and enhanced prediction models for high-resolution content.
:`WEBM / VP9 <https://en.wikipedia.org/wiki/VP9>`__:
   A free open-standard lossy video compression format.
   One of the most recent codecs, it is widely used for internet streaming.

-----

:`DNxHD <https://en.wikipedia.org/wiki/Avid_DNxHD>`__:
   Intended to be usable as both an intermediate format suitable for use while editing,
   and as a presentation format. It can be either lossless or lossy.
:`DV <https://en.wikipedia.org/wiki/DV>`__:
   See :ref:`Containers <files-video-containers>`.
:`FFmpeg video codec #1 <https://en.wikipedia.org/wiki/FFV1>`__:
   FFV1 is a lossless intra-frame video codec.
   It can use either variable length coding or arithmetic coding for entropy coding.
   The encoder and decoder are part of the free, open-source library libavcodec in FFmpeg.
   Supports an alpha channel.
:`Flash Video <https://en.wikipedia.org/wiki/Flash_Video>`__:
   See :ref:`Containers <files-video-containers>`.
:`HuffYUV <https://en.wikipedia.org/wiki/Huffyuv>`__:
   Lossless video codec created by Ben Rudiak-Gould which is
   meant to replace uncompressed YCbCr as a video capture format.
:`MPEG-1 <https://en.wikipedia.org/wiki/MPEG-1>`__:
   See :ref:`Containers <files-video-containers>`.
:`MPEG-2 <https://en.wikipedia.org/wiki/MPEG-2>`__:
   See :ref:`Containers <files-video-containers>`.
:`MPEG-4(DivX) <https://en.wikipedia.org/wiki/MPEG-4>`__:
   Inherits many of the features of MPEG-1, MPEG-2 and other related standards, but also adds new features.
:`ProRes <https://en.wikipedia.org/wiki/Apple_ProRes>`__:
   A high-quality, visually lossless video codec developed by Apple Inc.
   It is commonly used in professional post-production workflows.

   ProRes output supports a configurable :ref:`Profile <bpy.types.FFmpegSettings.ffmpeg_prores_profile>`
   to control the quality, compression level, and data rate of the encoded video.

:`PNG <https://en.wikipedia.org/wiki/Portable_Network_Graphics>`__:
   Lossless, this stores each frame as an independent image in the video stream.
   Compression will be poor, but as every frame is fully self-contained, scrubbing and editing can be simpler.
   Supports an alpha channel.
:`QuickTime Animation <https://en.wikipedia.org/wiki/QuickTime_Animation>`__:
   Original format of QuickTime videos. Supports an alpha channel.
:`Theora <https://en.wikipedia.org/wiki/Theora>`__:
   A free open-standard lossy codec designed together with the :ref:`Ogg container <files-video-containers>`.


.. _files-audio-codecs:

FFmpeg Audio Codecs
===================

:No Audio:
   For video-only encoding.
:`AAC <https://en.wikipedia.org/wiki/Advanced_Audio_Coding>`__:
   Advanced Audio Codec, a standardized, lossy compression and encoding scheme for digital audio.
   AAC generally achieves better sound quality than MP3 at similar bit rates.
:`AC3 <https://en.wikipedia.org/wiki/Dolby_Digital>`__:
   Audio Codec 3, an audio compression technology developed by Dolby Laboratories.
:`FLAC <https://en.wikipedia.org/wiki/FLAC>`__:
   Free Lossless Audio Codec.
   Digital audio compressed by FLAC's algorithm can typically be reduced to 50-60% of its original size.
:`MP2 <https://en.wikipedia.org/wiki/MPEG-1_Audio_Layer_II>`__:
   A lossy audio compression format.
:`MP3 <https://en.wikipedia.org/wiki/MP3>`__:
   A lossy audio compression format, widely used as final audio format.
:`Opus <https://en.wikipedia.org/wiki/Opus_(audio_format)>`__:
   A lossy audio compression format, designed to encode speech or general audio
   and is intended to replace the *Vorbis* codec.
:`PCM <https://en.wikipedia.org/wiki/PCM>`__:
   Pulse Code Modulation, a method used to digitally represent sampled analog signals.
   It is the standard form for digital audio in computers and various Blu-ray,
   Compact Disc and DVD formats, as well as other uses such as digital telephone systems.
:`Vorbis <https://en.wikipedia.org/wiki/Vorbis>`__:
   An open-standard, highly-compressed format comparable to MP3 or AAC.
   Vorbis generally achieves better sound quality than MP3 at similar bit rates.


Known Limitations
=================

Video Output Size
-----------------

Some codecs impose limitations on output size,
``H.264``, for example requires both the height and width to be divisible by 2.
