KeyingSetPaths(bpy_prop_collection)
===================================

.. currentmodule:: bpy.types

base classes --- :class:`bpy_prop`, :class:`bpy_prop_collection`

.. class:: KeyingSetPaths(bpy_prop_collection)

   Collection of keying set paths

   .. attribute:: active

      Active Keying Set used to insert/delete keyframes

      :type: :class:`KeyingSetPath` | None

   .. attribute:: active_index

      Current Keying Set index (in [-inf, inf], default 0)

      :type: int

   .. method:: add(target_id, data_path, *, index=-1, group_method='KEYINGSET', group_name="")

      Add a new path for the Keying Set

      :param target_id: Target ID, ID data-block for the destination
      :type target_id: :class:`ID` | None
      :param data_path: Data-Path, RNA-Path to destination property (never None)
      :type data_path: str
      :param index: Index, The index of the destination property (i.e. axis of Location/Rotation/etc.), or -1 for the entire array (in [-1, inf], optional)
      :type index: int
      :param group_method: Grouping Method, Method used to define which Group-name to use (optional)
      :type group_method: Literal[:ref:`rna_enum_keyingset_path_grouping_items`]
      :param group_name: Group Name, Name of Action Group to assign destination to (only if grouping mode is to use this name) (optional, never None)
      :type group_name: str
      :return: New Path, Path created and added to the Keying Set
      :rtype: :class:`KeyingSetPath`

   .. method:: remove(path)

      Remove the given path from the Keying Set

      :param path: Path, (never None)
      :type path: :class:`KeyingSetPath` | None

   .. method:: clear()

      Remove all the paths from the Keying Set


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

   - :class:`KeyingSet.paths`

