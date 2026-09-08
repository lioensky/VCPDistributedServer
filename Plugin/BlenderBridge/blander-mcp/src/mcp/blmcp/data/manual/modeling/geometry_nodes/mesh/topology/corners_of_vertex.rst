.. index:: Geometry Nodes; Corners of Vertex
.. _bpy.types.GeometryNodeCornersOfVertex:

**********************
Corners of Vertex Node
**********************

.. figure:: /images/node-types_GeometryNodeCornersOfVertex.webp
   :align: right
   :alt: Corners of Vertex node.

Selects a neighboring face corner of a vertex and outputs its index.

This node is a bit special because it operates in two different domains.
First, it evaluates a *Weight* for each corner in the geometry.
Then, for each item in the context domain, it will:

- Pick a vertex from the geometry based on the *Vertex Index*.
- Find the face corners adjacent to this vertex.
- Sort these corners by their associated weight.
- Pick a corner from the above sorted list based on the *Sort Index*,
  where 0 means the corner with the lowest weight,
  1 means the corner with the second-lowest weight and so on.
- Output the geometry-wide index of this corner.


Inputs
======

Vertex Index
   The index of the vertex for which to find the corners.

   .. note::

      If this input is not connected, it uses the
      :doc:`index </modeling/geometry_nodes/geometry/read/input_index>`
      of the context item, which means it's important that the node is evaluated
      in the Point domain.

Weights
   The weights of the corners in the geometry. Unlike the other inputs which follow
   the context domain, this one is always evaluated in the Face Corner domain.

   The corners are sorted by their associated weight in ascending order.
   Corners with the same weight are sorted by their index.

Sort Index
   The 0-based index of the corner to select from the vertex's sorted corners.
   If this value is outside the range of valid indices, it wraps around.

Outputs
=======

Corner Index
   The geometry-wide index of the selected corner. You can pass this to the
   :doc:`/modeling/geometry_nodes/utilities/field/evaluate_at_index` or the
   :doc:`/modeling/geometry_nodes/geometry/sample/sample_index` (with the domain set to Face Corner)
   to retrieve details about the corner.

Total
   The number of adjacent corners, which is also the number of faces.

.. seealso::

   The page for the :doc:`/modeling/geometry_nodes/mesh/topology/edges_of_vertex` has an example
   of how to work with the different domains.
