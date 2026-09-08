Ed Operators
============

.. module:: bpy.ops.ed

.. function:: flush_edits()

   Flush edit data from active editing modes

   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]
.. function:: lib_id_fake_user_toggle()

   Save this data-block even if it has no users

   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]
.. function:: lib_id_generate_preview()

   Create an automatic preview for the selected data-block

   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]
.. function:: lib_id_generate_preview_from_object()

   Create a preview for this asset by rendering the active object

   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]
.. function:: lib_id_load_custom_preview(*, filepath="", hide_props_region=True, check_existing=False, filter_blender=False, filter_backup=False, filter_image=True, filter_movie=False, filter_python=False, filter_font=False, filter_sound=False, filter_text=False, filter_archive=False, filter_btx=False, filter_alembic=False, filter_usd=False, filter_obj=False, filter_volume=False, filter_folder=True, filter_blenlib=False, filemode=9, show_multiview=False, use_multiview=False, display_type='DEFAULT', sort_method='')

   Choose an image to help identify the data-block visually

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
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: lib_id_override_editable_toggle()

   Set if this library override data-block can be edited

   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]
.. function:: lib_id_remove_preview()

   Remove the preview of this data-block

   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]
.. function:: lib_id_unlink()

   Remove a usage of a data-block, clearing the assignment

   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]
.. function:: redo()

   Redo previous action

   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]
.. function:: undo()

   Undo previous action

   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]
.. function:: undo_history(*, item=0)

   Undo or redo specific action in history

   :param item: Item, (in [0, inf], optional)
   :type item: int
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: undo_push(*, message="Add an undo step *function may be moved*")

   Add an undo state (internal use only)

   :param message: Undo Message, (optional, never None)
   :type message: str
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: undo_redo()

   Undo and redo previous action

   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]
