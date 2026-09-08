.. index:: Geometry Nodes; Viewport Transform
.. _bpy.types.GeometryNodeViewportTransform:

***********************
Viewport Transform Node
***********************

.. figure:: /images/node-types_GeometryNodeViewportTransform.webp
   :align: right
   :alt: Viewport Transform node.

The *Viewport Transform* node retrieves the view direction and location of the :doc:`/editors/3dview/index`.

.. note::

   This node can only be used in the :ref:`Tool context <tool_context>`.


Inputs
======

This node has no inputs.


Outputs
=======

Projection
   The 3D Viewport's perspective or orthographic projection matrix.
View
   The view direction and location of the 3D viewport.
Is Orthographic
   Whether the viewport is using orthographic projection.
