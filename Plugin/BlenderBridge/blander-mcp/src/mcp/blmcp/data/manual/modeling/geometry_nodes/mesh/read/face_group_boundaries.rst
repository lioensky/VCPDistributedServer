.. index:: Geometry Nodes; Face Group Boundaries
.. _bpy.types.GeometryNodeMeshFaceSetBoundaries:

**************************
Face Group Boundaries Node
**************************

.. figure:: /images/node-types_GeometryNodeMeshFaceSetBoundaries.webp
   :align: right
   :alt: Face Group Boundaries node.

The *Face Group Boundaries Node* finds the edges which lie on the boundaries of
specified regions. These edges could be used to mark seams for UV unwrapping,
for example.


Inputs
======

Face Group ID
   Identifier for which group of faces this face belongs to. All contiguous faces
   with the same value are in the same region.


Output
======

Boundary Edges
   Selection of the boundary edges of the different face sets. An edge is
   considered to be at the boundary if it lies on at least two faces with
   different identifiers.


Examples
========

.. figure:: /images/modeling_geometry-nodes_face-set-boundaries_voronoi-seams.png

Combined with the :doc:`UV Unwrap Node </modeling/geometry_nodes/mesh/uv/uv_unwrap>`,
this node is used to turn the face sets (right cube) into a UV map for a texture (left cube).
