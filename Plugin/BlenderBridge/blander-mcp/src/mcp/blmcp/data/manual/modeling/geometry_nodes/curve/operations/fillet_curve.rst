.. index:: Geometry Nodes; Fillet Curve
.. _bpy.types.GeometryNodeFilletCurve:

*****************
Fillet Curve Node
*****************

.. figure:: /images/node-types_GeometryNodeFilletCurve.webp
   :align: right
   :alt: Fillet Curve node.

The *Fillet Curve* rounds corners on curve control points, similar to the effect of
the :doc:`Bevel Modifier </modeling/modifiers/generate/bevel>` on a 2D mesh.
However, a key difference is that the rounded portions created by the Fillet Curve node
are always portions of a circle.


Inputs
======

Curve
   Standard geometry input with a curve component.

Radius
   The radius of the circle portion generated at each fillet.

Count
   Only in *Poly* mode, the number of control points to add for each fillet.

Limit Radius
   Whether to limit the maximum value of the radius in order to avoid overlapping fillets.

Mode
   How to choose number of vertices on fillet

   :Bézier:
      Only two control points will be generated for every filleted control point. The shape generated
      by the aligned handles on the generated control points on either side of the fillet is used to
      create the circle portion shape, meaning that the number of segments in the fillet shape depends on
      the :doc:`spline's resolution value </modeling/geometry_nodes/curve/read/spline_resolution>`.
   :Poly:
      The number of control points generated for each field
      input is controlled directly with an integer field input.
      This mode works better for poly and NURBS splines.


Outputs
=======

Curve
   Standard geometry input with a curve component.


Examples
========

.. figure:: /images/modeling_geometry-nodes_curve_fillet-curve_example_1.png
   :align: center

   The node can be used to round the corners of simple 3D poly splines.

.. figure:: /images/modeling_geometry-nodes_curve_fillet-curve_example_2.png
   :align: center

   The node can be combined with the curve primitive nodes to make more interesting shapes.
