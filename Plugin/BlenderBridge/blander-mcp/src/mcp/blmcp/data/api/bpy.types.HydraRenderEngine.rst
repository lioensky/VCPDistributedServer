HydraRenderEngine(RenderEngine)
===============================

.. currentmodule:: bpy.types


Base class for integrating USD Hydra based renderers.

USD Hydra Based Renderer
++++++++++++++++++++++++

.. literalinclude:: ./examples/bpy.types.HydraRenderEngine.0.py
   :lines: 8-

base classes --- :class:`bpy_struct`, :class:`RenderEngine`

.. class:: HydraRenderEngine(RenderEngine)

   Base class from USD Hydra based renderers

   .. method:: get_render_settings(engine_type: str)

      Provide render settings for ``HdRenderDelegate``.

   .. method:: render(depsgraph)

   .. method:: update(data, depsgraph)

   .. method:: view_draw(context, depsgraph)

   .. method:: view_update(context, depsgraph)

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
   - :class:`RenderEngine.is_animation`
   - :class:`RenderEngine.is_preview`
   - :class:`RenderEngine.camera_override`
   - :class:`RenderEngine.layer_override`
   - :class:`RenderEngine.resolution_x`
   - :class:`RenderEngine.resolution_y`
   - :class:`RenderEngine.temporary_directory`
   - :class:`RenderEngine.render`
   - :class:`RenderEngine.use_highlight_tiles`
   - :class:`RenderEngine.bl_idname`
   - :class:`RenderEngine.bl_label`
   - :class:`RenderEngine.bl_use_preview`
   - :class:`RenderEngine.bl_use_postprocess`
   - :class:`RenderEngine.bl_use_eevee_viewport`
   - :class:`RenderEngine.bl_use_custom_freestyle`
   - :class:`RenderEngine.bl_use_image_save`
   - :class:`RenderEngine.bl_use_gpu_context`
   - :class:`RenderEngine.bl_use_shading_nodes_custom`
   - :class:`RenderEngine.bl_use_spherical_stereo`
   - :class:`RenderEngine.bl_use_stereo_viewport`
   - :class:`RenderEngine.bl_use_materialx`

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
   - :class:`RenderEngine.update`
   - :class:`RenderEngine.render`
   - :class:`RenderEngine.render_frame_finish`
   - :class:`RenderEngine.draw`
   - :class:`RenderEngine.bake`
   - :class:`RenderEngine.view_update`
   - :class:`RenderEngine.view_draw`
   - :class:`RenderEngine.update_script_node`
   - :class:`RenderEngine.update_render_passes`
   - :class:`RenderEngine.update_custom_camera`
   - :class:`RenderEngine.tag_redraw`
   - :class:`RenderEngine.tag_update`
   - :class:`RenderEngine.begin_result`
   - :class:`RenderEngine.update_result`
   - :class:`RenderEngine.end_result`
   - :class:`RenderEngine.add_pass`
   - :class:`RenderEngine.get_result`
   - :class:`RenderEngine.test_break`
   - :class:`RenderEngine.pass_by_index_get`
   - :class:`RenderEngine.active_view_get`
   - :class:`RenderEngine.active_view_set`
   - :class:`RenderEngine.camera_shift_x`
   - :class:`RenderEngine.camera_model_matrix`
   - :class:`RenderEngine.use_spherical_stereo`
   - :class:`RenderEngine.update_stats`
   - :class:`RenderEngine.frame_set`
   - :class:`RenderEngine.update_progress`
   - :class:`RenderEngine.update_memory_stats`
   - :class:`RenderEngine.report`
   - :class:`RenderEngine.error_set`
   - :class:`RenderEngine.bind_display_space_shader`
   - :class:`RenderEngine.unbind_display_space_shader`
   - :class:`RenderEngine.support_display_space_shader`
   - :class:`RenderEngine.get_preview_pixel_size`
   - :class:`RenderEngine.free_blender_memory`
   - :class:`RenderEngine.tile_highlight_set`
   - :class:`RenderEngine.tile_highlight_clear_all`
   - :class:`RenderEngine.register_pass`
   - :class:`RenderEngine.bl_rna_get_subclass`
   - :class:`RenderEngine.bl_rna_get_subclass_py`

