Clip Operators
==============

.. module:: bpy.ops.clip

.. function:: add_marker(*, location=(0.0, 0.0))

   Place new marker at specified location

   :param location: Location, Location of marker on frame (array of 2 items, in [-inf, inf], optional)
   :type location: :class:`mathutils.Vector` | Sequence[float]
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: add_marker_at_click()

   Place new marker at the desired (clicked) position

   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]
.. function:: add_marker_move(*, CLIP_OT_add_marker={}, TRANSFORM_OT_translate={})

   Add new marker and move it on movie

   :param CLIP_OT_add_marker: Add Marker, Place new marker at specified location (optional, :func:`bpy.ops.clip.add_marker` keyword arguments)
   :type CLIP_OT_add_marker: dict[str, Any]
   :param TRANSFORM_OT_translate: Move, Move selected items (optional, :func:`bpy.ops.transform.translate` keyword arguments)
   :type TRANSFORM_OT_translate: dict[str, Any]
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: add_marker_slide(*, CLIP_OT_add_marker={}, TRANSFORM_OT_translate={})

   Add new marker and slide it with mouse until mouse button release

   :param CLIP_OT_add_marker: Add Marker, Place new marker at specified location (optional, :func:`bpy.ops.clip.add_marker` keyword arguments)
   :type CLIP_OT_add_marker: dict[str, Any]
   :param TRANSFORM_OT_translate: Move, Move selected items (optional, :func:`bpy.ops.transform.translate` keyword arguments)
   :type TRANSFORM_OT_translate: dict[str, Any]
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: apply_solution_scale(*, distance=0.0)

   Apply scale on solution itself to make distance between selected tracks equals to desired

   :param distance: Distance, Distance between selected tracks (in [-inf, inf], optional)
   :type distance: float
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: average_tracks(*, keep_original=True)

   Average selected tracks into active

   :param keep_original: Keep Original, Keep original tracks (optional)
   :type keep_original: bool
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: bundles_to_mesh()

   Create vertex cloud using coordinates of reconstructed tracks

   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]
   :File: `startup/bl_operators/clip.py\:292 <https://projects.blender.org/blender/blender/src/branch/main/scripts/startup/bl_operators/clip.py#L292>`__

.. function:: camera_preset_add(*, name="", remove_name=False, remove_active=False, use_focal_length=True)

   Add or remove a Tracking Camera Intrinsics Preset

   :param name: Name, Name of the preset, used to make the path name (optional, never None)
   :type name: str
   :param remove_name: remove_name, (optional)
   :type remove_name: bool
   :param remove_active: remove_active, (optional)
   :type remove_active: bool
   :param use_focal_length: Include Focal Length, Include focal length into the preset (optional)
   :type use_focal_length: bool
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]
   :File: `startup/bl_operators/presets.py\:119 <https://projects.blender.org/blender/blender/src/branch/main/scripts/startup/bl_operators/presets.py#L119>`__


.. function:: change_frame(*, frame=0)

   Interactively change the current frame number

   :param frame: Frame, (in [-1048574, 1048574], optional)
   :type frame: int
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: clean_tracks(*, frames=0, error=0.0, action='SELECT')

   Clean tracks with high error values or few frames

   :param frames: Tracked Frames, Affect tracks which are tracked less than the specified number of frames (in [0, inf], optional)
   :type frames: int
   :param error: Reprojection Error, Affect tracks which have a larger reprojection error (in [0, inf], optional)
   :type error: float
   :param action: Action, Cleanup action to execute (optional)

      - ``SELECT``
        Select -- Select unclean tracks.
      - ``DELETE_TRACK``
        Delete Track -- Delete unclean tracks.
      - ``DELETE_SEGMENTS``
        Delete Segments -- Delete unclean segments of tracks.
   :type action: Literal['SELECT', 'DELETE_TRACK', 'DELETE_SEGMENTS']
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: clear_solution()

   Clear all calculated data

   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]
