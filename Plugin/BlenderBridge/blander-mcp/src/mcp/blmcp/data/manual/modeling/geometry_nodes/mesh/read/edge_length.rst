.. index:: Geometry Nodes; Edge Length

****************
Edge Length Node
****************

.. figure:: /images/node-types_GeometryNodeEdgeLength.webp
   :align: right
   :alt: Edge Length Node.

The *Edge Length* node outputs the length of each edge in a mesh.
It calculates the distance between the two vertices that define each edge.

This node can be used for geometric analysis, mesh-based effects, or procedural operations
that depend on edge length (such as adaptive subdivision, weight mapping, or trimming).


Inputs
======

This node has no inputs.


Outputs
=======

Length
   The length of each edge as a floating-point value, measured in the same units as the scene scale.
