.. index:: Modeling Modifiers; Boolean Modifier
.. _bpy.types.BooleanModifier:

****************
Boolean Modifier
****************

The *Boolean* modifier combines multiple meshes using a Boolean operation.

.. figure:: /images/modeling_modifiers_generate_booleans_union-intersect-difference-examples.png

   Applying the modifier to a sphere and creating the Intersection, Union, and Difference
   with a cube. The cube is hidden for a better view.

.. warning::

   Only :term:`Manifold` meshes are guaranteed to give proper results.
   :term:`Non-manifold` ones (especially meshes with holes) will usually work well,
   but might give odd glitches and artifacts.
   However, the :guilabel:`Manifold Solver` will not work at all on non-manifold meshes.

.. tip::

   If you have marked your objects to show the edges
   (in :menuselection:`Properties --> Object --> Viewport Display`, enable *Wireframe*),
   you will see the edge creation process while you are moving your objects around.
   You can also enable :ref:`X-Ray <bpy.types.View3DShading.show_xray>` to see inside the objects.

.. seealso::

   :doc:`/modeling/meshes/editing/face/intersect_boolean` for performing one-off
   Boolean operations inside a mesh in Edit Mode.


Options
=======

.. figure:: /images/modeling_modifiers_generate_booleans_panel.png
   :align: center

   The Boolean modifier.

Operation
   :Intersect:
      Only keep the volume that's inside the modified mesh and all of the source meshes.
   :Union:
      Add the source meshes to the modified mesh while removing any interior faces.
   :Difference:
      Cut the source meshes out of the modified mesh.

Operand Type
   :Object:
      The source is a single mesh object.

   :Collection:
      The source is a collection of any number of mesh objects.
      If the *Solver* is *Float*, the *Intersect* operation is not allowed.

Object
   The source mesh object.

Collection
   The source collection. May be empty if *Solver* is *Exact*,
   in which case the modifier simply removes the modified mesh's
   interior (self-intersecting) geometry.

Solver
   Algorithm used to perform the Boolean operation.

   :Float:
      Uses a simple solver which offers good performance but lacks support for overlapping geometry.
   :Exact:
      Uses a complex solver which offers the best results and has full
      support for overlapping geometry, but is much slower.
   :Manifold:
      Uses a solver that is usually fastest but only works on :term:`Manifold` meshes
      (plus the special case of Difference with a plane).


Solver Options
--------------

Materials :guilabel:`Exact Solver`
   Method for setting materials on the new faces.

   :Index Based:
      Map the :ref:`first material <bpy.types.MaterialSlot>` of the source mesh to the first material
      of the modified mesh, the second to the second, and so on. If a source face has a higher
      material index than the number of material slots on the modified mesh, the modified mesh's
      first material is used.
   :Transfer:
      Use the same materials as on the source mesh, adding new material slots to the modified mesh
      as necessary. For empty slots, fall back to using the same material index as the source mesh.

Self Intersection :guilabel:`Exact Solver`
   Correctly handle self-intersection in the participating meshes, at the cost of performance.

Hole Tolerant :guilabel:`Exact Solver`
   Optimizes the Boolean output for :term:`Non-manifold` geometry
   at the cost of increased computational time.
   Because of the performance impact, this option should only be enabled
   when the *Exact* solver demonstrates errors with non-manifold geometry.

Overlap Threshold :guilabel:`Float Solver`
   Maximum distance between two faces to consider them as overlapping.
   This helps solve the limitation of this solver.
   If the result is still not as expected, try using the *Exact* solver.
