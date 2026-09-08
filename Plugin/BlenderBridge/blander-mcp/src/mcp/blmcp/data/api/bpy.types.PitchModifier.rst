PitchModifier(StripModifier)
============================

.. currentmodule:: bpy.types

base classes --- :class:`bpy_struct`, :class:`StripModifier`

.. class:: PitchModifier(StripModifier)

   Shift Audio Pitch

   .. attribute:: cents

      A cent is one one-hundredth of a semi-tone. (in [-100, 100], default 0)

      :type: int

   .. attribute:: mode

      Mode of the pitch shift (default ``'SEMITONES'``)

      - ``SEMITONES``
        Semitones -- Shift pitch using semitones and cents.
      - ``RATIO``
        Ratio -- Shift pitch using a direct ratio.

      :type: Literal['SEMITONES', 'RATIO']

   .. attribute:: preserve_formant

      Whether to preserve the vocal formants when shifting the pitch. (default False)

      :type: bool

   .. attribute:: quality

      Quality of the pitch shifting (default ``'HIGH'``)

      - ``HIGH``
        High -- Prioritize high-quality pitch processing.
      - ``FAST``
        Fast -- Prioritize speed over audio quality.
      - ``CONSISTENT``
        Consistent -- Prioritize consistency for dynamic pitch changes.

      :type: Literal['HIGH', 'FAST', 'CONSISTENT']

   .. attribute:: ratio

      Factor by which the audio pitch is scaled. (in [0.5, 2], default 0.0)

      :type: float

   .. attribute:: semitones

      Number of semitones to shift the pitch. (in [-12, 12], default 0)

      :type: int

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

