
****************
Strip Properties
****************

Type
   Strip type, represented by an icon.

.. _bpy.types.Strip.name:

Name
   A text field to adjust the name of the strip, which is shown on the strip in the timeline.

   .. _bpy.ops.sequencer.strip_color_tag_set:

   Color Tag
      Strips are given a :ref:`Default Color <sequencer-strip-colors>` based on their type;
      using the color tag, you can assign a custom color to help organize your sequence.

Mute
   Uncheck to prevent the strip from producing output.


Compositing
===========

.. reference::

   :Panel:     :menuselection:`Sidebar --> Strip --> Compositing`

Blend
   The method for blending the current strip with strips in lower channels.
   See :term:`Blend Modes` for more information.
Opacity
   The opacity (:term:`alpha <Alpha Channel>`) of the strip.

   When this property is animated, the opacity is drawn as an overlay on the strip.
   The overlay will look like a dark section that follows the animation curve.
   This can be hidden by disabling the :ref:`F-Curves <bpy.types.SequencerTimelineOverlay.show_fcurves>`.


.. _bpy.types.StripTransform:

Transform
=========

.. reference::

   :Panel:     :menuselection:`Sidebar --> Strip --> Transform`

.. _bpy.types.StripTransform.filter:

Filter
   The technique used to estimate the values of pixels at non-integer coordinates within the image.

   :Auto:
      Automatically choose filter based on scaling factor.

      - No scale, no rotation, integer positions: *Nearest*
      - Scaling up by more than 2x: *Cubic Mitchell*
      - Scaling down by more than 2x: *Box*
      - Otherwise: Bilinear
   :Nearest: No interpolation; uses nearest neighboring pixel (fastest).
   :Bilinear: Interpolate between 2×2 samples.
   :Cubic Mitchell: Cubic Mitchell filter on 4×4 samples.
   :Cubic B-Spline: Cubic B-Spline filter (blurry but no ringing) on 4×4 samples.
   :Box: Averages source image samples that fall under destination pixel.

.. _bpy.types.StripTransform.offset:

Position X, Y
   Used to move the frames along the X and Y axis.

.. _bpy.types.StripTransform.scale:

Scale X, Y
   Scale the image on the X and Y axis.

.. _bpy.types.StripTransform.rotation:

Rotation
   Rotates the input two-dimensionally along the Z axis.

.. _bpy.types.ImageStrip.use_flip:

Mirror
   Mirrors the image along the X axis (left to right) or the Y axis (top to bottom).


.. _bpy.types.StripCrop:

Crop
====

.. reference::

   :Panel:     :menuselection:`Sidebar --> Strip --> Crop`

Used to crop the source image. Use *Top*, *Left*,
*Bottom*, and *Right* to control the number of pixels that are cropped.


Video
=====

.. reference::

   :Panel:     :menuselection:`Sidebar --> Strip --> Video`

Strobe
   Display every nth frame.
   For example, if you set this to 10,  the strip will only display frames 1, 11, 21, 31, 41... of the source.

   It is important to realize that this property is a float value.
   This allows you to strobe effect synced exactly to a beat.

Reverse Frames
   Plays the strip backwards starting from the last frame in the sequence.


Color
=====

.. reference::

   :Panel:     :menuselection:`Sidebar --> Strip --> Color`

Saturation
   Adjusts the vividness of colors in the image.
Multiply
   Multiplies the colors by this value. This will increase the brightness.
Multiply Alpha
   Multiply alpha along with color channels when using the *Multiply* option.
Convert to Float
   Converts input to float data.


.. _vse_sidebar_strip_sound:

Sound
=====

.. reference::

   :Panel:     :menuselection:`Sidebar --> Strip --> Sound`

Working with sound is documented further at :ref:`bpy.types.SoundStrip`.

.. _bpy.types.SoundStrip.volume:

Volume
   Adjusts the perceived loudness or intensity of the sound.

   When this property is animated, the volume is drawn as an overlay on the strip.
   The overlay will look like a dark section that follows the animation curve.
   This can be hidden by disabling the :ref:`F-Curves <bpy.types.SequencerTimelineOverlay.show_fcurves>`.
   The value is also reflected in the waveform.

.. _bpy.types.SoundStrip.sound_offset:

Offset
   Offset of the sound from the beginning of the strip, expressed in seconds.

.. _bpy.types.Sound.use_mono:

Mono
   Mixdown all audio channels into a single channel.

.. figure:: /images/vse_setup_project_striptypes_sound-pan.png
   :align: right
   :width: 220px

.. _bpy.types.SoundStrip.pan:

Pan
   Used to pan the audio between speakers in multichannel audio.
   Only mono sources can be panned; if the source file is not mono, enable *Mono* to mix the channels together.

   This value basically represents the angle at
   which it's played if you multiply the value by 90 degrees.

   For stereo, output panning works from left (-1) to center (0) and finally right (1).

   To address rear speakers, you can pan to those with higher values,
   where -2 is back left and 2 is back right.

   .. tip::

      For smooth animation you can assign values outside the soft bounds,
      since the angle wraps around over multiple rotations.

   .. note::

      The number of audio channels can be configured in the
      :ref:`Audio Output <render-output-video-encoding-audio>` settings.

.. _bpy.types.SoundStrip.pitch_correction:

