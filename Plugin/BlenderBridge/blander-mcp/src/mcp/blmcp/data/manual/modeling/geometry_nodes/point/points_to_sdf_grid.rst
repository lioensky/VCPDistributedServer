.. index:: Geometry Nodes; Points to SDF Grid
.. _bpy.types.GeometryNodePointsToSDFGrid:

******************
Points to SDF Grid
******************

.. figure:: /images/node-types_GeometryNodePointsToSDFGrid.webp
   :align: center
   :alt: Points to SDF Grid node.

The *Points to SDF Grid* node generates a Signed Distance Field (SDF)*grid
from a set of input points. Each voxel in the resulting grid stores the
shortest signed distance to the nearest point, allowing points to be
represented as smooth, volumetric shapes.

Positive values represent distances outside the influence of the points,
negative values represent distances inside, and zero corresponds to the surface
of the generated implicit sphere around each point.

This node is useful for constructing volumetric fields or collision volumes
from particles, instances, or procedurally generated point clouds.


Inputs
======

Points
   The input points that define the centers of the generated SDF regions.

Radius
   The radius of influence for each point, defining how far the signed
   distance extends from the point center. Each point is treated as a sphere
   with this radius.

Voxel Size
   The size of each voxel in object space units.
   Smaller voxel sizes yield higher-resolution fields that better capture
   fine detail, at the cost of increased memory and processing time.


Outputs
=======

SDF Grid
   A scalar (float) grid representing the signed distance field of the input points.
   Each voxel stores the shortest signed distance to any point's surface,
   with negative values inside the combined spheres and positive values outside.
