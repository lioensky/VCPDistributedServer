.. _bpy.types.ParticleHairKey:
.. _bpy.types.ParticleKey:
.. _bpy.types.ParticleTarget:

*****
Keyed
*****

.. reference::

   :Panel:     :menuselection:`Particle System --> Physics`
   :Type:      Keyed

The path of Keyed particles is determined between particles of any two (or more) particle systems.
This allows the creation of a chains of systems to create long strands or groovy moving particles.
Basically the particles have no dynamics but are interpolated from one system to the next each frame.

To setup *Keyed* particles you need at least two particle systems in the *Keys* list.


Options
=======

.. figure:: /images/physics_particles_emitter_physics_keyed_panel.png
   :align: right

   Keyed Physics settings.

Loops
   Sets the number of times the entire *Keys* list is repeated. Disabled if *Use Timing* is enabled.
Use Timing
   Enabling this option allows you to specify the timing for each key independently,
   using the *Time* and *Duration* options.
   By default, the *Use Timing* option is deactivated, and the particles will pass through all keys
   for a time equal to its lifetime. A shorter lifetime means faster movement.
   The lifetime will be split equally between the keys,
   this may lead to varying particle speeds between the targets.


Relations
=========

.. reference::

   :Panel:     :menuselection:`Particle System --> Physics --> Relations`

Key Targets
   The :ref:`list view <ui-list-view>` of keys (target particle systems).
Object
   The name of a target object for the selected key. If empty it uses the current particle system.
System
   Index of particle system on the target object.
Time
   The time (frame number) at which the particles will be at the position of the selected system.
   Note also that the *Start* frame of the Keyed system adds an offset to this time.
Duration
   How long (in frames) the particles stay on this system before they start moving to the next one.
