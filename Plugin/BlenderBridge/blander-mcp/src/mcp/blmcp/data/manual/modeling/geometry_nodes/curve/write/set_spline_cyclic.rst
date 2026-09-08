.. index:: Geometry Nodes; Set Spline Cyclic
.. _bpy.types.GeometryNodeSetSplineCyclic:

**********************
Set Spline Cyclic Node
**********************

.. figure:: /images/node-types_GeometryNodeSetSplineCyclic.webp
   :align: right
   :alt: Set Spline Cyclic node.

The *Set Spline Cyclic* node changes whether splines loop back on themselves --
that is, whether their first and last control points are connected.

You can use the :doc:`/modeling/geometry_nodes/curve/read/is_spline_cyclic`
to read this property.


Inputs
======

Curve
   Standard geometry input.

Selection
   Whether to change the cyclic setting for each spline. *True* means the
   setting will be changed, *false* means it will stay the same.

Cyclic
   Whether to connect the first and last control points of each spline.


Outputs
=======

Curve
   Standard geometry output.
