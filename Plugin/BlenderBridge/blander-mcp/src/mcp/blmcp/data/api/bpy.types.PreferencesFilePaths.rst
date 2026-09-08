PreferencesFilePaths(bpy_struct)
================================

.. currentmodule:: bpy.types

base class --- :class:`bpy_struct`

.. class:: PreferencesFilePaths(bpy_struct)

   Default paths for external files

   .. attribute:: active_asset_library

      Index of the asset library being edited in the Preferences UI (in [-32768, 32767], default 0)

      :type: int

   .. attribute:: animation_player

      Path to a custom animation/frame sequence player (default "", never None)

      :type: str

   .. attribute:: animation_player_preset

      Preset configs for external animation players (default ``'INTERNAL'``)

      - ``INTERNAL``
        Internal -- Built-in animation player.
      - ``DJV``
        DJV -- Open source frame player.
      - ``FRAMECYCLER``
        FrameCycler -- Frame player from IRIDAS.
      - ``RV``
        RV -- Frame player from Tweak Software.
      - ``MPLAYER``
        MPlayer -- Media player for video and PNG/JPEG/SGI image sequences.
      - ``CUSTOM``
        Custom -- Custom animation player executable path.

      :type: Literal['INTERNAL', 'DJV', 'FRAMECYCLER', 'RV', 'MPLAYER', 'CUSTOM']

   .. data:: asset_libraries

      (default None, readonly)

      :type: :class:`AssetLibraryCollection`\ [:class:`UserAssetLibrary`]

   .. attribute:: auto_save_time

      The time (in minutes) to wait between automatic temporary saves (in [1, 60], default 2)

      :type: int

   .. attribute:: file_preview_type

      What type of blend preview to create (default ``'AUTO'``)

      - ``NONE``
        None -- Do not create blend previews.
      - ``AUTO``
        Auto -- Automatically select best preview type.
      - ``SCREENSHOT``
        Screenshot -- Capture the entire window.
      - ``CAMERA``
        Camera View -- Workbench render of scene.

      :type: Literal['NONE', 'AUTO', 'SCREENSHOT', 'CAMERA']

   .. attribute:: font_directory

      The default directory to search for loading fonts (default "", never None, blend relative ``//`` prefix supported)

      :type: str

   .. attribute:: i18n_branches_directory

      The path to the '/branches' directory of your local svn-translation copy, to allow translating from the UI (default "", never None)

      :type: str

   .. attribute:: image_editor

      Path to an image editor (default "", never None)

      :type: str

   .. attribute:: recent_files

      Maximum number of recently opened files to remember (in [0, 1000], default 200)

      :type: int

   .. attribute:: render_cache_directory

      Where to cache raw render results (default "", never None, blend relative ``//`` prefix supported)

      :type: str

   .. attribute:: render_output_directory

      The default directory for rendering output, for new scenes (default "", never None, blend relative ``//`` prefix supported)

      :type: str

   .. attribute:: save_version

      The number of old versions to maintain in the current directory, when manually saving (in [0, 32], default 1)

      :type: int

   .. data:: script_directories

      (default None, readonly)

      :type: :class:`ScriptDirectoryCollection`\ [:class:`ScriptDirectory`]

   .. attribute:: show_hidden_files_datablocks

      Show files and data-blocks that are normally hidden (default True)

      :type: bool

   .. attribute:: show_recent_locations

      Show Recent locations list in the File Browser (default True)

      :type: bool

   .. attribute:: show_system_bookmarks

      Show System locations list in the File Browser (default True)

      :type: bool

   .. attribute:: sound_directory

      The default directory to search for sounds (default "", never None, blend relative ``//`` prefix supported)

      :type: str

   .. attribute:: temporary_directory

      The directory for storing temporary save files. The path must reference an existing directory or it will be ignored (default "", never None)

      :type: str

   .. attribute:: text_editor

      Command to launch the text editor, either a full path or a command in $PATH.
      Use the internal editor when left blank
      
      (default "", never None)

      :type: str

   .. attribute:: text_editor_args

      Defines the specific format of the arguments with which the text editor opens files. The supported expansions are as follows:
      
      $filepath The absolute path of the file.
      $line The line to open at (Optional).
      $column The column to open from the beginning of the line (Optional).
      $line0 & column0 start at zero.
      Example: -f $filepath -l $line -c $column
      
      (default "", never None)

      :type: str

   .. attribute:: texture_directory

      The default directory to search for textures (default "", never None, blend relative ``//`` prefix supported)

      :type: str

   .. attribute:: use_auto_save_temporary_files

      Automatic saving of temporary files in temp directory, uses process ID.
      Warning: Sculpt and edit mode data won't be saved
      
      (default True)

      :type: bool

   .. attribute:: use_extension_online_access_handled

      The user has been shown the "Online Access" prompt and made a choice (default False)

      :type: bool

   .. attribute:: use_file_compression

      Enable file compression when saving .blend files (default True)

      :type: bool

   .. attribute:: use_filter_files

      Enable filtering of files in the File Browser (default True)

      :type: bool

   .. attribute:: use_load_ui

      Load user interface setup when loading .blend files (default True)

      :type: bool

   .. attribute:: use_relative_paths

      Default relative path option for the file selector, when no path is defined yet (default True)

      :type: bool

   .. attribute:: use_scripts_auto_execute

      Allow any .blend file to run scripts automatically (unsafe with blend files from an untrusted source) (default False)

      :type: bool

   .. attribute:: use_tabs_as_spaces

      Automatically convert all new tabs into spaces for new and loaded text files (default True)

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

   - :class:`Preferences.filepaths`

