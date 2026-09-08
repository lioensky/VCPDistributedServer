
************
Introduction
************

A UV texture is a picture (image, sequence or movie)
that is used to color the surface of a mesh.
The UV texture is mapped to the mesh through one or more UV maps.
There are three ways to establish the image used by the UV texture:

#. Use any image editing program to create an image. In the Image Editor,
   select the UV texture and load the image. Blender will then use
   that texture's UV map to transfer the colors to the faces of the mesh.
#. Paint a flat image in the Image Editor onto the currently selected UV texture,
   using its UV map to transfer the colors to the faces of the mesh.
#. Paint the mesh in the 3D Viewport, and let Blender use
   the currently selected UV map to update the UV texture
   (as discussed below).

Blender features a built-in paint mode called *Texture Paint* which is designed
specifically to help you edit your UV textures and images quickly and
easily in either the Image Editor or the 3D Viewport.
Since a UV texture is just a special-purpose image,
you can also use any external paint program, like GIMP or Krita.

.. figure:: /images/sculpt-paint_texture-paint_introduction_example.png
   :align: right
   :width: 430px

   Texture painting in Blender.

Since a mesh can have layers of UV textures, there may be many images that color the mesh.
However, each UV texture only has one image.

*Texture Paint* works in both a 3D Viewport and the Image Editor.
In the 3D Viewport in Texture Paint Mode, you paint directly on the mesh by projecting onto the UVs.

.. tip:: Memory Optimization

   *Texture Paint* is fast and responsive when working in the 3D Viewport and
   when your image is sized as a square where the side lengths are a power of two,
   e.g. 256×256, 512×512, 1024×1024, etc.


Getting Started
===============

The object to be painted on must first be :doc:`unwrapped </modeling/meshes/uv/unwrapping/introduction>`.
UVs can be added traditionally, with standard :doc:`Unwrapping Tools </modeling/meshes/editing/uv>`,
or by adding :ref:`Simple UVs <bpy.ops.paint.add_simple_uvs>` in Texture Paint mode.

.. note::

   When no UV layers can be detected, Blender will display a warning message.

Once you have unwrapped your model to a UV map, you can begin the texturing process.
To use texture paint you may do any of the following:

- Activate the Texture Paint workspace. Here the 3D Viewport has the Texture Paint Mode enabled
  and the Image Editor is already switched to Paint mode.
- In the 3D Viewport, select Texture Paint Mode from the mode selector in the header,
  and you can paint directly onto the mesh.
- In the Image Editor, switch the mode to Paint (shown in the image to the right).

.. figure:: /images/sculpt-paint_texture-paint_introduction_paint-mode.png
   :align: right

   Enabling Paint mode.

Once you enable Texture Painting, your mouse becomes a brush.
As soon as you enable Texture Painting or switch to Texture Paint Mode,
different tools become available in the Toolbar.

In the Image Editor, you paint on a flat canvas that is wrapped around the mesh using UV coordinates.
Any changes made in the Image Editor show up immediately in the 3D Viewport, and vice versa.

To work with the UV layout (for example, to move coordinates) you must use the :doc:`/editors/uv/index`.

A full complement of brushes and colors can be selected from the Sidebar region in the Image Editor.
Brush changes made in either panel are immediately reflected in the other panel.
However, the modified texture will **not** be saved automatically;
you must explicitly do so with :ref:`Save Image <bpy.ops.image.save>`.


Texture Preview
===============

If your texture is already used to color, bump map, displace, alpha-transparent, etc.,
a surface of a model in your scene (in other technical words,
is mapped to some aspect of a texture via a texture channel using UV as a map input),
you can see the effects of your painting in the context of your scene as you paint.

To do this, set up side-by-side areas, one Area in 3D Viewport set to *Texture* shading option,
and in the second Area the Image Editor loaded with your image.
Position the 3D Viewport to show the object that is UV-mapped to the loaded image.
In the image to the right, the texture being painted is mapped to the "Normal" attribute,
and is called "bump mapping", where the grayscale image is used to make the flat surface appear bumpy.
See Texture Mapping Output for more information on bump mapping.


Saving
======

If the header menu item Image has an asterisk next to it
means that the image has been changed, but not saved.
Use :ref:`Save Image <bpy.ops.image.save>` or :ref:`Save Image As <bpy.ops.image.save_as>`
to save your work with a different name or overwrite the original image.

.. note:: UV Textures

   Since images used as UV textures are functionally different from other images,
   you should keep them in a directory separate from other images.

The image format for saving is independent of the format for rendering.
The format for saving a UV image is selected in the header of the File Browser,
and defaults to ``PNG`` (``.png``).

If Packing is enabled in the File Browser's header, or if you :ref:`manually pack <bpy.ops.image.pack>`,
saving your images to a separate file is not necessary.


Using an External Image Editor
==============================

If you use an external program to edit your UV texture, you must:

#. Run that paint program (GIMP, Krita, etc.).
#. Load the image or create a new one.
#. Change the image.
#. And re-save it within that program.
#. Back in Blender, you reload the image in the Image Editor.

You want to use an external program if you have teams of people using different programs
that are developing the UV textures, or if you want to apply any special effects
that Texture Paint does not feature, or if you are much more familiar with
your favorite paint program.


Known Limitations
=================

UV Overlap
----------

In general overlapping UVs are not supported (as with texture baking).

However, this is only a problem when a single brush stroke paints onto multiple faces
that share a texture.


Perspective View & Faces Behind the View
----------------------------------------

When painting onto a face which is partially behind the view (in perspective mode),
the face cannot be painted on.
To avoid this, zoom out or use an orthographic viewport.


Perspective View & Low Poly
---------------------------

When painting onto a face in perspective mode onto a low-poly object with
normals pointing away from the view, painting may fail; to workaround disable
the :ref:`Normal Falloff <bpy.types.ImagePaint.use_normal_falloff>` option in the stroke settings.

Typically this happens when painting onto the side of a cube
(see `Blender bug #34665 <https://projects.blender.org/blender/blender/issues/34665>`__).
