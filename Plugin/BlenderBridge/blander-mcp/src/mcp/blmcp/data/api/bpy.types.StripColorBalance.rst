StripColorBalance(StripColorBalanceData)
========================================

.. currentmodule:: bpy.types

base classes --- :class:`bpy_struct`, :class:`StripColorBalanceData`

.. class:: StripColorBalance(StripColorBalanceData)

   Color balance parameters for a sequence strip

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
   - :class:`StripColorBalanceData.correction_method`
   - :class:`StripColorBalanceData.lift`
   - :class:`StripColorBalanceData.gamma`
   - :class:`StripColorBalanceData.gain`
   - :class:`StripColorBalanceData.slope`
   - :class:`StripColorBalanceData.offset`
   - :class:`StripColorBalanceData.power`
   - :class:`StripColorBalanceData.invert_lift`
   - :class:`StripColorBalanceData.invert_gamma`
   - :class:`StripColorBalanceData.invert_gain`
   - :class:`StripColorBalanceData.invert_slope`
   - :class:`StripColorBalanceData.invert_offset`
   - :class:`StripColorBalanceData.invert_power`

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
   - :class:`StripColorBalanceData.bl_rna_get_subclass`
   - :class:`StripColorBalanceData.bl_rna_get_subclass_py`

