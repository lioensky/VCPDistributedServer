.. index:: Geometry Nodes; Cube Grid Topology
.. _bpy.types.GeometryNodeCubeGridTopology:

***********************
Cube Grid Topology Node
***********************

.. figure:: /images/node-types_GeometryNodeCubeGridTopology.webp
   :align: right
   :alt: The Cube Grid Topology node.

The *Cube Grid Topology* node generates a boolean grid topology
with the specified bounds and resolution.
This topology defines the voxel layout and active region and can be used with nodes such as
:doc:`/modeling/geometry_nodes/volume/operations/field_to_grid` to construct volume grids.

The output topology contains active voxels within a regular, axis-aligned cube region.


Inputs
======

Bounds Min
   The minimum world-space boundary of the grid.
   Defines the lower corner of the cube.

Bounds Max
   The maximum world-space boundary of the grid.
   Defines the upper corner of the cube.

Resolution X / Y / Z
   Number of voxels along the X, Y, and Z axes.
   Higher values increase detail and memory usage.


Min
---

X, Y, Z
   Minimum coordinate in grid index space.
   This defines the starting voxel index for each axis.


Outputs
=======

Topology
   A boolean grid defining the grid topology and active region.
   Active voxels correspond to the cube defined by the bounds
   and resolution inputs.
