
******
Topbar
******

Menus
=====

.. figure:: /images/interface_window-system_topbar_menus.png


.. _topbar-blender_menu:

Blender Menu
------------

Splash Screen
   Open the :ref:`splash`.

.. _bpy.ops.wm.splash_about:

About Blender
   Opens a menu displaying the following information about Blender:

   - **Version**: The Blender version.
   - **Date**: Date when Blender was compiled.
   - **Hash**: The Git Hash of the build.
     This can be useful to give to support personnel when diagnosing a problem.
   - **Branch**: Optional branch name.
   - **Windowing Environment**: On Linux, this will show either Wayland or X11 depending
     on the windowing environment that Blender is running on.

   - **Donate**: Open Blender's `Development Fund <https://fund.blender.org/>`__ website.
   - **What's New**: Open the latest release notes.
   - **Credits**: Open the `credits <https://www.blender.org/about/credits/>`__ webpage.
   - **License**: Open the `license <https://www.blender.org/about/license/>`__ webpage.
   - **Blender Store**: Open the `Blender Store <https://store.blender.org/>`__ website.
   - **Blender Website**: Open main `Blender <https://www.blender.org/>`__ website.

Install Application Template
   Install a new :ref:`application template <app_templates>`.


File Menu
---------

The options to manage files are:

New :kbd:`Ctrl-N`
   Clears the current scene and loads the selected application template.
Open :kbd:`Ctrl-O`
   :ref:`Open <bpy.ops.wm.open_mainfile>` a blend-file.
Open Recent :kbd:`Shift-Ctrl-O`
   Displays a list of the most :ref:`recently opened <other-file-open-options>` blend-files.
   Hovering over items will show a preview, and information about the blend-file.
   Select any of the file names in the list to open that blend-file.

   Clear Recent Files List
      Removes items from the recent files list.
Revert
   Reopens the current file to its last saved version.
Recover
   Options to recover a blend-file from the accidentally closing Blender or a crash. See:

   - :ref:`bpy.ops.wm.recover_last_session`
   - :ref:`bpy.ops.wm.recover_auto_save`

-----

Save :kbd:`Ctrl-S`
   :ref:`Save <bpy.ops.wm.save_mainfile>` the current blend-file.
Save As... :kbd:`Shift-Ctrl-S`
   Opens the File Browser to specify file name and location of :ref:`save <bpy.ops.wm.save_mainfile>`.
Save Copy...
   :ref:`Saves <bpy.ops.wm.save_mainfile>` a copy of the current file.
Save Incremental :kbd:`Ctrl-Alt-S`
   Save the current Blender file with a numerically
   incremented name that does not overwrite any existing files.

----

Link...
   Links data from an external blend-file (library) to the current one.
   The editing of that data is only possible in the external library.
   *Link* and *Append* are used to load in only selected parts from another file.
   See :doc:`Linked Libraries </files/linked_libraries/index>`.
Append...
   Appends data from an external blend-file to the current one.
   The new data is copied from the external file, and completely unlinked from it.
Data Previews
   Tools for managing :doc:`data-block previews </files/blend/previews>`.

-----

Import
   Blender can use information stored in a variety of other format files which are created by
   other graphics programs. See :doc:`Import/Export </files/import_export/index>`.
Export
   Normally you save your work in a blend-file,
   but you can export some or all of your work to a format that can be processed by other graphics programs.
   See :doc:`Import/Export </files/import_export/index>`.

.. _bpy.ops.wm.collection_export_all:

Export All Collections
   Invokes all :ref:`configured exporters <collections-exporters>` for all collection.

-----

