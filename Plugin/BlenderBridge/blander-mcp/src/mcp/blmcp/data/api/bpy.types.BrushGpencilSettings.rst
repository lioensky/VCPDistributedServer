BrushGpencilSettings(bpy_struct)
================================

.. currentmodule:: bpy.types

base class --- :class:`bpy_struct`

.. class:: BrushGpencilSettings(bpy_struct)

   Settings for Grease Pencil brush

   .. attribute:: active_smooth_factor

      Amount of smoothing while drawing (in [0, 1], default 0.0)

      :type: float

   .. attribute:: angle

      Direction of the stroke at which brush gives maximal thickness (0° for horizontal) (in [-1.5708, 1.5708], default 0.0)

      :type: float

   .. attribute:: angle_factor

      Reduce brush thickness by this factor when stroke is perpendicular to 'Angle' direction (in [0, 1], default 0.0)

      :type: float

   .. attribute:: aspect

      (array of 2 items, in [0.01, 1], default (0.0, 0.0))

      :type: :class:`mathutils.Vector`

   .. attribute:: brush_draw_mode

      Preselected mode when using this brush (default ``'ACTIVE'``)

      - ``ACTIVE``
        Active -- Use current mode.
      - ``MATERIAL``
        Material -- Use always material mode.
      - ``VERTEXCOLOR``
        Vertex Color -- Use always Vertex Color mode.

      :type: Literal['ACTIVE', 'MATERIAL', 'VERTEXCOLOR']

   .. attribute:: caps_type

      The shape of the start and end of the stroke (default ``'ROUND'``)

      :type: Literal['ROUND', 'FLAT']

   .. data:: curve_jitter

      Curve used for the jitter effect (readonly)

      :type: :class:`CurveMapping` | None

   .. data:: curve_random_hue

      Curve used for modulating effect (readonly)

      :type: :class:`CurveMapping` | None

   .. data:: curve_random_pressure

      Curve used for modulating effect (readonly)

      :type: :class:`CurveMapping` | None

   .. data:: curve_random_saturation

      Curve used for modulating effect (readonly)

      :type: :class:`CurveMapping` | None

   .. data:: curve_random_strength

      Curve used for modulating effect (readonly)

      :type: :class:`CurveMapping` | None

   .. data:: curve_random_uv

      Curve used for modulating effect (readonly)

      :type: :class:`CurveMapping` | None

   .. data:: curve_random_value

      Curve used for modulating effect (readonly)

      :type: :class:`CurveMapping` | None

   .. data:: curve_sensitivity

      Curve used for the sensitivity (readonly)

      :type: :class:`CurveMapping` | None

   .. data:: curve_strength

      Curve used for the strength (readonly)

      :type: :class:`CurveMapping` | None

   .. attribute:: dilate

      Number of pixels to expand or contract fill area (in [-40, 40], default 1)

      :type: int

   .. attribute:: eraser_mode

      Eraser Mode (default ``'SOFT'``)

      - ``SOFT``
        Dissolve -- Erase strokes, fading their points strength and thickness.
      - ``HARD``
        Point -- Erase stroke points.
      - ``STROKE``
        Stroke -- Erase entire strokes.

      :type: Literal['SOFT', 'HARD', 'STROKE']

   .. attribute:: eraser_strength_factor

      Amount of erasing for strength (in [0, 100], default 0.0)

      :type: float

   .. attribute:: eraser_thickness_factor

      Amount of erasing for thickness (in [0, 100], default 0.0)

      :type: float

   .. attribute:: extend_stroke_factor

      Strokes end extension for closing gaps, use zero to disable (in [0, 10], default 0.0)

      :type: float

   .. attribute:: fill_direction

      Direction of the fill (default ``'NORMAL'``)

      - ``NORMAL``
        Normal -- Fill internal area.
      - ``INVERT``
        Inverted -- Fill inverted area.

      :type: Literal['NORMAL', 'INVERT']

   .. attribute:: fill_draw_mode

      Mode to draw boundary limits (default ``'BOTH'``)

      - ``BOTH``
        All -- Use both visible strokes and edit lines as fill boundary limits.
      - ``STROKE``
        Strokes -- Use visible strokes as fill boundary limits.
      - ``CONTROL``
        Edit Lines -- Use edit lines as fill boundary limits.

      :type: Literal['BOTH', 'STROKE', 'CONTROL']

   .. attribute:: fill_extend_mode

      Types of stroke extensions used for closing gaps (default ``'EXTEND'``)

      - ``EXTEND``
        Extend -- Extend strokes in straight lines.
      - ``RADIUS``
        Radius -- Connect endpoints that are close together.

      :type: Literal['EXTEND', 'RADIUS']

   .. attribute:: fill_factor

      Factor for fill boundary accuracy, higher values are more accurate but slower (in [0.05, 8], default 0.0)

      :type: float

   .. attribute:: fill_layer_mode

      Layers used as boundaries (default ``'VISIBLE'``)

      - ``VISIBLE``
        Visible -- Visible layers.
      - ``ACTIVE``
        Active -- Only active layer.
      - ``ABOVE``
        Layer Above -- Layer above active.
      - ``BELOW``
        Layer Below -- Layer below active.
      - ``ALL_ABOVE``
        All Above -- All layers above active.
      - ``ALL_BELOW``
        All Below -- All layers below active.

      :type: Literal['VISIBLE', 'ACTIVE', 'ABOVE', 'BELOW', 'ALL_ABOVE', 'ALL_BELOW']

   .. attribute:: fill_simplify_level

      Number of simplify steps (large values reduce fill accuracy) (in [0, 10], default 0)

      :type: int

   .. attribute:: fill_threshold

      Threshold to consider color transparent for filling (in [0, 1], default 0.0)

      :type: float

   .. attribute:: hardness

      Gradient from the center of Dot and Box strokes (set to 1 for a solid stroke) (in [0.001, 1], default 1.0)

      :type: float

   .. attribute:: input_samples

      Generated intermediate points for very fast mouse movements (Set to 0 to disable) (in [0, 10], default 0)

      :type: int

   .. attribute:: material

      Material used for strokes drawn using this brush

      :type: :class:`Material` | None

   .. attribute:: material_alt

      Material used for secondary uses for this brush

      :type: :class:`Material` | None

   .. attribute:: outline_thickness_factor

      Thickness of the outline stroke relative to current brush thickness (in [0, 1], default 0.0)

      :type: float

   .. attribute:: pen_jitter

      Jitter factor of brush radius for new strokes (in [0, 100], default 0.0)

      :type: float

   .. attribute:: pen_smooth_factor

      Amount of smoothing to apply after finish newly created strokes, to reduce jitter/noise (in [0, 2], default 0.0)

      :type: float

   .. attribute:: pen_smooth_steps

      Number of times to smooth newly created strokes (in [0, 100], default 0)

      :type: int

   .. attribute:: pen_strength

      Color strength for new strokes (affect alpha factor of color) (in [0, 1], default 0.0)

      :type: float

   .. attribute:: pen_subdivision_steps

      Number of times to subdivide newly created strokes, for less jagged strokes (in [0, 3], default 0)

      :type: int

   .. attribute:: pin_draw_mode

      Pin the mode to the brush (default False)

      :type: bool

   .. attribute:: random_hue_factor

      Random factor to modify original hue (in [0, 1], default 0.0)

      :type: float

   .. attribute:: random_pressure

      Randomness factor for pressure in new strokes (in [0, 1], default 0.0)

      :type: float

   .. attribute:: random_saturation_factor

      Random factor to modify original saturation (in [0, 1], default 0.0)

      :type: float

   .. attribute:: random_strength

      Randomness factor strength in new strokes (in [0, 1], default 0.0)

      :type: float

   .. attribute:: random_value_factor

      Random factor to modify original value (in [0, 1], default 0.0)

      :type: float

   .. attribute:: show_fill

      Show transparent lines to use as boundary for filling (default True)

      :type: bool

   .. attribute:: show_fill_boundary

      Show help lines for filling to see boundaries (default True)

      :type: bool

   .. attribute:: show_fill_extend

      Show help lines for stroke extension (default True)

      :type: bool

   .. attribute:: show_lasso

      Do not display fill color while drawing the stroke (default True)

      :type: bool

   .. attribute:: simplify_factor

      Factor of Simplify using adaptive algorithm (in [0, 100], default 0.0)

      :type: float

   .. attribute:: simplify_pixel_threshold

      Threshold in screen space used for the simplify algorithm. Points within this threshold are treated as if they were in a straight line. (in [0, 10], default 0.0)

      :type: float

   .. attribute:: stroke_type

      Mode to use when creating strokes (default ``'STROKE'``)

      :type: Literal['STROKE', 'FILL', 'BOTH']

   .. attribute:: use_active_layer_only

      Only edit the active layer of the object (default False)

      :type: bool

   .. attribute:: use_auto_remove_fill_guides

      Automatically remove fill guide strokes after fill operation (default True)

      :type: bool

   .. attribute:: use_collide_strokes

      Check if extend lines collide with strokes (default False)

      :type: bool

   .. attribute:: use_edit_position

      The brush affects the position of the point (default False)

      :type: bool

   .. attribute:: use_edit_strength

      The brush affects the color strength of the point (default False)

      :type: bool

   .. attribute:: use_edit_thickness

      The brush affects the thickness of the point (default False)

      :type: bool

   .. attribute:: use_edit_uv

      The brush affects the UV rotation of the point (default False)

      :type: bool

   .. attribute:: use_fill_limit

      Fill only visible areas in viewport (default True)

      :type: bool

   .. attribute:: use_jitter_pressure

      Use tablet pressure for jitter (default False)

      :type: bool

   .. attribute:: use_keep_caps_eraser

      Keep the caps as they are and don't flatten them when erasing (default False)

      :type: bool

   .. attribute:: use_material_pin

      Keep material assigned to brush (default False)

      :type: bool

   .. attribute:: use_occlude_eraser

      Erase only strokes visible and not occluded (default False)

      :type: bool

   .. attribute:: use_pressure

      Use tablet pressure (default False)

      :type: bool

   .. attribute:: use_random_press_hue

      Use pressure to modulate randomness (default False)

      :type: bool

   .. attribute:: use_random_press_radius

      Use pressure to modulate randomness (default False)

      :type: bool

   .. attribute:: use_random_press_sat

      Use pressure to modulate randomness (default False)

      :type: bool

   .. attribute:: use_random_press_strength

      Use pressure to modulate randomness (default False)

      :type: bool

   .. attribute:: use_random_press_uv

      Use pressure to modulate randomness (default False)

      :type: bool

   .. attribute:: use_random_press_val

      Use pressure to modulate randomness (default False)

      :type: bool

   .. attribute:: use_settings_outline

      Convert stroke to outline (default False)

      :type: bool

   .. attribute:: use_settings_postprocess

      Additional post processing options for new strokes (default False)

      :type: bool

   .. attribute:: use_settings_random

      Random brush settings (default False)

      :type: bool

   .. attribute:: use_settings_stabilizer

      Draw lines with a delay to allow smooth strokes (press Shift key to override while drawing) (default True)

      :type: bool

   .. attribute:: use_strength_pressure

      Use tablet pressure for color strength (default False)

      :type: bool

   .. attribute:: use_stroke_random_hue

      Use randomness at stroke level (default False)

      :type: bool

   .. attribute:: use_stroke_random_radius

      Use randomness at stroke level (default False)

      :type: bool

   .. attribute:: use_stroke_random_sat

      Use randomness at stroke level (default False)

      :type: bool

   .. attribute:: use_stroke_random_strength

      Use randomness at stroke level (default False)

      :type: bool

   .. attribute:: use_stroke_random_uv

      Use randomness at stroke level (default False)

      :type: bool

   .. attribute:: use_stroke_random_val

      Use randomness at stroke level (default False)

      :type: bool

   .. attribute:: use_trim

      Trim intersecting stroke ends (default False)

      :type: bool

   .. attribute:: uv_random

      Random factor for auto-generated UV rotation (in [0, 1], default 0.0)

      :type: float

   .. attribute:: vertex_color_factor

      Factor used to mix vertex color to get final color (in [0, 1], default 0.0)

      :type: float

   .. attribute:: vertex_mode

      Defines how vertex color affect to the strokes (default ``'STROKE'``)

      - ``STROKE``
        Stroke -- Vertex Color affects to Stroke only.
      - ``FILL``
        Fill -- Vertex Color affects to Fill only.
      - ``BOTH``
        Stroke & Fill -- Vertex Color affects to Stroke and Fill.

      :type: Literal['STROKE', 'FILL', 'BOTH']

   .. classmethod:: bl_rna_get_subclass(id, default=None, /)
   
      :param id: The RNA type identifier.
      :type id: str
      :param default: The value to return when not found.
      :type default: :class:`bpy.types.Struct` | None
      :return: The RNA type or default when not found.
      :rtype: :class:`bpy.types.Struct`


   .. classmethod:: bl_rna_get_subclass_py(id, default=None, /)
   
      :param id: The RNA type identifier.
      :type id: str
      :param default: The value to return when not found.
      :type default: type | None
      :return: The class or default when not found.
      :rtype: type


