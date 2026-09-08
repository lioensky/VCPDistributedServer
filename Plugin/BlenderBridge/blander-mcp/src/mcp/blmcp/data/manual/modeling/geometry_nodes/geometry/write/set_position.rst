.. index:: Geometry Nodes; Set Position
.. _bpy.types.GeometryNodeSetPosition:

*****************
Set Position Node
*****************

.. figure:: /images/node-types_GeometryNodeSetPosition.webp
   :align: right
   :alt: Set Position node.

The *Set Position* node controls the location of each point, the same way as controlling
the ``position`` attribute.
If the input geometry contains instances, this node will affect the location of the origin of each instance.

The input node for this data is the :doc:`/modeling/geometry_nodes/geometry/read/position`.


Inputs
======

Geometry
   Standard geometry input.

Selection
   Whether or not to change the position of each point or instance.
   True values mean the position will be changed, false values mean it will remain the same.

Position
   The new position for selected elements. By default, this is the same as
   if the :doc:`/modeling/geometry_nodes/geometry/read/position` was connected,
   meaning the node will do nothing.

Offset
   An optional translation for each point. This is evaluated at the same time as the *Position* input,
   meaning that fields evaluated for it will not reflect the changed position.


Outputs
=======

Geometry
   Standard geometry output.
