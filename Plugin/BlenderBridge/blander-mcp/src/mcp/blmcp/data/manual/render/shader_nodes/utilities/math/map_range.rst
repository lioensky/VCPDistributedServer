.. _bpy.types.ShaderNodeMapRange:
.. Editor's Note: This page gets copied into:

.. - :doc:`</compositing/types/utilities/map_range>`
.. - :doc:`</modeling/geometry_nodes/utilities/math/map_range>`
.. --- copy below this line ---

**************
Map Range Node
**************

.. figure:: /images/node-types_ShaderNodeMapRange.webp
   :align: right
   :alt: Map Range Node.

The *Map Range* node remaps a value from a range to a target range.


Inputs
======

Value/Vector
   The input value or vector to be remapped.
From Min
   The lower bound of the range to remap from.
From Max
   The higher bound of the range to remap from.
To Min
   The lower bound of the target range.
To Max
   The higher bound of the target range.
Steps
   The number of values allowed between *To Min* and *To Max* when using *Stepped Linear* interpolation.
   A higher value will give a smoother interpolation while lower values will progressively quantize the input.


Properties
==========

Data Type
   Map Range supports both Float and Vector data types. Changing the data type will
   also update the sockets to reflect the data type chosen.

Interpolation Type
   The mathematical method used to transition between gaps in the numerical inputs.

   :Linear: Linear interpolation between From Min and From Max values.
   :Stepped Linear: Stepped linear interpolation between From Min and From Max values.
   :Smooth Step: Smooth Hermite edge interpolation between From Min and From Max values.
   :Smoother Step: Smoother Hermite edge interpolation between From Min and From Max values.

Clamp
   If enabled, the output is clamped to the target range.


Outputs
=======

Result/Vector
   The input value after remapping.


Examples
========

The *Noise Texture* node outputs a value in the range [0, 1].
We can use the *Map Range* node to remap this value into the range [-1, 1].

.. figure:: /images/render_shader-nodes_converter_map-range_example.jpg

   Example of Map Range node.
