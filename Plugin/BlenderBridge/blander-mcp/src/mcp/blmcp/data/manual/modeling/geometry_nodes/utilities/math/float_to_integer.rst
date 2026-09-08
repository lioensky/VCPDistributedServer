.. index:: Geometry Nodes; Float To Integer
.. _bpy.types.FunctionNodeFloatToInt:

*********************
Float To Integer Node
*********************

.. figure:: /images/node-types_FunctionNodeFloatToInt.webp
   :align: right
   :alt: Float To Integer Node.

The *Float To Integer* node takes a single floating point number input and converts it to
an integer with a choice of methods.


Inputs
======

Float
   Standard float value input.


Properties
==========

Rounding Mode
   :Round: Outputs the closest integer to Float, rounding either up or down based on the value.
   :Floor: Outputs the closest integer less than Float, always rounding down.
   :Ceiling: Outputs the closest integer greater than Float, always rounding up.
   :Truncate: Outputs the closest integer between Float and zero. For positive numbers, acts like Floor.
              For negative numbers, acts as Ceiling.


Output
======

Result
   Standard integer output.


Examples
========

+--------------+---------+---------+-----------+------------+
| Input Value  |  Round  |  Floor  |  Ceiling  |  Truncate  |
+==============+=========+=========+===========+============+
|  -69.6574    |   -70   |   -70   |    -69    |    -69     |
+--------------+---------+---------+-----------+------------+
|   -3.14159   |   -3    |   -4    |    -3     |    -3      |
+--------------+---------+---------+-----------+------------+
|   -1.5       |   -2    |   -2    |    -1     |    -1      |
+--------------+---------+---------+-----------+------------+
+--------------+---------+---------+-----------+------------+
|    1.5       |    2    |    1    |     2     |     1      |
+--------------+---------+---------+-----------+------------+
|    3.14159   |    3    |    3    |     4     |     3      |
+--------------+---------+---------+-----------+------------+
|   69.6574    |    70   |    69   |     70    |     69     |
+--------------+---------+---------+-----------+------------+
