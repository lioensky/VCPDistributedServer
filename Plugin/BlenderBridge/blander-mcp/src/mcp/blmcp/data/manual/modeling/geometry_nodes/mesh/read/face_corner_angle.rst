.. index:: Geometry Nodes; Face Corner Angle

**********************
Face Corner Angle Node
**********************

.. figure:: /images/node-types_GeometryNodeFaceCornerAngle.webp
   :align: right
   :alt: Face Corner Angle Node.

The *Face Corner Angle* node outputs geometric information about the angle at each face corner
of a mesh. It can be used to analyze the shape of polygons, detect sharp corners, or create
procedural effects based on corner geometry.


Inputs
======

This node has no inputs.


Outputs
=======

Corner Angle
   The internal angle at each face corner, measured in radians.
   For example, a right angle returns approximately ``1.571``.

Bisector
   A normalized vector pointing along the bisector of the corner angle,
   halfway between the directions of the two connected edges.
