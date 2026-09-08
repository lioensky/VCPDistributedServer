.. index:: Compositor Nodes; Posterize
.. _bpy.types.CompositorNodePosterize:

*********
Posterize
*********

.. figure:: /images/node-types_CompositorNodePosterize.webp
   :align: right
   :alt: Posterize Node.

The *Posterize Node* reduces the number of colors in image, converting
smooth gradients into sharp transitions.
This node is useful for generating masks in particular for rotoscoping.


Inputs
======

Image
   Standard color input.
Steps
   The number of colors per channel;
   A value of 8 will result in :math:`8^3 = 512` total colors.


Outputs
=======

Image
   Standard color output.