.. function:: clear_track_path(*, action='REMAINED', clear_active=False)

   Clear tracks after/before current position or clear the whole track

   :param action: Action, Clear action to execute (optional)

      - ``UPTO``
        Clear Up To -- Clear path up to current frame.
      - ``REMAINED``
        Clear Remained -- Clear path at remaining frames (after current).
      - ``ALL``
        Clear All -- Clear the whole path.
   :type action: Literal['UPTO', 'REMAINED', 'ALL']
   :param clear_active: Clear Active, Clear active track only instead of all selected tracks (optional)
   :type clear_active: bool
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: constraint_to_fcurve()

   Create F-Curves for object which will copy object's movement caused by this constraint

   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]
   :File: `startup/bl_operators/clip.py\:530 <https://projects.blender.org/blender/blender/src/branch/main/scripts/startup/bl_operators/clip.py#L530>`__

.. function:: copy_tracks()

   Copy the selected tracks to the internal clipboard

   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]
.. function:: create_plane_track()

   Create new plane track out of selected point tracks

   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]
.. function:: cursor_set(*, location=(0.0, 0.0))

   Set 2D cursor location

   :param location: Location, Cursor location in normalized clip coordinates (array of 2 items, in [-inf, inf], optional)
   :type location: :class:`mathutils.Vector` | Sequence[float]
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: delete_marker(*, confirm=True)

   Delete marker for current frame from selected tracks

   :param confirm: Confirm, Prompt for confirmation (optional)
   :type confirm: bool
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: delete_proxy()

   Delete movie clip proxy files from the hard drive

   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]
   :File: `startup/bl_operators/clip.py\:359 <https://projects.blender.org/blender/blender/src/branch/main/scripts/startup/bl_operators/clip.py#L359>`__

.. function:: delete_track(*, confirm=True)

   Delete selected tracks

   :param confirm: Confirm, Prompt for confirmation (optional)
   :type confirm: bool
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: detect_features(*, placement='FRAME', margin=16, threshold=0.5, min_distance=120)

   Automatically detect features and place markers to track

   :param placement: Placement, Placement for detected features (optional)

      - ``FRAME``
        Whole Frame -- Place markers across the whole frame.
      - ``INSIDE_GPENCIL``
        Inside Annotated Area -- Place markers only inside areas outlined with the Annotation tool.
      - ``OUTSIDE_GPENCIL``
        Outside Annotated Area -- Place markers only outside areas outlined with the Annotation tool.
   :type placement: Literal['FRAME', 'INSIDE_GPENCIL', 'OUTSIDE_GPENCIL']
   :param margin: Margin, Only features further than margin pixels from the image edges are considered (in [0, inf], optional)
   :type margin: int
   :param threshold: Threshold, Threshold level to consider feature good enough for tracking (in [0.0001, inf], optional)
   :type threshold: float
   :param min_distance: Distance, Minimal distance accepted between two features (in [0, inf], optional)
   :type min_distance: int
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: disable_markers(*, action='DISABLE')

   Disable/enable selected markers

   :param action: Action, Disable action to execute (optional)

      - ``DISABLE``
        Disable -- Disable selected markers.
      - ``ENABLE``
        Enable -- Enable selected markers.
      - ``TOGGLE``
        Toggle -- Toggle disabled flag for selected markers.
   :type action: Literal['DISABLE', 'ENABLE', 'TOGGLE']
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: dopesheet_select_channel(*, location=(0.0, 0.0), extend=False)

   Select movie tracking channel

   :param location: Location, Mouse location to select channel (array of 2 items, in [-inf, inf], optional)
   :type location: :class:`mathutils.Vector` | Sequence[float]
   :param extend: Extend, Extend selection rather than clearing the existing selection (optional)
   :type extend: bool
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: dopesheet_view_all()

   Reset viewable area to show full keyframe range

   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]
.. function:: filter_tracks(*, track_threshold=5.0)

   Filter tracks which has weirdly looking spikes in motion curves

   :param track_threshold: Track Threshold, Filter Threshold to select problematic tracks (in [-inf, inf], optional)
   :type track_threshold: float
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]
   :File: `startup/bl_operators/clip.py\:206 <https://projects.blender.org/blender/blender/src/branch/main/scripts/startup/bl_operators/clip.py#L206>`__


.. function:: frame_jump(*, position='PATHSTART')

   Jump to special frame

   :param position: Position, Position to jump to (optional)

      - ``PATHSTART``
        Path Start -- Jump to start of current path.
      - ``PATHEND``
        Path End -- Jump to end of current path.
      - ``FAILEDPREV``
        Previous Failed -- Jump to previous failed frame.
      - ``FAILNEXT``
        Next Failed -- Jump to next failed frame.
   :type position: Literal['PATHSTART', 'PATHEND', 'FAILEDPREV', 'FAILNEXT']
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: graph_center_current_frame()

   Scroll view so current frame would be centered

   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]
