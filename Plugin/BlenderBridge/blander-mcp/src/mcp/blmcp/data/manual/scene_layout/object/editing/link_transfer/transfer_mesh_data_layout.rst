.. _bpy.ops.object.datalayout_transfer:

*************************
Transfer Mesh Data Layout
*************************

.. reference::

   :Mode:      Object Mode
   :Menu:      :menuselection:`Object --> Link/Transfer Data --> Transfer Mesh Data Layout`

Transfers layout of data layer(s) from active to selected meshes.

Data Type
   Which data to transfer.

   .. figure:: /images/scene-layout_object_editing_link-transfer_transfer-mesh-data_menu.png

      Data types.

Exact Match
   Also Delete some data layers from destination if necessary, so that it matches the source exactly.
Source Layers Selection
   Which layers to transfer, in case of multi-layer types.

   Active Layer
      Only transfer the active data layer.
   All Layers
      Transfer all data layers.

Destination Layers Matching
   How to match source and destination layers.

   By Name
      Match target data layers to affect by name.
   By Order
      Match target data layers to affect by order (indices).

.. seealso::

   :doc:`Data Transfer Modifier </modeling/modifiers/modify/data_transfer>`
