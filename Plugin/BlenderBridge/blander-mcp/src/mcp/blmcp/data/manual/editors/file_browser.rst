.. index:: Editors; File Browser

.. _bpy.ops.file:
.. _bpy.types.FileSelectParams:
.. _bpy.types.SpaceFileBrowser:

************
File Browser
************

The File Browser is used in all file-related operations. These include:

- Opening and saving blend-files.
- Browsing the content of other blend-files when appending or linking data-blocks
  (see :doc:`Linked Libraries </files/linked_libraries/index>`).
- Importing from/exporting to other file formats.
- Updating the locations of previously imported media (images, videos, fonts...).

The most common way to use this editor is through modal operators (like opening or saving a blend-file).
The File Browser will appear in a new window, wait for you to select a file, and then close again.

You can also use the File Browser like a regular, permanently visible editor. In fact,
the predefined Video Editing :doc:`workspace </interface/window_system/workspaces>` uses it this way.
This lets you drag-and-drop media from the browser straight into e.g. the
:doc:`3D Viewport </editors/3dview/introduction>` or the
:doc:`Video Sequencer </editors/video_sequencer/introduction>`, saving you some overhead.

.. figure:: /images/editors_file-browser_editor.png

   The File Browser.


Interface
=========

Main Region
-----------

The main region lists files, folders, or blend-file contents.
Hovering over an item will show a tooltip with extra information.


.. _file_browser-previews:

Previews
^^^^^^^^

In its *Thumbnail* display mode, the File Browser supports many types of previews. These include:

- Image and video formats
- Fonts
- Blend-files
- Internal :doc:`Data-blocks </files/data_blocks>`

In order to get previews for data-blocks, these must first be generated.
See :doc:`/files/blend/previews`.

.. figure:: /images/editors_file-browser_previews.png
   :align: center
   :width: 50%

   The File Browser in *Thumbnail* mode.


Directory Region
----------------

Above the file list, there's a textbox showing the current folder path, along with buttons for navigating.

.. _bpy.ops.file.previous:

Previous Folder :kbd:`Backspace`, :kbd:`Alt-Left`, :kbd:`Mouse4`
   Move to previous folder in navigation history.

.. _bpy.ops.file.next:

Next Folder :kbd:`Shift-Backspace`, :kbd:`Alt-Right` :kbd:`Mouse5`
   Move to next folder in navigation history.

.. _bpy.ops.file.parent:

Parent Directory :kbd:`P`, :kbd:`Alt-Up`
   Move up to parent directory.

.. _bpy.ops.file.refresh:

Refresh File List :kbd:`R`, :kbd:`NumpadPeriod`
   Refresh current folder.

.. _bpy.ops.file.directory_new:

Create New Directory :kbd:`I`
   Create a new directory inside the current one.

.. _bpy.types.FileSelectParams.directory:

Directory :kbd:`Ctrl-L`
   The current folder path.
   :kbd:`Tab` will auto-complete an existing path.
   If you type a nonexistent path, you will be prompted to create it.

.. _bpy.types.FileSelectParams.filter_search:

Search :kbd:`Ctrl-F`
   Filter items by name.
   The wildcard ``*`` will match anything, e.g. ``bl*er`` will match both ``blender`` and ``blogger``.
   There is always an implicit wildcard at the start and end of the search text,
   so ``blender`` will also match ``test_blender_file.blend``.
   This field can also be used to filter some specific file extension (e.g. ``.png`` will list all PNG files).

.. _bpy.types.FileSelectParams.display_type:

Display Mode
   Control how files are displayed.

   :Vertical List: Displays files and folders in a vertical list.
   :Horizontal List: Displays files and folders in a horizontal list.
   :Thumbnails: Shows :ref:`previews <file_browser-previews>`.


Display Settings
^^^^^^^^^^^^^^^^

.. _bpy.types.FileSelectParams.display_size:

Size
   The size of the thumbnails.

.. _bpy.types.FileSelectParams.recursion_level:

Recursions
   The number of directory levels to show at once in a flat way.

   :None: List only the current directory's content.
   :Blend File: List the whole content of a blend-file (only available when linking or appending data-blocks).
   :One Level: List all subdirectories' content, one level of recursion.
   :Two Levels: List all subdirectories' content, two levels of recursion.
   :Three Levels: List all subdirectories' content, three levels of recursion.

   .. hint::

      Showing several levels of directories at once can be handy to e.g. see your whole collection of textures,
      even if you have arranged them in a nice set of directories to avoid having hundreds of
      files in a single place.

      In the *Append/Link* case, showing the content of the whole blend-file lets you
      link different types of data-blocks in a single operation.

   .. warning::

      The more levels you show at once, the more time it will take to list them all.

.. _bpy.types.FileSelectParams.sort_method:

Sort By
   Sorts items by one of the four methods:

   :Name: Sort the file list alphabetically.
   :Extension: Sort the file list by extension/type.
   :Modified Date: Sort files by modification time.
   :Size: Sort files by size.


.. _bpy.types.FileSelectParams.use_filter:

Filter Settings
^^^^^^^^^^^^^^^

The toggle with the funnel icon controls whether filtering is enabled or not.
The dropdown button next to it shows the filtering options.

