
************
Draw Brushes
************

.. reference::

   :Mode:      Draw Mode
   :Brush:     :menuselection:`Asset Shelf --> Draw`

The Draw brush allows you to draw free-hand strokes.


.. _grease-pencil-draw-common-options:

Brush Settings
==============

.. figure:: /images/grease-pencil_modes_draw_tools_draw_settings.png
   :width: 275px
   :align: right

Material
   Data-block selector for the :doc:`material </grease_pencil/materials/index>`.

Radius
   The radius of the brush in pixels.

   :kbd:`F` allows you to change the brush size interactively by dragging the pointer or
   by typing a number then confirm.

   :bl-icon:`stylus_pressure` (Size Pressure)
      Adjusts the radius based on the stylus pressure when using a :ref:`Graphics Tablet <hardware-tablet>`.
      The gradient of the pressure can be customized using
      the :doc:`curve widget </interface/controls/templates/curve>`.

Strength
   Control the stroke transparency (alpha).
   From fully transparent (0.0) to fully opaque (1.0).

   You can change the brush strength interactively by pressing :kbd:`Shift-F`
   in the 3D Viewport and then moving the pointer and then :kbd:`LMB`.
   You can also enter the size numerically.

   :bl-icon:`stylus_pressure` (Strength Pressure)
      Adjusts the strength based on the stylus pressure when using a :ref:`Graphics Tablet <hardware-tablet>`.
      The gradient of the pressure can be customized using
      the :doc:`curve widget </interface/controls/templates/curve>`.

.. _bpy.types.BrushGpencilSettings.caps_type:

Caps Type
   The shape of the start and end of the stroke.

   :Round: Strokes start and stop with a curved shape.
   :Flat: Strokes start and stop with a straight cutoff.


Advanced
--------

Spacing
   Controls the minimum spacing between points in the stroke as a percentage of
   the brush size.

   A lower spacing is useful when doing fast movements. Normally this would generate
   less samples and lead to a larger spacing between points. When the spacing percentage
   is lowered, more points are generated to ensure the minimum spacing.

   When drawing slowly, the point density is usually already high. In this case the
   spacing setting doesn't add new points. It only ensures a minimum spacing and won't
   remove points.

.. _bpy.types.BrushGpencilSettings.active_smooth_factor:

Active Smooth
   The number of smoothing iterations to apply to the stroke while drawing.

.. _bpy.types.BrushGpencilSettings.angle:

Angle
   Direction of the input device that gives the maximum thickness to the stroke (0° for horizontal).

.. _bpy.types.BrushGpencilSettings.angle_factor:

Factor
   Amount of thickness reduction when the stroke is perpendicular to the *Angle* value.

.. _bpy.types.BrushGpencilSettings.hardness:

Hardness
   Amount of transparency (alpha) to apply from the border of the point to the center.
   Works only when the brush is using stroke materials of *Dot* or *Box* style.

.. _bpy.types.BrushGpencilSettings.aspect:

Aspect X, Y
   Controls the width and height of the alpha gradient.


Stroke
------

.. _bpy.types.BrushGpencilSettings.use_settings_postprocess:

Post-Processing
^^^^^^^^^^^^^^^

Post-processing methods that are executed on the strokes
when you finished drawing, right after releasing the :kbd:`LMB` or :kbd:`Pen` tip.
You can toggle the use of post-processing using the checkbox in the section panel header.

.. _bpy.types.BrushGpencilSettings.pen_smooth_factor:

Smooth
   Strength of smoothing process on the points location along the stroke.

.. _bpy.types.BrushGpencilSettings.pen_smooth_steps:

Iterations
   The number of smoothing iterations to apply to the stroke.

.. _bpy.types.BrushGpencilSettings.pen_subdivision_steps:

Subdivision Steps
   Number of subdivisions to apply to newly created strokes.

.. _bpy.types.BrushGpencilSettings.simplify_factor:

Simplify
   Reduces final points numbers in the stroke with an adaptive algorithm.

.. _bpy.types.BrushGpencilSettings.use_trim:

Trim Strokes End
   Automatically trim intersection strokes ends.

.. _bpy.types.BrushGpencilSettings.use_settings_outline:

Outline
   Activate the conversion of the newly created stroke to its outline.

   Material
      Material used for outline stroke.
   Thickness
      Thickness used for outline stroke.


.. _bpy.types.BrushGpencilSettings.use_settings_random:

Randomize
^^^^^^^^^

Adds randomness to the position of the points along the stroke.
You can toggle the use of Randomize using the checkbox in the section panel header.

.. _bpy.types.BrushGpencilSettings.use_stroke_random_radius:
.. _bpy.types.BrushGpencilSettings.use_random_press_radius:
.. _bpy.types.BrushGpencilSettings.random:

Radius
   The amount of randomness to apply using the pressure of the input device.

.. _bpy.types.BrushGpencilSettings.use_stroke_random_strength:
.. _bpy.types.BrushGpencilSettings.use_random_press_strength:
.. _bpy.types.BrushGpencilSettings.random_strength:

Strength
   The amount of randomness to apply to the stroke strength value (alpha).

.. _bpy.types.BrushGpencilSettings.use_stroke_random_uv:
.. _bpy.types.BrushGpencilSettings.use_random_press_uv:
.. _bpy.types.BrushGpencilSettings.uv_random:

UV
   The amount of randomness to apply to the UV rotation.

.. _bpy.types.BrushGpencilSettings.use_stroke_random_hue:
.. _bpy.types.BrushGpencilSettings.use_random_press_hue:
.. _bpy.types.BrushGpencilSettings.random_hue_factor:
.. _bpy.types.BrushGpencilSettings.use_stroke_random_sat:
.. _bpy.types.BrushGpencilSettings.use_random_press_sat:
.. _bpy.types.BrushGpencilSettings.random_saturation_factor:
.. _bpy.types.BrushGpencilSettings.use_stroke_random_val:
.. _bpy.types.BrushGpencilSettings.use_random_press_val:
.. _bpy.types.BrushGpencilSettings.random_value_factor:

Hue, Saturation, Value
   Randomizes the hue, saturation, and value of the stroke's :ref:`Color <grease-pencil-draw-color>`.

.. _bpy.types.BrushGpencilSettings.use_jitter_pressure:
.. _bpy.types.BrushGpencilSettings.pen_jitter:

Jitter
   The amount of jittering to add to the stroke.


.. rubric:: Common Options

:bl-icon:`gp_select_strokes` Stroke Random
   Use randomness only at stroke level.

:bl-icon:`stylus_pressure` Use Pressure
   Uses the stylus pressure to control how strong the effect is.
   The gradient of the pressure can be customized using
   the :doc:`curve widget </interface/controls/templates/curve>`.


.. _bpy.types.BrushGpencilSettings.use_settings_stabilizer:

Stabilize Stroke
^^^^^^^^^^^^^^^^

*Stabilize Stroke* helps to reduce jitter of the strokes while drawing by
delaying and correcting the location of points.
You can toggle the use of *Stabilize Stroke* using the checkbox in the section panel header.

Radius
   Minimum distance from the last point before the stroke continues.
Factor
   A smooth factor, where higher values result in smoother strokes but the drawing sensation
   feels like as if you were pulling the stroke.


Cursor
------

The cursor can be disabled by toggling the checkbox in the *Cursor* header.

.. _bpy.types.BrushGpencilSettings.show_lasso:

Show Fill Color while Drawing
   Shows the brush linked material color in the viewport.
