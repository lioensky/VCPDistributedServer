.. index:: Geometry Nodes; Points of Curve
.. _bpy.types.GeometryNodePointsOfCurve:

********************
Points of Curve Node
********************

.. figure:: /images/node-types_GeometryNodePointsOfCurve.webp
   :align: right
   :alt: Points of Curve node.

The *Points of Curve* node retrieves indices of specific control points in a curve.


Inputs
======

Curve Index
   The index of the input curve.

   .. note::

      By default this uses the :doc:`index </modeling/geometry_nodes/geometry/read/input_index>`
      from the field context, which makes it important that the node is evaluated on
      the curve domain.

Weights
   Values used to sort the curve's control points.
   By default the control points are sorted by index, so the control points with the smallest indices come first.

Sort Index
   Which of the sorted control points to use for the *Point Index* output. If the value is larger than
   the total number of control points, it will wrap around to the beginning.


Outputs
=======

Point Index
   The index of one of the curve's control points, chosen by the *Sort Index* input.

Total
   The number of control points in the curve.
