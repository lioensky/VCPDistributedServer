.. index:: Geometry Nodes; Is UV Split

****************
Is UV Split Node
****************

.. figure:: /images/node-types_GeometryNodeIsUVSplit.webp
   :align: right
   :alt: Is UV Split Node.

The *Is UV Split* node outputs a selection indicating which edges in a mesh are *UV splits*.
A UV split occurs when an edge connects two faces that use different UV coordinates along that edge,
causing a discontinuity in the UV map.

This node is useful for detecting UV seams, isolating edges used for UV islands, or
creating procedural operations that depend on UV boundaries.


Inputs
======

UV Map
   The UV map to evaluate for discontinuities.
   This input must be a vector attribute representing the mesh's UV coordinates.


Outputs
=======

Is UV Split
   A selection identifying edges where the UV coordinates differ between connected faces.
   True for UV seams or discontinuities; false otherwise.
