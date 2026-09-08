.. index:: Geometry Nodes; Magic Texture

******************
Magic Texture Node
******************

.. note::

   This node is ported from shader nodes. The manual and images are
   referencing the shader version of the node.
   This node accepts field inputs and outputs.
   When not connected the Vector input has an implicit ``position`` attribute value.

.. figure:: /images/node-types_ShaderNodeTexMagic.webp
   :align: right
   :alt: Magic Texture Node.

The *Magic Texture* node is used to add a psychedelic color texture.


Inputs
======

Vector
   Texture coordinate to sample texture at;
   defaults to Generated texture coordinates if the socket is left unconnected.
Scale
   Scale of the texture.
Distortion
   Amount of distortion.


Properties
==========

Depth
   Number of iterations.


Outputs
=======

Color
   Texture color output.
Factor
   Texture intensity output.


Examples
========

.. figure:: /images/render_shader-nodes_textures_magic_example.jpg
   :width: 200px

   Magic texture: Depth 10, Distortion 2.0.
