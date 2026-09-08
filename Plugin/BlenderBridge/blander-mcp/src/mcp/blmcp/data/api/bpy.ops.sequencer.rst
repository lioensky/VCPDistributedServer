Sequencer Operators
===================

.. module:: bpy.ops.sequencer

.. function:: add_scene_strip_from_scene_asset(*, move_strips=True, frame_start=0, channel=1, replace_sel=True, overlap=False, overlap_shuffle_override=False, skip_locked_or_muted_channels=True, asset_library_type='LOCAL', asset_library_identifier="", relative_asset_identifier="")

   Add a strip using a duplicate of this scene asset as the source

   :param move_strips: Move Strips, Automatically begin translating strips with the mouse after adding them to the timeline (optional)
   :type move_strips: bool
   :param frame_start: Start Frame, Start frame of the strip (in [-inf, inf], optional)
   :type frame_start: int
   :param channel: Channel, Channel to place this strip into (in [1, 128], optional)
   :type channel: int
   :param replace_sel: Replace Selection, Deselect previously selected strips after add operation completes (optional)
   :type replace_sel: bool
   :param overlap: Allow Overlap, Don't correct overlap on new strips (optional)
   :type overlap: bool
   :param overlap_shuffle_override: Override Overlap Shuffle Behavior, Use the overlap_mode tool settings to determine how to shuffle overlapping strips (optional)
   :type overlap_shuffle_override: bool
   :param skip_locked_or_muted_channels: Skip Locked or Muted Channels, Add strips to muted or locked channels when adding movie strips (optional)
   :type skip_locked_or_muted_channels: bool
   :param asset_library_type: Asset Library Type, (optional)
   :type asset_library_type: Literal[:ref:`rna_enum_asset_library_type_items`]
   :param asset_library_identifier: Asset Library Identifier, (optional, never None)
   :type asset_library_identifier: str
   :param relative_asset_identifier: Relative Asset Identifier, (optional, never None)
   :type relative_asset_identifier: str
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: box_blade(*, xmin=0, xmax=0, ymin=0, ymax=0, wait_for_input=True, mode='SET', type='SOFT', ignore_selection=True, ignore_connections=False, remove_gaps=True)

   Draw a box around the parts of strips you want to cut away

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
   :param type: Type, The type of split operation to perform on strips (optional)
   :type type: Literal['SOFT', 'HARD']
   :param ignore_selection: Ignore Selection, In box blade mode, make cuts to all strips, even if they are not selected (optional)
   :type ignore_selection: bool
   :param ignore_connections: Ignore Connections, Don't propagate split to connected strips (optional)
   :type ignore_connections: bool
   :param remove_gaps: Remove Gaps, In box blade mode, close gaps between cut strips, rippling later strips on the same channel (optional)
   :type remove_gaps: bool
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: change_effect_type(*, type='CROSS')

   Replace effect strip with another that takes the same number of inputs

   :param type: Type, Strip effect type (optional)

      - ``CROSS``
        Crossfade -- Fade out of one video, fading into another.
      - ``ADD``
        Add -- Add together color channels from two videos.
      - ``SUBTRACT``
        Subtract -- Subtract one strip's color from another.
      - ``ALPHA_OVER``
        Alpha Over -- Blend alpha on top of another video.
      - ``ALPHA_UNDER``
        Alpha Under -- Blend alpha below another video.
      - ``GAMMA_CROSS``
        Gamma Crossfade -- Crossfade with color correction.
      - ``MULTIPLY``
        Multiply -- Multiply color channels from two videos.
      - ``WIPE``
        Wipe -- Sweep a transition line across the frame.
      - ``GLOW``
        Glow -- Add blur and brightness to light areas.
      - ``COLOR``
        Color -- Add a simple color strip.
      - ``SPEED``
        Speed -- Timewarp video strips, modifying playback speed.
      - ``MULTICAM``
        Multicam Selector -- Control active camera angles.
      - ``ADJUSTMENT``
        Adjustment Layer -- Apply nondestructive effects.
      - ``GAUSSIAN_BLUR``
        Gaussian Blur -- Soften details along axes.
      - ``TEXT``
        Text -- Add a simple text strip.
      - ``COLORMIX``
        Color Mix -- Combine two strips using blend modes.
   :type type: Literal['CROSS', 'ADD', 'SUBTRACT', 'ALPHA_OVER', 'ALPHA_UNDER', 'GAMMA_CROSS', 'MULTIPLY', 'WIPE', 'GLOW', 'COLOR', 'SPEED', 'MULTICAM', 'ADJUSTMENT', 'GAUSSIAN_BLUR', 'TEXT', 'COLORMIX']
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: change_path(*, filepath="", directory="", files=None, hide_props_region=True, check_existing=False, filter_blender=False, filter_backup=False, filter_image=False, filter_movie=False, filter_python=False, filter_font=False, filter_sound=False, filter_text=False, filter_archive=False, filter_btx=False, filter_alembic=False, filter_usd=False, filter_obj=False, filter_volume=False, filter_folder=True, filter_blenlib=False, filemode=9, relative_path=True, display_type='DEFAULT', sort_method='', use_placeholders=False)

   Undocumented, consider `contributing <https://developer.blender.org/>`__.

   :param filepath: File Path, Path to file (optional, never None)
   :type filepath: str
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
   :type sort_method: str
   :param use_placeholders: Use Placeholders, Use placeholders for missing frames of the strip (optional)
   :type use_placeholders: bool
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: change_scene(*, scene='')

   Change Scene assigned to Strip

   :param scene: Scene, (optional)
   :type scene: str
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: connect(*, toggle=True)

   Link selected strips together for simplified group selection

   :param toggle: Toggle, Toggle strip connections (optional)
   :type toggle: bool
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: copy()

   Copy the selected strips to the internal clipboard

   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]
.. function:: crossfade_sounds()

   Do cross-fading volume animation of two selected sound strips

   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]
   :File: `startup/bl_operators/sequencer.py\:43 <https://projects.blender.org/blender/blender/src/branch/main/scripts/startup/bl_operators/sequencer.py#L43>`__

