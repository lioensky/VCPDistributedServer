.. index:: Compositor Nodes; Exposure
.. _bpy.types.CompositorNodeExposure:

*************
Exposure Node
*************

.. figure:: /images/node-types_CompositorNodeExposure.webp
   :align: right
   :alt: Exposure Node.

The Exposure Node adjusts the brightness of an image using a camera exposure parameter.

.. seealso::

   The exposure can also be adjusted in the scene :ref:`Color Management <render-post-color-management>`.


Inputs
======

Image
   Standard color input.
Exposure
   Scalar factor to adjust the exposure of the image.


Outputs
=======

Image
   Standard color output.


Examples
========

In the example below, the Exposure node is used to increase the brightness of the window area using a mask.

.. figure:: /images/compositing_types_color_exposure_example.png

   Example of an Exposure node.
