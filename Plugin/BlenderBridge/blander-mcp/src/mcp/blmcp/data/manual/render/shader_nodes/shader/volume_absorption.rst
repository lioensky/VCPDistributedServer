.. _bpy.types.ShaderNodeVolumeAbsorption:

*****************
Volume Absorption
*****************

.. figure:: /images/node-types_ShaderNodeVolumeAbsorption.webp
   :align: right
   :alt: Volume Absorption node.

The *Volume Absorption* node allows light to be absorbed as it passes through the volume.
Typical usage for this node would be water and colored glass.


Inputs
======

Color
   Color of the volume.
Density
   The density of the absorption effect.


Properties
==========

This node has no properties.


Outputs
=======

Volume
   The Volume Shader output must be plugged into the *Volume Input*
   of the :doc:`Material </render/shader_nodes/output/material>`
   or :doc:`World </render/shader_nodes/output/world>` Output node.


Examples
========

.. figure:: /images/render_shader-nodes_shader_volume-absorption_example.png

   Example of Volume Absorption.
