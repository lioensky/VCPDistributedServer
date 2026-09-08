GreasePencilBuildModifier(Modifier)
===================================

.. currentmodule:: bpy.types

base classes --- :class:`bpy_struct`, :class:`Modifier`

.. class:: GreasePencilBuildModifier(Modifier)

   Animate strokes appearing and disappearing

   .. attribute:: concurrent_time_alignment

      How should strokes start to appear/disappear (default ``'START'``)

      - ``START``
        Align Start -- All strokes start at same time (i.e. short strokes finish earlier).
      - ``END``
        Align End -- All strokes end at same time (i.e. short strokes start later).

      :type: Literal['START', 'END']

   .. attribute:: fade_factor

      Defines how much of the stroke is fading in/out (in [0, 1], default 0.0)

      :type: float

   .. attribute:: fade_opacity_strength

      How much strength fading applies on top of stroke opacity (in [0, 1], default 0.0)

      :type: float

   .. attribute:: fade_thickness_strength

      How much strength fading applies on top of stroke thickness (in [0, 1], default 0.0)

      :type: float

   .. attribute:: frame_end

      End Frame (when Restrict Frame Range is enabled) (in [-1.04857e+06, 1.04857e+06], default 125.0)

      :type: float

   .. attribute:: frame_start

      Start Frame (when Restrict Frame Range is enabled) (in [-1.04857e+06, 1.04857e+06], default 1.0)

      :type: float

   .. attribute:: invert_layer_filter

      Invert layer filter (default False)

      :type: bool

   .. attribute:: invert_layer_pass_filter

      Invert layer pass filter (default False)

      :type: bool

   .. attribute:: invert_material_filter

      Invert material filter (default False)

      :type: bool

   .. attribute:: invert_material_pass_filter

      Invert material pass filter (default False)

      :type: bool

   .. attribute:: layer_pass_filter

      Layer pass filter (in [0, 100], default 0)

      :type: int

   .. attribute:: length

      Maximum number of frames that the build effect can run for (unless another GP keyframe occurs before this time has elapsed) (in [1, 1.04857e+06], default 100.0)

      :type: float

   .. attribute:: material_filter

      Material used for filtering

      :type: :class:`Material` | None

   .. attribute:: material_pass_filter

      Material pass (in [0, 100], default 0)

      :type: int

   .. attribute:: mode

      How strokes are being built (default ``'SEQUENTIAL'``)

      - ``SEQUENTIAL``
        Sequential -- Strokes appear/disappear one after the other, but only a single one changes at a time.
      - ``CONCURRENT``
        Concurrent -- Multiple strokes appear/disappear at once.
      - ``ADDITIVE``
        Additive -- Builds only new strokes (assuming 'additive' drawing).

      :type: Literal['SEQUENTIAL', 'CONCURRENT', 'ADDITIVE']

   .. attribute:: object

      Object used as build starting position

      :type: :class:`Object` | None

   .. attribute:: open_fading_panel

      (default False)

      :type: bool

   .. attribute:: open_frame_range_panel

      (default False)

      :type: bool

   .. attribute:: open_influence_panel

      (default False)

      :type: bool

   .. attribute:: percentage_factor

      Defines how much of the stroke is visible (in [0, 1], default 0.0)

      :type: float

   .. attribute:: speed_factor

      Multiply recorded drawing speed by a factor (in [0, 100], default 1.2)

      :type: float

   .. attribute:: speed_maxgap

      The maximum gap between strokes in seconds (in [0, 100], default 0.5)

      :type: float

   .. attribute:: start_delay

      Number of frames after each GP keyframe before the modifier has any effect (in [0, 1.04857e+06], default 0.0)

      :type: float

   .. attribute:: target_vertex_group

      Output Vertex group (default "", never None)

      :type: str

   .. attribute:: time_mode

      Use drawing speed, a number of frames, or a manual factor to build strokes (default ``'FRAMES'``)

      - ``DRAWSPEED``
        Natural Drawing Speed -- Use recorded speed multiplied by a factor.
      - ``FRAMES``
        Number of Frames -- Set a fixed number of frames for all build animations.
      - ``PERCENTAGE``
        Percentage Factor -- Set a manual percentage to build.

      :type: Literal['DRAWSPEED', 'FRAMES', 'PERCENTAGE']

   .. attribute:: transition

      How are strokes animated (i.e. are they appearing or disappearing) (default ``'GROW'``)

      - ``GROW``
        Grow -- Show points in the order they occur in each stroke (e.g. for animating lines being drawn).
      - ``SHRINK``
        Shrink -- Hide points from the end of each stroke to the start (e.g. for animating lines being erased).
      - ``FADE``
        Vanish -- Hide points in the order they occur in each stroke (e.g. for animating ink fading or vanishing after getting drawn).

      :type: Literal['GROW', 'SHRINK', 'FADE']

   .. attribute:: tree_node_filter

      Layer name (default "", never None)

      :type: str

   .. attribute:: use_fading

      Fade out strokes instead of directly cutting off (default False)

      :type: bool

   .. attribute:: use_layer_group_filter

      Filter by layer group name (default False)

      :type: bool

   .. attribute:: use_layer_pass_filter

      Use layer pass filter (default False)

      :type: bool

   .. attribute:: use_material_pass_filter

      Use material pass filter (default False)

      :type: bool

   .. attribute:: use_percentage

      Use a percentage factor to determine the visible points (default False)

      :type: bool

   .. attribute:: use_restrict_frame_range

      Only modify strokes during the specified frame range (default False)

      :type: bool

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
   - :class:`Modifier.name`
   - :class:`Modifier.type`
   - :class:`Modifier.show_viewport`
   - :class:`Modifier.show_render`
   - :class:`Modifier.show_in_editmode`
   - :class:`Modifier.show_on_cage`
   - :class:`Modifier.show_expanded`
   - :class:`Modifier.is_active`
   - :class:`Modifier.use_pin_to_last`
   - :class:`Modifier.is_override_data`
   - :class:`Modifier.use_apply_on_spline`
   - :class:`Modifier.execution_time`
   - :class:`Modifier.persistent_uid`

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
   - :class:`Modifier.bl_rna_get_subclass`
   - :class:`Modifier.bl_rna_get_subclass_py`

