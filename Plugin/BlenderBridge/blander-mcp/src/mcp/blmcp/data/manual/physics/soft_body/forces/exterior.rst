
********
Exterior
********

Exterior forces are applied to the vertices (and nearly exclusively to the vertices)
of soft body objects. This is done using Newton's Laws of Physics:

- If there is no force on a vertex, it stays either unmoved or moves with constant speed in a straight line.
- The acceleration of a vertex depends on its mass and the force.
  The heavier the mass of a vertex the slower the acceleration. The larger the force the greater the acceleration.
- For every action there is an equal and opposite reaction.

Well, this is done only in the range of computing accurateness,
there is always a little damping to avoid overshoot of the calculation.


Example
=======

We will begin with a very simple example: the default cube.

- To judge the effect of the external forces you should at first turn off the *Goal*,
  so that the vertices are not retracted to their original position.
- Start playback to run the simulation.

What happens? The cube moves in negative Z direction.
Each of its eight vertices is affected by a global, constant force -- the gravitation.
Gravitation without friction is independent from the weight of an object,
so each object you would use as a soft body here would fall with the same acceleration.
The object does not deform, because every vertex moves with the same speed in the same direction.


Force Fields
============

Soft body vertices interact with all the :doc:`Force Fields </physics/forces/force_fields/index>`
applied (usually to particles) in the layer, such as wind, force fields,
and what ever physics field effect is on a common layer.


Soft Body Field Weights
-----------------------

.. reference::

   :Panel:     :menuselection:`Physics --> Soft Body --> Field Weights`

The *Soft Body Field Weights* panel allows you to control how much influence
each type of external force field has on the soft body system.

Effector Collection
   Limit effectors to a specified group. Only effectors in this group will have an effect on the current system.
Gravity
   Control how much the Global Gravity has an effect on the system.
All
   Scale all of the effector weights.


.. _physics-softbody-forces-exterior-aerodynamics:

Aerodynamics
============

Edges can be affected by wind as they move, and sail or flutter in a breeze.
A simple aerodynamic model of a flag sailing in the wind.

This special exterior force is not applied to the vertices but to the connecting edges.
Technically, a force perpendicular to the edge is applied.
The force scales with the projection of the relative speed on the edge (dot product).
Note that the force is the same if wind is blowing or if you drag the edge through the air
with the same speed. That means that an edge moving in its own direction subject to no force,
and an edge moving perpendicular to its own direction is subjected to maximum force.

The angle and the relative speed between medium and edge is used to calculate the force on the edge.
This force results that vertices with few connecting edges (front of a plane)
fall faster than vertices with more connecting edges (middle of a plane).
If all vertices have the same amount of edges in a direction they fall with equal speed.

The *Aerodynamics* settings are set in the :ref:`Soft Body Edges <physics-softbody-settings-aerodynamics>` panel.


.. _physics-softbody-forces-exterior-goal:

Goal
====

A "goal" is a shape that a soft body object tries to conform to.
It acts like a pin on a chosen set of vertices, controlling how much of an effect soft body has on them.

Enabling *Soft Body Goal* tells Blender to use the position (or animated position) of a vertex in the simulation.
Animating the vertices can be done in all the usual ways (F-Curves, armatures, parents, lattices, etc.)
before the soft body simulation is applied. The "goal" is the desired end position for vertices.
How a soft body tries to achieve this goal can be defined using stiffness forces and damping.

See the :doc:`Goal Settings </physics/soft_body/settings/goal>` for details.


Goal Strength
-------------

The *Goal Strength* defines how much motion from an animation system gets applied.

A *Goal* value of 1.0 means no soft body simulation,
the object act like any regular animated object (i.e. the vertex is kept at its original position).
When setting *Goal* to 0.0 (or no goal), the vertex is only influenced by physical laws
according to soft body simulation.

By setting goal values between 0.0 and 1.0,
you can blend between having the object affected only by the animation system,
and having the object affected only by the soft body effect.

Goal also serves as a memory, to make sure soft objects don't deform too much,
ending up in the non-soft animated shape. Using the *Vertex Group* weight system,
you can define a *Goal* weight per vertex. To make this look more natural,
spring forces can be defined to control how far vertices can move from their original position.

Often :ref:`painting-weight-index` is used to adjust the weight comfortably.
For non-mesh objects the *Weight* parameter of their vertices/control points is used instead;
Use the Context menu in Edit Mode or the *Transform* panel in the Sidebar region.
The weight of *Hair* particles can also be painted in :doc:`Particle Edit Mode </physics/particles/mode>`.


Technical Details
=================

In the Soft Body world, vertices of meshes are treated as particles having a mass.
Their movement is determined by the forces affecting them. Beside other forces
the individual particles can interact with another along edges using a physical model
which is very close to shock absorbers used in cars. The working parts are:

- A spring trying to keep the particles at a certain distance.
  How hard the spring tries to do that is controlled by the soft body parameter *Stiffness*.
- A damping element to calm the movement down.
  The resistance the element builds up against motion is controlled by the soft body parameter *Damping*.
