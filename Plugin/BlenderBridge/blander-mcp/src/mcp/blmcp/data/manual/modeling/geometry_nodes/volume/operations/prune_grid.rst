.. index:: Geometry Nodes; Prune Grid
.. _bpy.types.GeometryNodeGridPrune:

***************
Prune Grid Node
***************

.. figure:: /images/node-types_GeometryNodeGridPrune.webp
   :align: right
   :alt: Prune Grid node.

The *Prune Grid* node optimizes the storage of a voxel grid by collapsing
uniform regions into coarser tiles or inner nodes, reducing memory usage and
improving performance.

This node performs the inverse operation of the
:doc:`Voxelize Grid </modeling/geometry_nodes/volume/operations/voxelize_grid>` node.
While voxelization expands sparse tiles into dense voxels, pruning
detects large uniform areas and replaces them with more compact representations.
This is especially useful after operations that create large
regions of constant values, such as filling, clipping, or thresholding.


Inputs
======

Grid
   The input grid to optimize.

Mode
   The pruning method used to simplify the grid structure:

   :Inactive:
      Turns inactive voxels and tiles into inactive background tiles.
      This is the simplest mode and provides basic cleanup for grids with
      empty or unused regions.

   :Threshold:
      Collapses regions where all voxels have approximately the same value and
      active state (within a given tolerance threshold) into background tiles.
      This is useful for fog or scalar grids where smooth variations may leave
      near-uniform areas that can be simplified.

   :SDF:
      Specialized mode for signed distance field (SDF) grids.
      Replaces inactive tiles with inactive nodes, providing faster and more
      targeted pruning without the need for threshold comparison.
      This mode is efficient for narrow-band SDFs that contain large interior
      or exterior regions of constant sign.

Threshold :guilabel:`Threshold`
   Voxels within a region are considered uniform if the difference between
   their values is less than this amount. Higher thresholds allow more
   aggressive simplification, while smaller values preserve finer details.


Properties
==========

Data Type
   The type of data stored in the grid (e.g. *Float*, *Integer*, *Boolean*,
   *Vector*).
   Must match the type of the input grid.


Outputs
=======

Grid
   The resulting grid with optimized storage. Uniform regions are collapsed
   into larger tiles or nodes, resulting in a more compact and efficient
   representation.
