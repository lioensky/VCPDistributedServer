.. index:: Geometry Nodes; Sample Grid
.. _bpy.types.GeometryNodeSampleGrid:

****************
Sample Grid Node
****************

.. figure:: /images/node-types_GeometryNodeSampleGrid.webp
   :align: right
   :alt: Sample Grid node.

The *Sample Grid* node retrieves values from a voxel grid at given positions in space.
It evaluates the grid's stored data (such as float, integer, boolean, or vector values)
and returns the interpolated result for each queried position.

This node is useful for reading data from grids created by other nodes
(e.g. *Mesh to SDF Grid*, *Field to Grid*, or *Points to SDF Grid*) and using
those values to drive procedural effects, geometry deformation, or shading.


Inputs
======

Grid
   The input grid to sample from. The grid can store scalar, vector, or
   color data depending on its data type.

Position
   The spatial positions (in object space) where the grid values are
   evaluated. Each position is interpolated based on nearby voxel values.

Interpolation
   The interpolation method used to compute the sampled value between
   neighboring voxels:

   :Nearest Neighbor:
      Returns the value from the closest voxel without interpolation.
      Fastest method but can appear blocky or discrete.
   :Trilinear:
      Performs linear interpolation across the eight nearest voxels.
      Produces smooth transitions between samples and is suitable for most general uses.
   :Triquadratic:
      Uses a higher-order (quadratic) interpolation for even smoother
      gradients and more continuous results, at the cost of additional computation.


Properties
==========

Data Type
   The type of data stored in the grid (e.g. *Float*, *Integer*, *Boolean*, or *Vector*).
   Determines the output socket type of the node.


Outputs
=======

Value
   The interpolated value sampled from the grid at the given positions.
   The output type matches the *Data Type* of the input grid.
