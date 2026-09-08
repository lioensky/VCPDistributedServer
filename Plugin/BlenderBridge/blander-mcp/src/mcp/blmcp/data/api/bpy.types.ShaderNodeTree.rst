ShaderNodeTree(NodeTree)
========================

.. currentmodule:: bpy.types

base classes --- :class:`bpy_struct`, :class:`ID`, :class:`NodeTree`

.. class:: ShaderNodeTree(NodeTree)

   Node tree consisting of linked nodes used for materials (and other shading data-blocks)

   .. method:: get_output_node(target)

      Return active shader output node for the specified target

      :param target: Target

         - ``ALL``
           All -- Use shaders for all renderers and viewports, unless there exists a more specific output.
         - ``EEVEE``
           EEVEE -- Use shaders for EEVEE renderer.
         - ``CYCLES``
           Cycles -- Use shaders for Cycles renderer.
      :type target: Literal['ALL', 'EEVEE', 'CYCLES']
      :return: Node
      :rtype: :class:`ShaderNode`

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
   - :class:`NodeTree.color_tag`
   - :class:`NodeTree.default_group_node_width`
   - :class:`NodeTree.view_center`
   - :class:`NodeTree.description`
   - :class:`NodeTree.animation_data`
   - :class:`NodeTree.nodes`
   - :class:`NodeTree.links`
   - :class:`NodeTree.annotation`
   - :class:`NodeTree.type`
   - :class:`NodeTree.interface`
   - :class:`NodeTree.bl_idname`
   - :class:`NodeTree.bl_label`
   - :class:`NodeTree.bl_description`
   - :class:`NodeTree.bl_icon`
   - :class:`NodeTree.bl_use_group_interface`

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
   - :class:`NodeTree.interface_update`
   - :class:`NodeTree.contains_tree`
   - :class:`NodeTree.poll`
   - :class:`NodeTree.update`
   - :class:`NodeTree.get_from_context`
   - :class:`NodeTree.valid_socket_type`
   - :class:`NodeTree.debug_lazy_function_graph`
   - :class:`NodeTree.bl_rna_get_subclass`
   - :class:`NodeTree.bl_rna_get_subclass_py`

