.. index:: Geometry Nodes; Offset Point in Curve
.. _bpy.types.GeometryNodeOffsetPointInCurve:

**************************
Offset Point in Curve Node
**************************

.. figure:: /images/node-types_GeometryNodeOffsetPointInCurve.webp
   :align: right
   :alt: Offset Point in Curve node.

The *Offset Point in Curve* node retrieves other points in the same curve as
the input control point. This is like starting at a specific control point and
walking along neighboring points toward the start or end of the curve.

Conceptually the operation is similar to the
:doc:`/modeling/geometry_nodes/mesh/topology/offset_corner_in_face`,
but the point index doesn't wrap around to the other end of the curve unless it is cyclic.


Inputs
======

Point Index
   The index of the input control point.

   .. note::

      By default this uses the :doc:`index </modeling/geometry_nodes/geometry/read/input_index>`
      from the field context, which makes it important that the node is evaluated on
      the point domain.

Offset
   The number of points to move around the curve before finding the result.
   If the curve is :doc:`cyclic </modeling/geometry_nodes/curve/read/is_spline_cyclic>`
   and the offset goes past the start or end point of the curve, it will wrap around
   to the other side.


Outputs
=======

Is Valid Offset
   Whether the input control point plus the offset is a valid index of the original curve.
   Any offset in a cyclic curve is always valid.

Point Index
   The index of the offset curve point.
