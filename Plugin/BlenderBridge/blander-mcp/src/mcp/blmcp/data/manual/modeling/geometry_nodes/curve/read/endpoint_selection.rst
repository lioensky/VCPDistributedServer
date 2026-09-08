.. index:: Geometry Nodes; Endpoint Selection
.. _bpy.types.GeometryNodeCurveEndpointSelection:

***********************
Endpoint Selection Node
***********************

.. figure:: /images/node-types_GeometryNodeCurveEndpointSelection.webp
   :align: right
   :alt: Endpoint Selection node.

The *Endpoint Selection* node provides a selection for an arbitrary number of endpoints in each spline in a curve.

.. note::

   The selection operates for every control point. This may not correspond to the evaluated
   points displayed in the viewport for NURBS and Bézier splines, where one control point may
   correspond to many evaluated points.

.. tip::

   To use this data after the curve has been converted to another data type like mesh or a point cloud,
   the :doc:`/modeling/geometry_nodes/attribute/capture_attribute` can be used.


Inputs
======

Start Size
   The number of points to select from the start.

End Size
   The number of points to select from the end.


Outputs
=======

Selection
   Selection of the start and end of each spline of the curve.


Examples
========

.. figure:: /images/modeling_geometry-nodes_curve_endpoint-selection_example.png
   :align: center

Anywhere the geometry is a curve, this node can be used to generate a selection of
only the first and last points of each spline. Here, the *Points* input of
the :doc:`/modeling/geometry_nodes/instances/instance_on_points` is a curve
consisting of the poly spline shown in Edit Mode.
