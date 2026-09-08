.. index:: Geometry Nodes; Field Min & Max
.. _bpy.types.GeometryNodeFieldMinAndMax:

********************
Field Min & Max Node
********************

.. figure:: /images/node-types_GeometryNodeFieldMinAndMax.webp
   :align: right
   :alt: Field Min & Max Node.

The *Field Min & Max* calculates the minimum and maximum of a given field.


Inputs
======

Value
   The values the minimum and maximum will be calculated from

Group ID
   An index used to group values together for multiple separate averages.
   This can be thought of as a choice of the "bin" in which to place each value.
   This input has no effect when it is only a single value.


Properties
==========

Data Type
   :Float: The node will average a *Float* field.
   :Integer: The node will accumulate an *Integer* field.
   :Vector: The node will average a *Vector* field.

Domain
   The :ref:`attribute domain <attribute-domains>` used for evaluate the *Value* input.


Output
======

Min
   The lowest value in each group.

Max
   The highest value in each group.
