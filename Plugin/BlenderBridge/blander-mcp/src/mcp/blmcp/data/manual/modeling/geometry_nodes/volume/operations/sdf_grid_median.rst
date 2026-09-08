.. index:: Geometry Nodes; SDF Grid Median
.. _bpy.types.GeometryNodeSDFGridMedian:

********************
SDF Grid Median Node
********************

.. figure:: /images/node-types_GeometryNodeSDFGridMedian.webp
   :align: right
   :alt: SDF Grid Median node.

The *SDF Grid Median* node applies a median filter to a Signed Distance Field (SDF) grid.
This operation smooths the field by replacing each voxel value with the
median of its neighboring values, effectively removing noise and small
artifacts while preserving sharp features and edges.

Unlike :doc:`mean </modeling/geometry_nodes/volume/operations/sdf_grid_mean>`
or :doc:`Laplacian </modeling/geometry_nodes/volume/operations/sdf_grid_laplacian>`
smoothing, the median filter is non-linear and
better suited for cleaning up impulsive noise (isolated spikes or dips) in
the grid. It maintains the overall structure and boundaries of the surface,
making it useful for refining SDFs generated from noisy or voxelized meshes.


Inputs
======

Grid
   The input signed distance field to be filtered.

Width
   The radius of the median filter kernel, measured in voxels.
   Larger widths produce stronger smoothing by considering a wider
   neighborhood around each voxel.

Iterations
   The number of times the median filter is applied.
   Multiple iterations increase smoothing and noise reduction while
   maintaining edge sharpness.


Outputs
=======

Grid
   The resulting SDF grid after median filtering.
   The output has reduced high-frequency noise and artifacts while
   retaining sharp edges and important structural details of the surface.
