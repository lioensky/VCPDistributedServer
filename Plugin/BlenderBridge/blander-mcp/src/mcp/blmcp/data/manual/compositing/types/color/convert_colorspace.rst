.. index:: Compositor Nodes; Color Space
.. _bpy.types.CompositorNodeConvertColorSpace:

***********************
Convert Colorspace Node
***********************

.. figure:: /images/node-types_CompositorNodeConvertColorSpace.webp
   :align: right
   :alt: Color Space Node.

The *Convert Colorspace* node converts images between :term:`color spaces <Color Space>`.

.. note::

    Images are already automatically converted into linear color space unless specified in the image's
    :ref:`Color Space <bpy.types.ColorManagedInputColorspaceSettings.name>` option.


Inputs
======

Image
   Standard color input.


Properties
==========

From, To
   The color space of the input image and the color space to convert it to.

   The list of color spaces depends on the active :ref:`OCIO config <ocio-config>`.
   The default supported color spaces are described in detail here:
   :ref:`Default OpenColorIO Configuration <ocio-config-default-color-spaces>`


Outputs
=======

Image
   Standard color output.
