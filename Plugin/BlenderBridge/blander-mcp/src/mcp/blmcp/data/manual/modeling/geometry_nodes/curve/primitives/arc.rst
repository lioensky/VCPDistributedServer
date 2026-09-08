.. index:: Geometry Nodes; Arc
.. _bpy.types.GeometryNodeCurveArc:

********
Arc Node
********

.. figure:: /images/node-types_GeometryNodeCurveArc.webp
   :align: right
   :alt: Arc Node.

The *Arc* node generates a poly spline arc. The node has two modes, Radius and Points.


Inputs
======

Resolution
   Number of edges on the arc.

Radius
   The radius of the arc. *Radius* mode only.

Start Angle
   Starting angle of the arc.  *Radius* mode only.

Sweep Angle
   Length of the arc.   *Radius* mode only.

Connect Center
   Connect the arc at the center.

Invert Arc
   Invert and draw opposite arc.

Start, Middle, End
   The three points on the arc. *Points* mode only.
   The order of the points determines the direction (clockwise or counterclockwise) of the arc.
   The arc will always draw from Start to End via the Middle point. This can be changed by using
   the Invert Arc option.

Offset Angle
   Offset angle of the arc. *Points* mode only.

.. note::

   Because of the finite resolution, the middle point does not necessarily lie on the generated arc.


Properties
==========

Mode
   :Points:
      The position and radius of the arc are determined by three points.
      The center of the arc, radius and normal are also given as outputs.
   :Radius:
      The arc is determined by the radius, start angle and sweep angle.


Outputs
=======

Curve
   Poly spline generated from the inputs.

Center
   The center of the arc described by the three points. *Points* mode only.
Normal
   The normal direction of the plane described by the three points,
   pointing towards the positive Z axis. *Points* mode only.
Radius
   The radius of the arc described by the three points. *Points* mode only.
