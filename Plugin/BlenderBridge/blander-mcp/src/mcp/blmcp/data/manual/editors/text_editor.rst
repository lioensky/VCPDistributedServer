.. index:: Editors; Text Editor

.. _bpy.types.SpaceTextEditor:
.. _bpy.types.Text:
.. _bpy.ops.text:

***********
Text Editor
***********

This editor can be used to write Python scripts, scripting based shaders such as OSL and GLSL,
or just plain text notes. To open it, you can switch to the *Scripting*
:doc:`workspace </interface/window_system/workspaces>` or press
:kbd:`Shift-F11` to replace the current editor.


Header
======

The newly opened Text editor is empty, with a very simple header.
More options become available when a text file is created or opened.

.. _fig-text-header-plain:

.. figure:: /images/editors_text-editor_header.png

   Text header.

.. _fig-text-header-full:

.. figure:: /images/editors_text-editor_header-loaded.png

   Text header with a text loaded.

Editor Type
   The standard editor selection button.
Menus
   Editor's menus.

.. _bpy.ops.text.resolve_conflict:

Resolve Conflict
   Resolves modified file conflicts when an external text file is updated from another program.

   Reload from Disk
      Opens the file from drive again, overriding any local changes.
   Make Text Internal
      Converts the external text data-block into an internal one.
   Ignore
      Hides the warning message until the external text file is modified externally again.

Text
   A :ref:`data-block menu <ui-data-block>` to select a text or to create a new one.
   After that the header will change.

.. _editors-text-run-script:

Run Script (play icon)
   Executes the text as a Python script :kbd:`Alt-P`. See `Template Menu`_.
Show
   Toggles for line numbers, word wrapping, and syntax highlighting.
Script Node Update (refresh icon)
   When an `OSL-file <https://github.com/AcademySoftwareFoundation/OpenShadingLanguage>`__
   is opened, this updates the :ref:`Shader Script <bpy.types.ShaderNodeScript>` node
   with new options and sockets from the script.


View Menu
---------

Sidebar :kbd:`Ctrl-T`
   Show or hide the :ref:`Sidebar <ui-region-sidebar>`.

-----

Line Numbers
   Displays the text file's line numbers on the left of the `Main View`_.
Word Wrap
   Wraps words that don't fit into the horizontal space by pushing them to a new "pseudo line".
Syntax Highlight
   Colors special words, in the `Main View`_, that are used in the Python programming language.
Highlight Line
   Emphasizes the active line by altering the color of the background.

-----

Zoom In/Out
   Increase/decrease the font size of text in the main view.

-----

Navigation
   Top :kbd:`Ctrl-Home`
      Moves the view and cursor to the start of the text file.
   Bottom :kbd:`Ctrl-End`
      Moves the view and cursor to the end of the text file.
   Line Begin :kbd:`Home`
      Moves the cursor to the start of the current line.
   Line End :kbd:`End`
      Moves the cursor to the end of the current line.
   Previous Line :kbd:`Up`
      Moves the cursor to the same position in the line above the current line.
   Next Line :kbd:`Down`
      Moves the cursor to the same position in the line below the current line.
   Previous Word :kbd:`Ctrl-Left`
      Moves the cursor to the beginning of the previous word.
      If the cursor is in the middle of a word, the cursor is moved to the beginning of the current word.
   Next Word :kbd:`Ctrl-Right`
      Moves the cursor to the end of the next word.
      If the cursor is in the middle of a word, the cursor is moved to the end of the current word.


Text Menu
---------

.. _bpy.ops.text.new:

New :kbd:`Alt-N`
   Creates a new text Data Block.

.. _bpy.ops.text.open:

Open :kbd:`Alt-O`.
   Loads an external text file that is selected via the :doc:`File Browser </editors/file_browser>`.

.. _bpy.ops.text.reload:

Reload :kbd:`Alt-R`
   Reopens (reloads) the current buffer (all non-saved modifications are lost).

.. _bpy.ops.text.jump_to_file_at_point:

Edit Externally
   Edit text file in external text editor.
   The external editor can be configured in the :ref:`User Preferences <prefs-file_paths-text_editor>`.

.. _bpy.ops.text.save:

Save :kbd:`Alt-S`
   Saves an already open file.

.. _bpy.ops.text.save_as:

Save As :kbd:`Shift-Ctrl-Alt-S`.
   Saves text as a new text file.
   A :doc:`File Browser </editors/file_browser>` is opened to select the directory
   to save the file along with giving the file a name and extension.

.. _bpy.types.Text.use_module:

Register
   Runs the text data-block as a Python script on loading the blend-file.
   Read more about the registration of Python modules in
   `API documentation <https://docs.blender.org/api/current/info_overview.html#registration>`__.

.. _bpy.types.SpaceTextEditor.use_live_edit:

Live Edit
   Runs the Python script each time you make a change.

.. _bpy.ops.text.run_script:

Run Script :kbd:`Alt-P`
   Executes the text as a Python script. See `Running Scripts`_ for more information.


Edit Menu
---------

Undo/Redo
   See :doc:`/interface/undo_redo`.
Cut :kbd:`Ctrl-X`
   Cuts out the marked text into the clipboard.
Copy :kbd:`Ctrl-C`
   Copies the marked text into the clipboard.
