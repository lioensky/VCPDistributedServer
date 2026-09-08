.. _bpy.types.ShaderNodeTexChecker:
.. --- copy below this line ---

********************
Checker Texture Node
********************

.. figure:: /images/node-types_ShaderNodeTexChecker.webp
   :align: right
   :alt: Checker Texture Node.

The *Checker Texture* is used to add a checkerboard texture.


Inputs
======

Vector
   Texture coordinate to sample texture at;
   defaults to Generated texture coordinates if the socket is left unconnected.

   .. warning::

      This node can have precision issues with some vector inputs.
      See the notes for the :doc:`White Noise Texture </render/shader_nodes/textures/white_noise>`
      for ways to mitigate this issue.

Color1, Color 2
   Color of the checkers.
Scale
   Overall texture scale. The scale is a factor of the bounding box of the face divided by the scale.
   For example, a scale of 15 will result in 15 alternate patterns over the overall UV bounding box.
   Different patterns could be achieved using other nodes to give different input patterns to this socket.
   For example, using the Math Node.


Properties
==========

This node has no properties.


Outputs
=======

Color
   Texture color output.
Factor
   Checker 1 mask (1 = Checker 1).


Examples
========

.. figure:: /images/render_shader-nodes_textures_checker_example.jpg
   :width: 200px

   Default Checker texture.