Preserve Pitch
   When enabled, this option maintains the original pitch of the
   audio even when the playback speed of the strip is changed.
   When disabled, adjusting the playback speed of a sound strip also
   alters its pitch (for example, slowing down lowers the pitch, and speeding up raises it).

   This option is useful when synchronizing audio to video edits or animations
   that require timing adjustments without affecting tone or musical key.

.. _bpy.types.SoundStrip.show_waveform:

Display Waveform
   Display an approximate waveform of the sound file inside of the Sound strip.
   The waveform reflects strip volume and its animation using :doc:`keyframes </animation/keyframes/introduction>`.

   Clipping audio, i.e. values over 100% amplitude, will be shown in red.

   This option is only visible if the :ref:`Waveforms overlay <bpy.types.SequencerTimelineOverlay>` is set to *Strip*.

.. _sequencer-strips-properties-time:

Time
====

.. reference::

   :Panel:     :menuselection:`Sidebar --> Strip --> Time`

The Time panel is used to control source and timeline position of the strip.

Lock (padlock icon in panel header)
   Prevents the strip from being moved.

.. _bpy.types.Strip.show_retiming_keys:

Show Retiming Keys
   Toggle visibility and selectability of :ref:`sequencer-editing-retiming`.

.. _bpy.types.Strip.channel:

Channel
   Changes the channel number, or row, of the strip.

.. _bpy.types.Strip.frame_start:

Start
   Changes the starting frame of the strip, which is the same as selecting and moving the strip.

.. _bpy.types.Strip.frame_final_duration:

Duration
   Changes the length (in frames) of the strip. This works by changing the end frame,
   which is the same as selecting and moving the strip's right handle.
End
   Shows the ending time and frame of the strip.

.. _bpy.types.Strip.frame_offset_start:
.. _bpy.types.Strip.frame_offset_end:

Strip Offset Start/End
   Positive values will move the strip's handles inwards, making it start later than the start
   of the source material and stop before its end. This lets you trim down the source material
   to the part you need. You can enable the
   :ref:`Offsets overlay <bpy.types.SequencerTimelineOverlay.show_strip_offset>`
   to see the start and end of the full source file.

   Negative values will move the strip's handles outwards, making it start earlier than the start
   of the source material and stop after its end. This lets you show the first and/or last frame
   as a frozen image for some time.

   Instead of adjusting these offsets in the Sidebar, you can also drag the strip's handles.

.. _bpy.types.MovieStrip.animation_offset_start:
.. _bpy.types.MovieStrip.animation_offset_end:
.. _sequencer-duration-hard:

Hold Offset Start/End
   Used for trimming frames off the start/end of the source material. At first sight, this
   does the same as the *Strip Offset* properties, but you can in fact combine them
   to hold (freeze) a frame other than the first or last one. For example, if you set the
   *Hold Offset Start* to 10 and the *Strip Offset Start* to -20, the video will first show
   the 11th frame of the source for 21 frames, and then play the remaining frames.

Current Frame
   The Playhead's frame number relative to the start of the strip.


Source
======

.. reference::

   :Panel:     :menuselection:`Sidebar --> Strip --> Source`

The Source panel shows (and lets you change) the file which the strip points to,
as well as how this file should be displayed.

Directory
   The folder containing the source file for the strip.

.. _bpy.types.StripElement.filename:

Filename
   The name of the source file.
   Note that file names are limited to 256 characters.
Color Space
   The color space of the source file.

   The list of color spaces depends on the active :ref:`OCIO config <ocio-config>`.
   The default supported color spaces are described in detail here:
   :ref:`Default OpenColorIO Configuration <ocio-config-default-color-spaces>`
Alpha Mode
   If the source file has an Alpha (transparency) channel, you can choose between
   :term:`Straight Alpha` and :term:`Premultiplied Alpha`.
Stream Index :guilabel:`Movie Strip`
   The video stream to use, in case there are multiple.
Deinterlace
   Applies deinterlacing to analog video.

Source Information
   Displays information about the strip's media.

   Resolution
      Resolution of the active strip's image output.
   FPS :guilabel:`Movie Strip`
      The frame rate encoded into the video file.
      If this value does not match the scene's :ref:`Frame Rate <bpy.types.RenderSettings.fps>`,
      the perceived speed of the media will be wrong unless the speed is
      :ref:`changed <video_editing-change_fps>` to account for the difference.


Options for Image Strips
------------------------

Directory
   The directory that contains the source file(s).

Filename
   The name of the source file. For image sequences, this will be different for each frame.

Change Data/Files
   Opens a File Browser to let you select a new set of images (as an alternative to modifying
   the above textboxes). Same as :menuselection:`Strip --> Inputs --> Change Paths/Files`.


Options for Sound Strips
------------------------

Sound
   :ref:`Data-block menu <ui-data-block>` to select a sound.
File Path
   Path to the file used by the selected sound :ref:`data-block <ui-data-block>`.
Pack
   :doc:`Pack </files/blend/packed_data>` the sound into the blend-file.

.. _bpy.types.Sound.use_memory_cache:

Caching
   Sound file is decoded and loaded into the RAM.

Source Information
   Displays information about the strip's media.

   Sample Rate
      The number of samples per second the audio is encoded at.
   Channels
      The number of audio channels encoded into the audio stream.
