.. _bpy.types.ImagePaint.mode:
.. _bpy.types.ImagePaint.interpolation:

*************
Texture Slots
*************

.. figure:: /images/sculpt-paint_texture-paint_tool-settings_texture-slots_panel.png
   :align: right

   Texture Slots settings.

The combination of images associated with UV maps is called "slots".

Selecting a *Paint Slots* or *Canvas Image*
will also display the corresponding image in the Image Editor.

Mode
   The slot system includes two painting modes:

   Material
      This mode tries to detect the slots from the materials of the mesh.

      For the Cycles renderer, all textures (*Image Texture* node) in the material's node tree
      are added in the slots tab.

      Active Paint Texture Index
         A :ref:`List view <ui-list-view>` of slots.
         Activate a certain slot to use it for painting by :kbd:`LMB` click on it.

   Single Image
      You can just select an existing image and painting will use the active UV layer for painting.

      Image
         Allows you to select the image used as a canvas.

         New
            Create a new image.
      UV Map
         Allows you to select the UV layer for painting.
         (Same as the currently active UV map in the mesh's *UV Maps* panel.)
      Texture Filter Type
         Set the interpolation mode of the texture. This can be Linear or Closest.

Save All Images
   Repack (or save if external file) all edited images.
   Same as in the :doc:`Image Editor </editors/image/introduction>`.

.. _bpy.ops.paint.add_simple_uvs:

Add Simple UVs
   The *Add Simple UVs* does a simple cube unwrap followed by a pack operation.
   It's still recommended to make a custom unwrap.

   This operator is available when the object does not already have a UV Map.
