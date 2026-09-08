.. index:: Geometry Nodes; Find In String
.. _bpy.types.FunctionNodeFindInString:

*******************
Find in String Node
*******************

.. figure:: /images/node-types_FunctionNodeFindInString.webp
   :align: center
   :alt: Find In String node.

The *Find in String* node finds the number of times a substring occurs in a string, and the position of the start of
the first match.

Inputs
======

String
   The input string in which the search will be conducted.

Search
   The substring that will be searched for within the input string.


Outputs
=======

First Found
   The start position of the first occurrence of the substring within the input string.

Count
   The total number of occurrences of the substring within the input string.