File Types
   Filters files by categories, like folders, blend-files, images, etc.

.. _bpy.types.FileSelectIDFilter:

Blender IDs
   When appending or linking, you can also filter by data-block categories, like scenes, animations, materials, etc.

.. _bpy.types.FileSelectParams.show_hidden:

Show Hidden :kbd:`H`
   Shows hidden files (starting with a ``.``).


Execution Region
----------------

These controls are at the bottom of the editor.

.. _bpy.types.FileSelectParams.filename:

File Name
   Text field to edit the file name and extension. Turns red to warn you about overwriting an existing file.
   :kbd:`Tab` will auto-complete to existing names in the current directory.

   :bl-icon:`remove`/:bl-icon:`add` (Increment Number in Filename)
      Adds/increases or removes/decreases a trailing number in your file name
      (used e.g. to store different versions of a file).

.. _bpy.ops.file.cancel:

Cancel :kbd:`Esc`
   Closes the File Browser and cancels the operation.

.. _bpy.ops.file.execute:

Confirm :kbd:`Return`
   Confirm the current directory and file name. You can also double-click a file or data-block
   in the main region.


Quick Access Region
-------------------

The region on the left contains a few panels for quickly jumping to certain directories with a single click.

The *System* and *Recent* panels can be hidden using the :ref:`Save & Load <prefs-save-load>` preferences.

.. _bpy.types.SpaceFileBrowser.bookmarks:

Bookmarks
^^^^^^^^^

A custom list of folders that you use often. You can use the buttons to the right of the list to add/remove/move
items.


.. _bpy.types.SpaceFileBrowser.system_bookmarks:

System
^^^^^^

Common directories such as the home directory in Linux or the "Documents" folder in Windows.


.. _bpy.types.SpaceFileBrowser.system_folders:

Volumes
^^^^^^^

Drives and network mounts.


.. _bpy.types.SpaceFileBrowser.recent_folders:

Recent
^^^^^^

Recently accessed folders.

.. _bpy.ops.file.reset_recent:

Clicking the :bl-icon:`downarrow_hlt` button to the right reveals *Clear Recent Items* to fully clear this list.


Operator Options Region
-----------------------

The right region shows the options of the calling operator.
Besides the common actions listed below, many import/export add-ons will also expose their options there.

Open, Save, Save As Blender File
   See :doc:`/files/blend/open_save`.
Open, Replace, Save As Image
   See :doc:`/files/media/image_formats`.
Link/Append from Library
   See :doc:`Linked libraries </files/linked_libraries/index>`.

For the common option:

Relative Path
   See :ref:`files-blend-relative_paths`.


Header Region
-------------

The header only contains two menus, one with the standard editor *View* controls
and the other to list a few `Selecting`_ operators for the sake of discoverability.
These menus are not visible when the browser is in a modal window.


Navigating
==========

Entering a Directory :kbd:`Return`
   Double-click a directory to enter it.
Parent Directory :kbd:`P`
   Takes you up one level of directory.


File Drop
---------

You can also drag and drop a file or directory from your file manager into the Blender File Browser.
This will navigate to the item and select it.


.. _bpy.ops.file.select_all:

Selecting
=========

Select
   Click :kbd:`LMB` to select a single item. Additionally hold :kbd:`Ctrl` to add/remove that item
   to/from the selection, or :kbd:`Shift` to select a range of items.

.. _bpy.ops.file.select_box:

Dragging
   Dragging with :kbd:`LMB` starts a :ref:`box selection <tool-select-box>`.

.. note::

   You can always select several entries in the File Browser --
   the last selected one is considered the active one.
   If the calling operation expects a single path (like e.g. the main blend-file *Open* one),
   it will get that active item's path, and the other selected items will be ignored.


Arrow Keys
----------

It is also possible to select/deselect files by "walking" through them using the arrow keys:

- Press an arrow key to select the next/previous file in the list and deselect all the others.
- Hold :kbd:`Shift` to keep the current selection (and add to it).
- Hold :kbd:`Shift-Ctrl` to invert the selection as you pass over it.

If no file is selected, the arrow key navigation selects the first or last file in the directory,
depending on the arrow direction.


Editing
=======

The following operations are available in the file list's context menu.

.. _bpy.ops.file.external_operation:

External
   Use the operating system to perform an action on the file or directory.
   The options listed below might not be available on all operating systems.

   :Open: Open the file.
   :Open Folder: Open the folder.
   :Edit: Edit the file.
   :New: Create a new file of this type.
   :Find File: Search for files of this type.
   :Show: Show this file.
   :Play: Play this file.
   :Browse: Browse this file.
   :Preview: Preview this file.
   :Print: Print this file.
   :Install: Install this file.
   :Run As User: Run as specific user.
   :Properties: Show OS Properties for this item.
   :Find in Folder: Search for items in this folder.
   :Command Prompt Here: Open a command prompt here.

.. _bpy.ops.file.delete:

Delete :kbd:`Delete`, :kbd:`X`
   Delete the currently selected files or directories by moving them to the operating system's "trash".

   Note, on Linux deleting directories requires KDE or GNOME.

.. _bpy.ops.file.rename:

Rename :kbd:`F2`
   Change the name of the currently selected file or directory.
