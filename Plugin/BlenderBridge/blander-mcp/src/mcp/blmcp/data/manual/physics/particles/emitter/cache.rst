
*****
Cache
*****

.. reference::

   :Panel:     :menuselection:`Particle System --> Cache`

In order to improve real-time response and avoid unnecessary recalculation of particles,
the particle data can be cached in memory or stored on a drive.

The *Emitter* particle system uses a unified system for caching and baking (together with Soft Body and Cloth).

.. figure:: /images/physics_particles_emitter_cache_settings.png

   Particles Cache settings.

.. seealso::

   See the :doc:`General Baking </physics/baking>` docs for more information.


Hints
=====

- The simulation is only calculated for positive frames
  in between the *Start* and *End* frames of the *Cache* panel, whether you bake or not.
  So if you want a simulation that is longer than the default frame range, you have to change the *End* frame.
- When an animation is played, each physics system writes each frame to the cache.
  Note that for the cache to fill up,
  one has to start the playback before or on the frame that the simulation starts.
- The cache is cleared automatically on changes. But not on all changes,
  so it may be necessary to delete it manually, e.g. if you change a force field.
- The system is protected against changes after baking.
  If for example the mesh changes the simulation is not calculated anew.
- The bake result can be cleared by clicking on the *Delete Bake* button in the simulation cache settings.
- A simulation can only be edited in Particle Edit Mode when it has been baked in memory.
  And cannot be edited if the Disk Cache is used.
- If you are not allowed to write to the required subdirectory caching will not take place,
  e.g. if your blend-file path is very long and your operating system
  has a limit on the path length that is supported.
- Be careful with the sequence of modifiers in the modifier stack.
  You may have a different number of faces in the 3D Viewport and
  for rendering (e.g. when using subdivision surface), if so,
  the rendered result may be very different from what you see in
  the 3D Viewport.
