.. _hair-dynamics:

*************
Hair Dynamics
*************

.. reference::

   :Panel:     :menuselection:`Particle System --> Hair Dynamics`

Hair particles can have dynamic properties using physics.
To enable hair physics, click the checkbox beside *Hair Dynamics*.

Quality Steps
   Quality of the simulation in steps per frame (higher is better quality but slower).

Pin Goal Strength
   Spring stiffness of the vertex target position.

.. warning::

   If you use motion blur in your animation,
   you will need to bake one extra frame past the last frame which you will be rendering.


Collisions
==========

Quality
   A general setting for how fine and good a simulation you wish.
   Higher numbers take more time but ensure less tears and penetrations through the hair.
Distance
   The distance another object must get to the hair for
   the simulation to repel the hair out of the way.
   Smaller values might cause errors but provide some speed-up while
   larger will give unrealistic results if too large and can be slow.
   It is best to find a good in between value.
Impulse Clamping
   Prevents explosions in tight and complicated collision situations
   by restricting the amount of movement after a collision.
Collision Collection
   Only objects that are a part of this :doc:`Collection </scene_layout/collections/index>`
   can collide with the hair. Note that these objects must also have Collision physics enabled.


Structure
=========

.. reference::

   :Panel:     :menuselection:`Particle System --> Hair Dynamics --> Structure`

Vertex Mass
   Value for the mass of the hair.
Stiffness
   Controls the bending stiffness of the hair strands.

   Random
      Random stiffness of hair.

Damping
   Damping of bending motion.


Volume
======

.. reference::

   :Panel:     :menuselection:`Particle System --> Hair Dynamics --> Volume`

Some phenomena of real-world hair can be simulated more efficiently using a volumetric model instead
of the basic geometric strand model. This means constructing a regular grid such as those used in
fluid simulations and interpolating hair properties between the grid cells.

Air Drag
   Controls how thick the air is around the hair causing the hair to flow slower.
Internal Friction
   Amount of friction between individual hairs.
Voxel Grid Cell Size
   Size of the voxel grid cells for interaction effects.

Density Target
   Maximum density of the hair.
Density Strength
   The influence that the *Density Target* has on the simulation.
