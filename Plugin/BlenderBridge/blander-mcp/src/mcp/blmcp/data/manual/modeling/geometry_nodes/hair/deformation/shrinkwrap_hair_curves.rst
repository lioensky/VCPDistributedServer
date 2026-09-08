.. index:: Geometry Nodes; Shrinkwrap Hair Curves

**********************
Shrinkwrap Hair Curves
**********************

The *Shrinkwrap Hair Curves* node projects hair curves onto a target surface,
adjusting their positions so they follow the shape of a mesh.
It can be used to conform hair to a scalp or other underlying geometry,
ensuring curves remain properly positioned relative to a surface.

.. peertube:: rA2Ytunkm2SorWhXeVQTWq


Inputs
======

Geometry
   The input geometry containing the hair curves to be shrinkwrapped.

Surface Input Type
   Determines how the surface data is provided for shrinkwrapping.
   The geometry input takes priority over the object input.

   :Object:
      Use an object reference to sample the target surface.
   :Geometry:
      Use a geometry input to sample the surface directly.

Surface
   The surface object or geometry used as the target for the shrinkwrap projection.

Factor
   Controls the overall influence of the shrinkwrap effect.
   A value of 0.0 leaves the hair unchanged, while 1.0 fully conforms the hair to the surface.

Offset Distance
   Defines a distance offset from the target surface.
   Positive values move curves away from the surface, while negative values move them inward.

Above Surface
   Blends the shrinkwrap effect for points that start above the surface,
   allowing smoother transitions when only some parts of the curve should adhere to the mesh.

Smoothing Steps
   The number of smoothing iterations applied to the curves after shrinkwrapping.
   Increasing this value helps to reduce artifacts and achieve smoother results.

Lock Roots
   When enabled, prevents the root points of each curve from moving during the shrinkwrap operation.
   This ensures hair roots remain fixed to their original positions (e.g., attached to a scalp).


Outputs
=======

Geometry
   The resulting geometry with curves conformed to the target surface.
