NodeLink(bpy_struct)
====================

.. currentmodule:: bpy.types

base class --- :class:`bpy_struct`

.. class:: NodeLink(bpy_struct)

   Link between nodes in a node tree

   .. data:: from_node

      (readonly)

      :type: :class:`Node` | None

   .. data:: from_socket

      (readonly)

      :type: :class:`NodeSocket` | None

   .. data:: is_hidden

      Link is hidden due to invisible sockets (default False, readonly)

      :type: bool

   .. attribute:: is_muted

      Link is muted and can be ignored (default False)

      :type: bool

   .. attribute:: is_valid

      Link is valid (default False)

      :type: bool

   .. data:: multi_input_sort_id

      Used to sort multiple links coming into the same input. The highest ID is at the top. (in [0, inf], default 0, readonly)

      :type: int

   .. data:: to_node

      (readonly)

      :type: :class:`Node` | None

   .. data:: to_socket

      (readonly)

      :type: :class:`NodeSocket` | None

   .. method:: swap_multi_input_sort_id(other)

      Swap the order of two links connected to the same multi-input socket

      :param other: Other, The other link. Must link to the same multi-input socket. (never None)
      :type other: :class:`NodeLink` | None

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

   - :class:`Node.insert_link`
   - :class:`Node.internal_links`
   - :class:`NodeLink.swap_multi_input_sort_id`
   - :class:`NodeLinks.new`
   - :class:`NodeLinks.remove`
   - :class:`NodeTree.links`

