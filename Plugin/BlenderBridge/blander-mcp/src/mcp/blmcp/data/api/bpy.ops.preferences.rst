Preferences Operators
=====================

.. module:: bpy.ops.preferences

.. function:: addon_disable(*, module="")

   Turn off this add-on

   :param module: Module, Module name of the add-on to disable (optional, never None)
   :type module: str
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]
   :File: `startup/bl_operators/userpref.py\:547 <https://projects.blender.org/blender/blender/src/branch/main/scripts/startup/bl_operators/userpref.py#L547>`__


.. function:: addon_enable(*, module="")

   Turn on this add-on

   :param module: Module, Module name of the add-on to enable (optional, never None)
   :type module: str
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]
   :File: `startup/bl_operators/userpref.py\:483 <https://projects.blender.org/blender/blender/src/branch/main/scripts/startup/bl_operators/userpref.py#L483>`__


.. function:: addon_expand(*, module="")

   Display information and preferences for this add-on

   :param module: Module, Module name of the add-on to expand (optional, never None)
   :type module: str
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]
   :File: `startup/bl_operators/userpref.py\:924 <https://projects.blender.org/blender/blender/src/branch/main/scripts/startup/bl_operators/userpref.py#L924>`__


.. function:: addon_install(*, overwrite=True, enable_on_install=False, target='', filepath="", filter_folder=True, filter_python=True, filter_glob="*.py;*.zip")

   Install an add-on

   :param overwrite: Overwrite, Remove existing add-ons with the same ID (optional)
   :type overwrite: bool
   :param enable_on_install: Enable on Install, Enable after installing (optional)
   :type enable_on_install: bool
   :param target: Target Path, (optional)
   :type target: str
   :param filepath: filepath, (optional, never None)
   :type filepath: str
   :param filter_folder: Filter folders, (optional)
   :type filter_folder: bool
   :param filter_python: Filter Python, (optional)
   :type filter_python: bool
   :param filter_glob: filter_glob, (optional, never None)
   :type filter_glob: str
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]
   :File: `startup/bl_operators/userpref.py\:712 <https://projects.blender.org/blender/blender/src/branch/main/scripts/startup/bl_operators/userpref.py#L712>`__


.. function:: addon_refresh()

   Scan add-on directories for new modules

   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]
   :File: `startup/bl_operators/userpref.py\:645 <https://projects.blender.org/blender/blender/src/branch/main/scripts/startup/bl_operators/userpref.py#L645>`__

.. function:: addon_remove(*, module="")

   Delete the add-on from the file system

   :param module: Module, Module name of the add-on to remove (optional, never None)
   :type module: str
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]
   :File: `startup/bl_operators/userpref.py\:873 <https://projects.blender.org/blender/blender/src/branch/main/scripts/startup/bl_operators/userpref.py#L873>`__


.. function:: addon_show(*, module="")

   Show add-on preferences

   :param module: Module, Module name of the add-on to expand (optional, never None)
   :type module: str
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]
   :File: `startup/bl_operators/userpref.py\:950 <https://projects.blender.org/blender/blender/src/branch/main/scripts/startup/bl_operators/userpref.py#L950>`__


.. function:: app_template_install(*, overwrite=True, filepath="", filter_folder=True, filter_glob="*.zip")

   Install an application template

   :param overwrite: Overwrite, Remove existing template with the same ID (optional)
   :type overwrite: bool
   :param filepath: filepath, (optional, never None)
   :type filepath: str
   :param filter_folder: Filter folders, (optional)
   :type filter_folder: bool
   :param filter_glob: filter_glob, (optional, never None)
   :type filter_glob: str
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]
   :File: `startup/bl_operators/userpref.py\:1000 <https://projects.blender.org/blender/blender/src/branch/main/scripts/startup/bl_operators/userpref.py#L1000>`__


.. function:: asset_library_add(*, directory="", hide_props_region=True, check_existing=False, filter_blender=False, filter_backup=False, filter_image=False, filter_movie=False, filter_python=False, filter_font=False, filter_sound=False, filter_text=False, filter_archive=False, filter_btx=False, filter_alembic=False, filter_usd=False, filter_obj=False, filter_volume=False, filter_folder=True, filter_blenlib=False, filemode=9, display_type='DEFAULT', sort_method='')

   Add a directory to be used by the Asset Browser as source of assets

   :param directory: Directory, Directory of the file (optional, never None)
   :type directory: str
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

.. function:: asset_library_remove(*, index=0)

   Remove a path to a .blend file, so the Asset Browser will not attempt to show it anymore

   :param index: Index, (in [0, inf], optional)
   :type index: int
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: associate_blend()

   Use this installation for .blend files and to display thumbnails

   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]
.. function:: autoexec_path_add()

   Add path to exclude from auto-execution

   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]
.. function:: autoexec_path_remove(*, index=0)

   Remove path to exclude from auto-execution

   :param index: Index, (in [0, inf], optional)
   :type index: int
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: clear_filter()

   Clear the search filter

   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]
