KeyMapItem(bpy_struct)
======================

.. currentmodule:: bpy.types

base class --- :class:`bpy_struct`

.. class:: KeyMapItem(bpy_struct)

   Item in a Key Map

   .. attribute:: active

      Activate or deactivate item (default False)

      :type: bool

   .. attribute:: alt

      Alt key pressed, -1 for any state (in [-1, 1], default 0)

      :type: int

   .. attribute:: alt_ui

      Alt key pressed (default False)

      :type: bool

   .. attribute:: any

      Any modifier keys pressed (default False)

      :type: bool

   .. attribute:: ctrl

      Control key pressed, -1 for any state (in [-1, 1], default 0)

      :type: int

   .. attribute:: ctrl_ui

      Control key pressed (default False)

      :type: bool

   .. attribute:: direction

      The direction (only applies to drag events) (default ``'ANY'``)

      :type: Literal[:ref:`rna_enum_event_direction_items`]

   .. attribute:: hyper

      Hyper key pressed, -1 for any state (in [-1, 1], default 0)

      :type: int

   .. attribute:: hyper_ui

      Hyper key pressed. An additional modifier which can be configured on Linux, typically replacing CapsLock (default False)

      :type: bool

   .. data:: id

      ID of the item (in [-32768, 32767], default 0, readonly)

      :type: int

   .. attribute:: idname

      Identifier of operator to call on input event (default "", never None)

      :type: str

   .. data:: is_user_defined

      Is this keymap item user defined (does not just replace a builtin item) (default False, readonly)

      :type: bool

   .. data:: is_user_modified

      Is this keymap item modified by the user (default False, readonly)

      :type: bool

   .. attribute:: key_modifier

      Regular key pressed as a modifier (default ``'NONE'``)

      :type: Literal[:ref:`rna_enum_event_type_items`]

   .. attribute:: map_type

      Type of event mapping (default ``'KEYBOARD'``)

      :type: Literal['KEYBOARD', 'MOUSE', 'NDOF', 'TEXTINPUT', 'TIMER']

   .. data:: name

      Name of operator (translated) to call on input event (default "", readonly, never None)

      :type: str

   .. attribute:: oskey

      Operating system key pressed, -1 for any state (in [-1, 1], default 0)

      :type: int

   .. attribute:: oskey_ui

      Operating system key pressed (default False)

      :type: bool

   .. data:: properties

      Properties to set when the operator is called (readonly)

      :type: :class:`OperatorProperties` | None

   .. attribute:: propvalue

      The value this event translates to in a modal keymap (default ``'NONE'``)

      :type: Literal[:ref:`rna_enum_keymap_propvalue_items`]

   .. attribute:: repeat

      Active on key-repeat events (when a key is held) (default False)

      :type: bool

   .. attribute:: shift

      Shift key pressed, -1 for any state (in [-1, 1], default 0)

      :type: int

   .. attribute:: shift_ui

      Shift key pressed (default False)

      :type: bool

   .. attribute:: show_expanded

      Show key map event and property details in the user interface (default False)

      :type: bool

   .. attribute:: type

      Type of event (default ``'NONE'``)

      :type: Literal[:ref:`rna_enum_event_type_items`]

   .. attribute:: value

      (default ``'NOTHING'``)

      :type: Literal[:ref:`rna_enum_event_value_items`]

   .. method:: compare(item)

      compare

      :param item: Item
      :type item: :class:`KeyMapItem` | None
      :return: Comparison result
      :rtype: bool

   .. method:: to_string(*, compact=False)

      to_string

      :param compact: Compact, (optional)
      :type compact: bool
      :return: result, (never None)
      :rtype: str

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

   - :class:`KeyConfigurations.find_item_from_operator`
   - :class:`KeyMap.keymap_items`
   - :class:`KeyMap.restore_item_to_default`
   - :class:`KeyMapItem.compare`
   - :class:`KeyMapItems.find_from_operator`
   - :class:`KeyMapItems.find_match`
   - :class:`KeyMapItems.find_match`
   - :class:`KeyMapItems.from_id`
   - :class:`KeyMapItems.match_event`
   - :class:`KeyMapItems.new`
   - :class:`KeyMapItems.new_from_item`
   - :class:`KeyMapItems.new_from_item`
   - :class:`KeyMapItems.new_modal`
   - :class:`KeyMapItems.remove`
   - :class:`UILayout.template_event_from_keymap_item`
   - :class:`UILayout.template_keymap_item_properties`

