********
Rotation
********

.. reference::

   :Panel:     :menuselection:`Particle System --> Rotation`

These parameters specify how the individual particles are rotated at the start of,
and during, their lifetime. You can visualize their orientation by setting *Display As*
to *Axis* in the :doc:`/physics/particles/emitter/display` panel.

Orientation Axis
   Aligns the X axis of new particles to:

   None
      The global X axis.
   Normal
      The emitter's surface normal.
   Normal-Tangent
      The emitter's surface normal, additionally aligning the particle's Y axis to the positive V
      direction in the emitter's active UV map. This makes it possible to deform the emitter
      while keeping particle rotation consistent.
   Velocity / Hair
      The particle's initial velocity vector/hair growth direction.
   Global X, Y, Z
      One of the global axes.
   Object X, Y, Z
      One of the emitter's local axes.
Randomize
   How much to randomize the particle's initial rotation (along all axes).
Phase
   Initial rotation around the particle's X axis, going from -1 (-180°) to 1 (180°).
Randomize Phase
   Maximum random rotation to add to the *Phase*, going from 0 (0°) to 2 (360°).
Dynamic
   Whether the particles' rotation can change over time.


Angular Velocity
================

.. reference::

   :Panel:     :menuselection:`Particle System --> Rotation --> Angular Velocity`

Lets you configure if and how particles should spin over time.
*Dynamic* needs to be enabled for this to work.

Axis
   The axis to spin around. If this is set to *Velocity*, *Horizontal*, or *Vertical*,
   particles will additionally spin to keep the same orientation relative to their
   direction of movement, even if *Amount* is zero.

   None
      Spinning is disabled.
   Velocity
      Spin around the particle's velocity vector.
   Horizontal
      Spin around the axis that's horizontal (lying in the global XY plane)
      and perpendicular to the particle's velocity. Particles moving along the
      global Z axis won't spin because no unique rotation axis exists in this case.
   Vertical
      Spin around the axis that's perpendicular to both the particle's velocity
      and the above *Horizontal* axis. Particles moving along the global Z axis
      won't spin.
   Global X, Y, Z
      Spin around the chosen global axis.
   Random
      Spin around a random axis.

   .. hint::

      If you use a :doc:`/physics/forces/force_fields/types/curve_guide` and want the
      particles to always point in the direction of the curve, you should set the
      *Orientation Axis* to *Velocity / Hair*, enable *Dynamic*, and set the
      *Angular Velocity Axis* to *Velocity*.

      (For a regular object, you'd normally use the *Follow Curve* option of a
      :doc:`/animation/constraints/relationship/follow_path` or the legacy
      :ref:`Follow <bpy.types.Curve.use_path_follow>` option of the curve itself,
      but these don't work for particles.)

Amount
   How fast to spin around the *Axis*.
