******
Stroke
******

The stroke settings define the behavior of the sculpted/painted stroke.
Any other brush behavior and effect is applied on top of the stroke.

.. figure:: /images/sculpt-paint_brush_stroke_stroke-panel.png

   Stroke panel.

.. _bpy.types.Brush.stroke_method:

Stroke Method :kbd:`Alt-E`
   Defines the way brush strokes are applied to the canvas.

   .. container:: lead

      .. clear

   :Dots:
      Apply paint on each mouse move step. This is regardless of their distance to each other,
      and instead depends on the stroke speed.
      This means that a slower stroke will have more accumulative strength applied.
   :Drag Dot:
      Leaves only one dab on the canvas which can be placed by dragging.
   :Space:
      Creates brush stroke as a series of dots,
      whose distance (spacing) is determined by the *Spacing* setting.

      .. _bpy.types.Brush.spacing:

      Spacing
         Limits brush application to the distance specified by the percentage of the brush radius.

         .. _bpy.types.Brush.use_pressure_spacing:

         :bl-icon:`stylus_pressure` (Spacing Pressure)
            Brush *Spacing* can be affected by enabling the pressure sensitivity icon,
            if you are using a :ref:`Graphics Tablet <hardware-tablet>`.

   :Airbrush:
      Flow of the brush continues as long as the mouse click is held (spray),
      determined by the *Rate* setting.

      .. _bpy.types.Brush.rate:

      Rate
         Interval for how frequent the brush is applied during the stroke.
   :Anchored:
      Creates a single dab at the brush location.
      Clicking and dragging will resize the dab diameter.

      .. _bpy.types.Brush.use_edge_to_edge:

      Edge to Edge
         The brush location and orientation are determined by a two point circle,
         where the first click is one point, and dragging places the second point, opposite from the first.
   :Line:
      Clicking and dragging lets you define a line in screen space.
      The line dabs are separated by *Spacing*, similar to space strokes.
      With :kbd:`Alt` the line stroke is constrained to 45 degree increments.
   :Curve:
      Defines the stroke curve with a Bézier curve (dabs are separated according to *Spacing*).
      This Bézier curve is stored in Blender as a "Paint Curve" data-block.

      Use :kbd:`Ctrl-RMB` to create the initial control point of the curve.

      Paint Curves
         Paint Curves are reusable and can be stored and selected by using the :ref:`ui-data-block` menu.

         .. _bpy.ops.paintcurve.new:

      - **Add Points**
         You can define additional curve control points by using :kbd:`Ctrl-RMB`.
         The handles can be defined by dragging the mouse.
         The stroke flows in the direction of the first control point to the second control point, and so on.
      - **Transforming Points**
         The control points and handles can be dragged with :kbd:`RMB` (In right click select with :kbd:`LMB`).
         To make sure that the handles of a control point are symmetrical,
         drag them using :kbd:`Shift-RMB`.
         A few transform operators are supported such as moving
         (:kbd:`G`), rotating (:kbd:`R`) and scaling (:kbd:`S`).

         .. _bpy.ops.paintcurve.select:

      - **Selection**
         The handles can be selected individually by using :kbd:`LMB` (In right click select with :kbd:`RMB`),
         extend the selection by :kbd:`Shift-LMB` and deselect/select all by using :kbd:`A`.

         .. _bpy.ops.paintcurve.delete_point:

      - **Delete Points** :kbd:`X`
         To delete a curve point, use :kbd:`X`.

      .. _bpy.ops.paintcurve.draw:

      Draw Curve :kbd:`Return`
         To confirm and execute the curved stroke,
         press :kbd:`Return` or use the Draw Curve button.
         Alternativey, :kbd:`Ctrl-LMB` can be used to execute the stroke (In right click select with :kbd:`LMB`).

.. _bpy.types.Brush.use_scene_spacing:

Spacing Distance :guilabel:`Sculpt Mode Only`
   Method used to calculate the distance to generate a new brush step.

   :View:
      Calculates the brush spacing relative to the view.
   :Scene:
      Calculates the brush spacing relative to all three dimensions of the scene using the stroke location.
      This avoids artifacts when sculpting across curved surfaces and keeps the spacing much more consistent.

.. _bpy.types.Brush.use_space_attenuation:

Adjust Strength for Spacing
   Keep the brush strength consistent, even if the spacing changes.
   Available for the *Space*, *Line*, and *Curve* stroke methods.

.. _bpy.types.Brush.dash_ratio:

Dash Ratio
   Ratio of samples in a cycle that the brush is enabled.
   This is useful to create dashed lines in texture paint or stitches in Sculpt Mode.
   Available for the *Space*, *Line*, and *Curve* stroke methods.

.. _bpy.types.Brush.dash_samples:

Dash Length
   Length of a dash cycle measured in stroke samples.
   This is useful to create dashed lines in texture paint or stitches in Sculpt Mode.
   Available for the *Space*, *Line*, and *Curve* stroke methods.

.. _bpy.types.Brush.jitter:

Jitter
   Jitter the position of each step in the brush stroke.

   .. _bpy.types.Brush.use_pressure_jitter:

   :bl-icon:`stylus_pressure` (Jitter Pressure)
      Brush *Jitter* can be affected by enabling the pressure sensitivity icon,
      if you are using a :ref:`Graphics Tablet <hardware-tablet>`.
   :bl-icon:`rightarrow` / :bl-icon:`downarrow_hlt` (Expand/Collapse)
      Show or hide the customizable pressure curve.

      Custom Curve
         By default this is a straight line with positive slope such that
         increased pressure results in more jitter of the brush positions.

         For the curve controls see: :ref:`Curve widget <ui-curve-widget>`.

.. _bpy.types.Brush.jitter_unit:

Jitter Unit
   Controls how the brush *Jitter* is measured.

   :View:
      The *Jitter* is relative to the view direction i.e. "screen space".
   :Scene:
      The *Jitter* is measured relative to all three dimensions of the scene.
      The unit type and scaling can be configured in the :ref:`Scene Units <bpy.types.UnitSettings>`.

.. _bpy.types.Brush.input_samples:

Input Samples
   Recent mouse locations (input samples) are averaged together to smooth brush strokes.

   .. _bpy.types.UnifiedPaintSettings.use_unified_input_samples:

   :bl-icon:`brushes_all` Use Unified Input Samples
      Use the same brush *Input Samples* across all brushes.


.. _bpy.types.Brush.use_smooth_stroke:

Stabilize Stroke
================

*Stabilize Stroke* makes the stroke lag behind the cursor
and creates a smoothed curve to the path of the cursor.
This can be enabled pressing :kbd:`Shift S` or by clicking the checkbox found in the header.

.. _bpy.types.Brush.smooth_stroke_radius:

Radius
   Minimum distance from the last point before the stroke continues.

.. _bpy.types.Brush.smooth_stroke_factor:

Factor
   A smooth factor, where higher values result in smoother strokes but the drawing sensation
   feels like as if you were pulling the stroke.