.. function:: cursor_set(*, location=(0.0, 0.0))

   Set 2D cursor location

   :param location: Location, Cursor location in normalized preview coordinates (array of 2 items, in [-inf, inf], optional)
   :type location: :class:`mathutils.Vector` | Sequence[float]
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: deinterlace_selected_movies()

   Deinterlace all selected movie sources

   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]
   :File: `startup/bl_operators/sequencer.py\:134 <https://projects.blender.org/blender/blender/src/branch/main/scripts/startup/bl_operators/sequencer.py#L134>`__

.. function:: delete(*, delete_data=False)

   Delete selected strips from the sequencer

   :param delete_data: Delete Data, After removing the Strip, delete the associated data also (optional)
   :type delete_data: bool
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: disconnect()

   Unlink selected strips so that they can be selected individually

   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]
.. function:: duplicate(*, linked=False)

   Duplicate the selected strips

   :param linked: Linked, Duplicate strip but not strip data, linking to the original data (optional)
   :type linked: bool
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: duplicate_move(*, SEQUENCER_OT_duplicate={}, TRANSFORM_OT_seq_slide={})

   Duplicate selected strips and move them

   :param SEQUENCER_OT_duplicate: Duplicate Strips, Duplicate the selected strips (optional, :func:`bpy.ops.sequencer.duplicate` keyword arguments)
   :type SEQUENCER_OT_duplicate: dict[str, Any]
   :param TRANSFORM_OT_seq_slide: Sequence Slide, Slide a sequence strip in time (optional, :func:`bpy.ops.transform.seq_slide` keyword arguments)
   :type TRANSFORM_OT_seq_slide: dict[str, Any]
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: duplicate_move_linked(*, SEQUENCER_OT_duplicate={}, TRANSFORM_OT_seq_slide={})

   Duplicate selected strips, but not their data, and move them

   :param SEQUENCER_OT_duplicate: Duplicate Strips, Duplicate the selected strips (optional, :func:`bpy.ops.sequencer.duplicate` keyword arguments)
   :type SEQUENCER_OT_duplicate: dict[str, Any]
   :param TRANSFORM_OT_seq_slide: Sequence Slide, Slide a sequence strip in time (optional, :func:`bpy.ops.transform.seq_slide` keyword arguments)
   :type TRANSFORM_OT_seq_slide: dict[str, Any]
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: effect_strip_add(*, type='CROSS', move_strips=True, frame_start=0, length=0, channel=1, replace_sel=True, overlap=False, overlap_shuffle_override=False, skip_locked_or_muted_channels=True, color=(0.0, 0.0, 0.0))

   Add an effect to the sequencer, most are applied on top of existing strips

   :param type: Type, Sequencer effect type (optional)

      - ``CROSS``
        Crossfade -- Fade out of one video, fading into another.
      - ``ADD``
        Add -- Add together color channels from two videos.
      - ``SUBTRACT``
        Subtract -- Subtract one strip's color from another.
      - ``ALPHA_OVER``
        Alpha Over -- Blend alpha on top of another video.
      - ``ALPHA_UNDER``
        Alpha Under -- Blend alpha below another video.
      - ``GAMMA_CROSS``
        Gamma Crossfade -- Crossfade with color correction.
      - ``MULTIPLY``
        Multiply -- Multiply color channels from two videos.
      - ``WIPE``
        Wipe -- Sweep a transition line across the frame.
      - ``GLOW``
        Glow -- Add blur and brightness to light areas.
      - ``COLOR``
        Color -- Add a simple color strip.
      - ``SPEED``
        Speed -- Timewarp video strips, modifying playback speed.
      - ``MULTICAM``
        Multicam Selector -- Control active camera angles.
      - ``ADJUSTMENT``
        Adjustment Layer -- Apply nondestructive effects.
      - ``GAUSSIAN_BLUR``
        Gaussian Blur -- Soften details along axes.
      - ``TEXT``
        Text -- Add a simple text strip.
      - ``COLORMIX``
        Color Mix -- Combine two strips using blend modes.
   :type type: Literal['CROSS', 'ADD', 'SUBTRACT', 'ALPHA_OVER', 'ALPHA_UNDER', 'GAMMA_CROSS', 'MULTIPLY', 'WIPE', 'GLOW', 'COLOR', 'SPEED', 'MULTICAM', 'ADJUSTMENT', 'GAUSSIAN_BLUR', 'TEXT', 'COLORMIX']
   :param move_strips: Move Strips, Automatically begin translating strips with the mouse after adding them to the timeline (optional)
   :type move_strips: bool
   :param frame_start: Start Frame, Start frame of the strip (in [-inf, inf], optional)
   :type frame_start: int
   :param length: Length, Length of the strip in frames, or the length of each strip if multiple are added (in [-inf, inf], optional)
   :type length: int
   :param channel: Channel, Channel to place this strip into (in [1, 128], optional)
   :type channel: int
   :param replace_sel: Replace Selection, Deselect previously selected strips after add operation completes (optional)
   :type replace_sel: bool
   :param overlap: Allow Overlap, Don't correct overlap on new strips (optional)
   :type overlap: bool
   :param overlap_shuffle_override: Override Overlap Shuffle Behavior, Use the overlap_mode tool settings to determine how to shuffle overlapping strips (optional)
   :type overlap_shuffle_override: bool
   :param skip_locked_or_muted_channels: Skip Locked or Muted Channels, Add strips to muted or locked channels when adding movie strips (optional)
   :type skip_locked_or_muted_channels: bool
   :param color: Color, Initialize the strip with this color (array of 3 items, in [0, 1], optional)
   :type color: :class:`mathutils.Color` | Sequence[float]
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: enable_proxies(*, proxy_25=False, proxy_50=False, proxy_75=False, proxy_100=False, overwrite=False)

   Enable selected proxies on all selected Movie and Image strips

   :param proxy_25: 25%, (optional)
   :type proxy_25: bool
   :param proxy_50: 50%, (optional)
   :type proxy_50: bool
   :param proxy_75: 75%, (optional)
   :type proxy_75: bool
   :param proxy_100: 100%, (optional)
   :type proxy_100: bool
   :param overwrite: Overwrite, (optional)
   :type overwrite: bool
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: export_subtitles(*, filepath="", hide_props_region=True, check_existing=True, filter_blender=False, filter_backup=False, filter_image=False, filter_movie=False, filter_python=False, filter_font=False, filter_sound=False, filter_text=False, filter_archive=False, filter_btx=False, filter_alembic=False, filter_usd=False, filter_obj=False, filter_volume=False, filter_folder=True, filter_blenlib=False, filemode=8, display_type='DEFAULT', sort_method='')

   Export .srt file containing text strips

   :param filepath: File Path, Path to file (optional, never None)
   :type filepath: str
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
   :type sort_method: str
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: fades_add(*, duration_seconds=1.0, type='IN_OUT')

   Adds or updates a fade animation for either visual or audio strips

   :param duration_seconds: Fade Duration, Duration of the fade in seconds (in [0.01, inf], optional)
   :type duration_seconds: float
   :param type: Fade Type, Fade in, out, both in and out, to, or from the current frame. Default is both in and out (optional)

      - ``IN_OUT``
        Fade In and Out -- Fade selected strips in and out.
      - ``IN``
        Fade In -- Fade in selected strips.
      - ``OUT``
        Fade Out -- Fade out selected strips.
      - ``CURSOR_FROM``
        From Current Frame -- Fade from the time cursor to the end of overlapping strips.
      - ``CURSOR_TO``
        To Current Frame -- Fade from the start of strips under the time cursor to the current frame.
   :type type: Literal['IN_OUT', 'IN', 'OUT', 'CURSOR_FROM', 'CURSOR_TO']
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]
   :File: `startup/bl_operators/sequencer.py\:221 <https://projects.blender.org/blender/blender/src/branch/main/scripts/startup/bl_operators/sequencer.py#L221>`__


