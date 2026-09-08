.. index:: Geometry Nodes; Spline Parameter
.. _bpy.types.GeometryNodeSplineParameter:

*********************
Spline Parameter Node
*********************

.. figure:: /images/node-types_GeometryNodeSplineParameter.webp
   :align: right
   :alt: Spline Parameter node.

The *Spline Parameter* node outputs how far along each spline a control point is.
The *Factor* output is different from dividing the index by the total number of control points,
because the control points might not be equally spaced along the curve.

The first value is zero, so the output corresponds to the length at the control point rather than
including the length of the following segment.

When used on the spline domain, the node outputs the portion of the total length of the curve (including
all splines) has been traversed at the start of each spline. The order of the curve's splines is visible
in the :doc:`Spreadsheet Editor </editors/spreadsheet>`.

.. warning::

   For NURBS and Bézier spline curves, keep in mind that the value retrieved from this node is
   the value at every control point, which may not correspond to the visible *evaluated* points.
   For NURBS splines the difference may be even more pronounced and the result may not be as expected.
   A :doc:`/modeling/geometry_nodes/curve/operations/resample_curve` node can be used to create a poly spline,
   where there is a control point for every evaluated point.

.. note::

   When the *Length* is zero, the *Factor* is arbitrary. In this case the result is
   exceptionally calculated dividing the index by the total number of control points or curves.

Inputs
======

This node has no inputs.


Outputs
=======

Factor
   When the node is used on the point domain, the value is the portion of the spline's
   total length at each control point. On the spline domain it is the portion of the
   curve's total length at the start of the spline.

Length
   When the node is used on the point domain, the value is the distance along the spline to each
   control point. On the spline domain it is the length along the entire curve at the start
   of the spline.

Index
   Each control point's index on its spline. This is different from the output of the
   :doc:`index node </modeling/geometry_nodes/geometry/read/input_index>`, which also counts the
   control points in all previous splines.


Examples
========

.. figure:: /images/modeling_geometry-nodes_curve_curve-parameter_example.png
   :align: right

The parameter used to control the radius of the curve.
The beginning of the spline has a radius of 0, the end has a radius of 1.
