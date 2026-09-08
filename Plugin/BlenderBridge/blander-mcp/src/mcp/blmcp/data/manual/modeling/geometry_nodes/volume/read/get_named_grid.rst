.. index:: Geometry Nodes; Get Named Grid
.. _bpy.types.GeometryNodeGetNamedGrid:

*******************
Get Named Grid Node
*******************

.. figure:: /images/node-types_GeometryNodeGetNamedGrid.webp
   :align: right
   :alt: Get Named Grid node.

The *Get Named Grid* node retrieves a specific voxel grid from a volume geometry by its name.
Each volume object can contain multiple grids (for example, *density*, *color*,
*temperature*, or *velocity*), and this node allows accessing one of them for
further processing in the node tree.

The retrieved grid can then be sampled, modified, or converted to geometry
using other grid or SDF nodes.


Inputs
======

Volume
   The input volume geometry that contains one or more named grids.

Name
   The name of the grid to retrieve from the volume.
   The name must match an existing grid stored in the volume data block.

Remove
   When enabled, removes the grid from the volume after it has been retrieved.
   This can be useful when restructuring volume data to avoid duplication or
   manage memory more efficiently.


Properties
==========

Data Type
   The type of data stored in the grid (e.g. *Float*, *Integer*, *Boolean*, or *Vector*).
   Determines both the expected data type of the *Grid* output and how it can
   be used in subsequent nodes.


Outputs
=======

Volume
   The resulting volume geometry after optionally removing the retrieved grid.

Grid
   The extracted grid corresponding to the given *Name* and *Data Type*.
   This grid can be passed to other nodes such as
   :doc:`Sample Grid </modeling/geometry_nodes/volume/sample/sample_grid>` or
   :doc:`Grid to Mesh </modeling/geometry_nodes/volume/operations/grid_to_mesh>`
   for further manipulation or conversion.