.. function:: fades_clear()

   Removes fade animation from selected strips

   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]
   :File: `startup/bl_operators/sequencer.py\:157 <https://projects.blender.org/blender/blender/src/branch/main/scripts/startup/bl_operators/sequencer.py#L157>`__

.. function:: gap_insert(*, frames=10)

   Insert gap at current frame to first strips at the right, independent of selection or locked state of strips

   :param frames: Frames, Frames to insert after current strip (in [0, inf], optional)
   :type frames: int
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: gap_remove(*, all=False)

   Remove gap at current frame to first strip at the right, independent of selection or locked state of strips

   :param all: All Gaps, Do all gaps to right of current frame (optional)
   :type all: bool
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: image_strip_add(*, directory="", files=None, check_existing=False, filter_blender=False, filter_backup=False, filter_image=True, filter_movie=False, filter_python=False, filter_font=False, filter_sound=False, filter_text=False, filter_archive=False, filter_btx=False, filter_alembic=False, filter_usd=False, filter_obj=False, filter_volume=False, filter_folder=True, filter_blenlib=False, filemode=9, relative_path=True, show_multiview=False, use_multiview=False, display_type='DEFAULT', sort_method='', move_strips=True, frame_start=0, length=0, channel=1, replace_sel=True, overlap=False, overlap_shuffle_override=False, skip_locked_or_muted_channels=True, fit_method='FIT', set_view_transform=True, image_import_type='DETECT', use_sequence_detection=True, use_placeholders=False)

   Add an image or image sequence to the sequencer

   :param directory: Directory, Directory of the file (optional, never None)
   :type directory: str
   :param files: Files, (optional)
   :type files: :class:`bpy_prop_collection`\ [:class:`OperatorFileListElement`] | None
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
   :param move_strips: Move Strips, Automatically begin translating strips with the mouse after adding them to the timeline (optional)
   :type move_strips: bool
   :param frame_start: Start Frame, Start frame of the strip (in [-inf, inf], optional)
   :type frame_start: int
   :param length: Length, Length of the strip in frames, or the length of each strip if multiple are added (in [-inf, inf], optional)
   :type length: int
   :param channel: Channel, Channel to place this strip into (in [1, 128], optional)
   :type channel: int
   :param replace_sel: Replace Selection, Deselect previously selected strips after add operation completes (optional)
   :type replace_sel: bool
   :param overlap: Allow Overlap, Don't correct overlap on new strips (optional)
   :type overlap: bool
   :param overlap_shuffle_override: Override Overlap Shuffle Behavior, Use the overlap_mode tool settings to determine how to shuffle overlapping strips (optional)
   :type overlap_shuffle_override: bool
   :param skip_locked_or_muted_channels: Skip Locked or Muted Channels, Add strips to muted or locked channels when adding movie strips (optional)
   :type skip_locked_or_muted_channels: bool
   :param fit_method: Fit Method, Mode for fitting the image to the canvas (optional)
   :type fit_method: Literal[:ref:`rna_enum_strip_scale_method_items`]
   :param set_view_transform: Set View Transform, Set appropriate view transform based on media color space (optional)
   :type set_view_transform: bool
   :param image_import_type: Import As, Mode for importing selected images (optional)

      - ``DETECT``
        Auto Detect -- Add images as individual strips, unless their filenames match Blender's numbered sequence pattern, in which case they are grouped into a single image sequence.
      - ``SEQUENCE``
        Image Sequence -- Import all selected images as a single image sequence. The sequence of images does not have to match Blender's numbered sequence pattern, so placeholders cannot be inferred.
      - ``INDIVIDUAL``
        Individual Images -- Add each selected image as an individual strip.
   :type image_import_type: Literal['DETECT', 'SEQUENCE', 'INDIVIDUAL']
   :param use_sequence_detection: Detect Sequences, Automatically detect animated sequences in selected images (based on file names) (optional)
   :type use_sequence_detection: bool
   :param use_placeholders: Use Placeholders, Reserve placeholder frames for missing frames of the image sequence (optional)
   :type use_placeholders: bool
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: images_separate(*, length=1)

   On image sequence strips, it returns a strip for each image

   :param length: Length, Length of each frame (in [1, inf], optional)
   :type length: int
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: lock()

   Lock strips so they cannot be transformed

   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]
