.. index:: Geometry Nodes; Set Grid Transform
.. _bpy.types.GeometryNodeSetGridTransform:

***********************
Set Grid Transform Node
***********************

.. figure:: /images/node-types_GeometryNodeSetGridTransform.webp
   :align: right
   :alt: Set Grid Transform node.

The *Set Grid Transform* node defines the spatial transform of a voxel grid,
converting its index space (voxel coordinates) into object space.

By default, voxel grids use a transform that maps integer voxel indices
directly to object space coordinates. This node allows specifying a custom
transform, enabling operations such as repositioning, rotating, or scaling
a grid relative to an object or scene.


Inputs
======

Grid
   The input grid whose transform will be changed.

Transform
   The new transform from grid index space to object space.
   This determines how the voxel grid is positioned and oriented in 3D space.
   Typically this input comes from a :term:`Transformation Matrix`/



Properties
==========

Data Type
   The data type of the grid to which the transform is applied.
   Determines the kind of values stored in the grid
   (e.g. *Float*, *Integer*, *Boolean*, *Vector*), and must match the input grid's data type.


Outputs
=======

Is Valid
   Outputs ``true`` if the provided transform was valid and successfully
   applied to the grid.

   The new transform can fail to be applied if the input transform isn't
   invertible or for some extremes of scaling (0 or combinations of negative and positive).

Grid
   The resulting grid with the updated transform applied.
   The new transform affects how the grid's voxel indices are interpreted
   in object space, which in turn changes how the grid interacts with other
   geometry and sampling operations.
