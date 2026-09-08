.. index:: Geometry Nodes; Separate Spherical
.. --- copy below this line ---

***********************
Separate Spherical Node
***********************

.. figure:: /images/node-types_GeometryNodeSeparateSpherical.webp
   :align: right
   :alt: Separate Spherical node.

The *Separate Spherical* node converts a vector from Cartesian coordinates (X, Y, Z)
into spherical coordinates (R, Φ, Θ) and outputs each component separately.
It is the inverse of the :doc:`Combine Spherical </modeling/geometry_nodes/utilities/vector/combine_spherical>` node.

Spherical coordinates describe a position in 3D space using radius, azimuth (horizontal angle),
and polar (vertical) angle. This representation is useful for procedural effects involving
rotational symmetry, spherical gradients, or direction-based transformations.


Inputs
======

Vector
   The input Cartesian vector to be converted into spherical coordinates.


Outputs
=======

R
   The radial distance from the origin.

Phi
   The azimuthal angle (horizontal rotation) around the Z axis, measured in radians.

Theta
   The polar angle (vertical inclination) from the Z axis, measured in radians.
