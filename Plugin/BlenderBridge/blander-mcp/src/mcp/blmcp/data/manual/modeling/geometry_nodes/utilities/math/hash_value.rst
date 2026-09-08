.. index:: Geometry Nodes; Hash Value
.. _bpy.types.FunctionNodeHashValue:

***************
Hash Value Node
***************

.. figure:: /images/node-types_FunctionNodeHashValue.webp
   :align: right
   :alt: Hash Value Node.

The *Hash Value* node takes a value input and hashes this to
an integer.

.. important::

   Hashes cannot be relied upon to be used as unique
   identifiers because they are not guaranteed to be unique.
   It can be used to generate somewhat stable randomness
   especially in cases where *White Noise* does not offer
   enough flexibility.


Inputs
======

Value
   Value input determined by *Data Type* property.

Seed
   Integer input used to generate different Hashes	.


Properties
==========

Data Type
   The data type that is used for the *Value* input.
   The node supports float, integer, vector, color,
   boolean, rotation, matrix and string data types.


Output
======

Hash
   Standard integer output.
