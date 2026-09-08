.. index:: Geometry Nodes; Boolean Math
.. _bpy.types.FunctionNodeBooleanMath:

*****************
Boolean Math Node
*****************

.. figure:: /images/node-types_FunctionNodeBooleanMath.webp
   :align: right
   :alt: Boolean Math Node.

The *Boolean Math* node performs a basic logical operation on its inputs.


Inputs
======

Boolean
   Two standard Boolean inputs.


Properties
==========

Mode
   :And:
      True when both inputs are true.
      (`AND <https://en.wikipedia.org/wiki/AND_gate>`__)
   :Or:
      True when at least one input is true.
      (`OR <https://en.wikipedia.org/wiki/OR_gate>`__)
   :Not:
      Opposite of the input.
      (`NOT <https://en.wikipedia.org/wiki/NOT_gate>`__)
   :Not And:
      (True when at least one input is false.
      `NAND <https://en.wikipedia.org/wiki/NAND_gate>`__)
   :Nor:
      True when both inputs are false.
      (`NOR <https://en.wikipedia.org/wiki/NOR_gate>`__)
   :Equal:
      True when both inputs are equal. Also known as "exclusive nor".
      (`XNOR <https://en.wikipedia.org/wiki/XNOR_gate>`__)
   :Not Equal:
      (`XOR <https://en.wikipedia.org/wiki/XOR_gate>`__)
      True when both inputs are different. Also known as "exclusive or".
   :Imply:
      True unless the first input is true and the second is false.
      (`IMPLY <https://en.wikipedia.org/wiki/IMPLY_gate>`__)
   :Subtract:
      True when the first input is true and the second is false. Also known as ""not imply".
      (`NIMPLY <https://en.wikipedia.org/wiki/NIMPLY_gate>`__)


Output
======

Boolean
   Standard Boolean output.
