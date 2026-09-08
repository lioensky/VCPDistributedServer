.. index:: Geometry Nodes; Spline Resolution
.. _bpy.types.GeometryNodeInputSplineResolution:

**********************
Spline Resolution Node
**********************

.. figure:: /images/node-types_GeometryNodeInputSplineResolution.webp
   :align: right
   :alt: Spline Resolution node.

The *Spline Resolution* outputs the number of evaluated curve points that will be generated for
every control point on the spline. This node works for NURBS, Bézier, and Catmull Rom splines.

For poly splines, there is a one-to-one correspondence between original points and evaluated points,
so the resolution does not have an effect.

On Bézier splines, the resolution does not have an effect on segments between vector handles,
since there are no extra evaluated points between the neighboring control points.

The node to set this data is the :doc:`/modeling/geometry_nodes/curve/write/set_spline_resolution`.


Inputs
======

This node has no inputs.


Outputs
=======

Resolution
   The integer resolution value for each spline.
