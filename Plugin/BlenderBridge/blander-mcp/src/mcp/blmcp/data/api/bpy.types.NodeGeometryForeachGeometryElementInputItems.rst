NodeGeometryForeachGeometryElementInputItems(bpy_prop_collection)
=================================================================

.. currentmodule:: bpy.types

base classes --- :class:`bpy_prop`, :class:`bpy_prop_collection`

.. class:: NodeGeometryForeachGeometryElementInputItems(bpy_prop_collection)

   Collection of input items

   .. method:: new(socket_type, name)

      Add an item at the end

      :param socket_type: Socket Type, Socket type of the item
      :type socket_type: Literal[:ref:`rna_enum_node_socket_data_type_items`]
      :param name: Name, (never None)
      :type name: str
      :return: Item, New item
      :rtype: :class:`ForeachGeometryElementInputItem`

   .. method:: remove(item)

      Remove an item

      :param item: Item, The item to remove (never None)
      :type item: :class:`ForeachGeometryElementInputItem` | None

   .. method:: clear()

      Remove all items


   .. method:: move(from_index, to_index)

      Move an item to another position

      :param from_index: From Index, Index of the item to move (in [0, inf])
      :type from_index: int
      :param to_index: To Index, Target index for the item (in [0, inf])
      :type to_index: int

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

   - :class:`GeometryNodeForeachGeometryElementOutput.input_items`

