.. _bpy.types.ShaderNodeClamp:
.. Editor's Note: This page gets copied into:
.. - :doc:`</compositing/types/utilities/clamp>`
.. - :doc:`</modeling/geometry_nodes/utilities/clamp>`
.. --- copy below this line ---

**********
Clamp Node
**********

.. figure:: /images/node-types_ShaderNodeClamp.webp
   :align: right
   :alt: Clamp Node.

The *Clamp* node clamps a value between a minimum and a maximum.


Inputs
======

Value
   The input value to be clamped.
Min
   The minimum value.
Max
   The maximum value.


Properties
==========

Clamp Type
   Method to clamp.

   :Min Max:
      Constrain values between Min and Max. When Min is greater than Max,
      Result always outputs Max, irrespective of the input value.
   :Range:
      Constrain values between Min and Max. When Min is greater than Max,
      constrain between Max and Min instead.


Outputs
=======

Result
   The input value after clamping.


Examples
========

The *Voronoi Texture* node outputs a value whose minimum is zero.
We can use the *Clamp* node to clamp this value such that the minimum is 0.2.

.. figure:: /images/render_shader-nodes_converter_clamp_example.jpg

   Example of Clamp node.
