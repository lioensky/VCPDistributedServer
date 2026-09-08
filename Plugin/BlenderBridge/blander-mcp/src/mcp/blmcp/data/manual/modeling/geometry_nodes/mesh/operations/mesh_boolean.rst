.. index:: Geometry Nodes; Mesh Boolean
.. _bpy.types.GeometryNodeMeshBoolean:

*****************
Mesh Boolean Node
*****************

.. figure:: /images/node-types_GeometryNodeMeshBoolean.webp
   :align: right
   :alt: Mesh Boolean node.

The *Mesh Boolean Node* allows you to cut, subtract, and join the geometry of two inputs.
This node offers the same operations as the :doc:`Boolean modifier </modeling/modifiers/generate/booleans>`.


Inputs
======

Mesh 1/2
   Standard geometry input.

Self Intersection :guilabel:`Exact Solver`
   Correctly calculates cases when one or both operands have self-intersections.
   This involves more calculations making the node slower.

Hole Tolerant :guilabel:`Exact Solver`
   Optimizes the Boolean output for :term:`Non-manifold` geometry
   at the cost of increased computational time.
   Because of the performance impact, this option should only be enabled
   when the solver demonstrates errors with non-manifold geometry.


Properties
==========

Operation
   :Intersect:
      Produce a new geometry containing only the volume inside of both geometry 1 and geometry 2.
   :Union:
      The two input meshes are joined, then any interior elements are removed.
   :Difference:
      Geometry 2 is subtracted from geometry 1 (everything outside of geometry 2 is kept).

Solver
   Algorithm used to calculate the Boolean intersections.

   :Float:
      Uses a mathematically simple solver which offers the good performance;
      however, this solver lacks support for overlapping geometry.
   :Exact:
      Uses a mathematically complex solver which offers the best results
      when there are coplanar faces or other overlapping geometry;
      however, this solver is much slower.
   :Manifold:
      Uses a solver that is usually fastest but only works on :term:`Manifold` meshes,
      (plus the special case of Difference with a plane).


Output
======

Mesh
   Standard geometry output.

Intersecting Edges :guilabel:`Exact Solver`
   A boolean attribute field with a selection of the edges that were created where the two inputs
   meet.
