.. index:: Geometry Nodes; Is Viewport
.. _bpy.types.GeometryNodeIsViewport:

****************
Is Viewport Node
****************

.. figure:: /images/node-types_GeometryNodeIsViewport.webp
   :align: right
   :alt: Is Viewport Node.

The *Is Viewport* node outputs true when geometry nodes are evaluated for the viewport.
For the final render the node outputs false.


Inputs
======

This node has no inputs.


Outputs
=======

Is Viewport
   Boolean value that indicates whether geometry nodes are evaluated for preview.


Example
=======

.. figure:: /images/modeling_geometry-nodes_is_viewport_example.jpg

   Using *Is Viewport* to switch between low quality and high quality.
