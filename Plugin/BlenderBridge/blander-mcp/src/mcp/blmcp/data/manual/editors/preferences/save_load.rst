.. _prefs-save-load:

***********
Save & Load
***********

.. figure:: /images/editors_preferences_section_save-load.webp

   Preferences Save/Load section.


Blend Files
===========

.. _bpy.types.PreferencesView.use_save_prompt:

Save -- Save Prompt
   Asks for confirmation before closing or opening a new blend-file
   if the current file has unsaved changes.

.. _bpy.types.PreferencesFilePaths.save_version:

Save Versions
   Number of versions created (for backup) when saving newer versions of a file.

   This option keeps saved versions of your file in the same directory,
   using extensions: ``.blend1``, ``.blend2``, etc.,
   with the number increasing to the number of versions you specify.

   Older files will be named with a higher number.
   E.g. with the default setting of 2, you will have three versions of your file:

   - ``*.blend`` -- last saved.
   - ``*.blend1`` -- second last saved.
   - ``*.blend2`` -- third last saved.

.. _bpy.types.PreferencesFilePaths.recent_files:

Recent Files
   Number of files displayed in :menuselection:`File --> Open Recent`.

.. _bpy.types.PreferencesFilePaths.use_auto_save_temporary_files:

Auto Save
   Enables Blender's :ref:`Auto Save <bpy.ops.wm.recover_auto_save>` feature,
   which periodically saves a temporary backup of the current file to the :ref:`temp-dir`.

   This is useful for recovering work after a crash or unexpected shutdown.

   .. _bpy.types.PreferencesFilePaths.auto_save_time:

   Timer (Minutes)
      Specifies the interval, in minutes, between automatic saves.
      Shorter intervals provide better protection but may increase disk writes slightly,
      which could cause performance issues for larger files.

.. _bpy.types.PreferencesFilePaths.file_preview_type:

File Preview Types
   Select how blend-file preview are generated.
   These previews are used both in the :doc:`File Browser </editors/file_browser>`
   and for previews shown in the operating system's file browser.

   :None: Do not generate any blend-file previews.
   :Auto:
      If there is no camera in the 3D Viewport a preview using a screenshot of the active Workspace is generated.
      If a camera is in the scene, a preview of the viewport from the camera view is used.
   :Screenshot: Generate a preview by taking a screenshot of the active Workspace.
   :Camera View: Generate a preview of a Workbench render from the camera's point of view.

.. _bpy.types.PreferencesFilePaths.use_relative_paths:

Default To -- Relative Paths
   Default value for :ref:`Relative Paths <files-blend-relative_paths>` when loading external files
   such as images, sounds, and linked libraries. It will be ignored if a path is already set.

.. _bpy.types.PreferencesFilePaths.use_file_compression:

Default To -- Compress File
   Default value for :ref:`Compress file <files-blend-compress>` when saving blend-files.

.. _bpy.types.PreferencesFilePaths.use_load_ui:

Default To -- Load UI
   Default value for :ref:`Load UI <file-load-ui>` when loading blend-files.

.. _bpy.types.PreferencesFilePaths.use_tabs_as_spaces:

Text Files -- Tabs as Spaces
   Entering :kbd:`Tab` in the Text Editor adds the appropriate number of spaces
   instead of using characters.


.. _bpy.ops.preferences.autoexec_path:
.. _bpy.types.PreferencesFilePaths.use_scripts_auto_execute:

Auto Run Python Scripts
-----------------------

Python scripts (including driver expressions) are not executed by default for security reasons.
You may be working on projects where you only load files from trusted sources,
making it more convenient to allow scripts to be executed automatically.

.. _bpy.types.PathCompare:

Excluded Paths
   Blend-files in these folders will *not* automatically run Python scripts.
   This can be used to define where blend-files from untrusted sources are kept.

.. seealso::

   :doc:`Python Security </advanced/scripting/security>`.


File Browser
============

.. _bpy.types.PreferencesFilePaths.show_recent_locations:

Show Locations -- Recent
   Hide the *Recent* panel of the :doc:`File Browser </editors/file_browser>`
   which displays recently accessed folders.

.. _bpy.types.PreferencesFilePaths.show_system_bookmarks:

Show Locations -- System
   Hide System Bookmarks in the *File Browser*.

.. _bpy.types.PreferencesFilePaths.use_filter_files:

Defaults -- Filter Files
   By activating this, the file region in the File Browser will only show appropriate files
   (i.e. blend-files when loading a complete Blender setting).
   The selection of file types may be changed in the file region.

.. _bpy.types.PreferencesFilePaths.show_hidden_files_datablocks:

Defaults -- Show Hidden Files/Data-Blocks
   Display files and data-blocks whose names start with ``.`` in File Browsers.

   By default, dot-prefixed data-block names are hidden to prevent accidental use
   of internal or helper data-blocks. See :ref:`data-system-datablock-name-hidden`
   for more information about this naming convention.

   .. seealso::

      Hidden data-blocks can also be shown in :ref:`Data-Block Menus <ui-data-block>`
      by enabling :ref:`bpy.types.Preferences.show_hidden_ids`.
