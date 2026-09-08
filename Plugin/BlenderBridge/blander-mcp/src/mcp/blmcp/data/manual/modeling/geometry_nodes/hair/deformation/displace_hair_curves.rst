.. index:: Geometry Nodes; Displace Hair Curves

********************
Displace Hair Curves
********************

The *Displace Hair Curves* node offsets the shape or position of hair curves using a displacement vector.
This allows for procedural control over hair movement, direction, or surface alignment.
The displacement can be applied in object, world, or surface normal space, depending on the configuration.

.. peertube:: 8DP1hsJucDanf2s54P1qe3


Inputs
======

Geometry
   The input geometry containing the hair curves to displace.

Factor
   Scales the overall displacement strength.
   A value of 0.0 applies no displacement, while 1.0 applies the full displacement vector.

Shape
   Defines how the displacement factor changes along the length of each curve.
   A value of 0.0 applies a constant displacement, while 0.5 results in a linear falloff from root to tip.

Object Space
   The object whose transform defines the coordinate space of the displacement.
   If unset, displacement is applied in the modifier's local space.

Displace Vector
   The vector used to determine the direction and magnitude of the displacement.
   This can be driven by fields or other procedural inputs.


Surface Normal
--------------

When enabled, displaces the curves along the normal of a surface, allowing for effects like
"pushing" or "lifting" hair away from a mesh.

Can be enabled from the header.

Surface Input Type
   Determines how the surface data is provided for sampling the normals.
   The geometry input takes priority over the object input.

   :Object:
      Use an object reference to sample surface normals.
   :Geometry:
      Use a geometry input to sample normals directly.

Surface
   The surface object used to sample the normals for displacement.

Surface UV Map
   The UV map used when sampling the surface normals for displacement.

Surface Normal Displacement
   Amount of displacement applied along the sampled surface normal.
   Can be positive or negative depending on the desired direction.


Outputs
=======

Geometry
   The resulting geometry with displaced hair curves.
