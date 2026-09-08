.. _bpy.types.SpaceImageOverlay:

**************
Image Overlays
**************

The Overlays pop-over configures the overlays that are displayed on top of images.
In the header, there is a button to turn off all overlays for the Image Editor.
This option also toggles the visibility of :doc:`UDIM </modeling/meshes/uv/workflows/udims>`
tile information.

The options that are visible in the pop-over depend on the Image Editor mode.
The following overlay categories are available:


Geometry
========

Display UVs
   Display selected and active object's UVs.

UV Face Opacity
   Opacity of faces. Useful to differentiate between UV islands. Can also be reduced when
   texture painting to prevent faces from tinting the texture's colors.


Image
=====

Show Metadata
   Displays metadata about the selected Render Result. See the Output tab's
   :doc:`/render/output/properties/metadata` panel to change what metadata to include.


.. _editors-image-overlays-guides:

Guides
======

The following properties are only available when displaying the *Viewer Node* image
in the *Image Editor* set to *View* or *Mask* mode.

.. _bpy.types.SpaceImageOverlay.show_text_info:

Text Info
   Displays overlay text showing information about the active Viewer node:

   - **Render Size**: The resolution of the final render output.
     This is defined in the :ref:`Output Properties <bpy.types.RenderSettings.resolution_x>`.
   - **Image Size**: The resolution of the image currently displayed in the Viewer node.

.. _bpy.types.SpaceImageOverlay.show_render_size:

Render Region
   Displays a border showing the final render region defined in the scene.
   Space outside the render region appear shaded for reference.

   .. _bpy.types.SpaceImageOverlay.passepartout_alpha:

   Passepartout Alpha
      Controls the opacity of the shaded area outside the render region.
      Higher values darken the outside area more, making the render region stand out.