.. function:: copy_prev()

   Copy settings from previous version

   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]
   :File: `startup/bl_operators/userpref.py\:170 <https://projects.blender.org/blender/blender/src/branch/main/scripts/startup/bl_operators/userpref.py#L170>`__

.. function:: extension_repo_add(*, name="", remote_url="", use_access_token=False, access_token="", use_sync_on_startup=False, use_custom_directory=False, custom_directory="", type='REMOTE')

   Add a new repository used to store extensions

   :param name: Name, Unique repository name (optional, never None)
   :type name: str
   :param remote_url: URL, Remote URL to the extension repository, the file-system may be referenced using the file URI scheme: "file://" (optional, never None)
   :type remote_url: str
   :param use_access_token: Requires Access Token, Repository requires an access token (optional)
   :type use_access_token: bool
   :param access_token: Secret, Personal access token, may be required by some repositories (optional, never None)
   :type access_token: str
   :param use_sync_on_startup: Check for Updates on Startup, Allow Blender to check for updates upon launch (optional)
   :type use_sync_on_startup: bool
   :param use_custom_directory: Custom Directory, Manually set the path for extensions to be stored. When disabled a user's extensions directory is created. (optional)
   :type use_custom_directory: bool
   :param custom_directory: Custom Directory, The local directory containing extensions (optional, never None)
   :type custom_directory: str
   :param type: Type, The kind of repository to add (optional)

      - ``REMOTE``
        Add Remote Repository -- Add a repository referencing a remote repository with support for listing and updating extensions.
      - ``LOCAL``
        Add Local Repository -- Add a repository managed manually without referencing an external repository.
   :type type: Literal['REMOTE', 'LOCAL']
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: extension_repo_remove(*, index=0, remove_files=False)

   Remove an extension repository

   :param index: Index, (in [0, inf], optional)
   :type index: int
   :param remove_files: Remove Files, Remove extension files when removing the repository (optional)
   :type remove_files: bool
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: extension_url_drop(*, url="")

   Handle dropping an extension URL

   :param url: URL, Location of the extension to install (optional, never None)
   :type url: str
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: keyconfig_activate(*, filepath="")

   Undocumented, consider `contributing <https://developer.blender.org/>`__.

   :param filepath: filepath, (optional, never None)
   :type filepath: str
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]
   :File: `startup/bl_operators/userpref.py\:91 <https://projects.blender.org/blender/blender/src/branch/main/scripts/startup/bl_operators/userpref.py#L91>`__


.. function:: keyconfig_export(*, all=False, filepath="", filter_folder=True, filter_text=True, filter_python=True)

   Export key configuration to a Python script

   :param all: All Keymaps, Write all keymaps (not just user modified) (optional)
   :type all: bool
   :param filepath: filepath, (optional, never None)
   :type filepath: str
   :param filter_folder: Filter folders, (optional)
   :type filter_folder: bool
   :param filter_text: Filter text, (optional)
   :type filter_text: bool
   :param filter_python: Filter Python, (optional)
   :type filter_python: bool
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]
   :File: `startup/bl_operators/userpref.py\:324 <https://projects.blender.org/blender/blender/src/branch/main/scripts/startup/bl_operators/userpref.py#L324>`__


.. function:: keyconfig_import(*, filepath="keymap.py", filter_folder=True, filter_text=True, filter_python=True, keep_original=True)

   Import key configuration from a Python script

   :param filepath: filepath, (optional, never None)
   :type filepath: str
   :param filter_folder: Filter folders, (optional)
   :type filter_folder: bool
   :param filter_text: Filter text, (optional)
   :type filter_text: bool
   :param filter_python: Filter Python, (optional)
   :type filter_python: bool
   :param keep_original: Keep Original, Keep original file after copying to configuration folder (optional)
   :type keep_original: bool
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]
   :File: `startup/bl_operators/userpref.py\:259 <https://projects.blender.org/blender/blender/src/branch/main/scripts/startup/bl_operators/userpref.py#L259>`__


.. function:: keyconfig_remove()

   Remove key config

   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]
   :File: `startup/bl_operators/userpref.py\:463 <https://projects.blender.org/blender/blender/src/branch/main/scripts/startup/bl_operators/userpref.py#L463>`__

.. function:: keyconfig_test()

   Test key configuration for conflicts

   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]
   :File: `startup/bl_operators/userpref.py\:194 <https://projects.blender.org/blender/blender/src/branch/main/scripts/startup/bl_operators/userpref.py#L194>`__

.. function:: keyitem_add()

   Add key map item

   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]
   :File: `startup/bl_operators/userpref.py\:411 <https://projects.blender.org/blender/blender/src/branch/main/scripts/startup/bl_operators/userpref.py#L411>`__

