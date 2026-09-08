
********
Emission
********

.. reference::

   :Panel:     :menuselection:`Particle System --> Emission`

The *Emitter* system works just like its name says: it emits/produces particles for a certain amount of time.
In such a system, particles are emitted from the selected object from the *Start*
frame to the *End* frame and have a certain lifespan.
These particles are rendered default as :ref:`Halos <particle-halo>`,
but you may also render this kind of particles as objects
(depending on the particle system's render settings,
see :doc:`Visualization </physics/particles/emitter/render>`).

.. figure:: /images/physics_particles_emitter_emission_settings.png

   Particle Emission settings.

The buttons in the *Emission* panel control the way particles are emitted over time:

Number
   The maximum amount of parent particles used in the simulation.
Seed
   Blender uses this as starting point to produce random numbers during the simulation.
Frame Start
   The start frame of particle emission. You may set negative values,
   which enables you to start the simulation before the actual rendering.
End
   The end frame of particle emission.
Lifetime
   The lifespan (in frames) of the particles.
Lifetime Randomness
   A random variation of the lifetime of a given particle.
   The shortest possible lifetime is *Lifetime* × (1 - *Random*).
   Values above 1.0 are not allowed.
   For example with the default *Lifetime* value of 50 a *Random* setting of 0.5
   will give you particles with a live span ranging from 50 frames to :math:`50 × (1.0 - 0.5) = 25`
   frames, and with a *Random* setting of 0.75 you will get particles with live spans ranging
   from 50 frames to :math:`50 × (1.0 - 0.75) = 12.5` frames.


Source
======

.. reference::

   :Panel:     :menuselection:`Particle System --> Emission --> Source`

Emit From
   Defines how and where the particles are emitted,
   giving precise control over their distribution.

   .. tip::

      You may use vertex groups to confine the emission, that is done in the *Vertex Groups* panel.

   Vertices
      Emits particles from the vertices of a mesh.
   Faces
      Emits particles from the surface of a mesh's faces.
   Volume
      Emits particles from the volume of an enclosed mesh.

      .. tip::

         Your mesh must be :term:`Manifold` to emit particles from the volume.
         Some modifiers like the Edge Split Modifier break up the surface,
         in which case volume emission will not work correctly!

.. _bpy.types.ParticleSettings.use_modifier_stack:

Use Modifier Stack
   Take any :doc:`Modifiers </modeling/modifiers/introduction>` above the Particle Modifier
   in the :ref:`modifier stack <modifier-stack>` into account when emitting particles,
   else it uses the original mesh geometry.

   .. note::

      Note that particles may differ in the final render if these modifiers
      generate different geometry between the viewport and render.

Distribution
   These settings control how the emissions of particles are distributed
   throughout the emission locations when emitting from either *Faces* or *Volume*.

   Jittered
      Particles are placed at jittered intervals on the emitter elements.

      Particles/Face
         Number of emissions per face (0 = automatic).
      Jittering Amount
         Amount of jitter applied to the sampling.
   Random
      Particles are emitted from random locations in the emitter's elements.
   Grid
      Particles are set in a 3D grid and particles near/in the elements are kept.

      Invert Grid
         Invert what is considered the object and what is not.
      Hexagonal
         Uses a hexagonal-shaped grid instead of a rectangular one.
      Resolution
         Resolution of the grid.
      Random
         Add a random offset to grid locations.

Random Order
   The emitter element indices are gone through
   in a random order instead of linearly (one after the other).

   Not available for *Grid* distribution.
Even Distribution
   Particle distribution is made even based on surface area of the elements,
   i.e. small elements emit less particles than large elements, so that the particle density is even.
