.. index:: Geometry Nodes; Is Edge Smooth
.. _bpy.types.GeometryNodeInputEdgeSmooth:

*******************
Is Edge Smooth Node
*******************

.. figure:: /images/node-types_GeometryNodeInputEdgeSmooth.webp
   :align: right
   :alt: Is Edge Smooth Node.

The *Is Edge Smooth* node outputs true for each edge of the mesh that is *not* marked as sharp. Otherwise, if the edge
*is* marked as sharp, then the node outputs false.

.. seealso::

   :ref:`Mark Sharp & Clear Sharp <bpy.ops.mesh.mark_sharp>`


Inputs
======

This node has no inputs.


Outputs
=======

Smooth
   Boolean value that indicates whether the edges of the mesh are *not* marked as sharp.
