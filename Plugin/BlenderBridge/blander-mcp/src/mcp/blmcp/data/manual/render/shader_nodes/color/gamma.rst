.. _bpy.types.ShaderNodeGamma:
.. Editor's Note: The rest of the page gets copied into:
.. - :doc:`</compositing/types/color/adjust/gamma`
.. --- copy below this line ---

**********
Gamma Node
**********

.. figure:: /images/node-types_ShaderNodeGamma.webp
   :align: right
   :alt: Gamma Node.

Use this node to apply a gamma correction. The node is typically used to convert from gamma encoded to linear
color space, or in the reverse direction with 1/gamma.

Inputs
======

Color
   Standard color input.
Gamma
   An exponential brightness factor, applied as :math:`output\_value = input\_value ^ {\gamma}`


Outputs
=======

Color
   Standard color output.


Examples
========

.. figure:: /images/compositing_types_color_gamma_example.jpg
   :width: 700px

   Example of a Gamma node.