.. function:: graph_delete_curve(*, confirm=True)

   Delete track corresponding to the selected curve

   :param confirm: Confirm, Prompt for confirmation (optional)
   :type confirm: bool
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: graph_delete_knot()

   Delete curve knots

   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]
.. function:: graph_disable_markers(*, action='DISABLE')

   Disable/enable selected markers

   :param action: Action, Disable action to execute (optional)

      - ``DISABLE``
        Disable -- Disable selected markers.
      - ``ENABLE``
        Enable -- Enable selected markers.
      - ``TOGGLE``
        Toggle -- Toggle disabled flag for selected markers.
   :type action: Literal['DISABLE', 'ENABLE', 'TOGGLE']
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: graph_select(*, location=(0.0, 0.0), extend=False)

   Select graph curves

   :param location: Location, Mouse location to select nearest entity (array of 2 items, in [-inf, inf], optional)
   :type location: :class:`mathutils.Vector` | Sequence[float]
   :param extend: Extend, Extend selection rather than clearing the existing selection (optional)
   :type extend: bool
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: graph_select_all_markers(*, action='TOGGLE')

   Change selection of all markers of active track

   :param action: Action, Selection action to execute (optional)

      - ``TOGGLE``
        Toggle -- Toggle selection for all elements.
      - ``SELECT``
        Select -- Select all elements.
      - ``DESELECT``
        Deselect -- Deselect all elements.
      - ``INVERT``
        Invert -- Invert selection of all elements.
   :type action: Literal['TOGGLE', 'SELECT', 'DESELECT', 'INVERT']
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: graph_select_box(*, xmin=0, xmax=0, ymin=0, ymax=0, wait_for_input=True, deselect=False, extend=True)

   Select curve points using box selection

   :param xmin: X Min, (in [-inf, inf], optional)
   :type xmin: int
   :param xmax: X Max, (in [-inf, inf], optional)
   :type xmax: int
   :param ymin: Y Min, (in [-inf, inf], optional)
   :type ymin: int
   :param ymax: Y Max, (in [-inf, inf], optional)
   :type ymax: int
   :param wait_for_input: Wait for Input, (optional)
   :type wait_for_input: bool
   :param deselect: Deselect, Deselect rather than select items (optional)
   :type deselect: bool
   :param extend: Extend, Extend selection instead of deselecting everything first (optional)
   :type extend: bool
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: graph_view_all()

   View all curves in editor

   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]
.. function:: hide_tracks(*, unselected=False)

   Hide selected tracks

   :param unselected: Unselected, Hide unselected tracks (optional)
   :type unselected: bool
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: hide_tracks_clear()

   Clear hide selected tracks

   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]
.. function:: join_tracks()

   Join selected tracks

   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]
.. function:: keyframe_delete()

   Delete a keyframe from selected tracks at current frame

   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]
.. function:: keyframe_insert()

   Insert a keyframe to selected tracks at current frame

   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]
.. function:: lock_selection_toggle()

   Toggle Lock Selection option of the current clip editor

   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]
.. function:: lock_tracks(*, action='LOCK')

   Lock/unlock selected tracks

   :param action: Action, Lock action to execute (optional)

      - ``LOCK``
        Lock -- Lock selected tracks.
      - ``UNLOCK``
        Unlock -- Unlock selected tracks.
      - ``TOGGLE``
        Toggle -- Toggle locked flag for selected tracks.
   :type action: Literal['LOCK', 'UNLOCK', 'TOGGLE']
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: mode_set(*, mode='TRACKING')

   Set the clip interaction mode

   :param mode: Mode, (optional)
   :type mode: Literal[:ref:`rna_enum_clip_editor_mode_items`]
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: new_image_from_plane_marker()

   Create new image from the content of the plane marker

   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]
