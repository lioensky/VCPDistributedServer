
*****
Pinch
*****

.. reference::

   :Mode:      Edit Mode
   :Tool:      :menuselection:`Toolbar --> Pinch`

The Pinch tool moves UVs toward the brush's center.
The pinch tool can be inverted by pressing :kbd:`Ctrl-LMB`.


Tool Settings
=============

Size
   This option controls the radius of the brush, measured in pixels.
   :kbd:`F` allows you to change the brush size interactively by dragging the mouse and then :kbd:`LMB`.
   Typing a number then enter while using :kbd:`F` allows you to enter the size numerically.

Strength
   Controls how much each application of the brush affects the UVs.
   You can change the brush strength interactively by pressing :kbd:`Shift-F`
   in the 3D Viewport and then moving the brush and then :kbd:`LMB`.
   You can enter the size numerically also while in :kbd:`Shift-F` sizing.

Falloff
   The Falloff allows you to control the *Strength* falloff of the brush.
   The falloff is mapped from the center of the brush (left part of the curve)
   towards its borders (right part of the curve).
   Changing the shape of the curve will make the brush softer or harder.
   Read more about using the :ref:`ui-curve-widget`.

   Curve Preset
      :Custom:
         You can choose how the strength of the falloff is determined from the center of the brush
         to the borders by manually manipulating the control points within the curve widget.
         There are also a couple of preset custom curves displayed at the bottom of the curve widget
         that can be used on their own or as a starting point for tweaking.

         .. list-table:: Custom Preset types.

            * - .. figure:: /images/sculpt-paint_brush_falloff_custom-smooth.png

                  Smooth.

              - .. figure:: /images/sculpt-paint_brush_falloff_custom-sphere.png

                  Sphere.

              - .. figure:: /images/sculpt-paint_brush_falloff_custom-root.png

                  Root.

            * - .. figure:: /images/sculpt-paint_brush_falloff_custom-sharp.png

                  Sharp.

              - .. figure:: /images/sculpt-paint_brush_falloff_custom-linear.png

                  Linear.

              - .. figure:: /images/sculpt-paint_brush_falloff_custom-constant.png

                  Constant.

      :Smooth:
         The center strength, the border strength, and the falloff transition between them are evenly distributed.
      :Smoother:
         Similar to *Smooth* but produces a wider center point of the brush before tapering off.
      :Sphere:
         The strength of the brush is predominately at its strongest point
         with a steep falloff near the border of the brush.
      :Root:
         Similar to a Sphere but the center is a more concentrated point.
      :Sharp:
         The center of the brush is the strongest point
         then exponentially tapers off to a lower strength, creating a fine point.
      :Linear:
         With the center being the strongest,
         the strength will consistently weaken as it reaches the border of the brush.
      :Sharper:
         Similar to *Sharp* but the center point is more condensed.
      :Inverse Square:
         A hybrid between *Smooth* and *Sphere*.
      :Constant:
         The strength of the brush remains unified across the entire brush.
         This will create a sharp edge at the border of the brush.

Options
   Lock Borders
      Locks the boundary of UV islands from being affected by the brush.
      This is useful to preserve the shape of UV islands.
   Sculpt All Islands
      To edit all islands and not only the island nearest to the brush center
      when the sculpt stroke was started.
