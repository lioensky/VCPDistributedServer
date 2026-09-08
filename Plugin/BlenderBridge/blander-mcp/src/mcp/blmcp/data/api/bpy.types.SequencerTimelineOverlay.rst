SequencerTimelineOverlay(bpy_struct)
====================================

.. currentmodule:: bpy.types

base class --- :class:`bpy_struct`

.. class:: SequencerTimelineOverlay(bpy_struct)


   .. attribute:: show_fcurves

      Display strip opacity/volume curve (default False)

      :type: bool

   .. attribute:: show_grid

      Show vertical grid lines (default False)

      :type: bool

   .. attribute:: show_strip_duration

      (default False)

      :type: bool

   .. attribute:: show_strip_name

      (default False)

      :type: bool

   .. attribute:: show_strip_offset

      Display strip in/out offsets (default False)

      :type: bool

   .. attribute:: show_strip_retiming

      Display retiming keys on top of strips (default False)

      :type: bool

   .. attribute:: show_strip_source

      Display path to source file, or name of source data-block (default False)

      :type: bool

   .. attribute:: show_strip_tag_color

      Display the strip color tags in the sequencer (default False)

      :type: bool

   .. attribute:: show_thumbnails

      Show strip thumbnails (default False)

      :type: bool

   .. attribute:: waveform_display_style

      How Waveforms are displayed (default ``'FULL_WAVEFORMS'``)

      - ``FULL_WAVEFORMS``
        Full -- Display full waveform.
      - ``HALF_WAVEFORMS``
        Half -- Display upper half of the absolute value waveform.

      :type: Literal['FULL_WAVEFORMS', 'HALF_WAVEFORMS']

   .. attribute:: waveform_display_type

      How Waveforms are displayed (default ``'DEFAULT_WAVEFORMS'``)

      - ``ALL_WAVEFORMS``
        On -- Display waveforms for all sound strips.
      - ``DEFAULT_WAVEFORMS``
        Strip -- Display waveforms depending on strip setting.
      - ``NO_WAVEFORMS``
        Off -- Don't display waveforms for any sound strips.

      :type: Literal['ALL_WAVEFORMS', 'DEFAULT_WAVEFORMS', 'NO_WAVEFORMS']

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

   - :class:`SpaceSequenceEditor.timeline_overlay`

