
*********
Collision
*********

There are two different collision types that you may use:
collision between different objects and internal collision.
We should set one thing straight from the start --
the primary targets of the collision calculation are the vertices of a soft body.
So if you have too few vertices too few collision takes place.
Secondarily, you can use edges and faces to improve the collision calculation.


Collisions with Other Objects
=============================

For a soft body to collide with another object there are a few prerequisites:

- If *Collision Collection* is set, the object must belong to the collection.
- The collision object has to be a mesh object.
- You have to activate the *Collision* in the *Physics* tab for the collision object.
  The collision object may also be a soft body.


Examples
--------

A soft body cube colliding with a plane (Fig. :ref:`fig-softbody-collision-plane1`)
works pretty well, but a soft body plane falls right through a cube
that it is supposed to collide with (Fig. :ref:`fig-softbody-collision-plane2`).

.. list-table::

   * - .. _fig-softbody-collision-plane1:

       .. figure:: /images/physics_soft-body_collision_cube-plane-1.png

          A soft body cube colliding with a plane.

     - .. _fig-softbody-collision-plane2:

       .. figure:: /images/physics_soft-body_collision_cube-plane-2.png

          A soft body plane colliding with a cube, so no interaction at all.

Why is that? Because the default method of calculation only checks to see if the four vertices
of the soft body plane collides with the cube as the plane is pulled down by gravity.
You can activate *Collision: Face* (in the *Soft Body Edges* panel) to enable collision between
the face of the plane and the object instead, but this type of calculation takes much longer.

Let us have a closer look at the collision calculation, so you can get an idea of how we might optimize it.


Calculating Collisions
----------------------

Soft body simulations are by default done on a per-vertex basis. If the vertices of the soft body
do not collide with the collision object, there will be no interaction between the two objects.

In the video below, you can see the vertices colliding with a plane.
If a vertex penetrates the zone between *Outer* and *Inner*, it is repulsed by a force in
the direction of the face normal. The position that a vertex finally ends up in is dependent
on the forces that act upon it. In the example (the first vertex on the left in the video below)
gravity and the repulsion force of the face balance out.
The speed at which the vertex is pulled out of the collision zone is influenced by the *Choke* parameter
in the :ref:`Soft Body Solver settings <physics-softbody-settings-solver>`.

.. peertube:: fe40b174-484d-4715-82ac-70e10fa5bba5

.. seealso::

   Download the `blend-file <https://archive.blender.org/wiki/2015/uploads/8/8d/CollidingVertices.blend>`__.

Now let's see what happens if we make vertices heavier and let them travel at a faster speed.
In the video above, you can see vertices traveling at different speeds.
The two on the far right (fifth and sixth) are traveling so fast that they pass right through
the collision zone (this is because of the default solver precision, which we can fix later).
You will notice that the fourth vertex also travels quite fast and because it is heavier
it breaches the inner zone. The first three vertices collide correctly.

You can set up your collision so that edges and even faces are included in the collision calculation
in the *Soft Body Edges* panel with the Collision *Face* and *Edge* options.
The collision is then calculated differently. It is checked whether the edge or face
intersects with the collision object, the collision zones are not used.


Good Collisions
---------------

If the collision you have set up is not behaving properly, you can try the following:

- The soft body object must have more subdivisions than the collision object.
  Add loop cuts to the soft body object in strategic areas that
  you know are most likely to be involved in a collision.
- Check the direction of the face normals.
- If the collision object has sharp spikes, they might penetrate the soft body.
- The resolution of the solver must match the speed at which soft body vertices are traveling.
  Lower the parameter *Error Limit* and carefully increase *Min Step*.
- *Outer* and *Inner* should be large enough, but zones of opposite faces should not overlap,
  or you have forces in opposite directions.
- If you use strong forces you should use large zones.
- Set *Choke* to a high enough value (all the way up if necessary) if you have difficulties with repelled vertices.
- Colliding faces are difficult to control and need long calculation times. Try not to use them.

Often it is better to create a simplified mesh to use as your collision object,
however, this may be difficult if you are using an animated mesh.


Self-Collisions
===============

For information on self-collision please refer to
the :doc:`/physics/soft_body/settings/self_collision` settings.
