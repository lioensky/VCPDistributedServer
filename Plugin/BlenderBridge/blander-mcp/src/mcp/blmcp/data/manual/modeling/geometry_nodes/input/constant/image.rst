.. index:: Geometry Nodes; Image
.. _bpy.types.GeometryNodeInputImage:

**********
Image Node
**********

.. figure:: /images/node-types_GeometryNodeInputImage.webp
   :align: right
   :width: 300px

   Image node.

The *Image* node provides access to a image file which allows you to
conveniently enter and switch images for multiple nodes in the tree.

.. seealso::

   :doc:`/modeling/geometry_nodes/input/scene/image_info`


Inputs
======

This node has no inputs.


Properties
==========

Image Data-Block
   The :ref:`data-block selector <ui-data-block>` to select an existing image or open an image from the file browser.


Outputs
=======

Image
   The image file chosen from the data-block selector.
