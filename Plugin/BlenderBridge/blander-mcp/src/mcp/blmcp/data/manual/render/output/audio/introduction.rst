.. _bpy.ops.sound.mixdown:

************
Introduction
************

Audio can be rendered from the :ref:`topbar-render`.


Options
=======

Relative Path
   Select the file path relative to the blend-file.

Accuracy
   Sample accuracy, important for animation data (the lower the value, the more accurate).

Container
   See :doc:`here </files/media/video_formats>`.

Channels
   The number of audio source "locations" to encode.
   Each channel can be mixed to a separate file by enabling *Split Channels* (see below).

   :Mono: Output a single audio channel.
   :Stereo: Output two audio channels; typically a left and right channel.
   :Stereo LFE: Output a two audio channels with a "low-frequency effects" channel for frequencies below 120.
   :4 Channels: Output a four audio channels.
   :5.1 Surround:  Output a five audio channels with one :abbr:`LFE (low-frequency effects)` channel.
   :6.1 Surround: Output a six audio channels with one :abbr:`LFE (low-frequency effects)` channel.
   :7.1 Surround: Output a seven audio channels with one :abbr:`LFE (low-frequency effects)` channel.

Format
   Some *Audio Containers* also have option to choose a codec.
   For more information see :doc:`here </files/media/video_formats>`.

Sample Rate
   Sets the audio `sampling rate <https://en.wikipedia.org/wiki/Sampling_(signal_processing)#Sampling_rate>`__.

Split Channels
   Each audio channel will be rendered into a separate file.

.. seealso::

   - See :ref:`Scene Audio <data-scenes-audio>` settings.
   - See :ref:`Audio Output <render-output-video-encoding-audio>` settings.
   - See :ref:`Audio Preferences <prefs-system-sound>`.
