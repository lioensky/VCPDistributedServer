
************
Introduction
************

Particles are lots of items emitted from mesh objects, typically in the thousands.
Each particle can be a point of light or a mesh, and be joined or dynamic.
They may react to many different influences and forces, and have the notion of a lifespan.
Dynamic particles can represent fire, smoke, mist,
and other things such as dust or magic spells.

:doc:`Hair </physics/particles/hair/index>` type particles are a subset of regular particles.
Hair systems form curves that can represent hair, fur, grass and bristles.

You see particles as a Particle Modifier,
but all settings are done in the *Particle tab*.

.. figure:: /images/physics_particles_introduction_fur-example.jpg
   :width: 300px

   Some fur made from particles.

Particles generally flow out from their mesh into space.
Their movement can be affected by many things, including:

- Initial velocity out from the mesh.
- Movement of the emitter (vertex, face or object) itself.
- Movement according to "gravity" or "air resistance".
- Influence of force fields like wind, vortexes or guided along a curve.
- Interaction with other objects like collisions.
- Partially intelligent members of a flock (herd, school, ...),
  that react to other members of their flock, while trying to reach a target or avoid predators.
- Smooth motion with soft body physics (only *Hair* particle systems).
- Or even manual transformation with :doc:`Lattices </modeling/modifiers/deform/lattice>`.

Particles may be rendered as:

- :ref:`Halos <particle-halo>` (for Flames, Smoke, Clouds).
- Meshes which in turn may be animated (e.g. fish, bees, ...).
  In these cases, each particle "carries" another object.
- :doc:`Hair curves </physics/particles/hair/shape>`, following the path of the particle.
  These hair curves can be manipulated in the 3D Viewport (combing, adding, cutting, moving, etc.).

Every object may carry many particle systems. Each particle system may contain up to
10,000,000 particles. Certain particle types (*Hair* and *Keyed*)
may have up to 10,000 children for each particle
(children move and emit more or less like their respective parents).
The size of your memory and your patience are your practical boundaries.
