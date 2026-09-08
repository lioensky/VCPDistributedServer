********
Channels
********

A channel is a horizontal track that's similar to a layer in an image editing program:
higher channels are displayed in front of lower ones.

Within each channel, you can create one or more
:doc:`strips </video_editing/edit/montage/strips/introduction>`, which contain either
a segment of video content (a rendered scene, an external video file...)
or an :doc:`effect </video_editing/edit/montage/strips/effects/index>`
(color blending, blurring...). The X axis represents time, so the further a strip
is placed to the right, the later it will play in the final video.

While a channel can contain multiple strips, they can't overlap each other.
If you want two strips to play at the same time, you need to place them in different channels.

.. _bpy.types.SequenceTimelineChannel:

Channel Region
==============

The Channel region sits on the left side of the editor and contains the channel properties
listed below. Its visibility can be toggled with :menuselection:`View --> Channels`.

.. _bpy.types.SequenceTimelineChannel.name:

Name
   The name of the channel. Double-click to change.

.. _bpy.types.SequenceTimelineChannel.mute:

Mute Channel
   Disable the entire channel so that none of its strips can be seen (or heard) in the final video.
   Note that you can also mute individual strips.

.. _bpy.types.SequenceTimelineChannel.lock:

Lock Channel
   Lock the entire channel to protect all its strips against accidental changes.
   Note that you can also lock individual strips.

