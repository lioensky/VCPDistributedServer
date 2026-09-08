XrActionMapBindings(bpy_prop_collection)
========================================

.. currentmodule:: bpy.types

base classes --- :class:`bpy_prop`, :class:`bpy_prop_collection`

.. class:: XrActionMapBindings(bpy_prop_collection)

   Collection of XR action map bindings

   .. method:: new(name, replace_existing)

      new

      :param name: Name of the action map binding, (never None)
      :type name: str
      :param replace_existing: Replace Existing, Replace any existing binding with the same name
      :type replace_existing: bool
      :return: Binding, Added action map binding
      :rtype: :class:`XrActionMapBinding`

   .. method:: new_from_binding(binding)

      new_from_binding

      :param binding: Binding, Binding to use as a reference (never None)
      :type binding: :class:`XrActionMapBinding` | None
      :return: Binding, Added action map binding
      :rtype: :class:`XrActionMapBinding`

   .. method:: remove(binding)

      remove

      :param binding: Binding, (never None)
      :type binding: :class:`XrActionMapBinding` | None

   .. method:: find(name)

      find

      :param name: Name, (never None)
      :type name: str
      :return: Binding, The action map binding with the given name
      :rtype: :class:`XrActionMapBinding`

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

   - :class:`XrActionMapItem.bindings`

