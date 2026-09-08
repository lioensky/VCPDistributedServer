.. index:: Geometry Nodes; Is Edge Boundary

*********************
Is Edge Boundary Node
*********************

.. figure:: /images/node-types_GeometryNodeIsEdgeBoundary.webp
   :align: right
   :alt: Is Edge Boundary Node.

The *Is Edge Boundary* node outputs a boolean value indicating
whether each edge lies on the boundary of a mesh.
Boundary edges are edges connected to only one face,
typically located at the open borders of a mesh.

This node is useful for identifying open edges, detecting holes,
or creating effects that depend on mesh boundaries.


Inputs
======

This node has no inputs.


Outputs
=======

Is Edge Boundary
   Boolean value that indicates whether each edge is on the mesh boundary.
   True if the edge belongs to only one face; false otherwise.
