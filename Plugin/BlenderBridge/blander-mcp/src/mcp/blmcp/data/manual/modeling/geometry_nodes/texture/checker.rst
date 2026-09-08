.. index:: Geometry Nodes; Checker Texture

********************
Checker Texture Node
********************

.. note::

   This node is ported from shader nodes. The manual and images are
   referencing the shader version of the node.
   This node accepts field inputs and outputs.
   When not connected the Vector input has an implicit ``position`` attribute value.

.. tip::

   Texture nodes can produce details at a higher frequency
   than geometry can show. This may cause artifacts such
   as Moiré type patterns or a lack of detail due to
   insufficient sampling points.

.. figure:: /images/node-types_ShaderNodeTexChecker.webp
   :align: right
   :alt: Checker Texture node.

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
   For example, using the Math node.


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
