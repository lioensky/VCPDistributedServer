GreasePencilTimeModifier(Modifier)
==================================

.. currentmodule:: bpy.types

base classes --- :class:`bpy_struct`, :class:`Modifier`

.. class:: GreasePencilTimeModifier(Modifier)

   Offset keyframes

   .. attribute:: frame_end

      Final frame of the range (in [0, 1048574], default 250)

      :type: int

   .. attribute:: frame_scale

      Evaluation time in seconds (in [0.001, 100], default 1.0)

      :type: float

   .. attribute:: frame_start

      First frame of the range (in [0, 1048574], default 1)

      :type: int

   .. attribute:: invert_layer_filter

      Invert layer filter (default False)

      :type: bool

   .. attribute:: invert_layer_pass_filter

      Invert layer pass filter (default False)

      :type: bool

   .. attribute:: layer_pass_filter

      Layer pass filter (in [0, 100], default 0)

      :type: int

   .. attribute:: mode

      (default ``'NORMAL'``)

      - ``NORMAL``
        Regular -- Apply offset in usual animation direction.
      - ``REVERSE``
        Reverse -- Apply offset in reverse animation direction.
      - ``FIX``
        Fixed Frame -- Keep frame and do not change with time.
      - ``PINGPONG``
        Ping Pong -- Loop back and forth starting in reverse.
      - ``CHAIN``
        Chain -- List of chained animation segments.

      :type: Literal['NORMAL', 'REVERSE', 'FIX', 'PINGPONG', 'CHAIN']

   .. attribute:: offset

      Number of frames to offset original keyframe number or frame to fix (in [-32768, 32767], default 1)

      :type: int

   .. attribute:: open_custom_range_panel

      (default False)

      :type: bool

   .. attribute:: open_influence_panel

      (default False)

      :type: bool

   .. attribute:: segment_active_index

      Active index in the segment list (in [0, inf], default 0)

      :type: int

   .. data:: segments

      (default None, readonly)

      :type: :class:`bpy_prop_collection`\ [:class:`GreasePencilTimeModifierSegment`]

   .. attribute:: tree_node_filter

      Layer name (default "", never None)

      :type: str

   .. attribute:: use_custom_frame_range

      Define a custom range of frames to use in modifier (default False)

      :type: bool

   .. attribute:: use_keep_loop

      Retiming end frames and move to start of animation to keep loop (default True)

      :type: bool

   .. attribute:: use_layer_group_filter

      Filter by layer group name (default False)

      :type: bool

   .. attribute:: use_layer_pass_filter

      Use layer pass filter (default False)

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

