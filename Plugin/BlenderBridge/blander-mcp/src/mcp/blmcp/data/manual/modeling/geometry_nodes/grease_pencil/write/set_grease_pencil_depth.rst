.. index:: Geometry Nodes; Set Grease Pencil Depth
.. _bpy.types.GeometryNodeSetGreasePencilDepth:

****************************
Set Grease Pencil Depth Node
****************************

.. figure:: /images/node-types_GeometryNodeSetGreasePencilDepth.webp
   :align: right
   :alt: Set Grease Pencil Depth Node.

The *Set Grease Pencil Depth* node sets the Grease Pencil
:ref:`depth order <bpy.types.GreasePencil.stroke_depth_order>` to use.


Inputs
======

Grease Pencil
   The input Grease Pencil geometry.


Properties
==========

Depth Order
   Defines how the strokes are ordered in 3D space (for objects not displayed *In Front*).

   :2D Layers:
      The Strokes drawing order respect the order of the 2D layers list (top to bottom)
      and ignores the real position of the strokes in 3D space.
      See :doc:`2D Layers </grease_pencil/properties/layers>` for more information.
   :3D Location:
      The strokes drawing order is based on the stroke location in 3D space.


Outputs
=======

Grease Pencil
   The modified Grease Pencil geometry.
