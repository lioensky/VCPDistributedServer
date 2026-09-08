SurfaceCurve(Curve)
===================

.. currentmodule:: bpy.types

base classes --- :class:`bpy_struct`, :class:`ID`, :class:`Curve`

.. class:: SurfaceCurve(Curve)

   Curve data-block used for storing surfaces

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
   - :class:`ID.name`
   - :class:`ID.name_full`
   - :class:`ID.id_type`
   - :class:`ID.session_uid`
   - :class:`ID.is_evaluated`
   - :class:`ID.original`
   - :class:`ID.users`
   - :class:`ID.use_fake_user`
   - :class:`ID.use_extra_user`
   - :class:`ID.is_embedded_data`
   - :class:`ID.is_linked_packed`
   - :class:`ID.is_missing`
   - :class:`ID.is_runtime_data`
   - :class:`ID.is_editable`
   - :class:`ID.tag`
   - :class:`ID.is_library_indirect`
   - :class:`ID.library`
   - :class:`ID.library_weak_reference`
   - :class:`ID.asset_data`
   - :class:`ID.override_library`
   - :class:`ID.preview`
   - :class:`Curve.shape_keys`
   - :class:`Curve.splines`
   - :class:`Curve.path_duration`
   - :class:`Curve.use_path`
   - :class:`Curve.use_path_follow`
   - :class:`Curve.use_path_clamp`
   - :class:`Curve.use_stretch`
   - :class:`Curve.use_deform_bounds`
   - :class:`Curve.use_radius`
   - :class:`Curve.bevel_mode`
   - :class:`Curve.bevel_profile`
   - :class:`Curve.bevel_resolution`
   - :class:`Curve.offset`
   - :class:`Curve.extrude`
   - :class:`Curve.bevel_depth`
   - :class:`Curve.resolution_u`
   - :class:`Curve.resolution_v`
   - :class:`Curve.render_resolution_u`
   - :class:`Curve.render_resolution_v`
   - :class:`Curve.eval_time`
   - :class:`Curve.bevel_object`
   - :class:`Curve.taper_object`
   - :class:`Curve.dimensions`
   - :class:`Curve.fill_mode`
   - :class:`Curve.fill_solver`
   - :class:`Curve.fill_rule`
   - :class:`Curve.twist_mode`
   - :class:`Curve.taper_radius_mode`
   - :class:`Curve.bevel_factor_mapping_start`
   - :class:`Curve.bevel_factor_mapping_end`
   - :class:`Curve.twist_smooth`
   - :class:`Curve.use_fill_caps`
   - :class:`Curve.use_map_taper`
   - :class:`Curve.use_auto_texspace`
   - :class:`Curve.texspace_location`
   - :class:`Curve.texspace_size`
   - :class:`Curve.materials`
   - :class:`Curve.bevel_factor_start`
   - :class:`Curve.bevel_factor_end`
   - :class:`Curve.is_editmode`
   - :class:`Curve.animation_data`

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
   - :class:`ID.bl_system_properties_get`
   - :class:`ID.rename`
   - :class:`ID.evaluated_get`
   - :class:`ID.copy`
   - :class:`ID.asset_mark`
   - :class:`ID.asset_clear`
   - :class:`ID.asset_generate_preview`
   - :class:`ID.override_create`
   - :class:`ID.override_hierarchy_create`
   - :class:`ID.user_clear`
   - :class:`ID.user_remap`
   - :class:`ID.make_local`
   - :class:`ID.user_of_id`
   - :class:`ID.animation_data_create`
   - :class:`ID.animation_data_clear`
   - :class:`ID.update_tag`
   - :class:`ID.preview_ensure`
   - :class:`ID.bl_rna_get_subclass`
   - :class:`ID.bl_rna_get_subclass_py`
   - :class:`Curve.transform`
   - :class:`Curve.validate_material_indices`
   - :class:`Curve.update_gpu_tag`
   - :class:`Curve.bl_rna_get_subclass`
   - :class:`Curve.bl_rna_get_subclass_py`

