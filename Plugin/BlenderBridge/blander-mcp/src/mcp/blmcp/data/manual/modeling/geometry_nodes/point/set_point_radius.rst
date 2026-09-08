.. index:: Geometry Nodes; Set Point Radius
.. _bpy.types.GeometryNodeSetPointRadius:

*********************
Set Point Radius Node
*********************

.. figure:: /images/node-types_GeometryNodeSetPointRadius.webp
   :align: right
   :alt: Set Point Radius node.

The *Set Point Radius* node controls the size each selected point cloud point should display with in the viewport.

The input node for this data is the :doc:`/modeling/geometry_nodes/geometry/read/radius`.


Inputs
======

Geometry
   Standard geometry input.

Radius
   Float value indicating the radius of the point geometry at each point.

Selection
   Boolean input for selecting which points will have the radius value applied.


Outputs
=======

Geometry
   Standard geometry output.
