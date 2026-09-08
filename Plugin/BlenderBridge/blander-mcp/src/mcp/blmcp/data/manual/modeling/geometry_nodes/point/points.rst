.. index:: Geometry Nodes; Points
.. _bpy.types.GeometryNodePoints:

***********
Points Node
***********

.. figure:: /images/node-types_GeometryNodePoints.webp
   :align: right
   :alt: Points node.

The *Points* node generate a point cloud with positions and radii defined by
:doc:`fields </modeling/geometry_nodes/fields>`.


Inputs
======

Count
   The number of points to create.

Position
   The position of each generated point.

Radius
   The :doc:`radius </modeling/geometry_nodes/geometry/read/radius>` of each point.

.. note::

   Since the point cloud is created from scratch, the *Position* and *Radius* inputs can only depend on
   the :doc:`index </modeling/geometry_nodes/geometry/read/input_index>` node. Regular input nodes like
   the :doc:`position </modeling/geometry_nodes/geometry/read/position>` won't work.


Outputs
=======

Points
   Standard geometry output.
