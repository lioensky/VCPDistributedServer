.. index:: Geometry Nodes; Set Grid Background
.. _bpy.types.GeometryNodeSetGridBackground:

************************
Set Grid Background Node
************************

.. figure:: /images/node-types_GeometryNodeSetGridBackground.webp
   :align: right
   :alt: Set Grid Background node.

The *Set Grid Background* node defines the background value for a voxel grid.
This value is used when sampling regions of the grid that do not contain any
explicitly stored voxels, such as inactive areas or tiles that have not been
initialized.

By default, empty voxels in a grid evaluate to zero or another implicit value.
This node allows customizing that behavior, which can be useful when
constructing grids procedurally or when combining multiple grids.


Inputs
======

Grid
   The input grid whose background value will be modified.

Background
   The value to assign to inactive or uninitialized voxels and tiles.

   When sampling outside the defined region of the grid, this value will be
   returned instead of zero.


Properties
==========

Data Type
   The type of data stored in the grid.
   Determines the expected type of the *Background* input and the values the
   grid can hold (e.g. *Float*, *Integer*, *Boolean*, Vector).


Outputs
=======

Grid
   The resulting grid with the updated background value applied.

   This grid can be passed to other nodes such as
   :doc:`Sample Grid Index </modeling/geometry_nodes/volume/sample/sample_grid_index>`
   or :doc:`Sample Grid </modeling/geometry_nodes/volume/sample/sample_grid>`
   to ensure consistent results in areas where the grid has no stored voxels.
