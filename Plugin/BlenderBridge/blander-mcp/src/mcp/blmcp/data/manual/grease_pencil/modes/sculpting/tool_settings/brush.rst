
**************
Brush Settings
**************

.. reference::

   :Mode:      Sculpt Mode
   :Panel:     :menuselection:`Sidebar --> Tool --> Brush Settings`

Radius
   This option controls the radius of the brush, measured in pixels.
   :kbd:`F` allows you to change the brush size interactively by
   dragging the mouse and then :kbd:`LMB` (the texture of the brush should be visible inside the circle).
   Typing a number then enter while using :kbd:`F` allows you to enter the size numerically.

   :bl-icon:`stylus_pressure` (Size Pressure)
      Adjusts the radius based on the stylus pressure when using a :ref:`Graphics Tablet <hardware-tablet>`.

Strength
   Controls how much each application of the brush affects the model.
   For example, higher values cause the *Randomize* brush to add noise to the strokes more quickly,
   and cause the *Smooth* brush to soften the strokes more quickly.

   You can change the brush strength interactively by pressing :kbd:`Shift-F`
   in the 3D Viewport and then moving the brush and then :kbd:`LMB`.
   You can enter the size numerically also while in :kbd:`Shift-F` sizing.

   :bl-icon:`stylus_pressure` (Strength Pressure)
      Adjusts the strength based on the stylus pressure when using a :ref:`Graphics Tablet <hardware-tablet>`.

Use Falloff
   When enabled, use Strength falloff for the brush.
   Brush Strength decays with the distance from the center of the brush.

Sculpt Strokes
   Filters the effect of the brush over the strokes.
   Applies to *Smooth* and *Randomize* brushes only.

   .. note::

      If there is no filter selected *Affect Position* is the default behavior.

   Affect Position
      Toggles the brush effect on the position of the stroke points.

   Affect Strength
      Toggles the brush effect on the strength (alpha) of the stroke points.

   Affect Thickness
      Toggles the brush effect on the thickness of the stroke points.

   Affect UV
      Toggles the brush effect on the UV rotation of the stroke points.

Direction
   The influence direction of the brush. This can be Add or Subtract.


Cursor
======

The cursor can be disabled by toggling the checkbox in the *Cursor* header.

Color
   Set the color of the brush ring. Depending on the current mode there will
   be options to set a single Color or a Color for Adding/Subtracting.