.. function:: mask_strip_add(*, move_strips=True, frame_start=0, channel=1, replace_sel=True, overlap=False, overlap_shuffle_override=False, skip_locked_or_muted_channels=True, mask='')

   Add a mask strip to the sequencer

   :param move_strips: Move Strips, Automatically begin translating strips with the mouse after adding them to the timeline (optional)
   :type move_strips: bool
   :param frame_start: Start Frame, Start frame of the strip (in [-inf, inf], optional)
   :type frame_start: int
   :param channel: Channel, Channel to place this strip into (in [1, 128], optional)
   :type channel: int
   :param replace_sel: Replace Selection, Deselect previously selected strips after add operation completes (optional)
   :type replace_sel: bool
   :param overlap: Allow Overlap, Don't correct overlap on new strips (optional)
   :type overlap: bool
   :param overlap_shuffle_override: Override Overlap Shuffle Behavior, Use the overlap_mode tool settings to determine how to shuffle overlapping strips (optional)
   :type overlap_shuffle_override: bool
   :param skip_locked_or_muted_channels: Skip Locked or Muted Channels, Add strips to muted or locked channels when adding movie strips (optional)
   :type skip_locked_or_muted_channels: bool
   :param mask: Mask, (optional)
   :type mask: str
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: meta_make()

   Group selected strips into a meta-strip

   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]
.. function:: meta_separate()

   Put the contents of a meta-strip back in the sequencer

   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]
.. function:: meta_toggle()

   Toggle a meta-strip (to edit enclosed strips)

   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]
.. function:: movie_strip_add(*, filepath="", directory="", files=None, check_existing=False, filter_blender=False, filter_backup=False, filter_image=False, filter_movie=True, filter_python=False, filter_font=False, filter_sound=False, filter_text=False, filter_archive=False, filter_btx=False, filter_alembic=False, filter_usd=False, filter_obj=False, filter_volume=False, filter_folder=True, filter_blenlib=False, filemode=9, relative_path=True, show_multiview=False, use_multiview=False, display_type='DEFAULT', sort_method='', move_strips=True, frame_start=0, channel=1, replace_sel=True, overlap=False, overlap_shuffle_override=False, skip_locked_or_muted_channels=True, fit_method='FIT', set_view_transform=True, adjust_playback_rate=True, sound=True, use_framerate=True)

   Add a movie strip to the sequencer

   :param filepath: File Path, Path to file (optional, never None)
   :type filepath: str
   :param directory: Directory, Directory of the file (optional, never None)
   :type directory: str
   :param files: Files, (optional)
   :type files: :class:`bpy_prop_collection`\ [:class:`OperatorFileListElement`] | None
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
   :param move_strips: Move Strips, Automatically begin translating strips with the mouse after adding them to the timeline (optional)
   :type move_strips: bool
   :param frame_start: Start Frame, Start frame of the strip (in [-inf, inf], optional)
   :type frame_start: int
   :param channel: Channel, Channel to place this strip into (in [1, 128], optional)
   :type channel: int
   :param replace_sel: Replace Selection, Deselect previously selected strips after add operation completes (optional)
   :type replace_sel: bool
   :param overlap: Allow Overlap, Don't correct overlap on new strips (optional)
   :type overlap: bool
   :param overlap_shuffle_override: Override Overlap Shuffle Behavior, Use the overlap_mode tool settings to determine how to shuffle overlapping strips (optional)
   :type overlap_shuffle_override: bool
   :param skip_locked_or_muted_channels: Skip Locked or Muted Channels, Add strips to muted or locked channels when adding movie strips (optional)
   :type skip_locked_or_muted_channels: bool
   :param fit_method: Fit Method, Mode for fitting the image to the canvas (optional)
   :type fit_method: Literal[:ref:`rna_enum_strip_scale_method_items`]
   :param set_view_transform: Set View Transform, Set appropriate view transform based on media color space (optional)
   :type set_view_transform: bool
   :param adjust_playback_rate: Adjust Playback Rate, Play at normal speed regardless of scene FPS (optional)
   :type adjust_playback_rate: bool
   :param sound: Sound, Load sound with the movie (optional)
   :type sound: bool
   :param use_framerate: Set Scene Frame Rate, Set frame rate of the current scene to the frame rate of the movie (optional)
   :type use_framerate: bool
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: movieclip_strip_add(*, move_strips=True, frame_start=0, channel=1, replace_sel=True, overlap=False, overlap_shuffle_override=False, skip_locked_or_muted_channels=True, clip='')

   Add a movieclip strip to the sequencer

   :param move_strips: Move Strips, Automatically begin translating strips with the mouse after adding them to the timeline (optional)
   :type move_strips: bool
   :param frame_start: Start Frame, Start frame of the strip (in [-inf, inf], optional)
   :type frame_start: int
   :param channel: Channel, Channel to place this strip into (in [1, 128], optional)
   :type channel: int
   :param replace_sel: Replace Selection, Deselect previously selected strips after add operation completes (optional)
   :type replace_sel: bool
   :param overlap: Allow Overlap, Don't correct overlap on new strips (optional)
   :type overlap: bool
   :param overlap_shuffle_override: Override Overlap Shuffle Behavior, Use the overlap_mode tool settings to determine how to shuffle overlapping strips (optional)
   :type overlap_shuffle_override: bool
   :param skip_locked_or_muted_channels: Skip Locked or Muted Channels, Add strips to muted or locked channels when adding movie strips (optional)
   :type skip_locked_or_muted_channels: bool
   :param clip: Clip, (optional)
   :type clip: str
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: mute(*, unselected=False)

   Mute (un)selected strips

   :param unselected: Unselected, Mute unselected rather than selected strips (optional)
   :type unselected: bool
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: offset_clear()

   Clear strip in/out offsets from the start and end of content

   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]
.. function:: paste(*, keep_offset=False, x=0, y=0)

   Paste strips from the internal clipboard

   :param keep_offset: Keep Offset, Keep strip offset relative to the current frame when pasting (optional)
   :type keep_offset: bool
   :param x: X, (in [-inf, inf], optional)
   :type x: int
   :param y: Y, (in [-inf, inf], optional)
   :type y: int
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: preview_duplicate_move(*, SEQUENCER_OT_duplicate={}, TRANSFORM_OT_translate={})

   Duplicate selected strips and move them

   :param SEQUENCER_OT_duplicate: Duplicate Strips, Duplicate the selected strips (optional, :func:`bpy.ops.sequencer.duplicate` keyword arguments)
   :type SEQUENCER_OT_duplicate: dict[str, Any]
   :param TRANSFORM_OT_translate: Move, Move selected items (optional, :func:`bpy.ops.transform.translate` keyword arguments)
   :type TRANSFORM_OT_translate: dict[str, Any]
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: preview_duplicate_move_linked(*, SEQUENCER_OT_duplicate={}, TRANSFORM_OT_translate={})

   Duplicate selected strips, but not their data, and move them

   :param SEQUENCER_OT_duplicate: Duplicate Strips, Duplicate the selected strips (optional, :func:`bpy.ops.sequencer.duplicate` keyword arguments)
   :type SEQUENCER_OT_duplicate: dict[str, Any]
   :param TRANSFORM_OT_translate: Move, Move selected items (optional, :func:`bpy.ops.transform.translate` keyword arguments)
   :type TRANSFORM_OT_translate: dict[str, Any]
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: reassign_inputs()

   Reassign the inputs for the effect strip

   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]
