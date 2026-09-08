NodeSocketMask(NodeSocketStandard)
==================================

.. currentmodule:: bpy.types

base classes --- :class:`bpy_struct`, :class:`NodeSocket`, :class:`NodeSocketStandard`

.. class:: NodeSocketMask(NodeSocketStandard)

   Mask socket of a node

   .. attribute:: default_value

      :type: :class:`Mask` | None

   .. data:: links

      List of node links from or to this socket.
      
      :type: :class:`NodeLinks`
      
      .. note:: Takes ``O(len(nodetree.links))`` time.

      (readonly)

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
   - :class:`NodeSocket.name`
   - :class:`NodeSocket.label`
   - :class:`NodeSocket.identifier`
   - :class:`NodeSocket.description`
   - :class:`NodeSocket.is_output`
   - :class:`NodeSocket.select`
   - :class:`NodeSocket.hide`
   - :class:`NodeSocket.enabled`
   - :class:`NodeSocket.link_limit`
   - :class:`NodeSocket.is_linked`
   - :class:`NodeSocket.is_unavailable`
   - :class:`NodeSocket.is_multi_input`
   - :class:`NodeSocket.show_expanded`
   - :class:`NodeSocket.is_inactive`
   - :class:`NodeSocket.is_icon_visible`
   - :class:`NodeSocket.hide_value`
   - :class:`NodeSocket.pin_gizmo`
   - :class:`NodeSocket.node`
   - :class:`NodeSocket.type`
   - :class:`NodeSocket.display_shape`
   - :class:`NodeSocket.inferred_structure_type`
   - :class:`NodeSocket.bl_idname`
   - :class:`NodeSocket.bl_label`
   - :class:`NodeSocket.bl_subtype_label`
   - :class:`NodeSocket.links`
   - :class:`NodeSocketStandard.links`

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
   - :class:`NodeSocket.bl_system_properties_get`
   - :class:`NodeSocket.draw`
   - :class:`NodeSocket.draw_color`
   - :class:`NodeSocket.draw_color_simple`
   - :class:`NodeSocket.bl_rna_get_subclass`
   - :class:`NodeSocket.bl_rna_get_subclass_py`
   - :class:`NodeSocketStandard.draw`
   - :class:`NodeSocketStandard.draw_color`
   - :class:`NodeSocketStandard.draw_color_simple`
   - :class:`NodeSocketStandard.bl_rna_get_subclass`
   - :class:`NodeSocketStandard.bl_rna_get_subclass_py`

