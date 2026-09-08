.. index:: Geometry Nodes; Slice String
.. _bpy.types.FunctionNodeSliceString:

*****************
Slice String Node
*****************

.. figure:: /images/node-types_FunctionNodeSliceString.webp
   :align: center
   :alt: Slice String node.

The *Slice String* node extracts a string segment from a larger string.


Inputs
======

String
   String value to be sliced.

Position
   Integer value used to determine the starting point of the new string within the input string.
   The first letter of the string is at index 0.

Length
   Integer value used to determine how many characters are extracted from the input string.


Outputs
=======

String
   String value of the extracted substring.