.. function:: rebuild_proxy()

   Rebuild all selected proxies and timecode indices

   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]
.. function:: refresh_all()

   Refresh the sequencer editor

   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]
.. function:: reload(*, adjust_length=False)

   Reload strips in the sequencer

   :param adjust_length: Adjust Length, Adjust length of strips to their data length (optional)
   :type adjust_length: bool
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: rename_channel()

   Undocumented, consider `contributing <https://developer.blender.org/>`__.

   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]
.. function:: rendersize()

   Set render size and aspect from active strip

   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]
.. function:: retiming_add_freeze_frame_slide(*, SEQUENCER_OT_retiming_freeze_frame_add={}, TRANSFORM_OT_seq_slide={})

   Add freeze frame and move it

   :param SEQUENCER_OT_retiming_freeze_frame_add: Add Freeze Frame, Add freeze frame (optional, :func:`bpy.ops.sequencer.retiming_freeze_frame_add` keyword arguments)
   :type SEQUENCER_OT_retiming_freeze_frame_add: dict[str, Any]
   :param TRANSFORM_OT_seq_slide: Sequence Slide, Slide a sequence strip in time (optional, :func:`bpy.ops.transform.seq_slide` keyword arguments)
   :type TRANSFORM_OT_seq_slide: dict[str, Any]
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: retiming_add_transition_slide(*, SEQUENCER_OT_retiming_transition_add={}, TRANSFORM_OT_seq_slide={})

   Add smooth transition between 2 retimed segments and change its duration

   :param SEQUENCER_OT_retiming_transition_add: Add Speed Transition, Add smooth transition between 2 retimed segments (optional, :func:`bpy.ops.sequencer.retiming_transition_add` keyword arguments)
   :type SEQUENCER_OT_retiming_transition_add: dict[str, Any]
   :param TRANSFORM_OT_seq_slide: Sequence Slide, Slide a sequence strip in time (optional, :func:`bpy.ops.transform.seq_slide` keyword arguments)
   :type TRANSFORM_OT_seq_slide: dict[str, Any]
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: retiming_freeze_frame_add(*, duration=0)

   Add freeze frame

   :param duration: Duration, Duration of freeze frame segment (in [0, inf], optional)
   :type duration: int
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: retiming_key_add(*, timeline_frame=0)

   Add retiming Key

   :param timeline_frame: Timeline Frame, Frame where key will be added (in [0, inf], optional)
   :type timeline_frame: int
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: retiming_key_delete()

   Delete selected retiming keys from the sequencer

   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]
.. function:: retiming_reset()

   Reset strip retiming

   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]
.. function:: retiming_segment_speed_set(*, speed=100.0)

   Set speed of retimed segment

   :param speed: Speed, New speed of retimed segment (in [0.001, inf], optional)
   :type speed: float
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: retiming_show()

   Show retiming keys in selected strips

   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]
.. function:: retiming_transition_add(*, duration=0)

   Add smooth transition between 2 retimed segments

   :param duration: Duration, Duration of freeze frame segment (in [0, inf], optional)
   :type duration: int
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: sample(*, size=1)

   Use mouse to sample color in current frame

   :param size: Sample Size, (in [1, 128], optional)
   :type size: int
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: scene_frame_range_update()

   Update frame range of scene strip

   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]
