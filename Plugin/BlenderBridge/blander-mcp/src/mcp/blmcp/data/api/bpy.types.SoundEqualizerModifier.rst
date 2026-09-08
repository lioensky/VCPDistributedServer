SoundEqualizerModifier(StripModifier)
=====================================

.. currentmodule:: bpy.types

base classes --- :class:`bpy_struct`, :class:`StripModifier`

.. class:: SoundEqualizerModifier(StripModifier)

   Equalize audio

   .. data:: graphics

      Graphical definition equalization (default None, readonly)

      :type: :class:`bpy_prop_collection`\ [:class:`EQCurveMappingData`]

   .. method:: new_graphic(min_freq, max_freq)

      Add a new EQ band

      :param min_freq: Minimum Frequency, Minimum Frequency (in [0, 20000])
      :type min_freq: float
      :param max_freq: Maximum Frequency, Maximum Frequency (in [0, 20000])
      :type max_freq: float
      :return: Newly created graphical Equalizer definition
      :rtype: :class:`EQCurveMappingData`

   .. method:: clear_soundeqs()

      Remove all graphical equalizers from the Equalizer modifier


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
   - :class:`StripModifier.name`
   - :class:`StripModifier.type`
   - :class:`StripModifier.mute`
   - :class:`StripModifier.enable`
   - :class:`StripModifier.show_expanded`
   - :class:`StripModifier.input_mask_type`
   - :class:`StripModifier.mask_time`
   - :class:`StripModifier.input_mask_strip`
   - :class:`StripModifier.input_mask_id`
   - :class:`StripModifier.is_active`

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
   - :class:`StripModifier.bl_rna_get_subclass`
   - :class:`StripModifier.bl_rna_get_subclass_py`

