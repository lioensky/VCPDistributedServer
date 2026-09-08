.. index:: Geometry Nodes; Is Edge Manifold

*********************
Is Edge Manifold Node
*********************

.. figure:: /images/node-types_GeometryNodeIsEdgeManifold.webp
   :align: right
   :alt: Is Edge Manifold Node.

The *Is Edge Manifold* node outputs a boolean value indicating whether each edge in a mesh
is *manifold*. A manifold edge is shared by exactly two faces and has consistent face normals,
meaning it is part of a continuous surface without gaps or branching edges.

This node is useful for detecting mesh topology issues or isolating boundary or non-manifold edges.


Inputs
======

This node has no inputs.


Outputs
=======

Manifold
   Boolean value that indicates whether each edge is manifold.
   True if the edge is shared by exactly two faces; false otherwise
   (for example, if the edge belongs to one face, more than two faces, or no faces at all).
