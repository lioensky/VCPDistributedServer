ActionSlots(bpy_prop_collection)
================================

.. currentmodule:: bpy.types

base classes --- :class:`bpy_prop`, :class:`bpy_prop_collection`

.. class:: ActionSlots(bpy_prop_collection)

   Collection of action slots

   .. attribute:: active

      Active slot for this action

      :type: :class:`ActionSlot` | None

   .. method:: new(id_type, name)

      Add a slot to the Action

      :param id_type: Data-block Type, The data-block type that the slot is intended for. This is combined with the slot name to create the slot's unique identifier, and is also used to limit (on a best-effort basis) which data-blocks the slot can be assigned to.
      :type id_type: Literal[:ref:`rna_enum_id_type_items`]
      :param name: Name, Name of the slot. This will be made unique within the Action among slots of the same type (never None)
      :type name: str
      :return: Newly created action slot
      :rtype: :class:`ActionSlot`

   .. method:: remove(action_slot)

      Remove the slot from the Action, including all animation that is associated with that slot

      :param action_slot: Action Slot, The slot to remove
      :type action_slot: :class:`ActionSlot` | None

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

   - :class:`Action.slots`

