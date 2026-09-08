.. index:: Nodes; Store Bundle Item Node
.. _bpy.types.NodeStoreBundleItem:
.. --- copy below this line ---

**********************
Store Bundle Item Node
**********************

.. figure:: /images/node-types_NodeGetBundleItem.webp
   :align: right
   :alt: Store Bundle Item Node

The *Store Bundle Item* node writes a value into a bundle at a specified path.
If an item already exists at the given path, it is replaced.
If the path does not exist, it is created automatically.

This node is commonly used to build or modify bundles incrementally,
allowing heterogeneous data to be grouped and passed through node networks.


Inputs
======

Bundle
   The input bundle to store data into.

Path
   The path identifying where the item will be stored inside the bundle.
   Paths are written using slash-separated to represent bundles inside other bundles.
   (for example: ``settings/size`` or ``attributes/color``).

Item
   The value to store at the specified path.
   The data type and structure of this input are defined by the node properties.


Properties
==========

Socket Type
   The :ref:`data type <attribute-data-types>` of the *Item* input.
   This determines the type of data that can be stored in the bundle.

Shape
   Defines the data structure supported by the *Item* input, such as a *Single* value,
   *Field*, or *Grid*.
   The shape determines how the data is evaluated and stored in the bundle.

   This option is available in the Sidebar.


Outputs
=======

Bundle
   The resulting bundle containing the stored item.
