.. index:: Geometry Nodes; Set Geometry Name
.. _bpy.types.GeometryNodeSetGeometryName:

**********************
Set Geometry Name Node
**********************

.. figure:: /images/node-types_GeometryNodeSetGeometryName.png
   :align: right
   :alt: Set Geometry Name node.

The *Set Geometry Name* node stores a custom name on the geometry, overriding the name which
might come from the :doc:`/modeling/geometry_nodes/input/scene/object_info` or a
:doc:`/modeling/geometry_nodes/grease_pencil/operations/grease_pencil_to_curves`.
The name is displayed in the spreadsheet and can helpful for debugging purposes.


Inputs
======

Geometry
   Standard geometry input.

Name
   The new name for the geometry.


Outputs
=======

Geometry
   Standard geometry output.
