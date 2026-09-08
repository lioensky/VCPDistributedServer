.. index:: Geometry Nodes; Is Spline Cyclic
.. _bpy.types.GeometryNodeInputSplineCyclic:

*********************
Is Spline Cyclic Node
*********************

.. figure:: /images/node-types_GeometryNodeInputSplineCyclic.webp
   :align: right
   :alt: Is Spline Cyclic node.

The *Is Spline Cyclic* controls whether each of the curve splines start and endpoints form a connection.
Its output corresponds to the built-in ``cyclic`` attribute on the curve spline domain.

The node to set this data is the :doc:`/modeling/geometry_nodes/curve/write/set_spline_cyclic`.


Inputs
======

This node has no inputs.


Outputs
=======

Cyclic
   Whether the spline is cyclic.
