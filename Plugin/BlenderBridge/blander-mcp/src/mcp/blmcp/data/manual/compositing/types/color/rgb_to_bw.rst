.. index:: Compositor Nodes; RGB TO BW
.. _bpy.types.CompositorNodeRGBToBW:
.. Editor's Note: This page gets copied into:
.. - :doc:`</render/shader_nodes/color/rgb_to_bw>`
.. - :doc:`</editors/texture_node/types/converter/rgb_to_bw>`

.. --- copy below this line ---

**************
RGB to BW Node
**************

.. figure:: /images/node-types_CompositorNodeRGBToBW.webp
   :align: right
   :alt: RGB to BW Node.

The *RGB to BW Node* makes a color image black-and-white by outputting its luminance.

.. note::

   You can directly connect Color sockets to Value sockets in node graphs,
   which also converts the image to black-and-white. As such, this node is
   not always necessary.

Inputs
======

Image
   Color image input.


Outputs
=======

Value
   Grayscale value output.

.. (TODO add) examples of why this might be useful
