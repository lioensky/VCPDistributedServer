.. index:: Geometry Nodes; Edge Paths to Selection
.. _bpy.types.GeometryNodeEdgePathsToSelection:

****************************
Edge Paths to Selection Node
****************************

.. figure:: /images/node-types_GeometryNodeEdgePathsToSelection.webp
   :align: right
   :alt: Edge Paths to Selection Node.

The *Edge Paths to Selection* node follows paths across mesh edges and outputs a selection
of every visited edge.

.. seealso::

   This node is meant to use the output of the :doc:`/modeling/geometry_nodes/mesh/read/shortest_edge_paths`.
   It can be combined with the :doc:`/modeling/geometry_nodes/geometry/operations/separate_geometry` to remove
   any unused edges.


Inputs
======

Start Vertices
   A selection of the vertices to start at when traveling along the next vertex indices.

Next Vertex Index
   Describes the path to follow at every vertex.


Outputs
=======

Selection
   A boolean field indicating all edges visited when traversing the mesh.
