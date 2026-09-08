.. _sculpt-paint-brush-display:
.. _bpy.types.Paint.show_brush:

******
Cursor
******

.. reference::

   :Mode:      All Paint Modes
   :Header:    :menuselection:`Tool Settings --> Brush Settings --> Cursor`
   :Panel:     :menuselection:`Sidebar --> Tool --> Brush Settings --> Cursor`

.. figure:: /images/sculpt-paint_brush_cursor_panel.png
   :align: right
   :width: 400px

   Cursor options.

While painting or sculpting a special cursor is shown to display information about the active brush.
The cursor is shown as a circle in the 3D Viewport, the radius of the circle matches the size of the brush.

The cursor can be disabled by toggling the checkbox in the panel's header.

.. _bpy.types.Brush.cursor_color_add:

Cursor Color
   Set the color of the brush ring while performing an add/positive stroke.

.. _bpy.types.Brush.cursor_color_subtract:

Inverse Color
   In some paint/sculpt modes the brush can be negative and subtract information from the paint target;
   these brushes can be given a separate color.

.. _bpy.types.Brush.cursor_overlay_alpha:
.. _bpy.types.Brush.use_cursor_overlay:
.. _bpy.types.Brush.texture_overlay_alpha:
.. _bpy.types.Brush.use_primary_overlay:

Opacity Options
   Depending on the paint or sculpt mode different overlays are shown within the cursor
   to give information on how the brush is textured.
   This is most commonly used to show the brush falloff with a gradient from the circle center to the perimeter.

   Alpha
      You can change the amount of transparency used
      when showing the texture using the slider.
   :bl-icon:`brush_data` Override Overlay
      Allows you to turn off the viewport overlay during strokes.
   :bl-icon:`hide_on` / :bl-icon:`hide_off` Use Cursor Overlay
      Toggles whether to show or hide the given brush texture overlay.
