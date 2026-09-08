.. index:: Geometry Nodes; Grid Dilate & Erode
.. _bpy.types.GeometryNodeGridDilateAndErode:

************************
Grid Dilate & Erode Node
************************

.. figure:: /images/node-types_GeometryNodeGridDilateAndErode.webp
   :align: right
   :alt: Grid Dilate & Erode node.

The *Grid Dilate & Erode* node expands or contracts the active regions of a volume grid.
It modifies which voxels are considered active, without changing the stored voxel values.

This operation is commonly used to grow or shrink volume regions, fill small gaps,
remove noise, or adjust boundaries in volumetric data.


Properties
==========

Data Type
   The type of data stored in the grid (e.g. *Float*, *Integer*, *Boolean*,
   *Vector*).
   Must match the type of the input grid.


Inputs
======

Grid
   The input volume grid whose active voxels are modified.

Connectivity
   Defines which neighboring voxels are considered connected during the operation.

   :Face:
      Use 6-connectivity, affecting only voxels connected by faces.
   :Edge:
      Use 18-connectivity, affecting voxels connected by faces or edges.
   :Vertex:
      Use 26-connectivity, affecting voxels connected by faces, edges, or vertices.

Tiles
   Controls how active tiles are handled during dilation or erosion.

   :Ignore:
      Ignore active tiles entirely.
      Tiles are neither modified nor contribute to the operation.
   :Expand:
      Convert active tiles to individual voxels, apply the operation,
      and leave the result fully voxelized.
   :Preserve:
      Keep tiles unchanged when possible, only voxelizing when necessary.
      This option is more memory efficient.

Steps
   Number of times to apply the dilation or erosion operation.
   Higher values increase the distance the active region is expanded or contracted.


Outputs
=======

Grid
   The resulting grid with updated active voxel regions.
