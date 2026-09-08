.. index:: Geometry Nodes; Set Material Index
.. _bpy.types.GeometryNodeSetMaterialIndex:

***********************
Set Material Index Node
***********************

.. figure:: /images/node-types_GeometryNodeSetMaterialIndex.webp
   :align: right
   :alt: Set Material Index node.

The *Set Material Index* node sets the material index for a geometry.

The node to get this data is the :doc:`Material Index </modeling/geometry_nodes/geometry/material/material_index>`
node.


Inputs
======

Geometry
   Standard geometry input.

Selection
   Whether to change the material index for each face.
   True values mean the material index will be changed, false values mean it will remain the same.

Material Index
   The new material index.


Outputs
=======

Geometry
   Standard geometry output.
