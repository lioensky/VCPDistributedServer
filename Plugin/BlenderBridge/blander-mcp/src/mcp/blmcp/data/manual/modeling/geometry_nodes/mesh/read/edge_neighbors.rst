.. index:: Geometry Nodes; Edge Neighbors
.. _bpy.types.GeometryNodeInputMeshEdgeNeighbors:

*******************
Edge Neighbors Node
*******************

.. figure:: /images/node-types_GeometryNodeInputMeshEdgeNeighbors.webp
   :align: right
   :alt: Edge Neighbors Node.

The *Edge Neighbors* node outputs topology information relating to each edge of a mesh.


Inputs
======

This node has no inputs.


Outputs
=======

Face Count
    The number of faces that use the edge as one of their sides.
    When the value is one, the edge is a :term:`non-manifold <Non-manifold>` boundary edge.
    Alternatively, when the value is zero, the edge is a loose edge, not used by any faces.


Examples
========

.. figure:: /images/modeling_geometry-nodes_input_edge-vertices_boundary.png
   :align: center

   Using the *Face Count* output to create a curve on a mesh's boundary edges.