.. function:: open(*, directory="", files=None, hide_props_region=True, check_existing=False, filter_blender=False, filter_backup=False, filter_image=True, filter_movie=True, filter_python=False, filter_font=False, filter_sound=False, filter_text=False, filter_archive=False, filter_btx=False, filter_alembic=False, filter_usd=False, filter_obj=False, filter_volume=False, filter_folder=True, filter_blenlib=False, filemode=9, relative_path=True, show_multiview=False, use_multiview=False, display_type='DEFAULT', sort_method='')

   Load a sequence of frames or a movie file

   :param directory: Directory, Directory of the file (optional, never None)
   :type directory: str
   :param files: Files, (optional)
   :type files: :class:`bpy_prop_collection`\ [:class:`OperatorFileListElement`] | None
   :param hide_props_region: Hide Operator Properties, Collapse the region displaying the operator settings (optional)
   :type hide_props_region: bool
   :param check_existing: Check Existing, Check and warn on overwriting existing files (optional)
   :type check_existing: bool
   :param filter_blender: Filter .blend files, (optional)
   :type filter_blender: bool
   :param filter_backup: Filter backup .blend files, (optional)
   :type filter_backup: bool
   :param filter_image: Filter image files, (optional)
   :type filter_image: bool
   :param filter_movie: Filter movie files, (optional)
   :type filter_movie: bool
   :param filter_python: Filter Python files, (optional)
   :type filter_python: bool
   :param filter_font: Filter font files, (optional)
   :type filter_font: bool
   :param filter_sound: Filter sound files, (optional)
   :type filter_sound: bool
   :param filter_text: Filter text files, (optional)
   :type filter_text: bool
   :param filter_archive: Filter archive files, (optional)
   :type filter_archive: bool
   :param filter_btx: Filter btx files, (optional)
   :type filter_btx: bool
   :param filter_alembic: Filter Alembic files, (optional)
   :type filter_alembic: bool
   :param filter_usd: Filter USD files, (optional)
   :type filter_usd: bool
   :param filter_obj: Filter OBJ files, (optional)
   :type filter_obj: bool
   :param filter_volume: Filter OpenVDB volume files, (optional)
   :type filter_volume: bool
   :param filter_folder: Filter folders, (optional)
   :type filter_folder: bool
   :param filter_blenlib: Filter Blender IDs, (optional)
   :type filter_blenlib: bool
   :param filemode: File Browser Mode, The setting for the file browser mode to load a .blend file, a library or a special file (in [1, 9], optional)
   :type filemode: int
   :param relative_path: Relative Path, Select the file relative to the blend file (optional)
   :type relative_path: bool
   :param show_multiview: Enable Multi-View, (optional)
   :type show_multiview: bool
   :param use_multiview: Use Multi-View, (optional)
   :type use_multiview: bool
   :param display_type: Display Type, (optional)

      - ``DEFAULT``
        Default -- Automatically determine display type for files.
      - ``LIST_VERTICAL``
        Short List -- Display files as short list.
      - ``LIST_HORIZONTAL``
        Long List -- Display files as a detailed list.
      - ``THUMBNAIL``
        Thumbnails -- Display files as thumbnails.
   :type display_type: Literal['DEFAULT', 'LIST_VERTICAL', 'LIST_HORIZONTAL', 'THUMBNAIL']
   :param sort_method: File sorting mode, (optional)

      - ``DEFAULT``
        Default -- Automatically determine sort method for files.
      - ``FILE_SORT_ALPHA``
        Name -- Sort the file list alphabetically.
      - ``FILE_SORT_EXTENSION``
        Extension -- Sort the file list by extension/type.
      - ``FILE_SORT_TIME``
        Modified Date -- Sort files by modification time.
      - ``FILE_SORT_SIZE``
        Size -- Sort files by size.
      - ``ASSET_CATALOG``
        Asset Catalog -- Sort the asset list so that assets in the same catalog are kept together. Within a single catalog, assets are ordered by name. The catalogs are in order of the flattened catalog hierarchy..
   :type sort_method: Literal['', 'DEFAULT', 'FILE_SORT_ALPHA', 'FILE_SORT_EXTENSION', 'FILE_SORT_TIME', 'FILE_SORT_SIZE', 'ASSET_CATALOG']
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: paste_tracks()

   Paste tracks from the internal clipboard

   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]
.. function:: prefetch()

   Prefetch frames from disk for faster playback/tracking

   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]
.. function:: rebuild_proxy()

   Rebuild all selected proxies and timecode indices in the background

   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]
