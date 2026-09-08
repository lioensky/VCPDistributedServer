.. index:: Geometry Nodes; Face Neighbors
.. _bpy.types.GeometryNodeInputMeshFaceNeighbors:

*******************
Face Neighbors Node
*******************

.. figure:: /images/node-types_GeometryNodeInputMeshFaceNeighbors.webp
   :align: right
   :alt: Face Neighbors Node.

The *Face Neighbors* node outputs topology information relating to each face of a mesh.


Inputs
======

This node has no inputs.


Outputs
=======

Vertex Count
   This output is simply the number of sides of each face, or how many corners each face has.

Neighboring Face Count
   The number of faces that connect to this face with at least one edge. On a regular manifold
   mesh with only quads and triangles, this will be the same as the vertex count, otherwise it might
   be completely different.
