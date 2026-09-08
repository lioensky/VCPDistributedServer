.. index:: Geometry Nodes; Mesh to Density Grid
.. _bpy.types.GeometryNodeMeshToDensityGrid:

*************************
Mesh to Density Grid Node
*************************

.. figure:: /images/node-types_GeometryNodeMeshToDensityGrid.webp
   :align: right
   :alt: Mesh to Density Grid node.

The *Mesh to Density Grid* node converts a mesh into a **density grid**, where
each voxel stores a scalar value representing how far it lies inside or near
the surface of the mesh. This can be used to generate fog volumes, soft-body
representations, or as input to volumetric and field-based effects.

The resulting grid contains smooth gradients that transition from high values
inside the mesh to low values outside, allowing for continuous blending and
sampling operations.


Inputs
======

Mesh
   The input mesh to be converted into a density grid.
   The mesh defines the surface that will be voxelized.

Density
   The scalar value assigned to voxels inside the mesh.
   Typically a value of ``1.0`` for full density and ``0.0`` for empty space,
   though any scalar range can be used to represent material thickness or opacity.

Voxel Size
   The size of each voxel in object space units.
   Smaller values produce higher-resolution grids with more detail, while
   larger values reduce detail but improve performance and memory efficiency.

Gradient Width
   The width of the gradient region inside the mesh.
   Controls how smoothly the density falls off from the interior toward the
   exterior. Larger values create a broader transition, while smaller values
   produce a sharper surface boundary.


Outputs
=======

Density Grid
   The resulting float grid representing the density of the mesh.
   Voxels inside the mesh will have higher density values, while voxels
   outside the mesh will approach zero. The smooth transition is defined by
   the *Gradient Width* parameter.
