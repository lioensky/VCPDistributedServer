.. _bpy.types.ShaderNodeTexEnvironment:

************************
Environment Texture Node
************************

.. figure:: /images/node-types_ShaderNodeTexEnvironment.webp
   :align: right
   :alt: Environment Texture Node.

The Node *Environmental Texture* is used to light your scene using an environment map image file as a texture.


Inputs
======

Vector
   Texture coordinate for texture look-up. If this socket is left unconnected,
   the image is mapped as environment with the Z axis as up.


Properties
==========

Image
   Image data-block used as the image source.
   Additional settings can be found in :menuselection:`Sidebar --> Item --> Properties`:
   These include options to control the alpha channel along with addition options for the color space.
   These addition options are documented with the rest of
   :ref:`Common Image Settings <editors-image-image-settings-common>`.
Color Space
   Type of data that the image contains, either Color or Non-Color Data.
   For most color textures the default of Color should be used, but in case of e.g. a bump or alpha map,
   the pixel values should be interpreted as Non-Color Data, to avoid doing any unwanted color space conversions.

   The list of color spaces depends on the active :ref:`OCIO config <ocio-config>`.
   The default supported color spaces are described in detail here:
   :ref:`Default OpenColorIO Configuration <ocio-config-default-color-spaces>`

Texture Interpolation
   Interpolation method used for the environment texture. The following interpolations are available:

   .. same as in the Image Texture node

   :Linear: Regular quality interpolation.
   :Closest: No interpolation, use closest pixel.
   :Cubic: Smoother, better quality interpolation.
   :Smart: Bicubic when magnifying, otherwise Bilinear is used.
      This is only available for :doc:`OSL </render/cycles/osl/index>`.

Projection Method
   Allows you to use different types of environmental maps. The following methods are supported:

   :Equirectangular: Projection from an Equirectangular photo.
   :Mirror Ball: Projection from an orthographic photo or mirror ball.


Outputs
=======

Color
   RGB color from the image.


Examples
========

.. figure:: /images/render_shader-nodes_textures_environment_example.jpg
   :width: 200px

   HDR image from `OpenFootage.net <https://www.openfootage.net/?p=986>`__.
