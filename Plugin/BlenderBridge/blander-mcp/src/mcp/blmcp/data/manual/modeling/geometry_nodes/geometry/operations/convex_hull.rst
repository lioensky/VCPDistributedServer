.. index:: Geometry Nodes; Convex Hull
.. _bpy.types.GeometryNodeConvexHull:

****************
Convex Hull Node
****************

.. figure:: /images/node-types_GeometryNodeConvexHull.webp
   :alt: Convex Hull node.

The *Convex Hull* node outputs a convex mesh that is enclosing all points in the input geometry.

.. note::

   When the node is used on a geometry with instances, the algorithm will run once per instance,
   resulting in many convex hull meshes in the instance geometries. The *Realize Instances* node can
   be used to get a convex hull of an entire geometry.

.. important::

   Volumes are not supported by this node, and attributes are not automatically transferred to the result.

.. note::

   This node is affected by the limitations of floating point precision. If points are too close together,
   they may be merged in the result mesh.

Inputs
======

Geometry
   Standard geometry input.


Outputs
=======

Convex Hull
   Mesh that encloses all points in the input.
