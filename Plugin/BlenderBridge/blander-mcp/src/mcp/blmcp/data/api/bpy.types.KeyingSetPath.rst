KeyingSetPath(bpy_struct)
=========================

.. currentmodule:: bpy.types

base class --- :class:`bpy_struct`

.. class:: KeyingSetPath(bpy_struct)

   Path to a setting for use in a Keying Set

   .. attribute:: array_index

      Index to the specific setting if applicable (in [-inf, inf], default 0)

      :type: int

   .. attribute:: data_path

      Path to property setting (default "", never None)

      :type: str

   .. attribute:: group

      Name of Action Group to assign setting(s) for this path to (default "", never None)

      :type: str

   .. attribute:: group_method

      Method used to define which Group-name to use (default ``'NAMED'``)

      :type: Literal[:ref:`rna_enum_keyingset_path_grouping_items`]

   .. attribute:: id

      ID-Block that keyframes for Keying Set should be added to (for Absolute Keying Sets only)

      :type: :class:`ID` | None

   .. attribute:: id_type

      Type of ID-block that can be used (default ``'OBJECT'``)

      :type: Literal[:ref:`rna_enum_id_type_items`]

   .. attribute:: use_entire_array

      When an 'array/vector' type is chosen (Location, Rotation, Color, etc.), entire array is to be used (default False)

      :type: bool

   .. attribute:: use_insertkey_needed

      Only insert keyframes where they're needed in the relevant F-Curves (default False)

      :type: bool

   .. attribute:: use_insertkey_override_needed

      Override default setting to only insert keyframes where they're needed in the relevant F-Curves (default False)

      :type: bool

   .. attribute:: use_insertkey_override_visual

      Override default setting to insert keyframes based on 'visual transforms' (default False)

      :type: bool

   .. attribute:: use_insertkey_visual

      Insert keyframes based on 'visual transforms' (default False)

      :type: bool

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
   - :class:`KeyingSetPaths.active`
   - :class:`KeyingSetPaths.add`
   - :class:`KeyingSetPaths.remove`

