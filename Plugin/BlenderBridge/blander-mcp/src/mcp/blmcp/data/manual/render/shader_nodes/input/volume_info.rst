.. _bpy.types.ShaderNodeVolumeInfo:

****************
Volume Info Node
****************

.. figure:: /images/node-types_ShaderNodeVolumeInfo.webp
   :align: right
   :alt: Volume Info Node.

The *Volume Info* node provides information about *Smoke Domains*.


Inputs
======

This node has no inputs.


Properties
==========

This node has no properties.


Outputs
=======

Color
   Gives the color of the smoke inside the :doc:`Fluid Domain </physics/fluid/type/domain/index>`.
   The color and vector outputs are the same. The Factor output is an average of the channels.
Density
   Gives a scalar defining the density of any smoke inside
   the :doc:`Fluid Domain </physics/fluid/type/domain/index>`.
Flame
   Gives a scalar defining the density of any fire inside
   the :doc:`Fluid Domain </physics/fluid/type/domain/index>`.
   All three outputs are the same.
Temperature
   Gives a scalar defining the temperature of the volume. Values in the range 0 - 1 map to 0 - 1000 kelvin.
   This may be used to render physically-based fire with the Blackbody or Principled Volume shaders.
   All three outputs are the same.


Example
=======

.. figure:: /images/render_shader-nodes_input_volume-info_example.jpg

   Smoke density.

.. figure:: /images/render_shader-nodes_input_volume-info_example-fire.jpg

   Computing the color of fire using the *Blackbody* node.
   Since the *Blackbody* node expects its input in Kelvin,
   the temperature output has to be remapped first.
