.. index:: Nodes; Get Bundle Item Node
.. _bpy.types.NodeGetBundleItem:
.. --- copy below this line ---

********************
Get Bundle Item Node
********************

.. figure:: /images/node-types_NodeGetBundleItem.webp
   :align: right
   :alt: Get Bundle Item Node

The *Get Bundle Item* node retrieves a value stored inside a bundle using a string path.
Bundles are used to group heterogeneous data together, and this node allows accessing
individual items from such a structure.

If the requested path does not exist in the bundle, a default value is returned and the
*Exists* output is set to false.


Inputs
======

Bundle
   The input bundle to retrieve data from.

Path
   The path identifying the item inside the bundle.
   Paths are written using slash-separated to represent bundles inside other bundles.
   (for example: ``settings/size`` or ``attributes/color``).

Remove
   If enabled, the retrieved item is removed from the bundle before it is passed through
   to the *Bundle* output.


Properties
==========

Socket Type
   The :ref:`data type <attribute-data-types>` of the retrieved item.
   This determines the type of the *Item* output socket.

Shape
   Defines the data structure supported by the *Item* output, such as a *Single* value,
   *Field*, or *Grid*.
   The shape determines how the data is evaluated and passed through the node network.

   This option is available in the Sidebar.


Outputs
=======

Bundle
   The resulting bundle after optionally removing the retrieved item.

Item
   The value retrieved from the bundle at the specified path.
   If the path does not exist, this outputs the default value for the selected socket type.

Exists
   Outputs *True* if an item was found at the given path, otherwise *False*.
