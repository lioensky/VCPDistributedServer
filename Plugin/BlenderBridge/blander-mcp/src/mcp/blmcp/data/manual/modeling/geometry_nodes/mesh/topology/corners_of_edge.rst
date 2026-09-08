.. index:: Geometry Nodes; Corners of Edge
.. _bpy.types.GeometryNodeCornersOfEdge:

********************
Corners of Edge Node
********************

.. figure:: /images/node-types_GeometryNodeCornersOfEdge.webp
   :align: right
   :alt: Corners of Edge node.

Selects a neighboring face corner of an edge and outputs its index.

This node is a bit special because it operates in two different domains.
First, it evaluates a *Weight* for each corner in the geometry.
Then, for each item in the context domain, it will:

- Pick an edge from the geometry based on the *Edge Index*.
- Find *some* (not all) face corners connected to this edge -- see below.
- Sort these corners by their associated weight.
- Pick a corner from the above sorted list based on the *Sort Index*,
  where 0 means the corner with the lowest weight,
  1 means the corner with the second-lowest weight and so on.
- Output the geometry-wide index of this corner.

.. warning::

   As illustrated below, the node only looks at one corner per connected face.
   Even though the edge has four neighboring corners, *Corner Index* can only return the
   indexes of two of them, and *Total* will similarly return 2.

   You can use the :doc:`/modeling/geometry_nodes/mesh/topology/offset_corner_in_face`
   to retrieve the indexes of the other corners.

.. figure:: /images/modeling_geometry-nodes_corners-of-edge_explanation.png
   :align: center
   :width: 400px

   A graphic for which corners are returned for a given edge

- Red: selected edge.
- Blue: the corners whose index can be retrieved using this node.
- Purple: the corners that can be retrieved by offsetting the blue corner indices using
  the :doc:`/modeling/geometry_nodes/mesh/topology/offset_corner_in_face`.

Inputs
======

Edge Index
   The index of the edge for which to find connected corners.

   .. note::

      If this input is not connected, it uses the
      :doc:`index </modeling/geometry_nodes/geometry/read/input_index>`
      of the context item, which means it's important that the node is evaluated
      in the Edge domain.

Weights
   The weights of the corners in the geometry. Unlike the other inputs which follow
   the context domain, this one is always evaluated in the Face Corner domain.

   The corners are sorted by their associated weight in ascending order.
   Corners with the same weight are sorted by their index.

Sort Index
   The 0-based index of the corner to select from the edge's sorted corners.
   If this value is outside the range of valid indices, it wraps around.


Outputs
=======

Corner Index
   The geometry-wide index of the selected corner. You can pass this to the
   :doc:`/modeling/geometry_nodes/utilities/field/evaluate_at_index` or the
   :doc:`/modeling/geometry_nodes/geometry/sample/sample_index` (with the domain set to Face Corner)
   to retrieve details about the corner.

   If the edge has no connected corners, *Corner Index* will be zero.

Total
   The number of faces (not face corners!) connected to the edge.

.. seealso::

   The page for the :doc:`/modeling/geometry_nodes/mesh/topology/edges_of_vertex` has an example
   of how to work with the different domains.
