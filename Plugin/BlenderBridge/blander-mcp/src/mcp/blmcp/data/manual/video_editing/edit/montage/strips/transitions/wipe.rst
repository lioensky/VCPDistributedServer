.. _bpy.types.WipeStrip:

**********
Wipe Strip
**********

The *Wipe* transition strip can be used to transition from one strip to the next.
The wipe will have no effect if created from a single strip instead of two strips.
The duration of the wipe is the intersection of the two source strips and cannot be adjusted.
To adjust the start and end of the wipe you must adjust the temporal bounds of the source strips
in a way that alters their intersection.


Options
=======

Transition
   The type of transition used.

   Single
      Reveals the next strip by uncovering it in a straight line moving across the image.
   Double
      Similar to *Single*, but uses two lines either starting from the middle of the image or the outside.
      Like the blink of an eye.
   Iris
      Reveals the next strip through an expanding (or contracting) circle.
      Like the aperture of a camera or pupil of an eye.
      You can blur the transition, so it looks like ink bleeding through a paper.
   Clock
      Like the hands of an analog clock, it sweeps clockwise or (if Wipe In is enabled)
      counterclockwise from the 9:00 position. As it sweeps, it reveals the next strip.

Direction
   Controls whether to fade *In* or *Out*.
Blur Width
   The width of the blur used to blur the transition.
Angle
   Controls the angle of the line for *Single* and *Double* transition types.

Default Fade
   Automatically calculates a linear fade over the length of the strip.

   Effect Fader
      Allows you to manually :doc:`keyframe </animation/keyframes/index>` a custom fade.
      This can be used with different :ref:`easings <editors-graph-fcurves-settings-easing>`
      to fine-tune the fade in/out.


Example
=======

.. figure:: /images/video-editing_sequencer_strips_transitions_wipe_example.png

   Wipe Effect.
