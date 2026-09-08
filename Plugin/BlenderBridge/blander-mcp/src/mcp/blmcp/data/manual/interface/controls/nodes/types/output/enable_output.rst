.. _bpy.types.NodeEnableOutput:
.. --- copy below this line ---

******************
Enable Output Node
******************

.. figure:: /images/node-types_NodeEnableOutput.webp
   :align: right
   :alt: Enable Output Node

The *Enable Output* node toggles the visibility and value
of a socket for a :doc:`Node Group </interface/controls/nodes/groups>` outputs.
It can be used to conditionally show or hide outputs from a node group depending on an input value or condition.


Inputs
======

Enable
   A boolean field controlling whether the connected output socket is visible and active.
   When *False*, the corresponding output socket in the group is hidden.
Value
   The value to pass to the output when it is enabled.
   This input can be any supported data type depending on the node's *Data Type* property.


Properties
==========

Data Type
   The data type of the *Value* input and *Value* output.
   This determines what kind of data the node passes through (e.g. *Float*, *Vector*, *Color*, *Geometry*, etc.).


Outputs
=======

Value
   The same data as the *Value* input when *Enable* is *True*.
   When *Enable* is *False*, the output is disabled and not available to the group output.
