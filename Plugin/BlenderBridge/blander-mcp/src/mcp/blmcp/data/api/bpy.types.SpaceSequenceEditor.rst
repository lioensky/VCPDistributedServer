SpaceSequenceEditor(Space)
==========================

.. currentmodule:: bpy.types

base classes --- :class:`bpy_struct`, :class:`Space`

.. class:: SpaceSequenceEditor(Space)

   Sequence editor space data

   .. attribute:: annotation

      Annotation data for this Preview region

      :type: :class:`Annotation` | None

   .. data:: cache_overlay

      Settings for display of overlays (readonly, never None)

      :type: :class:`SequencerCacheOverlay`

   .. attribute:: cursor_location

      2D cursor location for this view (array of 2 items, in [-inf, inf], default (0.0, 0.0))

      :type: :class:`mathutils.Vector`

   .. attribute:: display_channel

      Preview all channels less than or equal to this value. 0 shows every channel, and negative values climb that many meta-strip levels if applicable, showing every channel there. (in [-5, 128], default 0)

      :type: int

   .. attribute:: display_mode

      View mode to use for displaying sequencer output (default ``'IMAGE'``)

      :type: Literal['IMAGE', 'WAVEFORM', 'RGB_PARADE', 'VECTOR_SCOPE', 'HISTOGRAM']

   .. attribute:: overlay_frame_type

      Overlay display method (default ``'RECTANGLE'``)

      - ``RECTANGLE``
        Rectangle -- Show rectangle area overlay.
      - ``REFERENCE``
        Reference -- Show reference frame only.
      - ``CURRENT``
        Current -- Show current frame only.

      :type: Literal['RECTANGLE', 'REFERENCE', 'CURRENT']

   .. attribute:: preview_channels

      Channels of the preview to display (default ``'COLOR'``)

      - ``COLOR_ALPHA``
        Color & Alpha -- Display image with RGB colors and alpha transparency.
      - ``COLOR``
        Color -- Display image with RGB colors.

      :type: Literal['COLOR_ALPHA', 'COLOR']

   .. data:: preview_overlay

      Settings for display of overlays (readonly, never None)

      :type: :class:`SequencerPreviewOverlay`

   .. attribute:: proxy_render_size

      Display preview using full resolution or different proxy resolutions (default ``'SCENE'``)

      :type: Literal['NONE', 'SCENE', 'PROXY_25', 'PROXY_50', 'PROXY_75', 'PROXY_100']

   .. attribute:: show_frames

      Display frames rather than seconds (default False)

      :type: bool

   .. attribute:: show_gizmo

      Show gizmos of all types (default True)

      :type: bool

   .. attribute:: show_gizmo_context

      Context sensitive gizmos for the active item (default True)

      :type: bool

   .. attribute:: show_gizmo_navigate

      Viewport navigation gizmo (default True)

      :type: bool

   .. attribute:: show_gizmo_tool

      Active tool gizmo (default True)

      :type: bool

   .. attribute:: show_markers

      If any exists, show markers in a separate row at the bottom of the editor (default False)

      :type: bool

   .. attribute:: show_overexposed

      Show overexposed areas with zebra stripes (in [0, 110], default 0)

      :type: int

   .. attribute:: show_overlays

      (default False)

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

   .. attribute:: show_region_tool_header

      (default False)

      :type: bool

   .. attribute:: show_region_toolbar

      (default False)

      :type: bool

   .. attribute:: show_region_ui

      (default False)

      :type: bool

   .. attribute:: show_seconds

      Show timing as a timecode instead of frames (default True)

      :type: bool

   .. attribute:: show_transform_preview

      Show a preview of the start or end frame of a strip while transforming its respective handle (default False)

      :type: bool

   .. data:: timeline_overlay

      Settings for display of overlays (readonly, never None)

      :type: :class:`SequencerTimelineOverlay`

   .. attribute:: use_clamp_view

      Limit timeline height to maximum used channel slot (default False)

      :type: bool

   .. attribute:: use_marker_sync

      Transform markers as well as strips (default False)

      :type: bool

   .. attribute:: use_proxies

      Use optimized files for faster scrubbing when available (default False)

      :type: bool

   .. attribute:: use_zoom_to_fit

      Automatically zoom preview image to make it fully fit the region (default False)

      :type: bool

   .. attribute:: view_type

      Type of the Sequencer view (sequencer, preview or both) (default ``'SEQUENCER'``)

      :type: Literal[:ref:`rna_enum_space_sequencer_view_type_items`]

   .. attribute:: zoom_percentage

      Zoom percentage (in [0.4, 80000], default 100.0)

      :type: float

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

