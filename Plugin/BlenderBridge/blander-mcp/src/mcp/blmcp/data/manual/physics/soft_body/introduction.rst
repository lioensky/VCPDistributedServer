
************
Introduction
************

Soft body simulation is used for simulating soft deformable objects.
It was designed primarily for adding secondary motion to animation,
like jiggle for body parts of a moving character.

It also works for simulating more general soft objects that bend, deform and
react to forces like gravity and wind, or collide with other objects.

While it can simulate cloth and other stiff types of deformable objects to
an extent, the :doc:`Cloth Simulation </physics/cloth/index>` can do it better
with a solver specifically designed for this purpose.

The simulation works by combining existing animation on the object with forces
acting on it. There are exterior forces like gravity or force fields and
interior forces that hold the vertices together.
This way you can simulate the shapes that an object would take on in reality if it had volume,
was filled with something, and was acted on by real forces.

Soft bodies can interact with other objects through *Collision*.
They can interact with themselves through *Self-Collision*.

The result of the soft body simulation can be converted to a static object.
You can also *bake edit* the simulation, i.e.
edit intermediate results and run the simulation from there.


Typical Scenarios for using Soft Bodies
=======================================

.. _fig-softbody-intro-cone:

.. figure:: /images/physics_soft-body_introduction_windcone.jpg
   :width: 300px

   The wind cone is a soft body, as the suspension.

   `Animation <https://vimeo.com/1865817>`__

Soft bodies are well suited for:

- Jiggle on moving characters.
- Elastic and deformable objects made of materials like rubber or gelatin.
- Tree branches moving in the wind, swinging ropes, and the like.
- Flags, wide sleeves, cushions or other simple fabric reacting to forces.


Creating a Soft Body
====================

Soft body simulation works for all objects that have vertices or control points
(meshes, curves, surfaces, and lattices).

To add a soft body simulation to an object,
go to the *Physics* tab in the Properties and activate the *Soft Body* button.
For a reference of all the settings see :doc:`this page </physics/soft_body/settings/index>`.

You start a soft body simulation by playback animation with :kbd:`Alt-A`,
and stop the simulation with :kbd:`Esc` or :kbd:`Alt-A`.


Interaction in Real-Time
========================

To work with a soft body simulation, you will find it handy to use the Timeline editor.
You can change between frames and the simulation will always be shown in the actual state.
You can interact in real-time with the simulation,
e.g. by moving collision objects or shaking a soft body object.

You can then select the soft body object while running the simulation and *Apply*
the modifier in the *Modifiers* tab of the Properties.
This makes the deformation permanent.


Tips
====

- Soft bodies work especially well if the objects have an even vertex distribution.
  You need enough vertices for good collisions. You change the deformation
  (the stiffness) if you add more vertices in a certain region.
- The calculation of collisions may take a long time. If something is not visible, why calculate it?
- To speed up the collision calculation it is often useful to collide with an additional,
  simpler, invisible, somewhat larger object.
- Use soft bodies only where it makes sense.
  If you try to cover a body mesh with a tight piece of cloth and animate solely with soft body,
  you will have no success. Self-collision of soft body hair may be activated,
  but that is a path that you have to wander alone. We will deal with
  :doc:`Collisions </physics/soft_body/collision>` in detail later.
- Try and use a *Lattice* or a *Curve Guide* soft body instead of the object itself. This may be magnitudes faster.
