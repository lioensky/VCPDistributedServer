.. index:: Geometry Nodes; String to Value
.. _bpy.types.FunctionNodeStringToValue:

********************
String to Value Node
********************

.. figure:: /images/node-types_FunctionNodeStringToValue.webp
   :align: center
   :alt: String to Value Node

The *String to Value* node converts a text string into a numerical value.
This is useful for parsing numbers from text input, file data, or dynamically generated strings.

The node reads characters from the beginning of the string until a valid number is parsed.
If parsing is unsuccessful, the node outputs a floating-point value of 0.


Inputs
======

String
   The input text string to be converted into a numerical value.


Properties
==========

Data Type
   The type of numerical value to convert to:

   :Float: Converts the text to a floating-point number.
   :Integer: Converts the text to a 32-bit integer.


Outputs
=======

Value
   The resulting numerical value after conversion.

Length
   The number of characters successfully parsed as part of the number.
   This indicates where the numeric portion of the string ends, allowing further substring operations.


Examples
========

- Converting the string ``"3.1415"`` with *Float* selected outputs a value of ``3.1415`` and a length of ``6``.
- Converting ``"42abc"`` with *Integer* selected outputs ``42`` and a length of ``2``.
- Converting an invalid string such as ``"hello"`` outputs ``0`` and a length of ``0``.
