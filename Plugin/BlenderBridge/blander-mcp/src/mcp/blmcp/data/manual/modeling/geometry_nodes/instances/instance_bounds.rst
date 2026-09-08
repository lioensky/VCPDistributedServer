.. index:: Geometry Nodes; Instance Bounds
.. _bpy.types.GeometryNodeInputInstanceBounds:

********************
Instance Bounds Node
********************

.. figure:: /images/node-types_GeometryNodeInputInstanceBounds.webp
   :align: right
   :alt: Instance Bounds node.

The *Instance Bounds* node outputs the axis-aligned bounding box of each instance in the input geometry.
This can be used to determine the spatial extent of instances,
for example, to position or scale objects based on their size.

.. note::

   Only top-level instances are considered; the bounds do not include nested instances inside the instance geometry.
   This avoids the performance cost of realizing nested instances for accurate bounds.

   See :ref:`geometry-nodes_nested-instancing` for more information.


Inputs
======

Use Radius
   For curves, point clouds, and Grease Pencil geometries,
   take the radius attribute into account when computing the bounds.


Outputs
=======

Min
   The minimum corner of the bounding box for each instance, in local space.

Max
   The maximum corner of the bounding box for each instance, in local space.
