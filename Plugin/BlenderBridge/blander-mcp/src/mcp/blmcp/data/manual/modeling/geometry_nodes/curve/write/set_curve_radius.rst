.. index:: Geometry Nodes; Set Curve Radius
.. _bpy.types.GeometryNodeSetCurveRadius:

*********************
Set Curve Radius Node
*********************

.. figure:: /images/node-types_GeometryNodeSetCurveRadius.webp
   :align: right
   :alt: Set Curve Radius node.

The *Set Curve Radius* controls the radius of the curve, used for operations like the size of the profile
in the :doc:`Curve to Mesh </modeling/geometry_nodes/curve/operations/curve_to_mesh>` node. The value is set for
every control point, and is then interpolated to each evaluated point in between the control points.

The input node for this data is the :doc:`Radius node </modeling/geometry_nodes/geometry/read/radius>`.


Inputs
======

Curve
   Standard geometry input, containing curves.

Selection
   Whether or not to change the value on each control point. True values mean the value will be changed,
   false values mean the value will remain the same.

Radius
   The radius value for each control point.


Outputs
=======

Geometry
   Standard geometry output.
