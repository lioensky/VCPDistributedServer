.. _bpy.types.ShaderNodeTexIES:

****************
IES Texture Node
****************

.. figure:: /images/node-types_ShaderNodeTexIES.webp
   :align: right
   :alt: Gradient Texture Node.

The *IES Texture* is used to match real world lights based on IES files
(:abbr:`IES (Illuminating Engineering Society of North America)`).
IES files store the directional intensity distribution of light sources.


Inputs
======

Vector
   Texture coordinate for lookup in the light distribution.
   Defaults to the normal.
Strength
   Light strength multiplier.


Properties
==========

Mode
   The location to load the IES file from.

   :Internal: Use IES profile from a file embedded in a text data-block in the blend-file, for easy distribution.
   :External: Load IES profile from a file on the drive.


Outputs
=======

Factor
   Light intensity, typically plugged into the Strength input of an Emission node.


Examples
========

.. figure:: /images/render_shader-nodes_textures_ies_example.jpg

   Lights with different IES profiles.
