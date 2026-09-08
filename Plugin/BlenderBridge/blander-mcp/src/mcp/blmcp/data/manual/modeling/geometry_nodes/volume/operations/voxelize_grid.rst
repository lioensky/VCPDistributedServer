.. index:: Geometry Nodes; Voxelize Grid
.. _bpy.types.GeometryNodeGridVoxelize:

******************
Voxelize Grid Node
******************

.. figure:: /images/node-types_GeometryNodeGridVoxelize.webp
   :align: right
   :alt: SDF Grid Voxelize node.

The *Voxelize Grid* node converts all active tiles in a sparse voxel grid
into fully populated voxel regions, removing sparseness.

In voxel-based grids such as signed distance fields (SDF) or fog volumes,
inactive areas are often stored as *tiles*—compact representations that save
memory by not allocating individual voxel values. This node expands those tiles
into explicit voxels, making every voxel within an active tile directly
accessible and editable.

This can be useful before performing operations that require dense voxel data,
such as sampling, filtering, or arithmetic operations that depend on
neighboring voxel values.


Inputs
======

Grid
   The input grid to voxelize.
   Typically a sparse SDF or fog volume grid whose active tiles should be
   expanded into dense voxels.


Properties
==========

Data Type
   The type of data stored in the grid (e.g. *Float*, *Integer*, *Boolean*, *Vector*).


Outputs
=======

Grid
   The resulting grid with all active tiles converted into individual voxels.

   For fog volumes, this means that interior sparse tiles are expanded into
   voxels with individually adjustable values. For SDF grids, this produces a
   fully dense voxel representation suitable for precise sampling and editing.
