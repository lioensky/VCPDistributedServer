Strip(bpy_struct)
=================

.. currentmodule:: bpy.types

base class --- :class:`bpy_struct`

subclasses --- 
:class:`EffectStrip`, :class:`ImageStrip`, :class:`MaskStrip`, :class:`MetaStrip`, :class:`MovieClipStrip`, :class:`MovieStrip`, :class:`SceneStrip`, :class:`SoundStrip`

.. class:: Strip(bpy_struct)

   A single container for content in the Video Sequence Editor

   .. attribute:: blend_alpha

      Percentage of how much the strip's colors affect other strips (in [0, 1], default 1.0)

      :type: float

   .. attribute:: blend_type

      Method for controlling how the strip combines with other strips (default ``'ALPHA_OVER'``)

      :type: Literal['REPLACE', 'CROSS', 'DARKEN', 'MULTIPLY', 'BURN', 'LINEAR_BURN', 'LIGHTEN', 'SCREEN', 'DODGE', 'ADD', 'OVERLAY', 'SOFT_LIGHT', 'HARD_LIGHT', 'VIVID_LIGHT', 'LINEAR_LIGHT', 'PIN_LIGHT', 'DIFFERENCE', 'EXCLUSION', 'SUBTRACT', 'HUE', 'SATURATION', 'COLOR', 'VALUE', 'ALPHA_OVER', 'ALPHA_UNDER', 'GAMMA_CROSS']

   .. attribute:: channel

      Vertical position of the strip (in [1, 128], default 0)

      :type: int

   .. attribute:: color_tag

      Color tag for a strip (default ``'COLOR_01'``)

      :type: Literal[:ref:`rna_enum_strip_color_items`]

   .. data:: content_duration

      Length of the underlying strip source in frames, excluding handles (in [1, 1048574], default 0, readonly)

      :type: int

   .. data:: content_end

      Timeline frame where underlying strip source ends (in [-inf, inf], default 0, readonly)

      :type: int

   .. attribute:: content_start

      Timeline frame where underlying strip source begins (in [-inf, inf], default 0.0)

      :type: float

   .. data:: duration

      Length of the strip in frames from left handle to right handle (in [-inf, inf], default 0, readonly)

      :type: int

   .. attribute:: effect_fader

      Custom fade value (in [0, 1], default 0.0)

      :type: float

   .. data:: frame_duration

      The length of the contents of this strip before the handles are applied (in [1, 1048574], default 0, readonly)

      .. deprecated:: 5.10 removal planned in version 6.0

         Replaced by '.content_duration'.

      :type: int

   .. attribute:: frame_final_duration

      The length of the contents of this strip after the handles are applied (in [1, 1048574], default 0)

      .. deprecated:: 5.10 removal planned in version 6.0

         Replaced by '.duration'.

      :type: int

   .. attribute:: frame_final_end

      End frame displayed in the sequence editor after offsets are applied (in [-inf, inf], default 0)

      .. deprecated:: 5.10 removal planned in version 6.0

         Replaced by '.right_handle'.

      :type: int

   .. attribute:: frame_final_start

      Start frame displayed in the sequence editor after offsets are applied, setting this is equivalent to moving the handle, not the actual start frame (in [-inf, inf], default 0)

      .. deprecated:: 5.10 removal planned in version 6.0

         Replaced by '.left_handle'.

      :type: int

   .. attribute:: frame_offset_end

      Offset from the end of the strip in frames (in [-inf, inf], default 0.0)

      .. deprecated:: 5.10 removal planned in version 6.0

         Replaced by '.right_handle_offset'.

      :type: float

   .. attribute:: frame_offset_start

      Offset from the start of the strip in frames (in [-inf, inf], default 0.0)

      .. deprecated:: 5.10 removal planned in version 6.0

         Replaced by '.left_handle_offset'.

      :type: float

   .. attribute:: frame_start

      X position where the strip begins (in [-inf, inf], default 0.0)

      .. deprecated:: 5.10 removal planned in version 6.0

         Replaced by '.content_start'.

      :type: float

   .. attribute:: left_handle

      Timeline frame of the left handle and the start frame of the strip (in [-inf, inf], default 0)

      :type: int

   .. attribute:: left_handle_offset

      Rightward frame offset of the left handle from the start of the strip content (in [-inf, inf], default 0.0)

      :type: float

   .. attribute:: lock

      Lock strip so that it cannot be transformed (default False)

      :type: bool

   .. data:: modifiers

      Modifiers affecting this strip (default None, readonly)

      :type: :class:`StripModifiers`\ [:class:`StripModifier`]

   .. attribute:: mute

      Disable strip so that it does not contribute any output (default False)

      :type: bool

   .. attribute:: name

      (default "", never None)

      :type: str

   .. attribute:: right_handle

      Timeline frame of the right handle, which is the first frame where the strip no longer contributes to the output (in [-inf, inf], default 0)

      :type: int

   .. attribute:: right_handle_offset

      Leftward frame offset of the right handle from the end of the strip content (in [-inf, inf], default 0.0)

      :type: float

   .. attribute:: select

      Whether the strip is selected (default False)

      :type: bool

   .. attribute:: select_left_handle

      Whether the left handle is selected (default False)

      :type: bool

   .. attribute:: select_right_handle

      Whether the right handle is selected (default False)

      :type: bool

   .. attribute:: show_retiming_keys

      Show retiming keys, so they can be moved (default False)

      :type: bool

   .. data:: type

      (default ``'IMAGE'``, readonly)

      :type: Literal['IMAGE', 'META', 'SCENE', 'MOVIE', 'MOVIECLIP', 'MASK', 'SOUND', 'CROSS', 'ADD', 'SUBTRACT', 'ALPHA_OVER', 'ALPHA_UNDER', 'GAMMA_CROSS', 'MULTIPLY', 'WIPE', 'GLOW', 'COLOR', 'SPEED', 'MULTICAM', 'ADJUSTMENT', 'GAUSSIAN_BLUR', 'TEXT', 'COLORMIX']

   .. attribute:: use_default_fade

      Fade effect using the built-in default (usually makes the transition as long as the effect strip) (default False)

      :type: bool

   .. attribute:: use_linear_modifiers

      Calculate modifiers in linear space instead of sequencer's space (default False)

      :type: bool

   .. method:: bl_system_properties_get(*, do_create=False)

      DEBUG ONLY. Internal access to runtime-defined RNA data storage, intended solely for testing and debugging purposes. Do not access it in regular scripting work, and in particular, do not assume that it contains writable data

      :param do_create: Ensure that system properties are created if they do not exist yet (optional)
      :type do_create: bool
      :return: The system properties root container, or None if there are no system properties stored in this data yet, and its creation was not requested
      :rtype: :class:`PropertyGroup`

   .. method:: strip_elem_from_frame(frame)

      Return the strip element from a given frame or None

      :param frame: Frame, The frame to get the strip element from (in [-1048574, 1048574])
      :type frame: int
      :return: strip element of the current frame
      :rtype: :class:`StripElement`

   .. method:: swap(other)

      Swap the position of this strip with another

      :param other: Other, Other strip to swap with (never None)
      :type other: :class:`Strip` | None

   .. method:: move_to_meta(meta_sequence)

      Move this strip into a meta Strip

      :param meta_sequence: Destination Meta Strip, Meta to move the strip into (never None)
      :type meta_sequence: :class:`Strip` | None

   .. method:: parent_meta()

      Returns parent meta Strip

      :return: Parent meta strip
      :rtype: :class:`Strip`

   .. method:: invalidate_cache(type)

      Invalidate cached images for strip and all dependent strips

      :param type: Type, Cache Type (never None)
      :type type: Literal['RAW', 'COMPOSITE']

   .. method:: split(frame, split_method, *, ignore_connections=False)

      Split Strip

      :param frame: Frame where to split the strip (in [-inf, inf])
      :type frame: int
      :param split_method: (never None)
      :type split_method: Literal['SOFT', 'HARD']
      :param ignore_connections: Don't propagate split to connected strips (optional)
      :type ignore_connections: bool
      :return: Right side Strip
      :rtype: :class:`Strip`

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

   - :mod:`bpy.context.active_strip`
   - :mod:`bpy.context.selected_editable_strips`
   - :mod:`bpy.context.selected_strips`
   - :mod:`bpy.context.strip`
   - :mod:`bpy.context.strips`
   - :class:`AddStrip.input_1`
   - :class:`AddStrip.input_2`
   - :class:`AlphaOverStrip.input_1`
   - :class:`AlphaOverStrip.input_2`
   - :class:`AlphaUnderStrip.input_1`
   - :class:`AlphaUnderStrip.input_2`
   - :class:`ColorMixStrip.input_1`
   - :class:`ColorMixStrip.input_2`
   - :class:`CrossStrip.input_1`
   - :class:`CrossStrip.input_2`
   - :class:`GammaCrossStrip.input_1`
   - :class:`GammaCrossStrip.input_2`
   - :class:`GaussianBlurStrip.input_1`
   - :class:`GlowStrip.input_1`
   - :class:`MetaStrip.strips`
   - :class:`MultiplyStrip.input_1`
   - :class:`MultiplyStrip.input_2`
   - :class:`SequenceEditor.active_strip`
   - :class:`SequenceEditor.display_stack`
   - :class:`SequenceEditor.meta_stack`
   - :class:`SequenceEditor.strips`
   - :class:`SequenceEditor.strips_all`
   - :class:`SpeedControlStrip.input_1`
   - :class:`Strip.move_to_meta`
   - :class:`Strip.parent_meta`
   - :class:`Strip.split`
   - :class:`Strip.swap`
   - :class:`StripModifier.input_mask_strip`
   - :class:`StripsMeta.new_clip`
   - :class:`StripsMeta.new_effect`
   - :class:`StripsMeta.new_effect`
   - :class:`StripsMeta.new_effect`
   - :class:`StripsMeta.new_image`
   - :class:`StripsMeta.new_mask`
   - :class:`StripsMeta.new_meta`
   - :class:`StripsMeta.new_movie`
   - :class:`StripsMeta.new_scene`
   - :class:`StripsMeta.new_sound`
   - :class:`StripsMeta.remove`
   - :class:`StripsTopLevel.new_clip`
   - :class:`StripsTopLevel.new_effect`
   - :class:`StripsTopLevel.new_effect`
   - :class:`StripsTopLevel.new_effect`
   - :class:`StripsTopLevel.new_image`
   - :class:`StripsTopLevel.new_mask`
   - :class:`StripsTopLevel.new_meta`
   - :class:`StripsTopLevel.new_movie`
   - :class:`StripsTopLevel.new_scene`
   - :class:`StripsTopLevel.new_sound`
   - :class:`StripsTopLevel.remove`
   - :class:`SubtractStrip.input_1`
   - :class:`SubtractStrip.input_2`
   - :class:`WipeStrip.input_1`
   - :class:`WipeStrip.input_2`

