File Operators
==============

.. module:: bpy.ops.file

.. function:: autopack_toggle()

   Automatically pack all external files into the .blend file

   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]
.. function:: bookmark_add()

   Add a bookmark for the selected/active directory

   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]
.. function:: bookmark_cleanup()

   Delete all invalid bookmarks

   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]
.. function:: bookmark_delete(*, index=-1)

   Delete selected bookmark

   :param index: Index, (in [-1, 20000], optional)
   :type index: int
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: bookmark_move(*, direction='TOP')

   Move the active bookmark up/down in the list

   :param direction: Direction, Direction to move the active bookmark towards (optional)

      - ``TOP``
        Top -- Top of the list.
      - ``UP``
        Up.
      - ``DOWN``
        Down.
      - ``BOTTOM``
        Bottom -- Bottom of the list.
   :type direction: Literal['TOP', 'UP', 'DOWN', 'BOTTOM']
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: cancel()

   Cancel file operation

   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]
.. function:: delete()

   Move selected files to the trash or recycle bin

   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]
.. function:: directory_new(*, directory="", open=False, confirm=True)

   Create a new directory

   :param directory: Directory, Name of new directory (optional, never None)
   :type directory: str
   :param open: Open, Open new directory (optional)
   :type open: bool
   :param confirm: Confirm, Prompt for confirmation (optional)
   :type confirm: bool
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: edit_directory_path()

   Start editing directory field

   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]
.. function:: execute()

   Execute selected file

   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]
.. function:: external_operation(*, operation='OPEN')

   Perform external operation on a file or folder

   :param operation: Operation, Operation to perform on the selected file or path (optional)

      - ``OPEN``
        Open -- Open the file.
      - ``FOLDER_OPEN``
        Open Folder -- Open the folder.
      - ``EDIT``
        Edit -- Edit the file.
      - ``NEW``
        New -- Create a new file of this type.
      - ``FIND``
        Find File -- Search for files of this type.
      - ``SHOW``
        Show -- Show this file.
      - ``PLAY``
        Play -- Play this file.
      - ``BROWSE``
        Browse -- Browse this file.
      - ``PREVIEW``
        Preview -- Preview this file.
      - ``PRINT``
        Print -- Print this file.
      - ``INSTALL``
        Install -- Install this file.
      - ``RUNAS``
        Run As User -- Run as specific user.
      - ``PROPERTIES``
        Properties -- Show OS Properties for this item.
      - ``FOLDER_FIND``
        Find in Folder -- Search for items in this folder.
      - ``CMD``
        Command Prompt Here -- Open a command prompt here.
   :type operation: Literal['OPEN', 'FOLDER_OPEN', 'EDIT', 'NEW', 'FIND', 'SHOW', 'PLAY', 'BROWSE', 'PREVIEW', 'PRINT', 'INSTALL', 'RUNAS', 'PROPERTIES', 'FOLDER_FIND', 'CMD']
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: filenum(*, increment=1)

   Increment number in filename

   :param increment: Increment, (in [-100, 100], optional)
   :type increment: int
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: filepath_drop(*, filepath="Path")

   Undocumented, consider `contributing <https://developer.blender.org/>`__.

   :param filepath: (optional, never None)
   :type filepath: str
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: find_missing_files(*, find_all=False, directory="", hide_props_region=True, check_existing=False, filter_blender=False, filter_backup=False, filter_image=False, filter_movie=False, filter_python=False, filter_font=False, filter_sound=False, filter_text=False, filter_archive=False, filter_btx=False, filter_alembic=False, filter_usd=False, filter_obj=False, filter_volume=False, filter_folder=False, filter_blenlib=False, filemode=9, display_type='DEFAULT', sort_method='')

   Try to find missing external files

   :param find_all: Find All, Find all files in the search path (not just missing) (optional)
   :type find_all: bool
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

.. function:: hidedot()

   Toggle hide hidden dot files

   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]
