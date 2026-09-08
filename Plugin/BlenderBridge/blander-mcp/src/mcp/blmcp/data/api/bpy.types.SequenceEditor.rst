SequenceEditor(bpy_struct)
==========================

.. currentmodule:: bpy.types

base class --- :class:`bpy_struct`

.. class:: SequenceEditor(bpy_struct)

   Sequence editing data for a Scene data-block

   .. attribute:: active_strip

      Sequencer's active strip

      :type: :class:`Strip` | None

   .. data:: cache_final_size

      Size of final rendered images cache in megabytes (in [-inf, inf], default 0, readonly)

      :type: int

   .. data:: cache_raw_size

      Size of raw source images cache in megabytes (in [-inf, inf], default 0, readonly)

      :type: int

   .. data:: channels

      (default None, readonly)

      :type: :class:`bpy_prop_collection`\ [:class:`SequenceTimelineChannel`]

   .. data:: meta_stack

      Meta strip stack, last is currently edited meta strip (default None, readonly)

      :type: :class:`bpy_prop_collection`\ [:class:`Strip`]

   .. attribute:: overlay_frame

      Number of frames to offset (in [-inf, inf], default 0)

      :type: int

   .. attribute:: proxy_dir

      (default "", never None, blend relative ``//`` prefix supported)

      :type: str

   .. attribute:: proxy_storage

      How to store proxies for this project (default ``'PER_STRIP'``)

      - ``PER_STRIP``
        Per Strip -- Store proxies using per strip settings.
      - ``PROJECT``
        Project -- Store proxies using project directory.

      :type: Literal['PER_STRIP', 'PROJECT']

   .. data:: selected_retiming_keys

      (default False, readonly)

      :type: bool

   .. attribute:: show_missing_media

      Render missing images/movies with a solid magenta color (default False)

      :type: bool

   .. attribute:: show_overlay_frame

      Partial overlay on top of the sequencer with a frame offset (default False)

      :type: bool

   .. data:: strips

      Top-level strips only (default None, readonly)

      :type: :class:`StripsTopLevel`\ [:class:`Strip`]

   .. data:: strips_all

      All strips, recursively including those inside metastrips (default None, readonly)

      :type: :class:`bpy_prop_collection`\ [:class:`Strip`]

   .. attribute:: use_cache_final

      Cache final image for each frame (default False)

      :type: bool

   .. attribute:: use_cache_raw

      Cache raw images read from disk, for faster tweaking of strip parameters at the cost of memory usage (default False)

      :type: bool

   .. attribute:: use_overlay_frame_lock

      (default False)

      :type: bool

   .. attribute:: use_prefetch

      Render frames ahead of current frame in the background for faster playback (default False)

      :type: bool

   .. method:: display_stack(meta_sequence)

      Display strips stack

      :param meta_sequence: Meta Strip, Meta to display its stack
      :type meta_sequence: :class:`Strip` | None

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

   - :class:`Scene.sequence_editor`
   - :class:`Scene.sequence_editor_create`

