.. _bpy.ops.transform.vertex_random:

*********
Randomize
*********

.. reference::

   :Mode:      Edit Mode
   :Menu:      :menuselection:`Mesh --> Transform --> Randomize`

Moves the selected vertices in random directions.

Options
=======

Amount
   Maximum displacement distance for each vertex.
Uniform
   How uniform the displacement distance should be. When 0, each vertex moves by a
   random distance between 0 and *Amount*. When 1, all vertices move by a distance
   of exactly *Amount*. The displacement direction stays random, however.
Normal
   How close the displacement direction should be to each vertex normal.
   When 0, the direction is completely random. When 1, the direction is always
   equal to the normal or its opposite.
Random Seed
   Different seeds will produce different random displacements.

.. seealso::

   :doc:`/scene_layout/object/editing/transform/randomize` in Object Mode
