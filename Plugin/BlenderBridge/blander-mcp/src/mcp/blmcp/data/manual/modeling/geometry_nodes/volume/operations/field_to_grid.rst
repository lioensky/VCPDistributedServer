.. index:: Geometry Nodes; Field to Grid
.. _bpy.types.GeometryNodeFieldToGrid:

******************
Field to Grid Node
******************

.. figure:: /images/node-types_GeometryNodeFieldToGrid.webp
   :align: right
   :alt: Field to Grid node.

The *Field to Grid* node creates one or more new voxel grids by evaluating
geometry fields on the topology of an existing grid.
This allows generating new volumetric data (such as density, temperature,
velocity, or distance fields) directly from field inputs defined in the node
tree.

Each input field is sampled at the voxel positions of the provided topology
grid, producing a corresponding output grid that matches the same resolution,
transform, and domain.
This enables consistent evaluation of multiple attributes or procedural
quantities across the same volume structure.


Inputs
======

Topology
   The reference grid whose voxel layout, resolution, and transform define
   where the input fields will be evaluated.

Additional input sockets can be added for each field to be evaluated.
Each field defines a scalar or vector value to sample on the topology grid.

Fields can be added by dragging them into the blank socket area.

.. note::

   When a color field is connected, it will be evaluated as a *Vector* data
   type, since color grids are not currently supported.


Properties
==========

In the properties panel, each field input can be configured individually.
This includes setting its **data type** (such as *Float*, *Vector*, or *Boolean*)
and managing the order of evaluation.
Each field input produces a corresponding output grid.


Outputs
=======

For each field input, a separate grid output is created that contains the
evaluated voxel data.
All output grids share the same topology as the input grid, ensuring that
they are aligned and compatible for further processing or combination.
