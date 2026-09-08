
*******
Brushes
*******

Brush Types
===========

See :ref:`Brush Type <sculpt-tool-settings-brush-type>`.

Available brush types are listed here, together with brushes from the
*Essentials* asset library using them.


Draw
   Brushes: Paint Hard, Paint Soft, Paint Hard Pressure, Paint Soft Pressure,
   Erase Hard, Erase Soft, Erase Hard Pressure, Erase Pixel Art, Paint Pixel Art.

   The normal brush, draws a swath of color.


Soften
   Brushes: Blur

   Uses a "blur effect" to soften or sharpen the image.

   Direction
      Soften
         Is used to paint a blur effect.

         Kernel Radius (2D only)
            Blur radius in pixels.
      Sharpen
         The Sharpen tool enhances the contrast of the image as you paint over it.

         Sharp Threshold
            The Threshold will only apply sharpening to only those pixels that
            differ more than the threshold value from their surrounding pixels.
         Kernel Radius (2D only)
            The kernel size controls how big an area the tool searches over is while calculating that difference.
   Blur Mode
      The blur kernel type controls how neighboring pixels are weighted when calculating the blur effect.

      :Gaussian: Gaussian will sample the pixels near the center of the brush most.
      :Box: Box samples all surrounding pixels equally.

Smear
   Brushes: Smear

   When you click, takes the colors under the cursor, and blends them in the direction you move the mouse.
   Similar to the "smudge" tool of *Gimp*.

Clone
   Brushes: Clone

   Copies the colors from the specified image (or location of the same image) to the active image.

   In 3D projective painting the clone cursor can be set with :kbd:`Ctrl-LMB`.
   In 2D painting the clone can be moved dragging it with :kbd:`RMB`.

   Clone from Paint Slot (3D projective only)
      Use another image as clone source, instead of using the 3D cursor position as the source in the same image.

      Source Clone Slot
         This allows you to select an image as a clone source.

   Image (2D only)
      Image used as a clone source.
   Alpha (2D only)
      Opacity of the clone image display.

Fill
   Brushes: Fill

   It can be used to fill large areas of the image with the brush color.
   The tool fills adjacent pixels that have a color value similar to the pixel you clicked on.

   Fill Threshold (2D only)
      Determines how much the color must be similar to the color of pixel you click to be filled.
      A low *Threshold* only fills very similar in color pixels.
      A higher *Threshold* fills pixels within a broader range of color.

   The *Gradient* type of the Color Picker allows the use of a gradient to fill the image.

   To apply the gradient with the *Fill* brush click :kbd:`LMB` and drag to define
   the gradient line, or radius if a radial gradient is used (depending on the *Gradient Fill Mode*).

   Gradient Fill Mode
      Linear, Radial

   .. note:: Overrides

      For projective texturing it will bypass some options for projective painting to paint the model.
      This means that occluded, backfacing and normal culled faces will always get filled,
      regardless of whether the options are activated
      in the :doc:`External </sculpt_paint/texture_paint/tool_settings/options>` panel.

Mask
   Brushes: Mask

   This brush paints gray-scale values on the mask texture
   specified in the :doc:`Mask panel </sculpt_paint/texture_paint/tool_settings/mask>`.
   Any masked surfaces will not be affected by other paint brushes, similar to
   :doc:`sculpt mode masking </sculpt_paint/sculpting/introduction/visibility_masking_face_sets>`.

   Mask Value
      Mask weight, a value of zero means not masked, while one is completely masked.
      Hold :kbd:`Ctrl` to invert the painted mask value.

   .. tip::

      A simpler alternative is to use the face selection mask.
      See :ref:`Face Selection Masking <bpy.types.Mesh.use_paint_mask>` for details.


Brush Assets
============

Pixel Art Brushes
-----------------

Paint Pixel Art
   Brush Type: Draw

   Paint specific pixels (Only supported in the Image Editor).

Erase Pixel Art
   Brush Type: Draw

   Erase pixels in the alpha channel of the texture (Only supported in the Image Editor).
