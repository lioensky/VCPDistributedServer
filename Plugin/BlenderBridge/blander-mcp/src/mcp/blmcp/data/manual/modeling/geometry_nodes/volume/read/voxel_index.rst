.. index:: Geometry Nodes; Voxel Index
.. _bpy.types.GeometryNodeInputVoxelIndex:

****************
Voxel Index Node
****************

.. figure:: /images/node-types_GeometryNodeInputVoxelIndex.webp
   :align: right
   :alt: Voxel Index node.

The *Voxel Index* node outputs the integer index of the voxel that the field
is currently being evaluated on.

Unlike a position in object space, the voxel index refers to the discrete
cell coordinates inside a voxel grid. This makes it possible to reason
about neighboring voxels directly in index space, without converting
through world or object space.

This node can be combined with nodes such as
:doc:`Integer Math </modeling/geometry_nodes/utilities/math/integer_math>`
and :doc:`Sample Grid Index </modeling/geometry_nodes/volume/sample/sample_grid_index>`
to sample values from nearby voxels by offsetting the indices.


Inputs
======

This node has no inputs.


Outputs
=======

X, Y, Z
   The integer indices of the current voxel in the grid along each axis.

   These values identify which voxel is being sampled by the field at this
   evaluation point. They can be offset (for example, add or subtract 1 on X)
   and then passed to :doc:`Sample Grid Index </modeling/geometry_nodes/volume/sample/sample_grid_index>`
   to read values from neighboring voxels.


Tile
----

Is Tile
   Whether the current evaluation is happening on a *tile* rather than on a
   single voxel.

   Some operations evaluate fields on tiles that cover multiple voxels at
   once for performance reasons. In those cases the coordinates given by
   *X*, *Y*, and *Z* alone are not enough to describe the full covered region.

   If this is false, the extent is always 1.

Extent X, Extent Y, Extent Z
   The number of voxels along each axis of the tile.

   For a normal voxel, the extent on each axis is ``1``.
   For a tile that covers multiple voxels, the extents describe how many
   voxels are grouped together in X, Y, and Z.

   These outputs can be used to detect and handle cases where an evaluation
   represents an aggregated region (a tile) instead of an individual voxel,
   so that the result is not misinterpreted as referring to just one voxel.
