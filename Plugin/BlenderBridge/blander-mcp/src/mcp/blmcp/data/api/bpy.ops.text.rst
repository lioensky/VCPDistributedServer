Text Operators
==============

.. module:: bpy.ops.text

.. function:: autocomplete()

   Show a list of used text in the open document

   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]
.. function:: comment_toggle(*, type='TOGGLE')

   Undocumented, consider `contributing <https://developer.blender.org/>`__.

   :param type: Type, Add or remove comments (optional)
   :type type: Literal['TOGGLE', 'COMMENT', 'UNCOMMENT']
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: convert_whitespace(*, type='SPACES')

   Convert whitespaces by type

   :param type: Type, Type of whitespace to convert to (optional)
   :type type: Literal['SPACES', 'TABS']
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: copy()

   Copy selected text to clipboard

   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]
.. function:: cursor_set(*, x=0, y=0)

   Set cursor position

   :param x: X, (in [-inf, inf], optional)
   :type x: int
   :param y: Y, (in [-inf, inf], optional)
   :type y: int
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: cut()

   Cut selected text to clipboard

   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]
.. function:: delete(*, type='NEXT_CHARACTER')

   Delete text by cursor position

   :param type: Type, Which part of the text to delete (optional)
   :type type: Literal['NEXT_CHARACTER', 'PREVIOUS_CHARACTER', 'NEXT_WORD', 'PREVIOUS_WORD']
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: duplicate_line()

   Duplicate the current line

   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]
.. function:: find()

   Find specified text

   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]
.. function:: find_set_selected()

   Find specified text and set as selected

   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]
.. function:: indent()

   Indent selected text

   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]
.. function:: indent_or_autocomplete()

   Indent selected text or autocomplete

   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]
.. function:: insert(*, text="")

   Insert text at cursor position

   :param text: Text, Text to insert at the cursor position (optional, never None)
   :type text: str
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: jump(*, line=1)

   Jump cursor to line

   :param line: Line, Line number to jump to (in [1, inf], optional)
   :type line: int
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: jump_to_file_at_point(*, filepath="", line=0, column=0)

   Jump to a file for the text editor

   :param filepath: Filepath, (optional, never None)
   :type filepath: str
   :param line: Line, Line to jump to (in [0, inf], optional)
   :type line: int
   :param column: Column, Column to jump to (in [0, inf], optional)
   :type column: int
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: line_break()

   Insert line break at cursor position

   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]
.. function:: line_number()

   The current line number

   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]
.. function:: make_internal()

   Make active text file internal

   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]
.. function:: move(*, type='LINE_BEGIN')

   Move cursor to position type

   :param type: Type, Where to move cursor to (optional)
   :type type: Literal['LINE_BEGIN', 'LINE_END', 'FILE_TOP', 'FILE_BOTTOM', 'PREVIOUS_CHARACTER', 'NEXT_CHARACTER', 'PREVIOUS_WORD', 'NEXT_WORD', 'PREVIOUS_LINE', 'NEXT_LINE', 'PREVIOUS_PAGE', 'NEXT_PAGE']
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: move_lines(*, direction='DOWN')

   Move the currently selected line(s) up/down

   :param direction: Direction, (optional)
   :type direction: Literal['UP', 'DOWN']
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: move_select(*, type='LINE_BEGIN')

   Move the cursor while selecting

   :param type: Type, Where to move cursor to, to make a selection (optional)
   :type type: Literal['LINE_BEGIN', 'LINE_END', 'FILE_TOP', 'FILE_BOTTOM', 'PREVIOUS_CHARACTER', 'NEXT_CHARACTER', 'PREVIOUS_WORD', 'NEXT_WORD', 'PREVIOUS_LINE', 'NEXT_LINE', 'PREVIOUS_PAGE', 'NEXT_PAGE']
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: new()

   Create a new text data-block

   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]
.. function:: open(*, filepath="", hide_props_region=True, check_existing=False, filter_blender=False, filter_backup=False, filter_image=False, filter_movie=False, filter_python=True, filter_font=False, filter_sound=False, filter_text=True, filter_archive=False, filter_btx=False, filter_alembic=False, filter_usd=False, filter_obj=False, filter_volume=False, filter_folder=True, filter_blenlib=False, filemode=9, relative_path=True, display_type='DEFAULT', sort_method='', internal=False)

   Open a new text data-block

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
   :param internal: Make Internal, Make text file internal after loading (optional)
   :type internal: bool
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: overwrite_toggle()

   Toggle overwrite while typing

   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]
.. function:: paste(*, selection=False)

   Paste text from clipboard

   :param selection: Selection, Paste text selected elsewhere rather than copied (X11/Wayland only) (optional)
   :type selection: bool
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: reload()

   Reload active text data-block from its file

   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]
.. function:: replace(*, all=False)

   Replace text with the specified text

   :param all: Replace All, Replace all occurrences (optional)
   :type all: bool
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: replace_set_selected()

   Replace text with specified text and set as selected

   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]
.. function:: resolve_conflict(*, resolution='IGNORE')

   When external text is out of sync, resolve the conflict

   :param resolution: Resolution, How to solve conflict due to differences in internal and external text (optional)
   :type resolution: Literal['IGNORE', 'RELOAD', 'SAVE', 'MAKE_INTERNAL']
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: run_script()

   Run active script

   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]
.. function:: save()

   Save active text data-block

   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]
.. function:: save_as(*, filepath="", hide_props_region=True, check_existing=True, filter_blender=False, filter_backup=False, filter_image=False, filter_movie=False, filter_python=True, filter_font=False, filter_sound=False, filter_text=True, filter_archive=False, filter_btx=False, filter_alembic=False, filter_usd=False, filter_obj=False, filter_volume=False, filter_folder=True, filter_blenlib=False, filemode=9, display_type='DEFAULT', sort_method='')

   Save active text file with options

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

.. function:: scroll(*, lines=1)

   Undocumented, consider `contributing <https://developer.blender.org/>`__.

   :param lines: Lines, Number of lines to scroll (in [-inf, inf], optional)
   :type lines: int
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: scroll_bar(*, lines=1)

   Undocumented, consider `contributing <https://developer.blender.org/>`__.

   :param lines: Lines, Number of lines to scroll (in [-inf, inf], optional)
   :type lines: int
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: select_all()

   Select all text

   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]
.. function:: select_line()

   Select text by line

   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]
.. function:: select_word()

   Select word under cursor

   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]
.. function:: selection_set()

   Set text selection

   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]
.. function:: start_find()

   Start searching text

   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]
.. function:: to_3d_object(*, split_lines=False)

   Create 3D text object from active text data-block

   :param split_lines: Split Lines, Create one object per line in the text (optional)
   :type split_lines: bool
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: unindent()

   Unindent selected text

   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]
.. function:: unlink()

   Unlink active text data-block

   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]
.. function:: update_shader()

   Update users of this shader, such as custom cameras and script nodes, with its new sockets and options

   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]
