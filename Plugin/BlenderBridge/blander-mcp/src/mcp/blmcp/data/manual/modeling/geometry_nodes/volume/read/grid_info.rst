.. index:: Geometry Nodes; Grid Info
.. _bpy.types.GeometryNodeGridInfo:

**************
Grid Info Node
**************

.. figure:: /images/node-types_GeometryNodeGridInfo.webp
   :align: right
   :alt: Grid Info node.

The *Grid Info* node retrieves structural and metadata information about a voxel grid.
It provides details such as the grid's spatial transform and background value,
which describe how the grid is positioned in space and what value is stored in
inactive (empty) voxels.

This node is useful for inspecting or reusing grid parameters in other grid
operations, such as aligning transforms, matching resolutions, or reconstructing
fields with consistent background values.


Inputs
======

Grid
   The input voxel grid to query information from.


Properties
==========

Data Type
   The type of data stored in the grid (e.g. *Float*, *Integer*, *Boolean*, or *Vector*).
   Determines both the expected data type of the *Grid* input and the type of
   the *Background Value* output.


Outputs
=======

Transform
   The transform matrix that converts from grid index space to object space.
   Defines how the grid's voxels are positioned, scaled, and oriented in 3D space.
   This can be passed to nodes such as
   :doc:`Set Grid Transform </modeling/geometry_nodes/volume/write/set_grid_transform>`
   or used to align other grids or geometry.

Background Value
   The value assigned to inactive voxels in the grid.
   This represents the default or “empty” value used when sampling outside of active regions, as set by the
   :doc:`Set Grid Background </modeling/geometry_nodes/volume/write/set_grid_background>`
   node or similar operations.
