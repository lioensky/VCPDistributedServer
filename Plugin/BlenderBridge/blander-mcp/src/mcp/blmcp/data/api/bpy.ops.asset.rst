Asset Operators
===============

.. module:: bpy.ops.asset

.. function:: assign_action()

   Set this pose Action as active Action on the active Object

   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]
   :File: `addons_core/pose_library/operators.py\:103 <https://projects.blender.org/blender/blender/src/branch/main/scripts/addons_core/pose_library/operators.py#L103>`__

.. function:: bundle_install(*, asset_library_reference='', filepath="", hide_props_region=True, check_existing=True, filter_blender=True, filter_backup=False, filter_image=False, filter_movie=False, filter_python=False, filter_font=False, filter_sound=False, filter_text=False, filter_archive=False, filter_btx=False, filter_alembic=False, filter_usd=False, filter_obj=False, filter_volume=False, filter_folder=True, filter_blenlib=False, filemode=8, display_type='DEFAULT', sort_method='')

   Copy the current .blend file into an Asset Library. Only works on standalone .blend files (i.e. when no other files are referenced)

   :param asset_library_reference: asset_library_reference, (optional)
   :type asset_library_reference: str
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

.. function:: catalog_delete(*, catalog_id="")

   Remove an asset catalog from the asset library (contained assets will not be affected and show up as unassigned)

   :param catalog_id: Catalog ID, ID of the catalog to delete (optional, never None)
   :type catalog_id: str
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: catalog_new(*, parent_path="")

   Create a new catalog to put assets in

   :param parent_path: Parent Path, Optional path defining the location to put the new catalog under (optional, never None)
   :type parent_path: str
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: catalog_redo()

   Redo the last undone edit to the asset catalogs

   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]
.. function:: catalog_undo()

   Undo the last edit to the asset catalogs

   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]
.. function:: catalog_undo_push()

   Store the current state of the asset catalogs in the undo buffer

   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]
.. function:: catalogs_save()

   Make any edits to any catalogs permanent by writing the current set up to the asset library

   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]
.. function:: clear(*, set_fake_user=False)

   Delete all asset metadata and turn the selected asset data-blocks back into normal data-blocks

   :param set_fake_user: Set Fake User, Ensure the data-block is saved, even when it is no longer marked as asset (optional)
   :type set_fake_user: bool
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: clear_single(*, set_fake_user=False)

   Delete all asset metadata and turn the asset data-block back into a normal data-block

   :param set_fake_user: Set Fake User, Ensure the data-block is saved, even when it is no longer marked as asset (optional)
   :type set_fake_user: bool
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: library_refresh()

   Reread assets and asset catalogs from the asset library on disk

   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]
.. function:: mark()

   Enable easier reuse of selected data-blocks through the Asset Browser, with the help of customizable metadata (like previews, descriptions and tags)

   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]
.. function:: mark_single()

   Enable easier reuse of a data-block through the Asset Browser, with the help of customizable metadata (like previews, descriptions and tags)

   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]
.. function:: open_containing_blend_file()

   Open the blend file that contains the active asset

   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]
   :File: `startup/bl_operators/assets.py\:103 <https://projects.blender.org/blender/blender/src/branch/main/scripts/startup/bl_operators/assets.py#L103>`__

.. function:: screenshot_preview(*, p1=(0, 0), p2=(0, 0), force_square=True)

   Capture a screenshot to use as a preview for the selected asset

   :param p1: Point 1, First point of the screenshot in screenspace (array of 2 items, in [0, inf], optional)
   :type p1: Sequence[int]
   :param p2: Point 2, Second point of the screenshot in screenspace (array of 2 items, in [0, inf], optional)
   :type p2: Sequence[int]
   :param force_square: Force Square, If enabled, the screenshot will have the same height as width (optional)
   :type force_square: bool
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: tag_add()

   Add a new keyword tag to the active asset

   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]
   :File: `startup/bl_operators/assets.py\:42 <https://projects.blender.org/blender/blender/src/branch/main/scripts/startup/bl_operators/assets.py#L42>`__

.. function:: tag_remove()

   Remove an existing keyword tag from the active asset

   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]
   :File: `startup/bl_operators/assets.py\:65 <https://projects.blender.org/blender/blender/src/branch/main/scripts/startup/bl_operators/assets.py#L65>`__

