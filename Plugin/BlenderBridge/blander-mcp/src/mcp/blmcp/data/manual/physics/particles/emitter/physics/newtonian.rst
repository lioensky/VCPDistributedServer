
*********
Newtonian
*********

.. reference::

   :Panel:     :menuselection:`Particle System --> Physics`
   :Type:      Newtonian

The particles will move according to classical (Newtonian) mechanics.
Particles start their life with the specified initial velocities and angular velocities,
and move according to external forces.
The response to environment and to forces is computed differently,
according to the given integrator chosen by the animator.

.. figure:: /images/physics_particles_emitter_physics_newtonian_panel.png

   Newtonian Physics settings.


Forces
======

.. reference::

   :Panel:     :menuselection:`Particle System --> Physics --> Forces`

Brownian
   Specify the amount of Brownian motion.
   Brownian motion adds random motion to the particles based on a Brownian noise field.
   This is nice to simulate small, random wind forces.
Drag
   A force that reduces particle velocity in relation to its speed and size
   (useful in order to simulate air drag or water drag).
Damp
   Reduces particle velocity (deceleration, friction, dampening).


Integration
===========

.. reference::

   :Panel:     :menuselection:`Particle System --> Physics --> Integration`

Integrators are a set of mathematical methods available to calculate the movement of particles.
The following guidelines will help to choose a proper integrator,
according to the behavior aimed at by the animator.

Integration
   Euler
      Also known as "Forward Euler". Simplest integrator.
      Very fast but also with less exact results.
      If no dampening is used, particles get more and more energy over time.
      For example, bouncing particles will bounce higher and higher each time.
      Should not be confused with "Backward Euler" (not implemented) which has the opposite feature,
      the energy decrease over time, even with no dampening.
      Use this integrator for short simulations or simulations with a lot of
      dampening where speedy calculations are more important than accuracy.
   Verlet
      Very fast and stable integrator, energy is conserved over time with very little numerical dissipation.
   Midpoint
      Also known as "2nd order Runge-Kutta". Slower than Euler but much more stable.
      If the acceleration is constant (no drag for example), it is energy conservative.
      It should be noted that in example of the bouncing particles,
      the particles might bounce higher than they started once in a while, but this is not a trend.
      This integrator is a generally good integrator for use in most cases.
   RK4
      Short for "4th order Runge-Kutta". Similar to Midpoint but slower and in most cases more accurate.
      It is energy conservative even if the acceleration is not constant.
      Only needed in complex simulations where Midpoint is found not to be accurate enough.
Timestep
   The amount of simulation time (in seconds) that passes during each frame.
Subframes
   The number of simulation steps per frame.
   Subframes to simulate for improved stability and finer granularity in simulations.
   Use higher values for faster-moving particles.

The following options are only available for Fluid type physics:

Adaptive
   Automatically set the number of subframes.

   Threshold
      A tolerance value that allows the number of subframes to vary.
      It sets the relative distance a particle can move before requiring more subframes.

      The number of steps per frame will be at least Subframes + 1.
      More subframes may be simulated if the fluid becomes turbulent, according to the Threshold.


Deflection
==========

.. reference::

   :Panel:     :menuselection:`Particle System --> Physics --> Deflection`

Size Deflect
   Use the particle size in deflections.
Die on Hit
   Kill particle when it hits a deflector object.
Collision Collection
   If set, particles collide with objects from the collection.
