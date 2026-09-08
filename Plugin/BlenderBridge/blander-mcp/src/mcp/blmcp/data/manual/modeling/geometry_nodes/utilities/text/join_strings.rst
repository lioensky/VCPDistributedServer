.. index:: Geometry Nodes; Join Strings
.. _bpy.types.GeometryNodeStringJoin:

*****************
Join Strings Node
*****************

.. figure:: /images/node-types_GeometryNodeStringJoin.webp
   :align: center
   :alt: Join Strings node.

The *Join Strings* node combines any number of input strings into the output string.
The order of the result depends on the vertical ordering of the inputs in the multi-input socket.

.. tip::

   This node can be used to create a multi-line string for
   the :doc:`/modeling/geometry_nodes/utilities/text/string_to_curves`,
   when combined with the line break output from
   the :doc:`/modeling/geometry_nodes/utilities/text/special_characters`.


Inputs
======

Delimiter
   String value to place between each concatenated string.

Strings
   Multiple string values to be combined in connection order.


Outputs
=======

String
   String result of the concatenation.
