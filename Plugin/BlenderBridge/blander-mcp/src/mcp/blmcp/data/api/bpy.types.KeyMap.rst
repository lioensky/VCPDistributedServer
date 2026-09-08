KeyMap(bpy_struct)
==================

.. currentmodule:: bpy.types

base class --- :class:`bpy_struct`

.. class:: KeyMap(bpy_struct)

   Input configuration, including keymaps

   .. attribute:: bl_owner_id

      Internal owner (default "", never None)

      :type: str

   .. data:: is_modal

      Indicates that a keymap is used for translate modal events for an operator (default False, readonly)

      :type: bool

   .. attribute:: is_user_modified

      Keymap is defined by the user (default False)

      :type: bool

   .. data:: keymap_items

      Items in the keymap, linking an operator to an input event (default None, readonly)

      :type: :class:`KeyMapItems`\ [:class:`KeyMapItem`]

   .. data:: modal_event_values

      Give access to the possible event values of this modal keymap's items (#KeyMapItem.propvalue), for API introspection (default None, readonly)

      :type: :class:`bpy_prop_collection`\ [:class:`EnumPropertyItem`]

   .. data:: name

      Name of the key map (default "", readonly, never None)

      :type: str

   .. data:: region_type

      Optional region type keymap is associated with (default ``'WINDOW'``, readonly)

      :type: Literal[:ref:`rna_enum_region_type_items`]

   .. attribute:: show_expanded_children

      Children expanded in the user interface (default False)

      :type: bool

   .. attribute:: show_expanded_items

      Expanded in the user interface (default False)

      :type: bool

   .. data:: space_type

      Optional space type keymap is associated with (default ``'EMPTY'``, readonly)

      :type: Literal[:ref:`rna_enum_space_type_items`]

   .. method:: active()

      active

      :return: Key Map, Active key map
      :rtype: :class:`KeyMap`

   .. method:: restore_to_default()

      restore_to_default


   .. method:: restore_item_to_default(item)

      restore_item_to_default

      :param item: Item, (never None)
      :type item: :class:`KeyMapItem` | None

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

   - :class:`GizmoGroup.setup_keymap`
   - :class:`KeyConfig.keymaps`
   - :class:`KeyConfigurations.find_item_from_operator`
   - :class:`KeyMap.active`
   - :class:`KeyMapItems.find_match`
   - :class:`KeyMaps.find`
   - :class:`KeyMaps.find_match`
   - :class:`KeyMaps.find_match`
   - :class:`KeyMaps.find_modal`
   - :class:`KeyMaps.new`
   - :class:`KeyMaps.remove`
   - :class:`WindowManager.popover_end__internal`

