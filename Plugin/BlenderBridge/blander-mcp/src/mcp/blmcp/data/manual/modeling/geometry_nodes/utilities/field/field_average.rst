.. index:: Geometry Nodes; Field Average
.. _bpy.types.GeometryNodeFieldAverage:

******************
Field Average Node
******************

.. figure:: /images/node-types_GeometryNodeFieldAverage.webp
   :align: right
   :alt: Field Average Node.

The *Field Average* calculates the mean and median of a given field.


Inputs
======

Value
   The values the mean and median will be calculated from.

Group ID
   An index used to group values together for multiple separate averages.
   This can be thought of as a choice of the "bin" in which to place each value.
   This input has no effect when it is only a single value.


Properties
==========

Data Type
   :Float: The node will average a *Float* field.
   :Vector: The node will average a *Vector* field.

Domain
   The :ref:`attribute domain <attribute-domains>` used for evaluate the *Value* input.


Output
======

Mean
   The sum of all values in each group divided by the size of said group.

Median
   The middle value in each group when all values are sorted from lowest to highest.
