GlowStrip(EffectStrip)
======================

.. currentmodule:: bpy.types

base classes --- :class:`bpy_struct`, :class:`Strip`, :class:`EffectStrip`

.. class:: GlowStrip(EffectStrip)

   Sequence strip creating a glow effect

   .. attribute:: blur_radius

      Radius of glow effect (in [0.5, 20], default 0.0)

      :type: float

   .. attribute:: boost_factor

      Brightness multiplier (in [0, 10], default 0.0)

      :type: float

   .. attribute:: clamp

      Brightness limit of intensity (in [0, 1], default 0.0)

      :type: float

   .. attribute:: input_1

      First input for the effect strip (never None)

      :type: :class:`Strip`

   .. data:: input_count

      (in [0, inf], default 0, readonly)

      :type: int

   .. attribute:: quality

      Accuracy of the blur effect (in [1, 5], default 0)

      :type: int

   .. attribute:: threshold

      Minimum intensity to trigger a glow (in [0, 1], default 0.0)

      :type: float

   .. attribute:: use_only_boost

      Show the glow buffer only (default False)

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
   - :class:`Strip.name`
   - :class:`Strip.type`
   - :class:`Strip.select`
   - :class:`Strip.select_left_handle`
   - :class:`Strip.select_right_handle`
   - :class:`Strip.mute`
   - :class:`Strip.lock`
   - :class:`Strip.frame_final_duration`
   - :class:`Strip.duration`
   - :class:`Strip.frame_duration`
   - :class:`Strip.content_duration`
   - :class:`Strip.frame_start`
   - :class:`Strip.content_start`
   - :class:`Strip.content_end`
   - :class:`Strip.frame_final_start`
   - :class:`Strip.left_handle`
   - :class:`Strip.frame_final_end`
   - :class:`Strip.right_handle`
   - :class:`Strip.frame_offset_start`
   - :class:`Strip.left_handle_offset`
   - :class:`Strip.frame_offset_end`
   - :class:`Strip.right_handle_offset`
   - :class:`Strip.channel`
   - :class:`Strip.use_linear_modifiers`
   - :class:`Strip.blend_type`
   - :class:`Strip.blend_alpha`
   - :class:`Strip.effect_fader`
   - :class:`Strip.use_default_fade`
   - :class:`Strip.color_tag`
   - :class:`Strip.modifiers`
   - :class:`Strip.show_retiming_keys`
   - :class:`EffectStrip.use_deinterlace`
   - :class:`EffectStrip.alpha_mode`
   - :class:`EffectStrip.use_flip_x`
   - :class:`EffectStrip.use_flip_y`
   - :class:`EffectStrip.use_float`
   - :class:`EffectStrip.use_reverse_frames`
   - :class:`EffectStrip.color_multiply`
   - :class:`EffectStrip.multiply_alpha`
   - :class:`EffectStrip.color_saturation`
   - :class:`EffectStrip.strobe`
   - :class:`EffectStrip.transform`
   - :class:`EffectStrip.crop`
   - :class:`EffectStrip.use_proxy`
   - :class:`EffectStrip.proxy`

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
   - :class:`Strip.bl_system_properties_get`
   - :class:`Strip.strip_elem_from_frame`
   - :class:`Strip.swap`
   - :class:`Strip.move_to_meta`
   - :class:`Strip.parent_meta`
   - :class:`Strip.invalidate_cache`
   - :class:`Strip.split`
   - :class:`Strip.bl_rna_get_subclass`
   - :class:`Strip.bl_rna_get_subclass_py`
   - :class:`EffectStrip.bl_rna_get_subclass`
   - :class:`EffectStrip.bl_rna_get_subclass_py`

