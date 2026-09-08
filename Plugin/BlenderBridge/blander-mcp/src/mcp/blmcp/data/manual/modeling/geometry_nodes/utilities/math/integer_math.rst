.. index:: Geometry Nodes; Integer Math
.. _bpy.types.FunctionNodeIntegerMath:

*****************
Integer Math Node
*****************

.. figure:: /images/node-types_FunctionNodeIntegerMath.webp
   :align: right
   :alt: Integer Math Node.

The *Integer Math* node performs math operations.


Inputs
======

Value
   Standard integer value input. Depending on the operation
   there will be more than one input.


Properties
==========

Operation
   The mathematical operator to be applied to the input values:

   Functions
      :Add: The sum of the two values.
      :Subtract: The difference between the two values.
      :Multiply: The product of the two values.
      :Divide: The division of the first value by the second value.
      :Multiply Add: The sum of the product of the two values with *Addend*.
      :Absolute:
         The input value is read without regard to its sign.
         This turns negative values into positive values.
      :Negate: Changes the sign of the input value.
      :Power: The *Base* raised to the power of *Exponent*.

   Comparison
      :Minimum: Outputs the smallest of the input values.
      :Maximum: Outputs the largest of two input values.
      :Sign:
         Extracts the sign of the input value. All positive numbers
         will output 1. All negative numbers will output -1. And 0 will output 0.

   Rounding
      :Divide Round: Divide the values and round the result toward zero.
      :Divide Floor: Divide the values and floor the result down to the nearest integer.
      :Divide Ceiling: Divide the values and ceil the result up to the nearest integer	.
      :Floored Modulo: Returns the positive remainder of a division operation.
      :Modulo: Outputs the remainder once the first value is divided by the second value.
      :Greatest Common Divisor: The largest positive integer that divides into each of the values.
      :Least Common Multiple: The smallest positive integer that is divisible by both values.


Output
======

Value
   Standard integer output.

