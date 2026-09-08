VIEWLAYER_UL_aov(UIList)
========================

.. currentmodule:: bpy.types

base classes --- :class:`bpy_struct`, :class:`UIList`

.. class:: VIEWLAYER_UL_aov(UIList)


   .. staticmethod:: aov_icon(item)

   .. method:: draw_item(_context, layout, _data, item, icon, _active_data, _active_propname)

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
   - :class:`UIList.bl_idname`
   - :class:`UIList.list_id`
   - :class:`UIList.layout_type`
   - :class:`UIList.use_filter_show`
   - :class:`UIList.filter_name`
   - :class:`UIList.use_filter_invert`
   - :class:`UIList.use_filter_sort_alpha`
   - :class:`UIList.use_filter_sort_reverse`
   - :class:`UIList.use_filter_sort_lock`
   - :class:`UIList.bitflag_filter_item`
   - :class:`UIList.bitflag_item_never_show`

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
   - :class:`UIList.bl_system_properties_get`
   - :class:`UIList.draw_item`
   - :class:`UIList.draw_filter`
   - :class:`UIList.filter_items`
   - :class:`UIList.append`
   - :class:`UIList.is_extended`
   - :class:`UIList.prepend`
   - :class:`UIList.remove`
   - :class:`UIList.bl_rna_get_subclass`
   - :class:`UIList.bl_rna_get_subclass_py`

