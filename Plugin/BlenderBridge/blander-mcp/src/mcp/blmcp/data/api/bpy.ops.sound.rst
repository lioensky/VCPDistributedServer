Sound Operators
===============

.. module:: bpy.ops.sound

.. function:: bake_animation()

   Update the audio animation cache

   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]
.. function:: mixdown(*, filepath="", check_existing=True, filter_blender=False, filter_backup=False, filter_image=False, filter_movie=False, filter_python=False, filter_font=False, filter_sound=True, filter_text=False, filter_archive=False, filter_btx=False, filter_alembic=False, filter_usd=False, filter_obj=False, filter_volume=False, filter_folder=True, filter_blenlib=False, filemode=9, relative_path=True, display_type='DEFAULT', sort_method='')

   Mix the scene's audio to a sound file

   :param filepath: File Path, Path to file (optional, never None)
   :type filepath: str
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
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: open(*, filepath="", hide_props_region=True, check_existing=False, filter_blender=False, filter_backup=False, filter_image=False, filter_movie=True, filter_python=False, filter_font=False, filter_sound=True, filter_text=False, filter_archive=False, filter_btx=False, filter_alembic=False, filter_usd=False, filter_obj=False, filter_volume=False, filter_folder=True, filter_blenlib=False, filemode=9, relative_path=True, show_multiview=False, use_multiview=False, display_type='DEFAULT', sort_method='', cache=False, mono=False)

   Load a sound file

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
   :type sort_method: str
   :param cache: Cache, Cache the sound in memory (optional)
   :type cache: bool
   :param mono: Mono, Merge all the sound's channels into one (optional)
   :type mono: bool
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: open_mono(*, filepath="", hide_props_region=True, check_existing=False, filter_blender=False, filter_backup=False, filter_image=False, filter_movie=True, filter_python=False, filter_font=False, filter_sound=True, filter_text=False, filter_archive=False, filter_btx=False, filter_alembic=False, filter_usd=False, filter_obj=False, filter_volume=False, filter_folder=True, filter_blenlib=False, filemode=9, relative_path=True, show_multiview=False, use_multiview=False, display_type='DEFAULT', sort_method='', cache=False, mono=True)

   Load a sound file as mono

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
   :type sort_method: str
   :param cache: Cache, Cache the sound in memory (optional)
   :type cache: bool
   :param mono: Mono, Mixdown the sound to mono (optional)
   :type mono: bool
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: pack()

   Pack the sound into the current blend file

   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]
.. function:: unpack(*, method='USE_LOCAL', id="")

   Unpack the sound to the samples filename

   :param method: Method, How to unpack (optional)
   :type method: Literal[:ref:`rna_enum_unpack_method_items`]
   :param id: Sound Name, Sound data-block name to unpack (optional, never None)
   :type id: str
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: update_animation_flags()

   Update animation flags

   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]
