Sound(ID)
=========

.. currentmodule:: bpy.types

base classes --- :class:`bpy_struct`, :class:`ID`

.. class:: Sound(ID)

   Sound data-block referencing an external or packed sound file

   .. data:: channels

      Definition of audio channels (default ``'INVALID'``, readonly)

      - ``INVALID``
        Invalid -- Invalid.
      - ``MONO``
        Mono -- Mono.
      - ``STEREO``
        Stereo -- Stereo.
      - ``STEREO_LFE``
        Stereo LFE -- Stereo FX.
      - ``CHANNELS_4``
        4 Channels -- 4 Channels.
      - ``CHANNELS_5``
        5 Channels -- 5 Channels.
      - ``SURROUND_51``
        5.1 Surround -- 5.1 Surround.
      - ``SURROUND_61``
        6.1 Surround -- 6.1 Surround.
      - ``SURROUND_71``
        7.1 Surround -- 7.1 Surround.

      :type: Literal['INVALID', 'MONO', 'STEREO', 'STEREO_LFE', 'CHANNELS_4', 'CHANNELS_5', 'SURROUND_51', 'SURROUND_61', 'SURROUND_71']

   .. attribute:: filepath

      Sound sample file used by this Sound data-block (default "", never None, blend relative ``//`` prefix supported)

      :type: str

   .. data:: packed_file

      (readonly)

      :type: :class:`PackedFile` | None

   .. data:: samplerate

      Sample rate of the audio in Hz (in [-inf, inf], default 0, readonly)

      :type: int

   .. attribute:: use_memory_cache

      The sound file is decoded and loaded into RAM (default False)

      :type: bool

   .. attribute:: use_mono

      If the file contains multiple audio channels they are rendered to a single one (default False)

      :type: bool

   .. data:: factory

      The aud.Factory object of the sound.

      (readonly)

   .. method:: pack()

      Pack the sound into the current blend file


   .. method:: unpack(*, method='USE_LOCAL')

      Unpack the sound to the samples filename

      :param method: method, How to unpack (optional)
      :type method: Literal[:ref:`rna_enum_unpack_method_items`]

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
   - :class:`ID.name`
   - :class:`ID.name_full`
   - :class:`ID.id_type`
   - :class:`ID.session_uid`
   - :class:`ID.is_evaluated`
   - :class:`ID.original`
   - :class:`ID.users`
   - :class:`ID.use_fake_user`
   - :class:`ID.use_extra_user`
   - :class:`ID.is_embedded_data`
   - :class:`ID.is_linked_packed`
   - :class:`ID.is_missing`
   - :class:`ID.is_runtime_data`
   - :class:`ID.is_editable`
   - :class:`ID.tag`
   - :class:`ID.is_library_indirect`
   - :class:`ID.library`
   - :class:`ID.library_weak_reference`
   - :class:`ID.asset_data`
   - :class:`ID.override_library`
   - :class:`ID.preview`

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
   - :class:`ID.bl_system_properties_get`
   - :class:`ID.rename`
   - :class:`ID.evaluated_get`
   - :class:`ID.copy`
   - :class:`ID.asset_mark`
   - :class:`ID.asset_clear`
   - :class:`ID.asset_generate_preview`
   - :class:`ID.override_create`
   - :class:`ID.override_hierarchy_create`
   - :class:`ID.user_clear`
   - :class:`ID.user_remap`
   - :class:`ID.make_local`
   - :class:`ID.user_of_id`
   - :class:`ID.animation_data_create`
   - :class:`ID.animation_data_clear`
   - :class:`ID.update_tag`
   - :class:`ID.preview_ensure`
   - :class:`ID.bl_rna_get_subclass`
   - :class:`ID.bl_rna_get_subclass_py`

References
----------

.. hlist::
   :columns: 2

   - :class:`BlendData.sounds`
   - :class:`BlendDataSounds.load`
   - :class:`BlendDataSounds.remove`
   - :class:`NodeSocketSound.default_value`
   - :class:`NodeTreeInterfaceSocketSound.default_value`
   - :class:`SoundStrip.sound`
   - :class:`Speaker.sound`