.. function:: scene_strip_add(*, move_strips=True, frame_start=0, channel=1, replace_sel=True, overlap=False, overlap_shuffle_override=False, skip_locked_or_muted_channels=True, scene='')

   Add a strip re-using this scene as the source

   :param move_strips: Move Strips, Automatically begin translating strips with the mouse after adding them to the timeline (optional)
   :type move_strips: bool
   :param frame_start: Start Frame, Start frame of the strip (in [-inf, inf], optional)
   :type frame_start: int
   :param channel: Channel, Channel to place this strip into (in [1, 128], optional)
   :type channel: int
   :param replace_sel: Replace Selection, Deselect previously selected strips after add operation completes (optional)
   :type replace_sel: bool
   :param overlap: Allow Overlap, Don't correct overlap on new strips (optional)
   :type overlap: bool
   :param overlap_shuffle_override: Override Overlap Shuffle Behavior, Use the overlap_mode tool settings to determine how to shuffle overlapping strips (optional)
   :type overlap_shuffle_override: bool
   :param skip_locked_or_muted_channels: Skip Locked or Muted Channels, Add strips to muted or locked channels when adding movie strips (optional)
   :type skip_locked_or_muted_channels: bool
   :param scene: Scene, (optional)
   :type scene: str
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: scene_strip_add_new(*, move_strips=True, frame_start=0, channel=1, replace_sel=True, overlap=False, overlap_shuffle_override=False, skip_locked_or_muted_channels=True, type='NEW')

   Add a strip using a new scene as the source

   :param move_strips: Move Strips, Automatically begin translating strips with the mouse after adding them to the timeline (optional)
   :type move_strips: bool
   :param frame_start: Start Frame, Start frame of the strip (in [-inf, inf], optional)
   :type frame_start: int
   :param channel: Channel, Channel to place this strip into (in [1, 128], optional)
   :type channel: int
   :param replace_sel: Replace Selection, Deselect previously selected strips after add operation completes (optional)
   :type replace_sel: bool
   :param overlap: Allow Overlap, Don't correct overlap on new strips (optional)
   :type overlap: bool
   :param overlap_shuffle_override: Override Overlap Shuffle Behavior, Use the overlap_mode tool settings to determine how to shuffle overlapping strips (optional)
   :type overlap_shuffle_override: bool
   :param skip_locked_or_muted_channels: Skip Locked or Muted Channels, Add strips to muted or locked channels when adding movie strips (optional)
   :type skip_locked_or_muted_channels: bool
   :param type: Type, (optional)

      - ``NEW``
        New -- Add new Strip with a new empty Scene with default settings.
      - ``EMPTY``
        Copy Settings -- Add a new Strip, with an empty scene, and copy settings from the current scene.
      - ``LINK_COPY``
        Linked Copy -- Add a Strip and link in the collections from the current scene (shallow copy).
      - ``FULL_COPY``
        Full Copy -- Add a Strip and make a full copy of the current scene.
   :type type: Literal['NEW', 'EMPTY', 'LINK_COPY', 'FULL_COPY']
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: select(*, wait_to_deselect_others=False, use_select_on_click=False, mouse_x=0, mouse_y=0, extend=False, deselect=False, toggle=False, deselect_all=False, select_passthrough=False, center=False, linked_handle=False, linked_time=False, side_of_frame=False, ignore_connections=False)

   Select a strip (last selected becomes the "active strip")

   :param wait_to_deselect_others: Wait to Deselect Others, (optional)
   :type wait_to_deselect_others: bool
   :param use_select_on_click: Act on Click, Instead of selecting on mouse press, wait to see if there's drag event. Otherwise select on mouse release (optional)
   :type use_select_on_click: bool
   :param mouse_x: Mouse X, (in [-inf, inf], optional)
   :type mouse_x: int
   :param mouse_y: Mouse Y, (in [-inf, inf], optional)
   :type mouse_y: int
   :param extend: Extend, Extend selection instead of deselecting everything first (optional)
   :type extend: bool
   :param deselect: Deselect, Remove from selection (optional)
   :type deselect: bool
   :param toggle: Toggle Selection, Toggle the selection (optional)
   :type toggle: bool
   :param deselect_all: Deselect On Nothing, Deselect all when nothing under the cursor (optional)
   :type deselect_all: bool
   :param select_passthrough: Only Select Unselected, Ignore the select action when the element is already selected (optional)
   :type select_passthrough: bool
   :param center: Center, Use the object center when selecting, in edit mode used to extend object selection (optional)
   :type center: bool
   :param linked_handle: Linked Handle, Select handles next to the active strip (optional)
   :type linked_handle: bool
   :param linked_time: Linked Time, Select other strips or handles at the same time, or all retiming keys after the current in retiming mode (optional)
   :type linked_time: bool
   :param side_of_frame: Side of Frame, Select all strips on same side of the current frame as the mouse cursor (optional)
   :type side_of_frame: bool
   :param ignore_connections: Ignore Connections, Select strips individually whether or not they are connected (optional)
   :type ignore_connections: bool
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: select_all(*, action='TOGGLE')

   Select or deselect all strips

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

.. function:: select_box(*, xmin=0, xmax=0, ymin=0, ymax=0, wait_for_input=True, mode='SET', tweak=False, include_handles=False, ignore_connections=False)

   Select strips using box selection

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
   :param tweak: Tweak, Make box select pass through to sequence slide when the cursor is hovering on a strip (optional)
   :type tweak: bool
   :param include_handles: Select Handles, Select the strips and their handles (optional)
   :type include_handles: bool
   :param ignore_connections: Ignore Connections, Select strips individually whether or not they are connected (optional)
   :type ignore_connections: bool
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: select_circle(*, x=0, y=0, radius=25, wait_for_input=True, mode='SET', ignore_connections=False)

   Select strips using circle selection

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
   :param ignore_connections: Ignore Connections, Select strips individually whether or not they are connected (optional)
   :type ignore_connections: bool
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: select_grouped(*, type='TYPE', extend=False, use_active_channel=False)

   Select all strips grouped by various properties

   :param type: Type, (optional)

      - ``TYPE``
        Type -- Shared strip type.
      - ``TYPE_BASIC``
        Global Type -- All strips of same basic type (graphical or sound).
      - ``TYPE_EFFECT``
        Effect Type -- Shared strip effect type (if active strip is not an effect one, select all non-effect strips).
      - ``DATA``
        Data -- Shared data (scene, image, sound, etc.).
      - ``EFFECT``
        Effect -- Shared effects.
      - ``EFFECT_LINK``
        Effect/Linked -- Other strips affected by the active one (sharing some time, and below or effect-assigned).
      - ``OVERLAP``
        Overlap -- Overlapping time.
   :type type: Literal['TYPE', 'TYPE_BASIC', 'TYPE_EFFECT', 'DATA', 'EFFECT', 'EFFECT_LINK', 'OVERLAP']
   :param extend: Extend, Extend selection instead of deselecting everything first (optional)
   :type extend: bool
   :param use_active_channel: Same Channel, Only consider strips on the same channel as the active one (optional)
   :type use_active_channel: bool
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: select_handle(*, wait_to_deselect_others=False, use_select_on_click=False, mouse_x=0, mouse_y=0, ignore_connections=False)

   Select strip handle

   :param wait_to_deselect_others: Wait to Deselect Others, (optional)
   :type wait_to_deselect_others: bool
   :param use_select_on_click: Act on Click, Instead of selecting on mouse press, wait to see if there's drag event. Otherwise select on mouse release (optional)
   :type use_select_on_click: bool
   :param mouse_x: Mouse X, (in [-inf, inf], optional)
   :type mouse_x: int
   :param mouse_y: Mouse Y, (in [-inf, inf], optional)
   :type mouse_y: int
   :param ignore_connections: Ignore Connections, Select strips individually whether or not they are connected (optional)
   :type ignore_connections: bool
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: select_handles(*, side='BOTH')

   Select gizmo handles on the sides of the selected strip

   :param side: Side, The side of the handle that is selected (optional)
   :type side: Literal['LEFT', 'RIGHT', 'BOTH', 'LEFT_NEIGHBOR', 'RIGHT_NEIGHBOR', 'BOTH_NEIGHBORS']
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: select_lasso(*, path=None, use_smooth_stroke=False, smooth_stroke_factor=0.75, smooth_stroke_radius=35, mode='SET')

   Select strips using lasso selection

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

