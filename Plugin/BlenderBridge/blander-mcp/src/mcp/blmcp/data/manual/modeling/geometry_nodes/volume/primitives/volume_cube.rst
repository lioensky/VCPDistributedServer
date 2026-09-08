.. index:: Geometry Nodes; Volume Cube
.. _bpy.types.GeometryNodeVolumeCube:

****************
Volume Cube Node
****************

.. figure:: /images/node-types_GeometryNodeVolumeCube.webp
   :align: right
   :alt: The Volume Cube node.

The *Volume Cube* generates a volume by evaluating a density field on a 3D grid.
The *Density* field can only depend on the :doc:`/modeling/geometry_nodes/geometry/read/position`.
The grid points are equally spaced between the *Min* and *Max* bounds of the grid.

Inputs
======

Density
   The value for the new grid at each voxel.

Background
   The value of the grid outside the *Min*..*Max* grid bounds.
   Voxels with a density equal to the background are pruned, which can lead to more memory-efficient volumes.

Min
   Location of the left-most grid point and lower bound of the voxel volume.

Max
   Location of the right-most grid point and upper bound of the voxel volume.

Resolution X,Y,Z
   The number of grid points on each axis.
   The grid contains one less full voxel on each axis than there are grid points.
   For example a *Volume Cube* with resolution 10 has 9 voxels between the left and right grid points.

   .. note::

      Changing these values can have a significant impact on performance. For example, the default values
      of 32 mean the input field will be evaluated about 33 thousand times. Increasing the values to 100
      will give 1 million evaluations, and 1000 would give 1 billion.


Outputs
=======

Volume
   Geometry containing the generated volume.
