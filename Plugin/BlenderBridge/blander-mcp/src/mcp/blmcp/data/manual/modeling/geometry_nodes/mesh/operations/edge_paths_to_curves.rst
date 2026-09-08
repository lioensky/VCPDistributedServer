.. index:: Geometry Nodes; Edge Paths to Curves
.. _bpy.types.GeometryNodeEdgePathsToCurves:

*************************
Edge Paths to Curves Node
*************************

.. figure:: /images/node-types_GeometryNodeEdgePathsToCurves.webp
   :align: right
   :alt: Edge Paths to Curves Node.

The *Edge Paths to Curves* node output curves that follow paths across mesh edges.

.. seealso::

   This node is meant to use the output of the :doc:`/modeling/geometry_nodes/mesh/read/shortest_edge_paths`.
   It is similar to the :doc:`/modeling/geometry_nodes/mesh/operations/edge_paths_to_selection`, but it creates
   a curve that follow each path, rather than a selection of every visited edge.


Inputs
======

Mesh
   Standard mesh input.

Start Vertices
   A selection of the vertices to start at when traveling along the next vertex indices.

Next Vertex Index
   Describes the path to follow at every vertex.


Outputs
=======

Mesh
   Standard curves output.
