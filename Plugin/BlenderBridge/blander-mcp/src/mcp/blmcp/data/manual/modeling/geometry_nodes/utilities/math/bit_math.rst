.. index:: Geometry Nodes; Bit Math
.. _bpy.types.FunctionNodeBitMath:

*************
Bit Math Node
*************

.. figure:: /images/node-types_FunctionNodeBitMath.webp
   :align: right
   :alt: Bit Math Node.

The *Bit Math* node performs bitwise operations on 32-bit integer values.
It is useful for low-level data manipulation and logic operations.


Inputs
======

A
   The first integer input. Used by all operations.
B
   The second integer input. Only used by operations that require two inputs (*And*, *Or*, *Exclusive Or*).
Shift
   The number of bits to shift or rotate. Used only for *Shift* and *Rotate* operations.


Properties
==========

Operation
   The bitwise operation to apply:

   :And: Returns a value where the bits of A and B are both set.
   :Or: Returns a value where the bits of either A or B are set.
   :Exclusive Or: Returns a value where only one of A or B has the bit set (XOR).
   :Not: Inverts the bits of A. Equivalent to `-A - 1` in decimal.
   :Shift: Shifts the bits of A by the amount specified in *Shift*. Positive shifts are to the left; negative to the
    right.
   :Rotate: Rotates the bits of A by the amount specified in *Shift*. Positive rotates left; negative rotates right.


Output
======

Value
   The result of the bitwise operation.
