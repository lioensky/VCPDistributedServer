
*********
Particles
*********

.. note::

   Enabling a secondary particle type will also create a particle system for that type of particle.
   Disabling a particle type will delete this particle system including its settings.
   These particle systems are not part of the mesh generation.
   They will need to have geometry assigned in order to be rendered.  

.. _bpy.types.FluidDomainSettings.use_spray_particles:

Spray
   Create spray particles during the secondary particle simulation. Spray particles are those that
   appear to fly through the air above the liquid surface when there is a bigger splash.

.. _bpy.types.FluidDomainSettings.use_foam_particles:

Foam
   Create foam particles during the secondary particle simulation. Foam particles are those that
   solely move on the liquid surface.

.. _bpy.types.FluidDomainSettings.use_bubble_particles:

Bubbles
   Create bubble particles during the secondary particle simulation. Bubble particles are those that
   move below the liquid surface.

.. _bpy.types.FluidDomainSettings.sndparticle_combined_export:

Combined Export
   Select particle types that should go into the same particle system. This option has no effect
   on the outcome of the simulation. It only changes the way particle systems are allocated in
   the particle settings.

.. _bpy.types.FluidDomainSettings.particle_scale:

Upres Factor
   Factor by which to enhance the resolution of the particle simulation. The scaling factor is coupled
   to the :ref:`Resolution Divisions <bpy.types.FluidDomainSettings.resolution_max>` (i.e. the particle
   simulation is this times bigger than the base simulation).

.. _bpy.types.FluidDomainSettings.sndparticle_potential_max_wavecrest:

Wave Crest Potential Maximum
   Upper clamping threshold for marking fluid cells as wave crests. A higher value results in less
   marked cells.

.. _bpy.types.FluidDomainSettings.sndparticle_potential_min_wavecrest:

Wave Crest Potential Minimum
   Lower clamping threshold for marking fluid cells as wave crests. A lower value results in more
   marked cells.

.. _bpy.types.FluidDomainSettings.sndparticle_potential_max_trappedair:

Trapped Air Potential Maximum
   Upper clamping threshold for marking fluid cells where air is trapped.
   A higher value results in less marked cells.

.. _bpy.types.FluidDomainSettings.sndparticle_potential_min_trappedair:

Trapped Air Potential Minimum
   Lower clamping threshold for marking fluid cells where air is trapped.
   A lower value results in more marked cells.

.. _bpy.types.FluidDomainSettings.sndparticle_potential_max_energy:

Kinetic Energy Potential Maximum
   Upper clamping threshold that indicates the fluid speed where cells start to emit particles.
   A higher value results in generally less particles.

.. _bpy.types.FluidDomainSettings.sndparticle_potential_min_energy:

Kinetic Energy Potential Minimum
   Lower clamping threshold that indicates the fluid speed where cells start to emit particles.
   A lower value results in generally more particles.

.. _bpy.types.FluidDomainSettings.sndparticle_potential_radius:

Potential Radius
   Radius to compute potential for each cell. Higher values are slower but create smoother potential grids.

.. _bpy.types.FluidDomainSettings.sndparticle_update_radius:

Particle Update Radius
   Radius to compute position update for each particle.
   Higher values are slower but particles move less chaotic.

.. _bpy.types.FluidDomainSettings.sndparticle_sampling_wavecrest:

Wave Crest Particle Sampling
   Maximum number of particles generated per wave crest cell per frame.

.. _bpy.types.FluidDomainSettings.sndparticle_sampling_trappedair:

Trapped Air Particle Sampling
   Maximum number of particles generated per trapped air cell per frame.

.. _bpy.types.FluidDomainSettings.sndparticle_life_max:

Particle Life Maximum
   Highest possible particle lifetime.

.. _bpy.types.FluidDomainSettings.sndparticle_life_min:

Particle Life Minimum
   Lowest possible particle lifetime.

.. _bpy.types.FluidDomainSettings.sndparticle_bubble_buoyancy:

Bubble Buoyancy
   Amount of buoyancy force that rises bubbles. A high value results in bubble movement mainly upwards.

.. _bpy.types.FluidDomainSettings.sndparticle_bubble_drag:

Bubble Drag
   Amount of drag force that moves bubbles along with the fluid. A high value results in bubble movement
   mainly along with the fluid.

.. _bpy.types.FluidDomainSettings.sndparticle_boundary:

Particles in Boundary
   :Delete: Delete secondary particles that are inside obstacles or left the domain.
   :Push Out: Push secondary particles that left the domain back into the domain.

.. _bpy.ops.fluid.bake_particles:
.. _bpy.ops.fluid.free_particles:

Bake Particles, Free Particles
   This option is only available when using the :ref:`Modular <bpy.types.FluidDomainSettings.cache_type>` cache type.

   The progress will be displayed in the status bar. Pressing :kbd:`Esc` will pause the simulation.

   Once the simulation has been baked, the cache can be deleted by pressing *Free Particles*.
   It is possible to pause or resume a *Bake Particles* process.
