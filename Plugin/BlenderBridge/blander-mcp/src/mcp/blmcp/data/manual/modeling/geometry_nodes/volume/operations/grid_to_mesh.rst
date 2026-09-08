.. index:: Geometry Nodes; Grid to Mesh
.. _bpy.types.GeometryNodeGridToMesh:

*****************
Grid to Mesh Node
*****************

.. figure:: /images/node-types_GeometryNodeGridToMesh.webp
   :align: right
   :alt: Grid to Mesh node.

The *Grid to Mesh* node converts a voxel grid into a polygonal mesh by
extracting an isosurface at a specified threshold value.
This process is similar to the *Marching Cubes* algorithm used in many
volumetric modeling systems.

The resulting mesh represents the boundary where the grid's values cross the
given threshold—typically the surface of a signed distance field (SDF) or density grid.
This makes it possible to convert procedural volumetric data into geometry for
rendering, simulation, or further modeling operations.


Inputs
======

Grid
   The input voxel grid to convert into a mesh.
   The grid must store float values such as those from a signed distance or density field.

Threshold
   The value that defines the surface of the generated mesh.
   Voxels with values larger than this threshold are considered *inside* the
   mesh, while smaller values are considered *outside*.
   For SDF grids, a threshold of ``0.0`` typically corresponds to the surface.

Adaptivity
   Controls the simplification of the generated mesh based on curvature.
   Higher values reduce polygon count by merging nearly flat areas, while
   smaller values preserve more detail.
   A value of ``0.0`` disables adaptivity and produces a uniform mesh density.


Outputs
=======

Mesh
   The resulting mesh extracted from the grid's isosurface.
   The mesh follows the region where the grid's scalar values equal the
   specified *Threshold*, and can be used for further geometry processing or rendering.