.. function:: select_less()

   Shrink the current selection of adjacent selected strips

   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]
.. function:: select_linked()

   Select all strips adjacent to the current selection

   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]
.. function:: select_linked_pick(*, extend=False)

   Select a chain of linked strips nearest to the mouse pointer

   :param extend: Extend, Extend the selection (optional)
   :type extend: bool
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: select_more()

   Select more strips adjacent to the current selection

   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]
.. function:: select_side(*, side='BOTH')

   Select strips on the nominated side of the selected strips

   :param side: Side, The side to which the selection is applied (optional)
   :type side: Literal['MOUSE', 'LEFT', 'RIGHT', 'BOTH', 'NO_CHANGE']
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: select_side_of_frame(*, extend=False, side='LEFT')

   Select strips relative to the current frame

   :param extend: Extend, Extend the selection (optional)
   :type extend: bool
   :param side: Side, (optional)

      - ``LEFT``
        Left -- Select to the left of the current frame.
      - ``RIGHT``
        Right -- Select to the right of the current frame.
      - ``CURRENT``
        Current Frame -- Select intersecting with the current frame.
   :type side: Literal['LEFT', 'RIGHT', 'CURRENT']
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: set_range_to_strips(*, preview=False)

   Set the frame range to the selected strips start and end

   :param preview: Preview, Set the preview range instead (optional)
   :type preview: bool
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: slip(*, offset=0.0, slip_keyframes=False, use_cursor_position=False, ignore_connections=False)

   Slip the contents of selected strips

   :param offset: Offset, Offset to the data of the strip (in [-inf, inf], optional)
   :type offset: float
   :param slip_keyframes: Slip Keyframes, Move the keyframes alongside the media (optional)
   :type slip_keyframes: bool
   :param use_cursor_position: Use Cursor Position, Slip strips under mouse cursor instead of all selected strips (optional)
   :type use_cursor_position: bool
   :param ignore_connections: Ignore Connections, Do not slip connected strips if using cursor position (optional)
   :type ignore_connections: bool
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: snap(*, frame=0, side='LEFT', keep_offset=True)

   Snap strips to the current frame, using the active strip as the anchor, and the mouse cursor relative to the playhead to determine the side of the playhead to snap to

   :param frame: Frame, Frame where selected strips will be snapped (in [-inf, inf], optional)
   :type frame: int
   :param side: Snap Side, Which side of the playhead strips should snap to when no handles are selected (optional)
   :type side: Literal['LEFT', 'RIGHT']
   :param keep_offset: Keep Offset, Whether the selection should be snapped as a whole or by each individual strip (optional)
   :type keep_offset: bool
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: sound_strip_add(*, filepath="", directory="", files=None, check_existing=False, filter_blender=False, filter_backup=False, filter_image=False, filter_movie=False, filter_python=False, filter_font=False, filter_sound=True, filter_text=False, filter_archive=False, filter_btx=False, filter_alembic=False, filter_usd=False, filter_obj=False, filter_volume=False, filter_folder=True, filter_blenlib=False, filemode=9, relative_path=True, display_type='DEFAULT', sort_method='', move_strips=True, frame_start=0, channel=1, replace_sel=True, overlap=False, overlap_shuffle_override=False, skip_locked_or_muted_channels=True, cache=False, mono=False)

   Add a sound strip to the sequencer

   :param filepath: File Path, Path to file (optional, never None)
   :type filepath: str
   :param directory: Directory, Directory of the file (optional, never None)
   :type directory: str
   :param files: Files, (optional)
   :type files: :class:`bpy_prop_collection`\ [:class:`OperatorFileListElement`] | None
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
   :param move_strips: Move Strips, Automatically begin translating strips with the mouse after adding them to the timeline (optional)
   :type move_strips: bool
   :param frame_start: Start Frame, Start frame of the strip (in [-inf, inf], optional)
   :type frame_start: int
   :param channel: Channel, Channel to place this strip into (in [1, 128], optional)
   :type channel: int
   :param replace_sel: Replace Selection, Deselect previously selected strips after add operation completes (optional)
   :type replace_sel: bool
   :param overlap: Allow Overlap, Don't correct overlap on new strips (optional)
   :type overlap: bool
   :param overlap_shuffle_override: Override Overlap Shuffle Behavior, Use the overlap_mode tool settings to determine how to shuffle overlapping strips (optional)
   :type overlap_shuffle_override: bool
   :param skip_locked_or_muted_channels: Skip Locked or Muted Channels, Add strips to muted or locked channels when adding movie strips (optional)
   :type skip_locked_or_muted_channels: bool
   :param cache: Cache, Cache the sound in memory (optional)
   :type cache: bool
   :param mono: Mono, Merge all the sound's channels into one (optional)
   :type mono: bool
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: split(*, frame=0, channel=0, type='SOFT', use_cursor_position=False, side='MOUSE', ignore_selection=False, ignore_connections=False)

   Split the selected strips in two

   :param frame: Frame, Frame where selected strips will be split (in [-inf, inf], optional)
   :type frame: int
   :param channel: Channel, Channel in which strip will be cut (in [-inf, inf], optional)
   :type channel: int
   :param type: Type, The type of split operation to perform on strips (optional)
   :type type: Literal['SOFT', 'HARD']
   :param use_cursor_position: Use Cursor Position, Split at position of the cursor instead of current frame (optional)
   :type use_cursor_position: bool
   :param side: Side, The side that remains selected after splitting (optional)
   :type side: Literal['MOUSE', 'LEFT', 'RIGHT', 'BOTH', 'NO_CHANGE']
   :param ignore_selection: Ignore Selection, Make cut even if strip is not selected preserving selection state after cut (optional)
   :type ignore_selection: bool
   :param ignore_connections: Ignore Connections, Don't propagate split to connected strips (optional)
   :type ignore_connections: bool
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: split_multicam(*, camera=1)

   Split multicam strip and select camera

   :param camera: Camera, (in [1, 32], optional)
   :type camera: int
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]
   :File: `startup/bl_operators/sequencer.py\:101 <https://projects.blender.org/blender/blender/src/branch/main/scripts/startup/bl_operators/sequencer.py#L101>`__


