.. _bpy.types.CollisionModifier:
.. _bpy.types.CollisionSettings:

*********
Collision
*********

.. reference::

   :Mode:      Object Mode
   :Panel:     :menuselection:`Physics --> Collision`

:doc:`Particles </physics/particles/index>`, :doc:`Soft Bodies </physics/soft_body/index>`
and :doc:`Cloth objects </physics/cloth/index>` may collide with mesh objects.
:doc:`Boids </physics/particles/emitter/physics/boids>` try to avoid *Collision* objects.

- You may limit the effect on particles to a group of objects
  (in the :doc:`Field Weights panel </physics/particles/emitter/force_field>`).
- *Deflection* for soft body objects is difficult, they often penetrate the colliding objects.
- Hair particles ignore deflecting objects
  (but you can animate them as soft bodies which take deflection into account).

If you change the deflection settings for an object you have to recalculate the particle,
soft body or cloth system by *Delete Bake*, this is not done automatically.

.. figure:: /images/physics_collision_toggle.png
   :align: right

A collider object can be temporarily disabled via an animatable toggle to
the right of the button that permanently activates or deactivates it.


Options
=======

.. figure:: /images/physics_collision_panel.png

   Collision panel.


Collision
---------

Field Absorption
   A deflector can also deflect effectors. You can specify some collision/deflector objects which deflect
   a specific portion of the effector force using the *Field Absorption* value. 100% absorption results in no force
   getting through the collision/deflector object at all. If you have three collision object behind each other with
   e.g. 10%, 43% and 3%, the absorption ends up at around 50% :math:`100 × (1 - 0.1) × (1 - 0.43) × (1 - 0.03)`.


Particle
--------

Permeability
   Fraction of particles passing through the mesh.
Stickiness
   How much particles stick to the object.
Kill Particles
   Deletes Particles upon impact.

Damping
   Damping during a collision (independent of the velocity of the particles).

   Randomize
      Random variation of damping.

Friction
   Friction during movements along the surface.

   Randomize
      Random variation of friction.


.. _physics-collision-soft-bodt-cloth:

Soft Body and Cloth
-------------------

It is also important to note that this collision panel is used to tell
all simulations that this object is to participate in colliding/deflecting other objects
on a shared layer (particles, soft bodies, and cloth).

.. note::

   The object's shape deforms the cloth,
   so the cloth simulation must be inputted the "true" shape of that mesh object at that frame.
   This true shape is the basis shape as modified by shape keys or armatures. Therefore,
   the Collision Modifier must be **after** any of those.
   The image below shows the *Modifiers* panel for the Character mesh object
   (not the cloth object).

.. figure:: /images/physics_collision_stack.png

   Collision stack.

Damping
   Damping during a collision.
   The amount of bounce that the surfaces will have.

   - 0.0 - No damping, soft bodies will have a maximum bounciness.
   - 1.0 - Maximum damping, soft bodies will not bounce at all.

Thickness
   A padding distance is added to the inside and outside of each face, to help to prevent intersections.
   The soft body will come to rest at this distance away from the face of the colliding object.
   Outside and inside is defined by the face normal, depicted as blue arrow in Fig. :ref:`fig-collision-soft-plane`.

   Outer
      Size of the outer collision zone.
   Inner
      Size of the inner collision zone (padding distance).

.. _fig-collision-soft-plane:

.. figure:: /images/physics_collision_outer-inner.png
   :width: 380px

   A soft body vertex colliding with a plane.

Friction
   A coefficient for how slippery the cloth is when it collides with itself.
   For example, silk has a lower coefficient of friction than cotton.

Single Sided
   When enabled, the collider is considered to represent the boundary of a solid object
   rather than a thin surface, and ejects intersecting cloth in the direction of its normal.

Override Normals
   When enabled, cloth collision impulses act in the direction of the collider normals.

.. note::

   *Soft body* collisions are difficult to get perfect.
   If one of the objects move too fast, the soft body will penetrate the mesh.
   See also the section about :doc:`Soft Bodies </physics/soft_body/index>`.


Examples
========

.. figure:: /images/physics_collision_defected-particles.png

   Deflected particles.

Here is a *Meta* object, using Instancing Vertices to a particle system emitting downwards,
and deflected by a mesh cube.


Hints
=====

- Make sure that the normals of the mesh surface are facing towards the particles/points
  for correct deflection. Negative scales on the object can have a similar effect.
  Make sure to recalculate the normals after applying the scale.
- Hair particles react directly to force fields,
  so if you use a force field with a short range you do not need necessarily collision.
- Hair particles avoid their emitting mesh if you edit them in *Particle Edit Mode*.
  So you can at least model the hair with collision.