.. function:: refine_markers(*, backwards=False)

   Refine selected markers positions by running the tracker from track's reference to current frame

   :param backwards: Backwards, Do backwards tracking (optional)
   :type backwards: bool
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: reload()

   Reload clip

   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]
.. function:: select(*, extend=False, deselect_all=False, location=(0.0, 0.0))

   Select tracking markers

   :param extend: Extend, Extend selection rather than clearing the existing selection (optional)
   :type extend: bool
   :param deselect_all: Deselect On Nothing, Deselect all when nothing under the cursor (optional)
   :type deselect_all: bool
   :param location: Location, Mouse location in normalized coordinates, 0.0 to 1.0 is within the image bounds (array of 2 items, in [-inf, inf], optional)
   :type location: :class:`mathutils.Vector` | Sequence[float]
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: select_all(*, action='TOGGLE')

   Change selection of all tracking markers

   :param action: Action, Selection action to execute (optional)

      - ``TOGGLE``
        Toggle -- Toggle selection for all elements.
      - ``SELECT``
        Select -- Select all elements.
      - ``DESELECT``
        Deselect -- Deselect all elements.
      - ``INVERT``
        Invert -- Invert selection of all elements.
   :type action: Literal['TOGGLE', 'SELECT', 'DESELECT', 'INVERT']
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: select_box(*, xmin=0, xmax=0, ymin=0, ymax=0, wait_for_input=True, mode='SET')

   Select markers using box selection

   :param xmin: X Min, (in [-inf, inf], optional)
   :type xmin: int
   :param xmax: X Max, (in [-inf, inf], optional)
   :type xmax: int
   :param ymin: Y Min, (in [-inf, inf], optional)
   :type ymin: int
   :param ymax: Y Max, (in [-inf, inf], optional)
   :type ymax: int
   :param wait_for_input: Wait for Input, (optional)
   :type wait_for_input: bool
   :param mode: Mode, (optional)

      - ``SET``
        Set -- Set a new selection.
      - ``ADD``
        Extend -- Extend existing selection.
      - ``SUB``
        Subtract -- Subtract existing selection.
   :type mode: Literal['SET', 'ADD', 'SUB']
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: select_circle(*, x=0, y=0, radius=25, wait_for_input=True, mode='SET')

   Select markers using circle selection

   :param x: X, (in [-inf, inf], optional)
   :type x: int
   :param y: Y, (in [-inf, inf], optional)
   :type y: int
   :param radius: Radius, (in [1, inf], optional)
   :type radius: int
   :param wait_for_input: Wait for Input, (optional)
   :type wait_for_input: bool
   :param mode: Mode, (optional)

      - ``SET``
        Set -- Set a new selection.
      - ``ADD``
        Extend -- Extend existing selection.
      - ``SUB``
        Subtract -- Subtract existing selection.
   :type mode: Literal['SET', 'ADD', 'SUB']
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: select_grouped(*, group='ESTIMATED')

   Select all tracks from specified group

   :param group: Group, Select tracks by group (optional)

      - ``KEYFRAMED``
        Keyframed Tracks -- Select all keyframed tracks.
      - ``ESTIMATED``
        Estimated Tracks -- Select all estimated tracks.
      - ``TRACKED``
        Tracked Tracks -- Select all tracked tracks.
      - ``LOCKED``
        Locked Tracks -- Select all locked tracks.
      - ``DISABLED``
        Disabled Tracks -- Select all disabled tracks.
      - ``COLOR``
        Tracks with Same Color -- Select all tracks with same color as active track.
      - ``FAILED``
        Failed Tracks -- Select all tracks which failed to be reconstructed.
   :type group: Literal['KEYFRAMED', 'ESTIMATED', 'TRACKED', 'LOCKED', 'DISABLED', 'COLOR', 'FAILED']
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: select_lasso(*, path=None, use_smooth_stroke=False, smooth_stroke_factor=0.75, smooth_stroke_radius=35, mode='SET')

   Select markers using lasso selection

   :param path: Path, (optional)
   :type path: :class:`bpy_prop_collection`\ [:class:`OperatorMousePath`] | None
   :param use_smooth_stroke: Stabilize Stroke, Selection lags behind mouse and follows a smoother path (optional)
   :type use_smooth_stroke: bool
   :param smooth_stroke_factor: Smooth Stroke Factor, Higher values give a smoother stroke (in [0.5, 0.99], optional)
   :type smooth_stroke_factor: float
   :param smooth_stroke_radius: Smooth Stroke Radius, Minimum distance from last point before selection continues (in [10, 200], optional)
   :type smooth_stroke_radius: int
   :param mode: Mode, (optional)

      - ``SET``
        Set -- Set a new selection.
      - ``ADD``
        Extend -- Extend existing selection.
      - ``SUB``
        Subtract -- Subtract existing selection.
   :type mode: Literal['SET', 'ADD', 'SUB']
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: set_active_clip()

   Undocumented, consider `contributing <https://developer.blender.org/>`__.

   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]
   :File: `startup/bl_operators/clip.py\:221 <https://projects.blender.org/blender/blender/src/branch/main/scripts/startup/bl_operators/clip.py#L221>`__