.. function:: strip_color_tag_set(*, color='NONE')

   Set a color tag for the selected strips

   :param color: Color Tag, (optional)
   :type color: Literal[:ref:`rna_enum_strip_color_items`]
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: strip_jump(*, next=True, center=True)

   Move frame to next or previous edit point

   :param next: Next Strip, (optional)
   :type next: bool
   :param center: Use Strip Center, (optional)
   :type center: bool
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: strip_modifier_add(*, type='')

   Add a modifier to the strip

   :param type: Type, (optional)
   :type type: str
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: strip_modifier_copy(*, type='REPLACE')

   Copy modifiers of the active strip to all selected strips

   :param type: Type, (optional)

      - ``REPLACE``
        Replace -- Replace modifiers in destination.
      - ``APPEND``
        Append -- Append active modifiers to selected strips.
   :type type: Literal['REPLACE', 'APPEND']
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: strip_modifier_equalizer_redefine(*, graphs='SIMPLE', name="Name")

   Redefine equalizer graphs

   :param graphs: Graphs, Number of graphs (optional)

      - ``SIMPLE``
        Unique -- One unique graphical definition.
      - ``DOUBLE``
        Double -- Graphical definition in 2 sections.
      - ``TRIPLE``
        Triplet -- Graphical definition in 3 sections.
   :type graphs: Literal['SIMPLE', 'DOUBLE', 'TRIPLE']
   :param name: Name, Name of modifier to redefine (optional, never None)
   :type name: str
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: strip_modifier_move(*, name="Name", direction='UP')

   Move modifier up and down in the stack

   :param name: Name, Name of modifier to remove (optional, never None)
   :type name: str
   :param direction: Type, (optional)

      - ``UP``
        Up -- Move modifier up in the stack.
      - ``DOWN``
        Down -- Move modifier down in the stack.
   :type direction: Literal['UP', 'DOWN']
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: strip_modifier_move_to_index(*, modifier="", index=0)

   Change the strip modifier's index in the stack so it evaluates after the set number of others

   :param modifier: Modifier, Name of the modifier to edit (optional, never None)
   :type modifier: str
   :param index: Index, The index to move the modifier to (in [0, inf], optional)
   :type index: int
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: strip_modifier_remove(*, name="Name")

   Remove a modifier from the strip

   :param name: Name, Name of modifier to remove (optional, never None)
   :type name: str
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: strip_modifier_set_active(*, modifier="")

   Activate the strip modifier to use as the context

   :param modifier: Modifier, Name of the strip modifier to edit (optional, never None)
   :type modifier: str
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: strip_transform_clear(*, property='ALL')

   Reset image transformation to default value

   :param property: Property, Strip transform property to be reset (optional)

      - ``POSITION``
        Position -- Reset strip transform location.
      - ``SCALE``
        Scale -- Reset strip transform scale.
      - ``ROTATION``
        Rotation -- Reset strip transform rotation.
      - ``ALL``
        All -- Reset strip transform location, scale and rotation.
   :type property: Literal['POSITION', 'SCALE', 'ROTATION', 'ALL']
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: strip_transform_fit(*, fit_method='FIT')

   Undocumented, consider `contributing <https://developer.blender.org/>`__.

   :param fit_method: Fit Method, Mode for fitting the image to the canvas (optional)
   :type fit_method: Literal[:ref:`rna_enum_strip_scale_method_items`]
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: swap(*, side='RIGHT')

   Swap active strip with strip to the right or left

   :param side: Side, Side of the strip to swap (optional)
   :type side: Literal['LEFT', 'RIGHT']
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: swap_data()

   Swap 2 sequencer strips

   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]
.. function:: swap_inputs()

   Swap the two inputs of the effect strip

   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]
.. function:: text_cursor_move(*, type='LINE_BEGIN', select_text=False)

   Move cursor in text

   :param type: Type, Where to move cursor to, to make a selection (optional)
   :type type: Literal['LINE_BEGIN', 'LINE_END', 'TEXT_BEGIN', 'TEXT_END', 'PREVIOUS_CHARACTER', 'NEXT_CHARACTER', 'PREVIOUS_WORD', 'NEXT_WORD', 'PREVIOUS_LINE', 'NEXT_LINE']
   :param select_text: Select Text, Select text while moving cursor (optional)
   :type select_text: bool
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: text_cursor_set(*, select_text=False)

   Set cursor position in text

   :param select_text: Select Text, Select text while moving cursor (optional)
   :type select_text: bool
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: text_delete(*, type='NEXT_OR_SELECTION')

   Delete text at cursor position

   :param type: Type, Which part of the text to delete (optional)
   :type type: Literal['NEXT_OR_SELECTION', 'PREVIOUS_OR_SELECTION']
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: text_deselect_all()

   Deselect all characters

   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]
.. function:: text_edit_copy()

   Copy text to clipboard

   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]
.. function:: text_edit_cut()

   Cut text to clipboard

   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]
.. function:: text_edit_mode_toggle()

   Toggle text editing

   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]
.. function:: text_edit_paste()

   Paste text from clipboard

   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]
.. function:: text_insert(*, string="")

   Insert text at cursor position

   :param string: String, String to be inserted at cursor position (optional, never None)
   :type string: str
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: text_line_break()

   Insert line break at cursor position

   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]
.. function:: text_select_all()

   Select all characters

   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]
.. function:: unlock()

   Unlock strips so they can be transformed

   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]
.. function:: unmute(*, unselected=False)

   Unmute (un)selected strips

   :param unselected: Unselected, Unmute unselected rather than selected strips (optional)
   :type unselected: bool
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: view_all()

   View all the strips in the sequencer

   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]
.. function:: view_all_preview()

   Zoom preview to fit in the area

   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]
.. function:: view_frame()

   Move the view to the current frame

   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]
.. function:: view_ghost_border(*, xmin=0, xmax=0, ymin=0, ymax=0, wait_for_input=True)

   Set the boundaries of the border used for offset view

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
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: view_selected()

   Zoom the sequencer on the selected strips

   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]
.. function:: view_zoom_ratio(*, ratio=1.0)

   Change zoom ratio of sequencer preview

   :param ratio: Ratio, Zoom ratio, 1.0 is 1:1, higher is zoomed in, lower is zoomed out (in [-inf, inf], optional)
   :type ratio: float
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