Paste :kbd:`Ctrl-V`
   Pastes the text from the clipboard at the cursor location in the Text editor.
Duplicate Line :kbd:`Ctrl-D`
   Duplicates the current line.
Move Line(s) Up :kbd:`Shift-Ctrl-Up`
   Swaps the current/selected line(s) with the above.
Move Line(s) Down :kbd:`Shift-Ctrl-Down`
   Swaps the current/selected line(s) with the below.
Find & Replace :kbd:`Ctrl-F`
   Shows the *Find & Replace* panel in the Sidebar.
Find & Set Selection :kbd:`Ctrl-G`
   Finds the next instance of the selected text.
Jump To :kbd:`Ctrl-J`
   Shows a pop-up, which lets you select a line number where to move the cursor to.
Text Auto Complete :kbd:`Tab`
   Shows a selectable list of words already used in the text.
Text to 3D Object
   Converts the text file to a :doc:`Text Object </modeling/texts/index>`
   either as *One Object* or *One Object Per Line*.


Select Menu
-----------

All :kbd:`Ctrl-A`
   Selects the entire text file.
Line :kbd:`Shift-Ctrl-A`
   Selects the entire current line.
Word double-click :kbd:`LMB`
   Selects the entire current word.
Top :kbd:`Shift-Ctrl-Home`
   Selects everything above the cursor.
Bottom :kbd:`Shift-Ctrl-End`
   Selects everything below the cursor.
Line Begin :kbd:`Shift-Home`
   Selects everything between the beginning of the current line and the cursor.
Line End :kbd:`Shift-End`
   Selects everything between the cursor and the end of the current line.
Previous Line :kbd:`Shift-Up`
   Selects everything between the cursor and the position of the cursor one line above.
Next Line :kbd:`Shift-Down`
   Selects everything between the cursor and the position of the cursor one line below.
Previous Word :kbd:`Shift-Ctrl-Left`
   Selects everything between the cursor and the beginning of the previous word.
   If the cursor is in the middle of a word, select everything to the beginning of the current word.
Next Word :kbd:`Shift-Ctrl-Right`
   Selects everything between the cursor and the end of the next word.
   If the cursor is in the middle of a word, select everything to the end of the current word.


Format Menu
-----------

Indent :kbd:`Tab`
   Inserts a tab character at the cursor.
Unindent :kbd:`Shift-Tab`.
   Unindents the selection.
Toggle Comments :kbd:`Ctrl-Slash`.
   Toggles whether the selected line(s) are a Python comment.
   If no lines are selected, the current line is toggled.
Convert Whitespace
   Converts indentation characters *To Spaces* or *To Tabs*.


Template Menu
-------------

Contains a number of templates for both Python and Open Shading Language scripts.


Main View
=========

Typing on the keyboard produces text in the text buffer.

As usual, pressing, dragging and releasing :kbd:`LMB` selects text.
Pressing :kbd:`RMB` opens the context menu.

.. tip::

   The Text editor is also handy when you want to share your blend-file with others:
   you can leave a note that explains how the file is structured.
   Be sure to keep the editor visible when saving so they'll see it!


Sidebar
=======

Find & Replace
--------------

.. _bpy.types.SpaceTextEditor.find_text:
.. _bpy.ops.text.find:

Find Text :kbd:`Ctrl-F`
   Searches for instances of a text that occur after the cursor.
   Using the eyedropper icon will search for the currently selected text
   and sets the selection to the match.
   *Find Next* searches for the next instance of the text.

.. _bpy.types.SpaceTextEditor.replace_text:
.. _bpy.ops.text.replace:

Replace Text :kbd:`Ctrl-H`
   Searches for the text specified in *Find Text* and replaces it with the new text.
   Using the eyedropper icon will set the currently selected text as the replace text.
   *Replace* searches for the next match and replaces it.
   *Replace All* searches for the match and replaces all occurrences of the match with the new text.

.. _bpy.types.SpaceTextEditor.use_match_case:
.. _bpy.types.SpaceTextEditor.use_find_wrap:
.. _bpy.types.SpaceTextEditor.use_find_all:

Case
   Search is sensitive to uppercase and lowercase letters.
Wrap
   Search again from the start of the file when reaching the end.
All
   Search in all text data-blocks instead of only the active one.


Properties
----------

.. _bpy.types.SpaceTextEditor.show_margin:
.. _bpy.types.SpaceTextEditor.margin_column:

Margin
   Shows a vertical margin line to help keep text lines at a reasonable length.
   The position of this margin line is specified by *Margin Column*.

.. _bpy.types.SpaceTextEditor.font_size:

Font Size :kbd:`Ctrl-WheelUp`
   The size of the font used to display text.

.. _bpy.types.SpaceTextEditor.tab_width:

Tab Width
   The number of character spaces to display tab characters with.

.. _bpy.types.Text.indentation:

Indentation
   Whether to use *Tabs* or *Spaces* for indentation.


Footer
======

The Text editor footer displays whether the text is saved internally or externally and
if there are unsaved changes to an external file.
For external files, this region also displays the file path to the text file.


Usage
=====

Running Scripts
---------------

The most notable keystroke is :kbd:`Alt-P` which executes the current text as a Python script.
You can access not just the standard Python modules, but also a whole bunch of Blender-specific ones;
see :doc:`/advanced/scripting/index`.
