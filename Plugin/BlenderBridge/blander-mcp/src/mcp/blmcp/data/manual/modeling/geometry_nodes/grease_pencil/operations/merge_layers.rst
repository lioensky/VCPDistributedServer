.. index:: Geometry Nodes; Merge Layers
.. _bpy.types.GeometryNodeMergeLayers:

*****************
Merge Layers Node
*****************

.. figure:: /images/node-types_GeometryNodeMergeLayers.webp
   :align: right
   :alt: Merge Layers node.

Combines multiple :doc:`Grease Pencil Layers </grease_pencil/properties/layers>` into a single layer.

.. seealso::

   :ref:`Merge Layers Operator <bpy.ops.grease_pencil.layer_merge>`


Inputs
======

Grease Pencil
   The Grease Pencil object with multiple layers to combine.
Selection
   Operate of a subset of layers by setting the field layer index value to *true*.
   By default, all layers are selected.
Group ID
   The index numbers of the layer to be merged.
   This input is only visible when using *By Group ID* Mode.


Properties
==========

Mode
   Determines how to choose which layers are merged.

   :By Name: Combine all layers which have the same name.
   :By Group ID: Provide a custom group ID for each layer and all layers with the same ID will be merged into one.


Outputs
=======

Grease Pencil
   The Grease Pencil object with combined layers.
