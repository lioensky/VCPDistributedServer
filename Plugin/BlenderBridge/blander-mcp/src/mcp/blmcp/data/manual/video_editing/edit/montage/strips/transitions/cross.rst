.. _bpy.types.CrossStrip:

***********
Cross Strip
***********

The *Cross* transition fades from one strip to another, also known as a crossfade.
Strips can be overlapping or have a gap between them,
however, when strips contain a gap the last and first frame of each strip
is extend which can cause a pause if any of the strips are a sequence.


Options
=======

Default Fade
   Automatically calculates a linear fade over the length of the strip.

   Effect Fader
      Allows you to manually :doc:`keyframe </animation/keyframes/index>` a custom fade.
      This can be used with different :ref:`easings <editors-graph-fcurves-settings-easing>`
      to fine-tune the fade in/out.


Example
=======

.. figure:: /images/video-editing_sequencer_strips_transitions_cross_example.png

   Cross Effect.
