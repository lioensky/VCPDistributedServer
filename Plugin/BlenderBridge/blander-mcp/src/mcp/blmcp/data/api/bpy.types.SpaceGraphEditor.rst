SpaceGraphEditor(Space)
=======================

.. currentmodule:: bpy.types

base classes --- :class:`bpy_struct`, :class:`Space`

.. class:: SpaceGraphEditor(Space)

   Graph Editor space data

   .. attribute:: cursor_position_x

      Graph Editor 2D-Value cursor - X-Value component (in [-inf, inf], default 0.0)

      :type: float

   .. attribute:: cursor_position_y

      Graph Editor 2D-Value cursor - Y-Value component (in [-inf, inf], default 0.0)

      :type: float

   .. data:: dopesheet

      Settings for filtering animation data (readonly)

      :type: :class:`DopeSheet` | None

   .. data:: has_ghost_curves

      Graph Editor instance has some ghost curves stored (default False, readonly)

      :type: bool

   .. attribute:: mode

      Editing context being displayed (default ``'FCURVES'``)

      :type: Literal[:ref:`rna_enum_space_graph_mode_items`]

   .. attribute:: pivot_point

      Pivot center for rotation/scaling (default ``'BOUNDING_BOX_CENTER'``)

      :type: Literal['BOUNDING_BOX_CENTER', 'CURSOR', 'INDIVIDUAL_ORIGINS']

   .. attribute:: show_cursor

      Show 2D cursor (default True)

      :type: bool

   .. attribute:: show_extrapolation

      (default True)

      :type: bool

   .. attribute:: show_handles

      Show handles of Bézier control points (default True)

      :type: bool

   .. attribute:: show_markers

      If any exists, show markers in a separate row at the bottom of the editor (default False)

      :type: bool

   .. attribute:: show_region_channels

      (default False)

      :type: bool

   .. attribute:: show_region_footer

      (default False)

      :type: bool

   .. attribute:: show_region_hud

      (default False)

      :type: bool

   .. attribute:: show_region_ui

      (default False)

      :type: bool

   .. attribute:: show_seconds

      Show timing as a timecode instead of frames (default False)

      :type: bool

   .. attribute:: show_sliders

      Show sliders beside F-Curve channels (default False)

      :type: bool

   .. attribute:: use_auto_lock_translation_axis

      Automatically locks the movement of keyframes to the dominant axis (default False)

      :type: bool

   .. attribute:: use_auto_merge_keyframes

      Automatically merge nearby keyframes (default True)

      :type: bool

   .. attribute:: use_auto_normalization

      Automatically recalculate curve normalization on every curve edit (default True)

      :type: bool

   .. attribute:: use_normalization

      Display curves in normalized range from -1 to 1, for easier editing of multiple curves with different ranges (default False)

      :type: bool

   .. attribute:: use_only_selected_keyframe_handles

      Only show and edit handles of selected keyframes (default False)

      :type: bool

   .. attribute:: use_realtime_update

      When transforming keyframes, changes to the animation data are flushed to other views (default True)

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


   .. classmethod:: draw_handler_add(callback, args, region_type, draw_type)
   
      Add a new draw handler to this space type.
      It will be called every time the specified region in the space type will be drawn.
      Note: All arguments are positional only for now.
   
      :param callback:
         A function that will be called when the region is drawn.
         It gets the specified arguments as input, it's return value is ignored.
      :type callback: Callable[..., Any]
      :param args: Arguments that will be passed to the callback.
      :type args: tuple[Any, ...]
      :param region_type: The region type the callback draws in; usually ``WINDOW``. (:class:`bpy.types.Region.type`)
      :type region_type: str
      :param draw_type: Usually ``POST_PIXEL`` for 2D drawing and ``POST_VIEW`` for 3D drawing. In some cases ``PRE_VIEW`` can be used. ``BACKDROP`` can be used for backdrops in the node editor.
      :type draw_type: str
      :return: Handler that can be removed later on.
      :rtype: object


   .. classmethod:: draw_handler_remove(handler, region_type)
   
      Remove a draw handler that was added previously.
   
      :param handler: The draw handler that should be removed.
      :type handler: object
      :param region_type: Region type the callback was added to.
      :type region_type: str


Inherited Properties
--------------------

.. hlist::
   :columns: 2

   - :class:`bpy_struct.id_data`
   - :class:`Space.type`
   - :class:`Space.show_locked_time`
   - :class:`Space.show_region_header`

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
   - :class:`Space.bl_rna_get_subclass`
   - :class:`Space.bl_rna_get_subclass_py`
   - :class:`Space.draw_handler_add`
   - :class:`Space.draw_handler_remove`

