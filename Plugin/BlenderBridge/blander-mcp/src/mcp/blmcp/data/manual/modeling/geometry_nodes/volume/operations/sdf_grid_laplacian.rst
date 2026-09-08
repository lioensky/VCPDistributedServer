.. index:: Geometry Nodes; SDF Grid Laplacian
.. _bpy.types.GeometryNodeSDFGridLaplacian:

***********************
SDF Grid Laplacian Node
***********************

.. figure:: /images/node-types_GeometryNodeSDFGridLaplacian.webp
   :align: right
   :alt: SDF Grid Laplacian node.

The *SDF Grid Laplacian* node applies Laplacian flow smoothing to a Signed Distance Field (SDF) grid.
This process gradually smooths the surface of the SDF by diffusing fine
details and noise across neighboring voxels, resulting in a cleaner, more uniform field.

Laplacian flow is a computationally efficient alternative to
:doc:`mean curvature flow </modeling/geometry_nodes/volume/operations/sdf_grid_mean_curvature>`
smoothing. It is particularly useful for refining SDFs generated from
meshes or boolean operations, where sharp transitions or voxel artifacts may occur.
The operation helps improve the quality of surfaces before converting the SDF back into a mesh.


Inputs
======

Grid
   The input signed distance field to be smoothed.

Iterations
   The number of Laplacian smoothing iterations to apply.
   Each iteration progressively diffuses high-frequency surface variations,
   reducing surface noise.
   Higher values increase smoothness but may cause slight surface shrinkage.


Outputs
=======

Grid
   The resulting SDF grid after Laplacian flow smoothing.
   The output surface is smoother and more continuous, while preserving
   the main shape features of the original field.
