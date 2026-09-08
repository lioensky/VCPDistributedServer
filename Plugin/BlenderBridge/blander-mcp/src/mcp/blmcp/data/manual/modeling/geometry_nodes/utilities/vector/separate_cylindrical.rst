.. index:: Geometry Nodes; Separate Cylindrical
.. --- copy below this line ---

*************************
Separate Cylindrical Node
*************************

.. figure:: /images/node-types_GeometryNodeSeparateCylindrical.webp
   :align: right
   :alt: Separate Cylindrical node.

The *Separate Cylindrical* node converts a vector from Cartesian coordinates (X, Y, Z)
into cylindrical coordinates (R, Φ, Z) and outputs each component separately. It is the inverse of the
:doc:`Combine Cylindrical </modeling/geometry_nodes/utilities/vector/combine_cylindrical>` node.

This node is useful for analyzing geometry or generating procedural effects that depend on
radial distance, angular position, or height -- for example, creating spiral deformations,
cylindrical gradients, or radial masks.


Inputs
======

Vector
   The input vector to be converted from Cartesian to cylindrical coordinates.


Outputs
=======

R
   The radial distance from the origin in the X-Y plane.

Phi
   The angular position around the Z axis.

Z
   The vertical component of the input vector, corresponding directly to its Z coordinate.
