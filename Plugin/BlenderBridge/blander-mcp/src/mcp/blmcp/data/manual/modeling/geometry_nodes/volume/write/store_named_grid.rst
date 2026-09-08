.. index:: Geometry Nodes; Store Named Grid
.. _bpy.types.GeometryNodeStoreNamedGrid:

*********************
Store Named Grid Node
*********************

.. figure:: /images/node-types_GeometryNodeStoreNamedGrid.webp
   :align: right
   :alt: Store Named Grid node.

The *Store Named Grid* node stores a voxel grid inside a volume geometry under a specified name.
This allows multiple grids (such as *density*, *temperature*, or *velocity*) to
be contained within a single volume object and accessed later using the
:doc:`Get Named Grid </modeling/geometry_nodes/volume/read/get_named_grid>` node.

If a grid with the same name already exists in the input volume, it will be replaced by the new grid.
This makes it possible to update or overwrite grids during a geometry node
evaluation, for example when generating or modifying simulation fields.


Inputs
======

Volume
   The input volume geometry to which the grid will be added or replaced.

Name
   The name under which the grid will be stored in the volume.
   This name is used later to retrieve the grid using the *Get Named Grid*
   node or in the Spreadsheet editor under the *Volume Grids* section.

Grid
   The grid to store within the volume.
   The grid must have a compatible resolution and transform with the target volume.
   The grid's data type must match the node's *Data Type* property.


Properties
==========

Data Type
   The type of data stored in the grid (e.g. *Float*, *Integer*, *Boolean*, or *Vector*).
   Determines the expected data type of the *Grid* input and ensures that the
   grid is stored correctly in the volume container.


Outputs
=======

Volume
   The resulting volume geometry containing the newly stored grid.
   If a grid with the same name previously existed, it is replaced with the
   new one; otherwise, the grid is added as a new entry.
