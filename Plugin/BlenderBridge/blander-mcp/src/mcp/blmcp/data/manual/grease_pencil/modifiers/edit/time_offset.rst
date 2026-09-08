.. index:: Grease Pencil Modifiers; Time Offset Modifier
.. _bpy.types.GreasePencilTimeModifier:

********************
Time Offset Modifier
********************

The *Time Offset* Modifier applies a temporal offset to Grease Pencil keyframes on your timeline.
If you have duplicated a Grease Pencil object you can use the Time Offset Modifier on the copies to
desynchronize their animation. This can give more natural looking results.

Using the Time Offset Modifier it's possible to have Grease Pencil frame ranges play back as repeating loops.
Traditionally, 2D animation that uses looped drawings includes characters walking, rising smoke, and falling
rain.
In Fixed Frame mode the Time Offset Modifier can display drawings on your timeline entirely independently of
the playhead position.


This can be handy for displaying drawings that will appear often in your animation. Think of switching between
predefined mouth shapes for instance.


Options
=======

.. figure:: /images/grease-pencil_modifiers_deform_time-offset_panel.png
   :align: right

   Time Offset Modifier.

Mode
   :Regular:
      Offsets keyframes in the default animation playback direction (playhead moving from left to right).
   :Reverse:
      Offsets keyframes in reversed animation playback direction (playhead moving from right to left).
   :Fixed Frame:
      The Frame parameter determines which frame is displayed. This value needs to be animated in order to
      have the displayed frame change during playback.

      Frame
         The number of the frame to display.

   :Ping Pong:
      Loop back and forth animation.
   :Chain:
      It allows to combine the different Modes consecutively.

      Repeat
         Number of cycle repeats

Frame Offset
   The number of frames to offset the original keyframes by.

Scale
   Controls the speed of the frames playback. 1 is equal to the actual frame rate, could be positive (faster)
   or negative (slower).

Keep Loop
   Moves end frame to the animation start to keep animation in a loop.


Custom Range
------------

When enabled, the animation playback is restricted only to a frame range.

Frame Start/End
   Sets the range start and end frames.


Influence
---------

See :ref:`grease-pencil-modifier-influence-filters`.
