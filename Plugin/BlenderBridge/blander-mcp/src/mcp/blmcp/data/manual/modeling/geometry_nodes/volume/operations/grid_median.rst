.. index:: Geometry Nodes; Grid Median
.. _bpy.types.GeometryNodeGridMedian:

****************
Grid Median Node
****************

.. figure:: /images/node-types_GeometryNodeGridMedian.webp
   :align: right
   :alt: Grid Median node.

The *Grid Median* node applies a median (box) filter to a volume grid.
For each active voxel, the value is replaced with the median value of
neighboring voxels within a box-shaped region defined by the filter width.

Unlike the :doc:`mean filter </modeling/geometry_nodes/volume/operations/grid_meant>`,
the median filter is more effective at preserving
sharp features and removing isolated noise or outliers.
It is commonly used to clean up sparse artifacts while maintaining edges
in density or level set volumes.


Properties
==========

Data Type
   The type of data stored in the grid (for example *Float*, *Integer*,
   or *Vector*). Must match the data type of the input grid.


Inputs
======

Grid
   The input volume grid to smooth.

Width
   The filter kernel radius in voxels.
   Larger values increase the size of the neighborhood considered,
   resulting in stronger smoothing.

Iterations
   Number of times the median filter is applied.
   Repeated iterations progressively increase the smoothing effect.


Outputs
=======

Grid
   The filtered grid with updated voxel values.
