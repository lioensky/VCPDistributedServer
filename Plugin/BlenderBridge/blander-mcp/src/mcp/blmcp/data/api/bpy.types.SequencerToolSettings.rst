SequencerToolSettings(bpy_struct)
=================================

.. currentmodule:: bpy.types

base class --- :class:`bpy_struct`

.. class:: SequencerToolSettings(bpy_struct)


   .. attribute:: fit_method

      Scale fit method (default ``'FIT'``)

      :type: Literal[:ref:`rna_enum_strip_scale_method_items`]

   .. attribute:: overlap_mode

      How to resolve overlap after transformation (default ``'EXPAND'``)

      - ``EXPAND``
        Expand -- Move strips so transformed strips fit.
      - ``OVERWRITE``
        Overwrite -- Trim or split strips to resolve overlap.
      - ``SHUFFLE``
        Shuffle -- Move transformed strips to nearest free space to resolve overlap.

      :type: Literal['EXPAND', 'OVERWRITE', 'SHUFFLE']

   .. attribute:: pivot_point

      Rotation or scaling pivot point (default ``'CENTER'``)

      - ``CENTER``
        Bounding Box Center.
      - ``MEDIAN``
        Median Point.
      - ``CURSOR``
        2D Cursor -- Pivot around the 2D cursor.
      - ``INDIVIDUAL_ORIGINS``
        Individual Origins -- Pivot around each selected island's own median point.

      :type: Literal['CENTER', 'MEDIAN', 'CURSOR', 'INDIVIDUAL_ORIGINS']

   .. attribute:: snap_distance

      Maximum distance for snapping in pixels (in [-inf, inf], default 15)

      :type: int

   .. attribute:: snap_ignore_muted

      Don't snap to hidden strips (default False)

      :type: bool

   .. attribute:: snap_ignore_sound

      Don't snap to sound strips (default False)

      :type: bool

   .. attribute:: snap_to_borders

      Snap to preview borders (default False)

      :type: bool

   .. attribute:: snap_to_center

      Snap to preview center (default False)

      :type: bool

   .. attribute:: snap_to_current_frame

      Snap to current frame (default False)

      :type: bool

   .. attribute:: snap_to_frame_range

      Snap to preview or scene start and end frame (default False)

      :type: bool

   .. attribute:: snap_to_hold_offset

      Snap to underlying strip content start and end in cases where the strip length extends beyond this range, producing holds (default False)

      :type: bool

   .. attribute:: snap_to_markers

      Snap to markers (default False)

      :type: bool

   .. attribute:: snap_to_retiming_keys

      Snap to retiming keys (default False)

      :type: bool

   .. attribute:: snap_to_strips_preview

      Snap to borders and origins of deselected, visible strips (default False)

      :type: bool

   .. attribute:: use_snap_current_frame_to_strips

      Snap current frame to strip start or end (default False)

      :type: bool

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

   - :class:`ToolSettings.sequencer_tool_settings`

