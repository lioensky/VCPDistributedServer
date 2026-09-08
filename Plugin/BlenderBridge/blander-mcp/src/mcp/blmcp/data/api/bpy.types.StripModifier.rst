StripModifier(bpy_struct)
=========================

.. currentmodule:: bpy.types

base class --- :class:`bpy_struct`

subclasses --- 
:class:`BrightContrastModifier`, :class:`ColorBalanceModifier`, :class:`CurvesModifier`, :class:`EchoModifier`, :class:`HueCorrectModifier`, :class:`MaskStripModifier`, :class:`PitchModifier`, :class:`SequencerCompositorModifierData`, :class:`SequencerTonemapModifierData`, :class:`SoundEqualizerModifier`, :class:`WhiteBalanceModifier`

.. class:: StripModifier(bpy_struct)

   Modifier for sequence strip

   .. attribute:: enable

      Enable this modifier (default True)

      :type: bool

   .. attribute:: input_mask_id

      Mask ID used as mask input for the modifier

      :type: :class:`Mask` | None

   .. attribute:: input_mask_strip

      Strip used as mask input for the modifier

      :type: :class:`Strip` | None

   .. attribute:: input_mask_type

      Type of input data used for mask (default ``'STRIP'``)

      - ``STRIP``
        Strip -- Use sequencer strip as mask input.
      - ``ID``
        Mask -- Use mask ID as mask input.

      :type: Literal['STRIP', 'ID']

   .. attribute:: is_active

      This modifier is active (default False)

      :type: bool

   .. attribute:: mask_time

      Time to use for the Mask animation (default ``'RELATIVE'``)

      - ``RELATIVE``
        Relative -- Mask animation is offset to start of strip.
      - ``ABSOLUTE``
        Absolute -- Mask animation is in sync with scene frame.

      :type: Literal['RELATIVE', 'ABSOLUTE']

   .. attribute:: mute

      Mute this modifier (default False)

      :type: bool

   .. attribute:: name

      (default "", never None)

      :type: str

   .. attribute:: show_expanded

      Mute expanded settings for the modifier (default False)

      :type: bool

   .. data:: type

      (default ``'BRIGHT_CONTRAST'``, readonly)

      :type: Literal[:ref:`rna_enum_strip_modifier_type_items`]

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

   - :mod:`bpy.context.strip_modifier`
   - :class:`Strip.modifiers`
   - :class:`StripModifiers.active`
   - :class:`StripModifiers.new`
   - :class:`StripModifiers.remove`

