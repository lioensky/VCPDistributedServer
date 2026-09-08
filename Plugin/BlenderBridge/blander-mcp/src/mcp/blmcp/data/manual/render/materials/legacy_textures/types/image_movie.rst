.. _bpy.types.ImageTexture:

**************
Image or Movie
**************

The term *Image Texture* simply means that a graphic image,
which is a pixel grid composed of R, G, B, and sometimes Alpha values.
It is used as the input source to the texture.
As with other types of textures, this information can be used in a number of ways,
not only as a simple "decal".

*Video textures* are a some kind of Image textures and
based on movie file or sequence of successive numbered separate images.
They are added in the same way that image textures are.

When the Texture Type *Image or Movie* is selected, three new panels present
themselves allowing to control most aspects of how image textures are applied:
*Image*, *Image Sampling*, and *Image Mapping*.


About Image-Based Texturing
===========================

Texture images take up precious memory space,
often being loaded into a special video memory bank that is very fast and very expensive,
so it is often very small. So, keep the images as small as possible.
A 64×64 image takes up only one fourth the memory of a 128×128 image.

For photorealistic rendering of objects in animations, often larger image textures are used,
because the object might be zoomed in on in camera moves. In general, you want to use
a texture sized proportionally to the number of pixels that it will occupy in the final render.
Ultimately, you only have a certain amount of physical RAM to hold an image texture and
the model and to provide workspace when rendering your image.

For the most efficient memory usage, image textures should be square, with dimensions as powers of 2,
such as 32×32, 64×64, 128×128, 256×256, 1024×1024, 2048×2048, and 4096×4096.

If you can reuse images across different meshes, this greatly reduces memory requirements.
You can reuse images if you map those areas of the meshes that "look alike" to a layout that
uses the common image.

When using file textures, it is very important that you have
:doc:`Mapped the UVs </modeling/meshes/uv/unwrapping/index>`
of the mesh, and they are laid out appropriately.

You do not have to UV map the *entire* mesh.
The sphere above on the left has some faces mapped,
but other faces use procedural materials and textures.
Only use UV textures for those portions of your mesh where you want very graphic,
precise detail. For example,
a model of a vase only needs UV texture for the rim where decorative artwork is incorporated.
A throw pillow does not need a different image for the back as the front;
in fact many throw pillows have a fabric (procedural material) back.

As another example, you should UV map both eyes of a head to the same image
(unless you want one bloodshot and the other clear).
Mapping both sides of a face to the same image might not be advisable,
because the location of freckles and skin defects are not symmetrical.
You could of course change the UV map for one side of the face to slightly offset,
but it might be noticeable.
Ears are another example where images or section of an image can be mapped to similar faces.


Options
=======

Image
   The Image :ref:`ui-data-block`.


.. _bpy.types.ImageTexture.use_alpha:

Alpha
-----

Use the alpha channel information stored in the image.
Where the alpha value in the image is less than 1.0,
the object will be partially transparent and things behind it will be visible.
Works with :ref:`image formats <files-media-image_formats>` that store transparency information.

.. _bpy.types.ImageTexture.use_calculate_alpha:

Calculate
   Calculate an alpha based on the RGB values of the Image.
   Black (0, 0, 0) is transparent, white (1, 1, 1) opaque.
   Enable this option if the image texture is a mask.
   Note that mask images can use shades of gray that result in semi-transparency,
   like ghosts, flames, and smoke/fog.

   .. list-table:: The image with various alpha and gray-scale values.

      * - .. figure:: /images/render_materials_legacy-textures_types_image-movie_alpha-use.png
             :width: 320px

             Image with *Use* alpha. The alpha values of the pixels are evaluated.

        - .. figure:: /images/render_materials_legacy-textures_types_image-movie_alpha-calculate.png
             :width: 320px

             Image with *Calculate* alpha only, *Use Alpha* in the *Image* panel is disabled.

.. _bpy.types.ImageTexture.invert_alpha:

Invert
   Reverses the alpha value.
   Use this option if the mask image has white where you want it transparent and vice versa.


Mapping
-------

.. figure:: /images/render_materials_legacy-textures_types_image-movie_image-mapping-panel.png

   Image Mapping panel.

In the *Mapping* panel,
you can control how the image is mapped or projected onto the 3D model.

.. _bpy.types.ImageTexture.use_flip_axis:

Flip Axes
   Rotates the image 90 degrees counterclockwise when rendered.

.. _bpy.types.ImageTexture.extension:

Extension
   How the image is extrapolated beyond its original bounds.

   :Extend:
      Outside the image the colors of the edges are extended.
   :Clip:
      Clip to image size and set exterior pixels as transparent.
      Outside the image, an alpha value of 0.0 is returned.
      This allows you to 'paste' a small logo on a large object.
   :Clip Cube:
      Clips to cubic-shaped area around the images and sets exterior pixels as transparent.
      The same as Clip, but now the 'Z' coordinate is calculated as well.
      An alpha value of 0.0 is returned outside a cube-shaped area around the image.
   :Repeat:
      The image is repeated horizontally and vertically.

      Repeat X, Y
         X/Y repetition multiplier.
      Mirror X, Y
         Mirror on X/Y axes. These buttons allow you to map the texture as a mirror, or automatic flip of the image,
         in the corresponding X and/or Y direction.
   :Checker:
      Checkerboards quickly made.
      You can use the option *size* on the *Mapping* panel as well to create the desired number of checkers.

      Tiles Even/Odd
         Set even/odd tiles.
      Distance
         Governs the distance between the checkers in parts of the texture size.


Crop
^^^^

Minimum X, Y / Maximum X, Y
   The offset and the size of the texture in relation to the texture space.
   Pixels outside this space are ignored.
   Use these to crop, or choose a portion of a larger image to use as the texture.


Sampling
--------

In the *Sampling* panel you can control how the information is retrieved from the image.

.. figure:: /images/render_materials_legacy-textures_types_image-movie_image-sampling-panel.png

   Image Sampling panel.

.. _bpy.types.ImageTexture.use_interpolation:

Interpolation
   This option interpolates the pixels of an image.
   This becomes visible when you enlarge the picture. By default, this option is on.
   Turn this option off to keep the individual pixels visible and if they are correctly anti-aliased.
   This last feature is useful for regular patterns, such as lines and tiles;
   they remain 'sharp' even when enlarged considerably.
   Turn this image off if you are using digital photos to preserve crispness.

   .. list-table::

      * - .. figure:: /images/render_materials_legacy-textures_types_image-movie_interpolation-off.png
             :width: 320px

             Enlarged Image texture without *Interpolation*.

        - .. figure:: /images/render_materials_legacy-textures_types_image-movie_interpolation-on.png
             :width: 320px

             Enlarged Image texture with *Interpolation*.

.. _bpy.types.ImageTexture.filter_size:

Size
   Multiply the filter size used by interpolation.
   If you notice gray lines or outlines around the textured object, particularly where the image is transparent,
   turn this value down from 1.0 to 0.1 or so.
