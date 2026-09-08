
********
Interior
********

By default, the edges of a soft-body mesh act like springs. This means that,
like a mechanical spring, they can stretch under tension and squeeze under pressure.
Their initial length is also their "ideal" or "rest" length, which they try to return to.

Having edges act like springs is what holds the mesh together. If you were to disable this
behavior (as well as the :doc:`/physics/soft_body/settings/goal`), each vertex would be free
to go anywhere independently of the others, which would stretch the mesh until it's
no longer recognizable.

Having springs along edges alone typically isn't enough, however:
vertices in quads are still free to move towards their diagonal opposite,
potentially collapsing the quad into a line.

You could solve this by creating diagonal edges everywhere, but fortunately,
you don't have to: simply enable the *Stiffness* option to have Blender create
diagonal springs internally. This way, you don't have to change your mesh.

.. list-table::

   * - .. _fig-softbody-force-interior-connection:

       .. figure:: /images/physics_soft-body_forces_interior_theory-1.svg
          :width: 180px
          :figwidth: 180px

          Base springs along edges.

     - .. _fig-softbody-force-interior-stiff:

       .. figure:: /images/physics_soft-body_forces_interior_theory-2.svg
          :width: 180px
          :figwidth: 180px

          Additional springs when Stiffness is enabled.

Another method of preventing mesh collapse is applying *Bending Stiffness*,
which adds rotational resistance: making edges try to keep their relative angles.

Both of these methods are described in more detail below. You can configure them,
as well as other settings, in the :doc:`Soft Body Edges panel </physics/soft_body/settings/edges>`.


Stiffness
=========

To show the effect of the Stiffness setting, we will drop two cubes onto a plane
(see :doc:`Collisions </physics/soft_body/collision>`). The blue cube uses quads,
while the red one uses triangles. Both cubes have their Goal setting disabled.

If *Stiffness* is disabled, the quad-only cube will collapse completely,
while the tri cube only temporarily deforms from the impact:

.. _fig-softbody-force-interior-without:

.. list-table:: Without Stiffness.

   * - .. figure:: /images/physics_soft-body_forces_interior_quadvstri-sb-001.png
          :width: 200px

          Frame 1.

     - .. figure:: /images/physics_soft-body_forces_interior_quadvstri-sb-036.png
          :width: 200px

          Frame 36.

     - .. figure:: /images/physics_soft-body_forces_interior_quadvstri-sb-401.png
          :width: 200px

          Frame 401.

If *Stiffness* is enabled, the quad cube maintains its shape as well thanks to the
extra springs:

.. _fig-softbody-force-interior-with:

.. list-table:: With Stiffness.

   * - .. figure:: /images/physics_soft-body_forces_interior_quadvstri-sb-001.png
          :width: 200px

          Frame 1.

     - .. figure:: /images/physics_soft-body_forces_interior_quadvstri-sb-sq-036.png
          :width: 200px

          Frame 36.

     - .. figure:: /images/physics_soft-body_forces_interior_quadvstri-sb-sq-401.png
          :width: 200px

          Frame 401.


Bending Stiffness
=================

The second method to stop an object from collapsing is to give it *Bending Stiffness.*
Just like the other settings, this can be combined with *Stiffness* to add bending
resistance to the diagonal springs as well.

We first do the same cube experiment as before, using only *Bending Stiffness*:

.. _fig-softbody-force-interior-bending:

.. list-table:: Bending Stiffness.

   * - .. figure:: /images/physics_soft-body_forces_interior_quadvstri-sb-001.png
          :width: 200px

          Frame 1.

     - .. figure:: /images/physics_soft-body_forces_interior_quadvstri-sb-bs-036.png
          :width: 200px

          Frame 36.

     - .. figure:: /images/physics_soft-body_forces_interior_quadvstri-sb-bs-401.png
          :width: 200px

          Frame 401.

Both cubes keep their shape. Now, we try the same thing with subdivided planes,
again a quad-based one and a triangulated one:

.. list-table::

   * - .. figure:: /images/physics_soft-body_forces_interior_quadvstri-bending-001.png
          :width: 200px

          Two planes falling.

     - .. _fig-softbody-force-interior-no-bending:

       .. figure:: /images/physics_soft-body_forces_interior_quadvstri-bending-101.png
          :width: 200px

          No bending stiffness.

     - .. figure:: /images/physics_soft-body_forces_interior_quadvstri-bending-high-101.png
          :width: 200px

          High bending stiffness (10).

Without any *Bending Stiffness*, the faces can rotate freely as though their edges were hinges.
Enabling *Stiffness* to add diagonal springs would not change this (just as triangulating doesn't).

With a high *Bending Stiffness*, however, the edges resist this rotation, and the planes
act more like planks than towels.
