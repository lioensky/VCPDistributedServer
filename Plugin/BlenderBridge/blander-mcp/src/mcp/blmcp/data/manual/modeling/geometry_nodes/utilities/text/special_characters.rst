.. index:: Geometry Nodes; Special Characters
.. _bpy.types.FunctionNodeInputSpecialCharacters:

***********************
Special Characters Node
***********************


.. figure:: /images/node-types_FunctionNodeInputSpecialCharacters.webp
   :align: center
   :alt: Special Characters node.

The *Special Characters* node is used to output string characters that can't be typed directly with the keyboard.

.. tip::

   This node can be used to create a multi-line string for
   the :doc:`/modeling/geometry_nodes/utilities/text/string_to_curves`,
   when combined with the :doc:`/modeling/geometry_nodes/utilities/text/join_strings`
   or the :doc:`/modeling/geometry_nodes/utilities/text/replace_string`.


Inputs
======

This node has no inputs.


Outputs
=======

Line Break
   A new line character (escape character ``\n``).

Tab
   A tab character used to add an indentation in the output.
