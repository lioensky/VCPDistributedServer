.. index:: Geometry Nodes; Points to Vertices
.. _bpy.types.GeometryNodePointsToVertices:

***********************
Points to Vertices Node
***********************

.. figure:: /images/node-types_GeometryNodePointsToVertices.webp
   :align: center
   :alt: Points to Vertices node.

The *Points to Vertices* node generate a mesh vertex in the output geometry for
each point cloud point in the input geometry.


Inputs
======

Geometry
   Standard geometry input.

Selection
   Boolean field used to determine if each point will be converted to a vertex.


Outputs
=======

Geometry
   Standard geometry output.