.. function:: keyitem_remove(*, item_id=0)

   Remove key map item

   :param item_id: Item Identifier, Identifier of the item to remove (in [-inf, inf], optional)
   :type item_id: int
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]
   :File: `startup/bl_operators/userpref.py\:443 <https://projects.blender.org/blender/blender/src/branch/main/scripts/startup/bl_operators/userpref.py#L443>`__


.. function:: keyitem_restore(*, item_id=0)

   Restore key map item

   :param item_id: Item Identifier, Identifier of the item to restore (in [-inf, inf], optional)
   :type item_id: int
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]
   :File: `startup/bl_operators/userpref.py\:395 <https://projects.blender.org/blender/blender/src/branch/main/scripts/startup/bl_operators/userpref.py#L395>`__


.. function:: keymap_restore(*, all=False)

   Restore key map(s)

   :param all: All Keymaps, Restore all keymaps to default (optional)
   :type all: bool
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]
   :File: `startup/bl_operators/userpref.py\:366 <https://projects.blender.org/blender/blender/src/branch/main/scripts/startup/bl_operators/userpref.py#L366>`__


.. function:: reset_default_theme()

   Reset to the default theme colors

   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]
.. function:: script_directory_add(*, directory="", filter_folder=True)

   Undocumented, consider `contributing <https://developer.blender.org/>`__.

   :param directory: directory, (optional, never None)
   :type directory: str
   :param filter_folder: Filter Folders, (optional)
   :type filter_folder: bool
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]
   :File: `startup/bl_operators/userpref.py\:1256 <https://projects.blender.org/blender/blender/src/branch/main/scripts/startup/bl_operators/userpref.py#L1256>`__


.. function:: script_directory_remove(*, index=0)

   Undocumented, consider `contributing <https://developer.blender.org/>`__.

   :param index: Index, Index of the script directory to remove (in [-inf, inf], optional)
   :type index: int
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]
   :File: `startup/bl_operators/userpref.py\:1286 <https://projects.blender.org/blender/blender/src/branch/main/scripts/startup/bl_operators/userpref.py#L1286>`__


.. function:: start_filter()

   Start entering filter text

   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]
.. function:: studiolight_copy_settings(*, index=0)

   Copy Studio Light settings to the Studio Light editor

   :param index: index, (in [-inf, inf], optional)
   :type index: int
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]
   :File: `startup/bl_operators/userpref.py\:1227 <https://projects.blender.org/blender/blender/src/branch/main/scripts/startup/bl_operators/userpref.py#L1227>`__


.. function:: studiolight_install(*, files=None, directory="", filter_folder=True, filter_glob="*.png;*.jpg;*.hdr;*.exr", type='MATCAP')

   Install a user defined light

   :param files: File Path, (optional)
   :type files: :class:`bpy_prop_collection`\ [:class:`OperatorFileListElement`] | None
   :param directory: directory, (optional, never None)
   :type directory: str
   :param filter_folder: Filter Folders, (optional)
   :type filter_folder: bool
   :param filter_glob: filter_glob, (optional, never None)
   :type filter_glob: str
   :param type: Type, (optional)

      - ``MATCAP``
        MatCap -- Install custom MatCaps.
      - ``WORLD``
        World -- Install custom HDRIs.
      - ``STUDIO``
        Studio -- Install custom Studio Lights.
   :type type: Literal['MATCAP', 'WORLD', 'STUDIO']
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]
   :File: `startup/bl_operators/userpref.py\:1110 <https://projects.blender.org/blender/blender/src/branch/main/scripts/startup/bl_operators/userpref.py#L1110>`__


.. function:: studiolight_new(*, filename="StudioLight")

   Save custom studio light from the studio light editor settings

   :param filename: Name, (optional, never None)
   :type filename: str
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]
   :File: `startup/bl_operators/userpref.py\:1157 <https://projects.blender.org/blender/blender/src/branch/main/scripts/startup/bl_operators/userpref.py#L1157>`__


.. function:: studiolight_uninstall(*, index=0)

   Delete Studio Light

   :param index: index, (in [-inf, inf], optional)
   :type index: int
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]
   :File: `startup/bl_operators/userpref.py\:1208 <https://projects.blender.org/blender/blender/src/branch/main/scripts/startup/bl_operators/userpref.py#L1208>`__


.. function:: theme_install(*, overwrite=True, filepath="", filter_folder=True, filter_glob="*.xml")

   Load and apply a Blender XML theme file

   :param overwrite: Overwrite, Remove existing theme file if exists (optional)
   :type overwrite: bool
   :param filepath: filepath, (optional, never None)
   :type filepath: str
   :param filter_folder: Filter folders, (optional)
   :type filter_folder: bool
   :param filter_glob: filter_glob, (optional, never None)
   :type filter_glob: str
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]
   :File: `startup/bl_operators/userpref.py\:598 <https://projects.blender.org/blender/blender/src/branch/main/scripts/startup/bl_operators/userpref.py#L598>`__


.. function:: unassociate_blend()

   Remove this installation's associations with .blend files

   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]
