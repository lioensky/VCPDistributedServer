SequencerTonemapModifierData(StripModifier)
===========================================

.. currentmodule:: bpy.types

base classes --- :class:`bpy_struct`, :class:`StripModifier`

.. class:: SequencerTonemapModifierData(StripModifier)

   Tone mapping modifier

   .. attribute:: adaptation

      If 0, global; if 1, based on pixel intensity (in [0, 1], default 0.0)

      :type: float

   .. attribute:: contrast

      Set to 0 to use estimate from input image (in [0, 1], default 0.0)

      :type: float

   .. attribute:: correction

      If 0, same for all channels; if 1, each independent (in [0, 1], default 0.0)

      :type: float

   .. attribute:: gamma

      If not used, set to 1 (in [0.001, 3], default 0.0)

      :type: float

   .. attribute:: intensity

      If less than zero, darkens image; otherwise, makes it brighter (in [-8, 8], default 0.0)

      :type: float

   .. attribute:: key

      The value the average luminance is mapped to (in [0, 1], default 0.0)

      :type: float

   .. attribute:: offset

      Normally always 1, but can be used as an extra control to alter the brightness curve (in [0.001, 10], default 0.0)

      :type: float

   .. attribute:: open_mask_input_panel

      (default False)

      :type: bool

   .. attribute:: tonemap_type

      Tone mapping algorithm (default ``'RH_SIMPLE'``)

      :type: Literal['RD_PHOTORECEPTOR', 'RH_SIMPLE']

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

