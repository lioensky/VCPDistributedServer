VIEW3D_AST_brush_gpencil_paint(AssetShelf)
==========================================

.. currentmodule:: bpy.types

base classes --- :class:`bpy_struct`, :class:`AssetShelf`

.. class:: VIEW3D_AST_brush_gpencil_paint(AssetShelf)


   .. classmethod:: brush_type_poll(context, asset)

   .. staticmethod:: draw_popup_selector(layout, context, brush, show_name=True)

   .. staticmethod:: get_shelf_name_from_context(context)

   .. classmethod:: has_tool_with_brush_type(context, brush_type)

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
   - :class:`AssetShelf.bl_idname`
   - :class:`AssetShelf.bl_space_type`
   - :class:`AssetShelf.bl_options`
   - :class:`AssetShelf.bl_activate_operator`
   - :class:`AssetShelf.bl_drag_operator`
   - :class:`AssetShelf.bl_default_preview_size`
   - :class:`AssetShelf.filter_action`
   - :class:`AssetShelf.filter_armature`
   - :class:`AssetShelf.filter_brush`
   - :class:`AssetShelf.filter_camera`
   - :class:`AssetShelf.filter_cachefile`
   - :class:`AssetShelf.filter_curve`
   - :class:`AssetShelf.filter_annotations`
   - :class:`AssetShelf.filter_grease_pencil`
   - :class:`AssetShelf.filter_group`
   - :class:`AssetShelf.filter_curves`
   - :class:`AssetShelf.filter_image`
   - :class:`AssetShelf.filter_light`
   - :class:`AssetShelf.filter_light_probe`
   - :class:`AssetShelf.filter_linestyle`
   - :class:`AssetShelf.filter_lattice`
   - :class:`AssetShelf.filter_material`
   - :class:`AssetShelf.filter_metaball`
   - :class:`AssetShelf.filter_movie_clip`
   - :class:`AssetShelf.filter_mesh`
   - :class:`AssetShelf.filter_mask`
   - :class:`AssetShelf.filter_node_tree`
   - :class:`AssetShelf.filter_object`
   - :class:`AssetShelf.filter_particle_settings`
   - :class:`AssetShelf.filter_palette`
   - :class:`AssetShelf.filter_paint_curve`
   - :class:`AssetShelf.filter_pointcloud`
   - :class:`AssetShelf.filter_scene`
   - :class:`AssetShelf.filter_speaker`
   - :class:`AssetShelf.filter_sound`
   - :class:`AssetShelf.filter_texture`
   - :class:`AssetShelf.filter_text`
   - :class:`AssetShelf.filter_font`
   - :class:`AssetShelf.filter_volume`
   - :class:`AssetShelf.filter_world`
   - :class:`AssetShelf.filter_work_space`
   - :class:`AssetShelf.asset_library_reference`
   - :class:`AssetShelf.show_names`
   - :class:`AssetShelf.preview_size`
   - :class:`AssetShelf.search_filter`

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
   - :class:`AssetShelf.poll`
   - :class:`AssetShelf.asset_poll`
   - :class:`AssetShelf.get_active_asset`
   - :class:`AssetShelf.draw_context_menu`
   - :class:`AssetShelf.bl_rna_get_subclass`
   - :class:`AssetShelf.bl_rna_get_subclass_py`

