SpaceClipEditor(Space)
======================

.. currentmodule:: bpy.types

base classes --- :class:`bpy_struct`, :class:`Space`

.. class:: SpaceClipEditor(Space)

   Clip editor space data

   .. attribute:: annotation_source

      Where the annotation comes from (default ``'CLIP'``)

      - ``CLIP``
        Clip -- Show annotation data-block which belongs to movie clip.
      - ``TRACK``
        Track -- Show annotation data-block which belongs to active track.

      :type: Literal['CLIP', 'TRACK']

   .. attribute:: blend_factor

      Overlay blending factor of rasterized mask (in [0, 1], default 0.7)

      :type: float

   .. attribute:: clip

      Movie clip displayed and edited in this space

      :type: :class:`MovieClip` | None

   .. data:: clip_user

      Parameters defining which frame of the movie clip is displayed (readonly, never None)

      :type: :class:`MovieClipUser`

   .. attribute:: cursor_location

      2D cursor location for this view (array of 2 items, in [-inf, inf], default (0.0, 0.0))

      :type: :class:`mathutils.Vector`

   .. attribute:: lock_selection

      Lock viewport to selected markers during playback (default False)

      :type: bool

   .. attribute:: lock_time_cursor

      Lock curves view to time cursor during playback and tracking (default False)

      :type: bool

   .. attribute:: mask

      Mask displayed and edited in this space

      :type: :class:`Mask` | None

   .. attribute:: mask_display_type

      Display type for mask splines (default ``'OUTLINE'``)

      - ``OUTLINE``
        Outline -- Display white edges with black outline.
      - ``DASH``
        Dash -- Display dashed black-white edges.
      - ``BLACK``
        Black -- Display black edges.
      - ``WHITE``
        White -- Display white edges.

      :type: Literal['OUTLINE', 'DASH', 'BLACK', 'WHITE']

   .. attribute:: mask_overlay_mode

      Overlay mode of rasterized mask (default ``'ALPHACHANNEL'``)

      - ``ALPHACHANNEL``
        Alpha Channel -- Show alpha channel of the mask.
      - ``COMBINED``
        Combined -- Combine space background image with the mask.

      :type: Literal['ALPHACHANNEL', 'COMBINED']

   .. attribute:: mode

      Editing context being displayed (default ``'TRACKING'``)

      :type: Literal[:ref:`rna_enum_clip_editor_mode_items`]

   .. data:: overlay

      Settings for display of overlays in the Movie Clip editor (readonly, never None)

      :type: :class:`SpaceClipOverlay`

   .. attribute:: path_length

      Length of displaying path, in frames (in [0, inf], default 20)

      :type: int

   .. attribute:: pivot_point

      Pivot center for rotation/scaling (default ``'MEDIAN_POINT'``)

      - ``BOUNDING_BOX_CENTER``
        Bounding Box Center -- Pivot around bounding box center of selected object(s).
      - ``CURSOR``
        2D Cursor -- Pivot around the 2D cursor.
      - ``INDIVIDUAL_ORIGINS``
        Individual Origins -- Pivot around each object's own origin.
      - ``MEDIAN_POINT``
        Median Point -- Pivot around the median point of selected objects.

      :type: Literal['BOUNDING_BOX_CENTER', 'CURSOR', 'INDIVIDUAL_ORIGINS', 'MEDIAN_POINT']

   .. data:: scopes

      Scopes to visualize movie clip statistics (readonly)

      :type: :class:`MovieClipScopes` | None

   .. attribute:: show_annotation

      Show annotations for this view (default True)

      :type: bool

   .. attribute:: show_blue_channel

      Show blue channel in the frame (default True)

      :type: bool

   .. attribute:: show_bundles

      Show projection of 3D markers into footage (default False)

      :type: bool

   .. attribute:: show_disabled

      Show disabled tracks from the footage (default True)

      :type: bool

   .. attribute:: show_filters

      Show filters for graph editor (default False)

      :type: bool

   .. attribute:: show_gizmo

      Show gizmos of all types (default True)

      :type: bool

   .. attribute:: show_gizmo_navigate

      Viewport navigation gizmo (default True)

      :type: bool

   .. attribute:: show_graph_frames

      Show curve for per-frame average error (camera motion should be solved first) (default True)

      :type: bool

   .. attribute:: show_graph_hidden

      Include channels from objects/bone that are not visible (default False)

      :type: bool

   .. attribute:: show_graph_only_selected

      Only include channels relating to selected objects and data (default False)

      :type: bool

   .. attribute:: show_graph_tracks_error

      Display the reprojection error curve for selected tracks (default False)

      :type: bool

   .. attribute:: show_graph_tracks_motion

      Display speed curves for the selected tracks (default True)

      :type: bool

   .. attribute:: show_green_channel

      Show green channel in the frame (default True)

      :type: bool

   .. attribute:: show_grid

      Show grid showing lens distortion (default False)

      :type: bool

   .. attribute:: show_marker_pattern

      Show pattern boundbox for markers (default True)

      :type: bool

   .. attribute:: show_marker_search

      Show search boundbox for markers (default False)

      :type: bool

   .. attribute:: show_mask_overlay

      (default False)

      :type: bool

   .. attribute:: show_mask_spline

      (default True)

      :type: bool

   .. attribute:: show_metadata

      Show metadata of clip (default False)

      :type: bool

   .. attribute:: show_names

      Show track names and status (default False)

      :type: bool

   .. attribute:: show_red_channel

      Show red channel in the frame (default True)

      :type: bool

   .. attribute:: show_region_channels

      (default False)

      :type: bool

   .. attribute:: show_region_hud

      (default False)

      :type: bool

   .. attribute:: show_region_toolbar

      (default False)

      :type: bool

   .. attribute:: show_region_ui

      (default False)

      :type: bool

   .. attribute:: show_seconds

      Show timing as a timecode instead of frames (default False)

      :type: bool

   .. attribute:: show_stable

      Show stable footage in editor (if stabilization is enabled) (default False)

      :type: bool

   .. attribute:: show_tiny_markers

      Show markers in a more compact manner (default False)

      :type: bool

   .. attribute:: show_track_path

      Show path of how track moves (default True)

      :type: bool

   .. attribute:: use_grayscale_preview

      Display frame in grayscale mode (default False)

      :type: bool

   .. attribute:: use_manual_calibration

      Use manual calibration helpers (default False)

      :type: bool

   .. attribute:: use_mute_footage

      Mute footage and show black background instead (default False)

      :type: bool

   .. attribute:: view

      Type of the clip editor view (default ``'CLIP'``)

      - ``CLIP``
        Clip -- Show editing clip preview.
      - ``GRAPH``
        Graph -- Show graph view for active element.
      - ``DOPESHEET``
        Dope Sheet -- Dope Sheet view for tracking data.

      :type: Literal['CLIP', 'GRAPH', 'DOPESHEET']

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

