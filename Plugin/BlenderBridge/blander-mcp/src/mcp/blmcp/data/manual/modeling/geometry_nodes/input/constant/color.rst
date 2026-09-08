.. index:: Geometry Nodes; Color
.. _bpy.types.FunctionNodeInputColor:

**********
Color Node
**********

.. figure:: /images/node-types_FunctionNodeInputColor.webp
   :align: right
   :alt: Color node.

The *Color* node outputs the color value chosen with the color picker widget.

.. tip::

   Dragging colors from a color picker button into a node editor creates a Color node.
   Alpha values are preserved, if the source color has no alpha, a value of 1.0 is used.


Inputs
======

This node has no inputs.


Outputs
=======

Color
   Color value indicated by the color picker widget.


Example
=======

.. figure:: /images/modeling_geometry-nodes_color_node_example.png

   Color converted into a vector by interpreting RGB as XYZ values.
