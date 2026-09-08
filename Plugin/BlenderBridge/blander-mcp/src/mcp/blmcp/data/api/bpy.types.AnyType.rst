AnyType(bpy_struct)
===================

.. currentmodule:: bpy.types

base class --- :class:`bpy_struct`

.. class:: AnyType(bpy_struct)

   RNA type used for pointers to any possible data

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

   - :mod:`bpy.context.property`
   - :class:`BoneCollection.assign`
   - :class:`BoneCollection.unassign`
   - :class:`FCurve.update_autoflags`
   - :class:`Gizmo.target_set_prop`
   - :class:`KeyingSetInfo.generate`
   - :class:`Region.data`
   - :class:`UILayout.context_pointer_set`
   - :class:`UILayout.enum_item_description`
   - :class:`UILayout.enum_item_icon`
   - :class:`UILayout.enum_item_name`
   - :class:`UILayout.icon`
   - :class:`UILayout.panel_prop`
   - :class:`UILayout.prop`
   - :class:`UILayout.prop_decorator`
   - :class:`UILayout.prop_enum`
   - :class:`UILayout.prop_menu_enum`
   - :class:`UILayout.prop_search`
   - :class:`UILayout.prop_search`
   - :class:`UILayout.prop_tabs_enum`
   - :class:`UILayout.prop_tabs_enum`
   - :class:`UILayout.prop_with_menu`
   - :class:`UILayout.prop_with_popover`
   - :class:`UILayout.props_enum`
   - :class:`UILayout.template_ID`
   - :class:`UILayout.template_ID_preview`
   - :class:`UILayout.template_ID_session_uid`
   - :class:`UILayout.template_ID_tabs`
   - :class:`UILayout.template_any_ID`
   - :class:`UILayout.template_cache_file`
   - :class:`UILayout.template_cache_file_layers`
   - :class:`UILayout.template_cache_file_time_settings`
   - :class:`UILayout.template_cache_file_velocity`
   - :class:`UILayout.template_color_picker`
   - :class:`UILayout.template_color_ramp`
   - :class:`UILayout.template_colormanaged_view_settings`
   - :class:`UILayout.template_colorspace_settings`
   - :class:`UILayout.template_component_menu`
   - :class:`UILayout.template_curve_mapping`
   - :class:`UILayout.template_curveprofile`
   - :class:`UILayout.template_greasepencil_color`
   - :class:`UILayout.template_histogram`
   - :class:`UILayout.template_icon_view`
   - :class:`UILayout.template_image`
   - :class:`UILayout.template_layers`
   - :class:`UILayout.template_layers`
   - :class:`UILayout.template_light_linking_collection`
   - :class:`UILayout.template_list`
   - :class:`UILayout.template_list`
   - :class:`UILayout.template_marker`
   - :class:`UILayout.template_matrix`
   - :class:`UILayout.template_movieclip`
   - :class:`UILayout.template_movieclip_information`
   - :class:`UILayout.template_palette`
   - :class:`UILayout.template_path_builder`
   - :class:`UILayout.template_search`
   - :class:`UILayout.template_search`
   - :class:`UILayout.template_search_preview`
   - :class:`UILayout.template_search_preview`
   - :class:`UILayout.template_track`
   - :class:`UILayout.template_vectorscope`
   - :class:`UILayout.template_waveform`
   - :class:`UIList.draw_item`
   - :class:`UIList.draw_item`
   - :class:`UIList.draw_item`
   - :class:`UIList.filter_items`

