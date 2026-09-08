
********
Children
********

.. reference::

   :Panel:     :menuselection:`Particle System --> Children`

*Children* are *Hair* or *Emitter* particles originating from individual particles.
They make it possible to work primarily with a relatively low amount of Parent particles,
for whom the physics are calculated. The children are then aligned to their parents.
The number and visualization of the children can be changed without a recalculation of the physics.

If you activate children, the parents are no longer rendered. This can be enabled in the Render panel
:ref:`Parent Particles <bpy.types.ParticleSettings.use_parent_particles>`. By default, parent particles
are not rendered because the shape of the children can be quite different from that of their parents.


Common Options
==============

Child Type
   None
      No children are generated.
   Simple
      Children are emitted from the parent position.
   Interpolated
      Children are emitted between the *Parent* particles on the faces of a mesh.
      They interpolate between adjacent parents. This is especially useful for fur,
      because you can achieve an even distribution.
      Some of the children can become virtual parents, which are influencing other particles nearby.
Display Amount
   The number of children in the 3D Viewport.
Render Amount
   The number of children to be rendered.
Length
   Length of child paths.
Threshold
   Amount of particles left untouched by child path length.
Seed
   Offset in the random number table for child particles, to get a different randomized result.


Clumping
--------

.. reference::

   :Panel:     :menuselection:`Particle System --> Children --> Clumping`

Use Clump Curve
   Use :ref:`ui-curve-widget` instead of parameters.
Clump
   Clumping amount along child strands.
   The children may meet at their tip (1.0) or start together at their root (-1.0).
Shape
   Form of *Clump*. Either inverse parabolic (0.99) or exponentially (-0.99).
Twist
   .. todo:: Add this information.
Use Twist Curve
   .. todo:: Add this information.


Clump Noise
^^^^^^^^^^^

Creates random clumps around the parent hair.

Clump Noise Size
   The size of the clumps.


Roughness
---------

.. reference::

   :Panel:     :menuselection:`Particle System --> Children --> Roughness`

Use Roughness Curve
   Use :ref:`ui-curve-widget` instead of parameters.
Uniform, Size
   It is based on children location so it varies the paths in a similar way when the children are near.
Endpoint, Shape
   "Rough End" randomizes path ends (a bit like random negative clumping).
   Shape may be varied from <1 (parabolic) to 10.0 (hyperbolic).
Random, Size, Threshold
   It is based on a random vector so it is not the same for nearby children.
   The threshold can be specified to apply this to only a part of children.
   This is useful for creating a few stray children that will not do what others do.


Kink
----

.. reference::

   :Panel:     :menuselection:`Particle System --> Children --> Kink`

.. _fig-particle-child-kink:

.. figure:: /images/physics_particles_emitter_children_kink.png

   Child particles with Kink.

   From left to right: Curl, Radial, Wave, Braid, Spiral.

With *Kink* you can rotate the children around the parent.
See Fig. :ref:`fig-particle-child-kink` above picture for the different types of *Kink*.

Kink Type
   Nothing
      Deactivated.
   Curl
      Children grow in a spiral around the parent hairs.
   Radial
      Children form around the parent a wave shape that passes through the parent hair.
   Wave
      Children form a wave, all in the same direction.
   Braid
      Children braid themselves around the parent hair.
   Spiral
      Generates a spiral at the end of each hair.

      Radius, Resolution
         Define the overall size.
      Shape
         Makes the spiral grow in- or outward.

   .. note:: Alignment Limitations

      When hair is pointing straight up (along the chosen spiral axis, default Z), spirals may not show up!
      This is a limitation of the projection method used.
      Giving a slight tilt or random orientation to hairs fixes this.

Amplitude
   The amplitude of the offset.
Clump
   How much clump effects kink amplitude.
Flatness
   How flat the hairs are.

Frequency
   The frequency of the offset (1/total length). The higher the frequency the more rotations are done.
Shape
   Where the rotation starts (offset of rotation).


Simple
======

Size
   A multiplier for children size.
Random Size
   Random variation to the size of child particles.

Radius
   The radius in which the children are distributed around their parents.
   This is 3D, so children may be emitted higher or lower than their parents.
Roundness
   The roundness of the children around their parents. Either in a sphere (1.0) or in-plane (0.0).


Interpolated
============

Virtual Parents
   Relative amount of virtual parents.
Long Hair
   Calculate children that suit long hair well.


Parting
-------

Parting
   Creates parting in the children based on parent strands.

Min/Max
   The minimum/maximum root to tip angle (tip distance/root distance for long hair).


Example
=======

.. figure:: /images/physics_particles_emitter_children_round-clump.png

   From left to right: Round: 0.0, Round: 1.0, Clump: 1.0, Clump: -1.0, Shape: -0.99.
