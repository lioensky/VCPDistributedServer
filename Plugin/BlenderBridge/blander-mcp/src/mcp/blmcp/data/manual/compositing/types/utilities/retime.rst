.. index:: Compositor Nodes; Retime

***********
Retime Node
***********

.. figure:: /images/node-types_CompositorNodeRetime.webp
   :align: right
   :alt: Retime Node.

The *Retime* node controls the timing of input sequences, animations, or time-based effects
by offsetting, skipping, or repeating frames.
It can be used to create time remapping effects such as slow motion, fast-forward, looping,
or rhythmic stutter effects within a compositing setup.


Inputs
======

Offset
   Adds or subtracts a constant frame offset from the input sequence.
   Positive values delay the input, while negative values advance it.

Step
   Skips frames by the specified step size.
   For example, a value of 2 plays every other frame, effectively doubling playback speed.

Speed
   Scales time globally, controlling how fast or slow the sequence progresses.
   A value of 1.0 plays the sequence at normal speed, 0.5 at half speed, and 2.0 at double speed.

Cyclic
   When enabled, the input sequence loops continuously when the retimed output exceeds
   its original frame range.

Cycle Length
   Defines the number of frames in one loop cycle when *Cyclic* is enabled.


Outputs
=======

Frame
   The remapped frame output based on the specified timing parameters.
   This output can be connected to nodes that take frame-based inputs to drive
   animated or sequential effects.
