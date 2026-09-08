.. _bpy.types.Speaker:
.. _bpy.ops.object.speaker:

***************
Speaker Objects
***************

Speaker objects are used to play sound within the 3D Viewport.
They allow for spatial audio playback, making them useful for animations and interactive scenes.
Once added, a speaker's properties can be adjusted in the Properties editor.

.. figure:: /images/render_output_audio_speaker_objects.png

   Speaker object.


Playback Time
=============

Unlike other objects, speaker playback timing is not set directly in the properties.
Instead, the :doc:`NLA editor </editors/nla/index>` is used to manage when a speaker plays
using :ref:`bpy.ops.nla.soundclip_add`:

- Sound strips in the NLA editor define when playback starts.
- Newly added speaker objects automatically receive a sound strip at the current frame.
- Multiple sound strips can be used to replay the same speaker at different times.
- Playback continues the length of audio file and does not take into account the length of the sound strip.


Data Properties
===============

.. reference::

   :Panel:     :menuselection:`Properties editor --> Data`

.. figure:: /images/render_output_audio_speaker_properties.png
   :align: right

   Speaker properties.


Sound
-----

Open
   The :doc:`/interface/controls/templates/data_block` for loading audio files.
   There are two properties you can check when loading a sound:

   Cache
      Decodes the sound and stores it in memory for faster playback.
      Best suited for short, frequently played sound effects but not for long audio tracks.
   Mono
      Forces the sound to be single-channel.
      Required for 3D audio and panning effects since multi-channel files assume premixed spatialization.

Mute
   Disables the speaker's audio output.
Volume
   Adjusts the overall loudness of the speaker.
Pitch
   Alters the playback speed, raising or lowering the pitch.
   Higher values speed up playback, while lower values slow it down.


Distance
--------

Distance-based volume attenuation controls how the loudness
of a speaker object decreases as the listener moves away.
This effect simulates real-world sound behavior,
making spatial audio more immersive by ensuring that
closer sounds are louder and distant sounds are quieter.

The following settings allow fine-tuning of how sound fades with distance:

Volume Min, Max
   Defines the minimum and maximum volume based on distance.
   The speaker's volume will not go below or above these values, regardless of distance.

Attenuation
   Controls how strongly volume decreases with distance.
   The effect depends on the scene's :ref:`Distance Model <bpy.types.Scene.audio_distance_model>`.

Max Distance
   The maximum distance at which volume attenuation calculations apply.
   Beyond this distance, the volume remains constant.


Distance Reference
   The reference distance at which the volume is considered full (1.0).
   This should match the distance at which the sound was recorded for accurate playback.


Cone
----

Settings that define the speaker's directional sound behavior.

Imagine a cone with the top at the origin of the speaker object
and the main axis of it facing in the same direction as the speaker.
The speaker emits sound directionally using an inner and an outer cone.
The angles represent their opening angles,
so 360° mean the cone is fully open and there is no directionality anymore.

- **Inside the inner cone**: Full volume is maintained.
- **Between the inner and outer cone**: Volume is interpolated linearly.
- **Outside the outer cone**: Volume is reduced according to the *Outer Cone Volume* setting.

Angle Outer
   The outer cone angle in degrees.
   Outside this cone, the volume is determined by *Outer Cone Volume*.

Angle Inner
   The inner cone angle in degrees.
   Inside this cone, full volume is maintained.

Outer Cone Volume
   The volume level outside the outer cone.
   A lower value makes the sound more directional.


.. _object-speaker-properties-animation:

Animation
---------

Controls animation data for scene-level properties, including active :doc:`Actions </animation/actions>`
and their assigned :ref:`Slot <animation-actions-slots>`.

See :ref:`animation-actions-slots-manual-assign` for more information.


Custom Properties
-----------------

Create and manage your own properties to store data in the action's data block.
See the :ref:`Custom Properties <files-data_blocks-custom-properties>` page for more information.