External Data
   External data, like texture images and other resources,
   can be stored inside the blend-file (packed) or as separate files (unpacked).
   Blender keeps track of all unpacked resources via a relative or absolute path.
   See :ref:`pack or unpack external data <pack-unpack-data>`.

   Automatically Pack Resources
      Pack all currently used external files into the blend-file and automatically pack any files
      that are added later. Unchecking this option will only stop the automatic packing for new files;
      it won't unpack existing ones.
   Pack Resources
      Pack all used external files into the blend-file. After running this operator and saving the
      blend-file, the external files will no longer be used -- any changes in them will no longer be
      reflected in the blend-file, and you are free to move or delete them.
   Unpack Resources
      Export previously packed files back to external ones. You can choose whether to reuse existing
      external files or overwrite them.
   Pack Linked Libraries
      Pack data-blocks that are :doc:`linked </files/linked_libraries/link_append>` from an external
      blend-file into the current one.
   Unpack Linked Libraries
      Export previously packed data-blocks back to external blend-files. Existing blend-files are
      overwritten.
   Make Paths Relative
      Make all paths to external files :ref:`relative <files-blend-relative_paths>` to the current blend-file.
   Make Paths Absolute
      Make all paths to external files absolute (= full path from the system's root).
   Report Missing Files
      This option is useful to check if there are links to unpacked files that no longer exist.
      After selecting this option, a warning message will appear in the Info editor's header.
      If no warning is shown, there are no missing external files.
   Find Missing Files
      In case you have broken links in a blend-file, this can help you to fix the problem.
      A File Browser will show up. Select the desired directory (or a file within that directory),
      and a search will be performed in it, recursively in all contained directories.
      Every missing file found in the search will be recovered.
      Those recoveries will be done as absolute paths,
      so if you want to have relative paths you will need to select *Make Paths Relative*.

      .. note::

         Recovered files might need to be reloaded. You can do that one by one, or
         you can save the blend-file and reload it again, so that all external files are reloaded at once.

Clean Up
   Purge Unused Data
      Opens a dialog to remove unused data-blocks from both the current blend-file or any
      :doc:`Linked Data </files/linked_libraries/link_append>` (cannot be undone).
      See the :ref:`Outliner <bpy.ops.outliner.orphans_purge>` for more information.

   .. _bpy.ops.outliner.orphans_manage:

   Manage Unused Data
      Opens a pop-up window of the :doc:`Outliner </editors/outliner/index>` in
      :ref:`Unused Data mode <bpy.types.SpaceOutliner.display_mode>` which lists
      :doc:`data-blocks </files/data_blocks>` and other data that are unused
      and/or will be lost when the file is reloaded. It includes data-blocks which have only a fake user.
      You can add/remove the Fake User by clicking on cross/tick icon on the right side of the Outliner.

-----

.. _startup-file:

Defaults
   This menu manages the startup file which is used to store the default scene,
   workspace, and interface displayed when creating a new file.

   Initially this contains the :doc:`startup scene </editors/3dview/startup_scene>` included with Blender.
   This can be replaced by your own customized setup.

   .. _bpy.ops.wm.save_homefile:

   Save Startup File
      Saves the current blend-file as the startup file.

   .. _bpy.ops.wm.read_factory_settings:

   Load Factory Settings
      Restores the default startup file and preferences.

   When an :doc:`/advanced/app_templates` is in use the following operators are shown:

   Load Factory Blender Settings
      Loads the default settings to the original Blender settings without
      the changes made from the current application template.
   Load Factory (Application Template Name) Settings
      Loads the default settings to the original application template.

   .. seealso:: :ref:`prefs-menu`.

-----

Quit :kbd:`Ctrl-Q`
   Closes Blender. The current scene is saved to a file called "quit.blend" in Blender's temporary directory
   (which can be found on the "File Paths" tab of the :doc:`Preferences </editors/preferences/file_paths>`).


Edit Menu
---------

Undo, Redo, Undo History
   See :doc:`/interface/undo_redo`.
Adjust Last Operation, Repeat Last, Repeat History
   See :doc:`/interface/undo_redo`.
Menu Search
   Find a menu based on its name.
Operator Search
   Execute an operator based on its name (:ref:`Developer Extras <bpy.types.PreferencesView.show_developer_ui>` only).
Rename Active Item
   Rename the active object or node;
   see :ref:`Rename tool <tools_rename-active>` for more information.
Batch Rename
   Renames multiple data types at once;
   see :ref:`Batch Rename tool <bpy.ops.wm.batch_rename>` for more information.

.. _bpy.types.ToolSettings.lock_object_mode:

Lock Object Modes
   Prevents selecting objects that are in a different mode than the current one.

   .. note::

      This option can prevent accidental mode changes, such as when you're
      trying to select a bone in Pose Mode to animate it, but instead
      click a piece of background scenery (which would normally select that
      piece and switch to Object Mode).

      You may want to disable *Lock Object Modes* for example when weighting rigged objects
      or sculpting/painting where you intentionally want to switch between objects in different modes.

Preferences :kbd:`Ctrl-Comma`
   Open the :doc:`Preferences window </editors/preferences/index>`.


.. _topbar-render:

Render Menu
-----------

Render Image :kbd:`F12`
   Render the active scene at the current frame.
Render Animation :kbd:`Ctrl-F12`
   Render the animation of the active scene.

   .. seealso::

      - :doc:`Rendering Animations </render/output/animation>` for details.
Render Sequencer Image :kbd:`Alt-F12`
   If a :doc:`Sequencer Scene </video_editing/sequencer_scene>` exists that differs from the active scene, render that
   scene instead. 
Render Sequencer Animation :kbd:`Ctrl-Alt-F12`
   Render the animation of the :doc:`Sequencer Scene </video_editing/sequencer_scene>`.

   .. note:: 
      Both of the sequencer render options automatically set the 
      :ref:`Show Sequencer Scene <bpy.types.SpaceImageEditor.show_sequencer_scene>` toggle in the image editor Render 
      Result after rendering.  

Render Audio
   Mix the scene's audio to a sound file.

   .. seealso::

      - :doc:`Rendering audio </render/output/audio/introduction>` for details.
View Render :kbd:`F11`
   Show the Render window. (Press again to switch back to the main Blender window.)

.. _topbar-render-view_animation:

View Animation :kbd:`Ctrl-F11`
   Playback rendered animation in a separate player.

   .. seealso::

      - :ref:`Animation player <bpy.ops.render.play_rendered_anim>` for details.
      - :ref:`Preferences <bpy.types.PreferencesFilePaths.animation_player_preset>` for selecting a
        different animation player than the default one.
Lock Interface
   Lock interface during rendering in favor of giving more memory to the renderer.


.. _topbar-window:

Window Menu
-----------

New Window
   Create a new window by copying the current window.
New Main Window
   Create a new window with its own workspace and scene selection.
Toggle Window Fullscreen
   Toggle the current window fullscreen.
Next Workspace
   Switch to the next workspace.
Previous Workspace
   Switch to the previous workspace.

.. _bpy.types.Screen.show_statusbar:

Show Status Bar
   Choose whether the :doc:`Status Bar </interface/window_system/status_bar>`
   at the bottom of the window should be displayed.

.. _bpy.ops.screen.screenshot:

Save Screenshot
   Capture a picture of the current Blender window.
   A File Browser will open to choose where the screenshot is saved.

.. _bpy.ops.screen.screenshot_area:

Save Screenshot (Editor)
   Capture a picture of the selected Editor.
   Select the Editor by clicking :kbd:`LMB` within its area after running the operator.
   A File Browser will open to choose where the screenshot is saved.


Help Menu
---------

See :ref:`help-menu`.


Workspaces
==========

.. figure:: /images/interface_window-system_topbar_workspaces.png
   :align: center

This set of tabs is used to switch between :doc:`Workspaces </interface/window_system/workspaces>`,
which are essentially predefined window layouts.


Scenes & Layers
===============

.. figure:: /images/interface_window-system_topbar_scenes-layers.png
   :align: center

These :ref:`data-block menus <ui-data-block>` are used to select
the current :doc:`Scene </scene_layout/scene/index>` and :doc:`View Layer </render/layers/index>`.
