.. index:: Geometry Nodes; Accumulate Field
.. _bpy.types.GeometryNodeAccumulateField:

*********************
Accumulate Field Node
*********************

.. figure:: /images/node-types_GeometryNodeAccumulateField.webp
   :align: right
   :alt: Accumulate Field Node.

The *Accumulate Field* node counts a running total of its input values, in the order defined
by the geometry's :doc:`indices </modeling/geometry_nodes/geometry/read/input_index>`. The node's essential
operation is just addition, but instead of only outputting the final total, it outputs the current
value at every element.


Inputs
======

Value
   The values to be accumulated.

   .. warning::

      When accumulating integer values, be careful to make sure that there are not
      too many large values. The maximum integer that Blender stores internally is
      around 2 billion. After that, values may wrap around and become negative.
      See `Wikipedia <https://en.wikipedia.org/wiki/Integer_%28computer_science%29>`__
      for more information.

Group Index
   An index used to group values together for multiple separate accumulations.
   This can be thought of as a choice of the "bin" in which to place each value.
   This input has no effect when it is only a single value.


Properties
==========

Data Type
   :Float: The node will accumulate a *Float* field.
   :Integer: The node will accumulate an *Integer* field.
   :Vector: The node will accumulate a *Vector* field.
   :Transform: The node will accumulate a *Matrix* field.

Domain
   The :ref:`attribute domain <attribute-domains>` used for accumulation
   and for evaluation of the *Value* input.


Output
======

Leading
   The running total of values in the corresponding group, starting at the first value.

Trailing
   The running total of values in the corresponding group, starting at zero.

Total
   The total of all the values in the corresponding group.


Examples
========

Table
-----

+-------+-------------+---------+----------+-------+
| Value | Group Index | Leading | Trailing | Total |
+=======+=============+=========+==========+=======+
|   1   |      7      |    1    |     0    |   6   |
+-------+-------------+---------+----------+-------+
|   3   |      7      |    4    |     1    |   6   |
+-------+-------------+---------+----------+-------+
|   2   |      7      |    6    |     4    |   6   |
+-------+-------------+---------+----------+-------+
|   1   |      3      |    1    |     0    |   3   |
+-------+-------------+---------+----------+-------+
|   0   |      3      |    1    |     1    |   3   |
+-------+-------------+---------+----------+-------+
|   2   |      3      |    3    |     1    |   3   |
+-------+-------------+---------+----------+-------+

A few examples of input values and the node's results. One important take-away from this table
is that the specific values for the *Group Input* do not matter; it only matters that the
values are shared between elements.

Stacking Boxes
--------------

.. figure:: /images/modeling_geometry-nodes_utilities_accumulate-field_box-stack.png
   :align: center

Here, the node is used in combination with the :doc:`/modeling/geometry_nodes/utilities/random_value`
to create a stack of randomly scaled boxes. The *Group Index* input is not used, because all boxes
are meant to be in the same stack.

.. figure:: /images/modeling_geometry-nodes_utilities_accumulate-field_box-stack-2.png
   :align: center

A slightly more complicated version of the previous example,
using the *Group Index* input to create three separate stacks.
