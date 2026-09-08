NodeLinks(bpy_prop_collection)
==============================

.. currentmodule:: bpy.types

base classes --- :class:`bpy_prop`, :class:`bpy_prop_collection`

.. class:: NodeLinks(bpy_prop_collection)

   Collection of Node Links

   .. method:: new(input, output, *, verify_limits=True, handle_dynamic_sockets=False)

      Add a node link to this node tree

      :param input: The input socket (never None)
      :type input: :class:`NodeSocket` | None
      :param output: The output socket (never None)
      :type output: :class:`NodeSocket` | None
      :param verify_limits: Verify Limits, Remove existing links if connection limit is exceeded (optional)
      :type verify_limits: bool
      :param handle_dynamic_sockets: Handle Dynamic Sockets, Handle node specific features like virtual sockets (optional)
      :type handle_dynamic_sockets: bool
      :return: New node link
      :rtype: :class:`NodeLink`

   .. method:: remove(link)

      remove a node link from the node tree

      :param link: The node link to remove (never None)
      :type link: :class:`NodeLink` | None

   .. method:: clear()

      remove all node links from the node tree


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

   - :class:`NodeTree.links`

