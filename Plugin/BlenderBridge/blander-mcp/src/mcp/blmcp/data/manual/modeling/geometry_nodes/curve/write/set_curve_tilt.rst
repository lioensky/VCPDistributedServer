.. index:: Geometry Nodes; Set Curve Tilt
.. _bpy.types.GeometryNodeSetCurveTilt:

*******************
Set Curve Tilt Node
*******************

.. figure:: /images/node-types_GeometryNodeSetCurveTilt.webp
   :align: right
   :alt: Set Curve Tilt node.

The *Set Curve Tilt* controls the tilt angle at each curve control point.
That angle rotates normal vector which is generated at each point
when evaluating the curve. The normal then can be retrieved with
the :doc:`/modeling/geometry_nodes/geometry/read/normal`.

The rotation of the normal vector is an :term:`Axis Angle` rotation.
It is the same as the :doc:`/modeling/geometry_nodes/utilities/vector/vector_rotate` operation
with the tangent vector as the axis, the raw evaluated normal is used as
the original vector, and the tilt as the rotation angle.

The input node for this data is the :doc:`/modeling/geometry_nodes/curve/read/curve_tilt`.


Inputs
======

Curve
   Standard geometry input, containing curves.

Selection
   Whether or not to change the value on each control point. True values mean the value will be changed,
   false values mean the value will remain the same.

Tilt
   The tilt angle for each control point.


Outputs
=======

Curve
   Standard geometry output.
