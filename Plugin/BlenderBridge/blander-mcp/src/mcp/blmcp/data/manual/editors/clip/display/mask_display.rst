
************
Mask Display
************

This popover controls how masks are displayed in Mask mode.

.. _bpy.types.SpaceClipEditor.show_mask_spline:

Spline
   Toggles the display of the mask splines. Note that if they're hidden,
   you won't be able to edit them.

   .. _bpy.types.SpaceClipEditor.mask_display_type:

   Edge Display Type
      Line style of the splines.

.. _bpy.types.SpaceClipEditor.show_mask_overlay:

Overlay
   Visualizes masks by shading the whole clip.

   .. _bpy.types.SpaceClipEditor.mask_overlay_mode:

   Overlay Mode
      :Alpha Channel:
         Displays just the masks as a grayscale image. Excluded areas are black,
         while included areas are white.
      :Combined:
         Displays the clip with excluded areas darkened.

.. _bpy.types.SpaceClipEditor.blend_factor:

Blending Factor
   How much excluded areas are darkened when using the "Combined" *Overlay Mode*.
