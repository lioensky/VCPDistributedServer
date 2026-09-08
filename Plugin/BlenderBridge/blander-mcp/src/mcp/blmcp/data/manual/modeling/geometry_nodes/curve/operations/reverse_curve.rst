.. index:: Geometry Nodes; Reverse Curve
.. _bpy.types.GeometryNodeReverseCurve:

******************
Reverse Curve Node
******************

.. figure:: /images/node-types_GeometryNodeReverseCurve.webp
   :align: center
   :alt: Reverse Curve node.

The *Reverse Curve* node swaps the start and end of splines.
The shape of the splines is not changed.

.. tip::

   When used on the *Profile* input of the :doc:`/modeling/geometry_nodes/curve/operations/curve_to_mesh`,
   this node fill flip the normals of the resulting mesh.


Inputs
======

Curve
   Standard geometry input.

Selection
   Whether or not to change the direction of each spline. True values mean the direction will be changed,
   false values mean the spline will be unaffected.


Outputs
=======

Curve
   Standard geometry output.