.. function:: highlight()

   Highlight selected file(s)

   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]
.. function:: make_paths_absolute()

   Make all paths to external files absolute

   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]
.. function:: make_paths_relative()

   Make all paths to external files relative to current .blend

   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]
.. function:: mouse_execute()

   Perform the current execute action for the file under the cursor (e.g. open the file)

   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]
.. function:: next()

   Move to next folder

   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]
.. function:: pack_all()

   Pack all used external files into this .blend

   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]
.. function:: pack_libraries()

   Store all data-blocks linked from other .blend files in the current .blend file. Library references are preserved so the linked data-blocks can be unpacked again

   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]
.. function:: parent()

   Move to parent directory

   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]
.. function:: previous()

   Move to previous folder

   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]
.. function:: refresh()

   Refresh the file list

   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]
.. function:: rename()

   Rename file or file directory

   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]
.. function:: report_missing_files()

   Report all missing external files

   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]
.. function:: reset_recent()

   Reset recent files

   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]
.. function:: select(*, wait_to_deselect_others=False, use_select_on_click=False, mouse_x=0, mouse_y=0, extend=False, fill=False, open=True, deselect_all=False, only_activate_if_selected=False, pass_through=False)

   Handle mouse clicks to select and activate items

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
   :param fill: Fill, Select everything beginning with the last selection (optional)
   :type fill: bool
   :param open: Open, Open a directory when selecting it (optional)
   :type open: bool
   :param deselect_all: Deselect On Nothing, Deselect all when nothing under the cursor (optional)
   :type deselect_all: bool
   :param only_activate_if_selected: Only Activate if Selected, Do not change selection if the item under the cursor is already selected, only activate it (optional)
   :type only_activate_if_selected: bool
   :param pass_through: Pass Through, Even on successful execution, pass the event on so other operators can execute on it as well (optional)
   :type pass_through: bool
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: select_all(*, action='TOGGLE')

   Select or deselect all files

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

.. function:: select_bookmark(*, dir="")

   Select a bookmarked directory

   :param dir: Directory, (optional, never None)
   :type dir: str
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: select_box(*, xmin=0, xmax=0, ymin=0, ymax=0, wait_for_input=True, mode='SET')

   Activate/select the file(s) contained in the border

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

.. function:: select_walk(*, direction='UP', extend=False, fill=False)

   Select/Deselect files by walking through them

   :param direction: Walk Direction, Select/Deselect element in this direction (optional)
   :type direction: Literal['UP', 'DOWN', 'LEFT', 'RIGHT']
   :param extend: Extend, Extend selection instead of deselecting everything first (optional)
   :type extend: bool
   :param fill: Fill, Select everything beginning with the last selection (optional)
   :type fill: bool
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: smoothscroll()

   Smooth scroll to make editable file visible

   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]
.. function:: sort_column_ui_context()

   Change sorting to use column under cursor

   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]
.. function:: start_filter()

   Start entering filter text

   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]
.. function:: unpack_all(*, method='USE_LOCAL')

   Unpack all files packed into this .blend to external ones

   :param method: Method, How to unpack (optional)
   :type method: Literal['USE_LOCAL', 'WRITE_LOCAL', 'USE_ORIGINAL', 'WRITE_ORIGINAL', 'KEEP', 'REMOVE']
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: unpack_item(*, method='USE_LOCAL', id_name="", id_type=19785)

   Unpack this file to an external file

   :param method: Method, How to unpack (optional)
   :type method: Literal['USE_LOCAL', 'WRITE_LOCAL', 'USE_ORIGINAL', 'WRITE_ORIGINAL']
   :param id_name: ID Name, Name of ID block to unpack (optional, never None)
   :type id_name: str
   :param id_type: ID Type, Identifier type of ID block (in [0, inf], optional)
   :type id_type: int
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: unpack_libraries()

   Restore all packed linked data-blocks to their original locations

   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]
.. function:: view_selected()

   Scroll the selected files into view

   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]
