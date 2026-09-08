.. index:: Geometry Nodes; Sample Grid Index
.. _bpy.types.GeometryNodeSampleGridIndex:

**********************
Sample Grid Index Node
**********************

.. figure:: /images/node-types_GeometryNodeSampleGridIndex.webp
   :align: right
   :alt: Sample Grid Index node.

The *Sample Grid Index* node retrieves values directly from a voxel grid at
specific voxel indices rather than at arbitrary spatial positions.
Unlike the :doc:`Sample Grid </modeling/geometry_nodes/volume/sample/sample_grid>`
node, which interpolates between voxels in object space, this node reads the
exact stored value of the voxel located at the specified integer coordinates.

This makes it useful for working in *index space*, for example when performing
voxel neighborhood lookups, procedural filtering, or sampling based on values
from the :doc:`Voxel Index </modeling/geometry_nodes/volume/read/voxel_index>` node.


Inputs
======

Grid
   The input voxel grid to sample values from. The grid may store scalar,
   vector, color, or boolean data depending on its data type.

X, Y, Z
   The integer voxel coordinates in grid index space to sample from.
   Each coordinate specifies which voxel to retrieve the value from along its respective axis.


Properties
==========

Data Type
   The type of data stored in the grid (e.g. *Float*, *Integer*, *Boolean*, or *Vector*).
   Determines both the expected data type of the *Grid* input and the type of the *Value* output.


Outputs
=======

Value
   The voxel value retrieved at the specified grid indices.
   The output type matches the grid's *Data Type*. No interpolation is
   performed—values are sampled exactly as stored in the grid.
