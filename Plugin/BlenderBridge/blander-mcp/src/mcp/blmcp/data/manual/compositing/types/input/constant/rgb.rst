.. index:: Compositor Nodes; Color
.. _bpy.types.CompositorNodeRGB:
.. Editor's Note: This page gets copied into :doc:`</render/cycles/nodes/types/input/rgb>`

.. --- copy below this line ---

**********
Color Node
**********

.. figure:: /images/node-types_CompositorNodeRGB.webp
   :align: right
   :alt: Color Node.

The *Color* node outputs the color value chosen with the color picker widget.

.. tip::

   Dragging colors from a color picker button into a node editor creates a Color node.
   Alpha values are preserved, if the source color has no alpha, a value of 1.0 is used.


Inputs
======

This node has no input sockets.


Properties
==========

The Color node uses the :ref:`color picker widget <ui-color-picker>`.


Outputs
=======

Color
   Outputs the chosen color as a single constant value.