.. function:: set_axis(*, axis='X')

   Set the direction of a scene axis by rotating the camera (or its parent if present). This assumes that the selected track lies on a real axis connecting it to the origin

   :param axis: Axis, Axis to use to align bundle along (optional)

      - ``X``
        X -- Align bundle to X axis.
      - ``Y``
        Y -- Align bundle to Y axis.
   :type axis: Literal['X', 'Y']
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: set_origin(*, use_median=False)

   Set active marker as origin by moving camera (or its parent if present) in 3D space

   :param use_median: Use Median, Set origin to median point of selected bundles (optional)
   :type use_median: bool
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: set_plane(*, plane='FLOOR')

   Set plane based on 3 selected bundles by moving camera (or its parent if present) in 3D space

   :param plane: Plane, Plane to be used for orientation (optional)

      - ``FLOOR``
        Floor -- Set floor plane.
      - ``WALL``
        Wall -- Set wall plane.
   :type plane: Literal['FLOOR', 'WALL']
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: set_scale(*, distance=0.0)

   Set scale of scene by scaling camera (or its parent if present)

   :param distance: Distance, Distance between selected tracks (in [-inf, inf], optional)
   :type distance: float
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: set_scene_frames()

   Set scene's start and end frame to match clip's start frame and length

   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]
.. function:: set_solution_scale(*, distance=0.0)

   Set object solution scale using distance between two selected tracks

   :param distance: Distance, Distance between selected tracks (in [-inf, inf], optional)
   :type distance: float
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: set_solver_keyframe(*, keyframe='KEYFRAME_A')

   Set keyframe used by solver

   :param keyframe: Keyframe, Keyframe to set (optional)
   :type keyframe: Literal['KEYFRAME_A', 'KEYFRAME_B']
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: set_viewport_background()

   Set current movie clip as a camera background in 3D Viewport (works only when a 3D Viewport is visible)

   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]
   :File: `startup/bl_operators/clip.py\:420 <https://projects.blender.org/blender/blender/src/branch/main/scripts/startup/bl_operators/clip.py#L420>`__

.. function:: setup_tracking_scene()

   Prepare scene for compositing 3D objects into this footage

   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]
   :File: `startup/bl_operators/clip.py\:936 <https://projects.blender.org/blender/blender/src/branch/main/scripts/startup/bl_operators/clip.py#L936>`__

.. function:: slide_marker(*, offset=(0.0, 0.0))

   Slide marker areas

   :param offset: Offset, Offset in floating-point units, 1.0 is the width and height of the image (array of 2 items, in [-inf, inf], optional)
   :type offset: :class:`mathutils.Vector` | Sequence[float]
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: slide_plane_marker()

   Slide plane marker areas

   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]
.. function:: solve_camera()

   Solve camera motion from tracks

   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]
.. function:: stabilize_2d_add()

   Add selected tracks to 2D translation stabilization

   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]
.. function:: stabilize_2d_remove()

   Remove selected track from translation stabilization

   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]
.. function:: stabilize_2d_rotation_add()

   Add selected tracks to 2D rotation stabilization

   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]
.. function:: stabilize_2d_rotation_remove()

   Remove selected track from rotation stabilization

   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]
.. function:: stabilize_2d_rotation_select()

   Select tracks which are used for rotation stabilization

   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]
.. function:: stabilize_2d_select()

   Select tracks which are used for translation stabilization

   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]
