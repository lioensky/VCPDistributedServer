NodesModifier(Modifier)
=======================

.. currentmodule:: bpy.types

base classes --- :class:`bpy_struct`, :class:`Modifier`

.. class:: NodesModifier(Modifier)


   .. attribute:: bake_directory

      Location on disk where the bake data is stored (default "", never None, blend relative ``//`` prefix supported)

      :type: str

   .. attribute:: bake_target

      Where to store the baked data (default ``'PACKED'``)

      - ``PACKED``
        Packed -- Pack the baked data into the .blend file.
      - ``DISK``
        Disk -- Store the baked data in a directory on disk.

      :type: Literal['PACKED', 'DISK']

   .. data:: bakes

      (default None, readonly)

      :type: :class:`NodesModifierBakes`\ [:class:`NodesModifierBake`]

   .. attribute:: node_group

      Node group that controls what this modifier does

      :type: :class:`NodeTree` | None

   .. data:: node_warnings

      (default None, readonly)

      :type: :class:`bpy_prop_collection`\ [:class:`NodesModifierWarning`]

   .. attribute:: open_bake_data_blocks_panel

      (default False)

      :type: bool

   .. attribute:: open_bake_panel

      (default False)

      :type: bool

   .. attribute:: open_manage_panel

      (default False)

      :type: bool

   .. attribute:: open_named_attributes_panel

      (default False)

      :type: bool

   .. attribute:: open_output_attributes_panel

      (default False)

      :type: bool

   .. attribute:: open_warnings_panel

      (default False)

      :type: bool

   .. data:: panels

      (default None, readonly)

      :type: :class:`NodesModifierPanels`\ [:class:`NodesModifierPanel`]

   .. attribute:: show_group_selector

      (default False)

      :type: bool

   .. attribute:: show_manage_panel

      (default False)

      :type: bool

   .. method:: bl_system_properties_get(*, do_create=False)

      DEBUG ONLY. Internal access to runtime-defined RNA data storage, intended solely for testing and debugging purposes. Do not access it in regular scripting work, and in particular, do not assume that it contains writable data

      :param do_create: Ensure that system properties are created if they do not exist yet (optional)
      :type do_create: bool
      :return: The system properties root container, or None if there are no system properties stored in this data yet, and its creation was not requested
      :rtype: :class:`PropertyGroup`

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
   - :class:`Modifier.name`
   - :class:`Modifier.type`
   - :class:`Modifier.show_viewport`
   - :class:`Modifier.show_render`
   - :class:`Modifier.show_in_editmode`
   - :class:`Modifier.show_on_cage`
   - :class:`Modifier.show_expanded`
   - :class:`Modifier.is_active`
   - :class:`Modifier.use_pin_to_last`
   - :class:`Modifier.is_override_data`
   - :class:`Modifier.use_apply_on_spline`
   - :class:`Modifier.execution_time`
   - :class:`Modifier.persistent_uid`

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
   - :class:`Modifier.bl_rna_get_subclass`
   - :class:`Modifier.bl_rna_get_subclass_py`

