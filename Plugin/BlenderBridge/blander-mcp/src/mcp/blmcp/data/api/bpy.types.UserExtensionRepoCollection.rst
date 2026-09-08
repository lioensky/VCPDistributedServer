UserExtensionRepoCollection(bpy_prop_collection)
================================================

.. currentmodule:: bpy.types

base classes --- :class:`bpy_prop`, :class:`bpy_prop_collection`

.. class:: UserExtensionRepoCollection(bpy_prop_collection)

   Collection of user extension repositories

   .. classmethod:: new(*, name="", module="", custom_directory="", remote_url="", source='USER')

      Add a new repository

      :param name: Name, (optional, never None)
      :type name: str
      :param module: Module, (optional, never None)
      :type module: str
      :param custom_directory: Custom Directory, (optional, never None)
      :type custom_directory: str
      :param remote_url: Remote URL, (optional, never None)
      :type remote_url: str
      :param source: Source, How the repository is managed (optional)

         - ``USER``
           User -- Repository managed by the user, stored in user directories.
         - ``SYSTEM``
           System -- Read-only repository provided by the system.
      :type source: Literal['USER', 'SYSTEM']
      :return: Newly added repository
      :rtype: :class:`UserExtensionRepo`

   .. classmethod:: remove(repo)

      Remove repos

      :param repo: Repository to remove (never None)
      :type repo: :class:`UserExtensionRepo` | None

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

   - :class:`PreferencesExtensions.repos`