.. function:: track_color_preset_add(*, name="", remove_name=False, remove_active=False)

   Add or remove a Clip Track Color Preset

   :param name: Name, Name of the preset, used to make the path name (optional, never None)
   :type name: str
   :param remove_name: remove_name, (optional)
   :type remove_name: bool
   :param remove_active: remove_active, (optional)
   :type remove_active: bool
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]
   :File: `startup/bl_operators/presets.py\:119 <https://projects.blender.org/blender/blender/src/branch/main/scripts/startup/bl_operators/presets.py#L119>`__


.. function:: track_copy_color()

   Copy color to all selected tracks

   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]
.. function:: track_markers(*, backwards=False, sequence=False)

   Track selected markers

   :param backwards: Backwards, Do backwards tracking (optional)
   :type backwards: bool
   :param sequence: Track Sequence, Track marker during image sequence rather than single image (optional)
   :type sequence: bool
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: track_settings_as_default()

   Copy tracking settings from active track to default settings

   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]
   :File: `startup/bl_operators/clip.py\:965 <https://projects.blender.org/blender/blender/src/branch/main/scripts/startup/bl_operators/clip.py#L965>`__

.. function:: track_settings_to_track()

   Copy tracking settings from active track to selected tracks

   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]
   :File: `startup/bl_operators/clip.py\:1014 <https://projects.blender.org/blender/blender/src/branch/main/scripts/startup/bl_operators/clip.py#L1014>`__

.. function:: track_to_empty()

   Create an Empty object which will be copying movement of active track

   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]
   :File: `startup/bl_operators/clip.py\:268 <https://projects.blender.org/blender/blender/src/branch/main/scripts/startup/bl_operators/clip.py#L268>`__

.. function:: tracking_object_new()

   Add new object for tracking

   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]
.. function:: tracking_object_remove()

   Remove object for tracking

   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]
.. function:: tracking_settings_preset_add(*, name="", remove_name=False, remove_active=False)

   Add or remove a motion tracking settings preset

   :param name: Name, Name of the preset, used to make the path name (optional, never None)
   :type name: str
   :param remove_name: remove_name, (optional)
   :type remove_name: bool
   :param remove_active: remove_active, (optional)
   :type remove_active: bool
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]
   :File: `startup/bl_operators/presets.py\:119 <https://projects.blender.org/blender/blender/src/branch/main/scripts/startup/bl_operators/presets.py#L119>`__


.. function:: update_image_from_plane_marker()

   Update current image used by plane marker from the content of the plane marker

   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]
.. function:: view_all(*, fit_view=False)

   View whole image with markers

   :param fit_view: Fit View, Fit frame to the viewport (optional)
   :type fit_view: bool
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: view_center_cursor()

   Center the view so that the cursor is in the middle of the view

   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]
.. function:: view_pan(*, offset=(0.0, 0.0))

   Pan the view

   :param offset: Offset, Offset in floating-point units, 1.0 is the width and height of the image (array of 2 items, in [-inf, inf], optional)
   :type offset: :class:`mathutils.Vector` | Sequence[float]
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: view_selected()

   View all selected elements

   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]
.. function:: view_zoom(*, factor=0.0, use_cursor_init=True)

   Zoom in/out the view

   :param factor: Factor, Zoom factor, values higher than 1.0 zoom in, lower values zoom out (in [-inf, inf], optional)
   :type factor: float
   :param use_cursor_init: Use Mouse Position, Allow the initial mouse position to be used (optional)
   :type use_cursor_init: bool
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: view_zoom_in(*, location=(0.0, 0.0))

   Zoom in the view

   :param location: Location, Cursor location in screen coordinates (array of 2 items, in [-inf, inf], optional)
   :type location: :class:`mathutils.Vector` | Sequence[float]
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: view_zoom_out(*, location=(0.0, 0.0))

   Zoom out the view

   :param location: Location, Cursor location in normalized (0.0 to 1.0) coordinates (array of 2 items, in [-inf, inf], optional)
   :type location: :class:`mathutils.Vector` | Sequence[float]
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: view_zoom_ratio(*, ratio=0.0)

   Set the zoom ratio (based on clip size)

   :param ratio: Ratio, Zoom ratio, 1.0 is 1:1, higher is zoomed in, lower is zoomed out (in [-inf, inf], optional)
   :type ratio: float
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