Inherited Properties
--------------------

.. hlist::
   :columns: 2

   - :class:`bpy_struct.id_data`

Inherited Functions
-------------------

.. hlist::
   :columns: 2

   - :class:`bpy_struct.as_pointer`
   - :class:`bpy_struct.driver_add`
   - :class:`bpy_struct.driver_remove`
   - :class:`bpy_struct.get`
   - :class:`bpy_struct.id_properties_clear`
   - :class:`bpy_struct.id_properties_ensure`
   - :class:`bpy_struct.id_properties_ui`
   - :class:`bpy_struct.is_property_hidden`
   - :class:`bpy_struct.is_property_overridable_library`
   - :class:`bpy_struct.is_property_readonly`
   - :class:`bpy_struct.is_property_set`
   - :class:`bpy_struct.items`
   - :class:`bpy_struct.keyframe_delete`
   - :class:`bpy_struct.keyframe_insert`
   - :class:`bpy_struct.keys`
   - :class:`bpy_struct.path_from_id`
   - :class:`bpy_struct.path_from_module`
   - :class:`bpy_struct.path_resolve`
   - :class:`bpy_struct.pop`
   - :class:`bpy_struct.property_overridable_library_set`
   - :class:`bpy_struct.property_unset`
   - :class:`bpy_struct.rna_ancestors`
   - :class:`bpy_struct.type_recast`
   - :class:`bpy_struct.values`

References
----------

.. hlist::
   :columns: 2

   - :class:`Brush.gpencil_settings`

