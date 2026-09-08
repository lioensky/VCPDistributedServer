.. index:: Editors; Python Console
.. _bpy.types.ConsoleLine:
.. _bpy.types.SpaceConsole:
.. _bpy.ops.console:

**************
Python Console
**************

The Python Console offers a quick way to test code snippets and explore Blender's API.
It executes whatever you type on its ``>>>`` prompt and has command history and auto-complete.

.. figure:: /images/editors_python-console_default.png

   Python Console.


Interface
=========

Header Menus
------------

View Menu
^^^^^^^^^

Zoom In / Zoom Out
   Increases/decreases the font size.
Move to Previous Word :kbd:`Ctrl-Left`
   Moves the cursor to the beginning of the previous word.
   If the cursor is in the middle of a word, the cursor is moved to the beginning of the current word.
Move to Next Word :kbd:`Ctrl-Right`
   Moves the cursor to the end of the next word.
   If the cursor is in the middle of a word, the cursor is moved to the end of the current word.
Move to Line Begin :kbd:`Home`
   Moves the cursor to the start of the current line.

   :kbd:`Shift-Home`: Selects all text between the cursor and the start of the current line.
Move to Line End :kbd:`End`
   Moves the cursor to the end of the current line.

   :kbd:`Shift-End`: Selects all text between the cursor and the end of the current line.


Console Menu
^^^^^^^^^^^^

Clear All
   Refreshes the console, giving the view a fresh start.
   Note that command history is not cleared.
Clear Line :kbd:`Shift-Return`.
   Removes everything from the prompt line.
Delete Previous Word :kbd:`Ctrl-Backspace`
   Deletes everything between the cursor and the beginning of the previous word (separated by periods).
   If the cursor is in the middle of a word, deletes everything to the beginning of the current word.
Delete Next Word :kbd:`Ctrl-Delete`
   Deletes everything between the cursor and the end of the next word.
   If the cursor is in the middle of a word, deletes everything to the end of the current word.
Copy as Script :kbd:`Shift-Ctrl-C`
   Copies the full history buffer to the clipboard.
   This can be pasted into a text file to be used as a Python script.
Cut :kbd:`Ctrl-X`
   Copies the selected text into the clipboard and deletes it.
Copy :kbd:`Ctrl-C`
   Copies the selected text into the clipboard.
Paste :kbd:`Ctrl-V`
   Pastes into the command line.
Indent :kbd:`Tab`
   Inserts a tab character at the cursor.
Unindent :kbd:`Shift-Tab`
   Unindents the selection.
Backward in History :kbd:`Up`
   Changes the current command to the previous one from the command history.
Forward in History :kbd:`Down`
   Changes the current command to the next one from the command history.
Autocomplete :kbd:`Tab`
   See `Auto Completion`_.


Main View
---------

.. rubric:: Key Bindings

- :kbd:`LMB` -- Moves the cursor along the input line.
- :kbd:`Left` / :kbd:`Right` -- Moves the cursor by one character.
- :kbd:`Ctrl-Left` / :kbd:`Ctrl-Right` -- Moves the cursor by one word.
- :kbd:`Shift-Left` / :kbd:`Shift-Right` -- Selects characters to the left/right.
- :kbd:`Shift-Ctrl-Left` / :kbd:`Shift-Ctrl-Right` -- Selects words to the left/right.
- :kbd:`Ctrl-A` Selects all text and text history.

- :kbd:`Backspace` / :kbd:`Delete` -- Erase characters.
- :kbd:`Ctrl-Backspace` / :kbd:`Ctrl-Delete` -- Erase words.

- :kbd:`Return` -- Execute command.
- :kbd:`Shift-Return` -- Add to command history without executing.


Usage
=====

Aliases
-------

Some variables and modules are available for convenience:

- ``C``: Quick access to ``bpy.context``.
- ``D``: Quick access to ``bpy.data``.
- ``bpy``: Top level Blender Python API module.


First Look at the Console Environment
-------------------------------------

To see the list of global functions and variables,
type ``dir()`` and press :kbd:`Return` to execute it.

.. figure:: /images/editors_python-console_dir.png


.. _bpy.ops.console.autocomplete:

Auto Completion
---------------

The Console can preview the available members of a module or variable.
As an example, type ``bpy.`` and press :kbd:`Tab`:

.. figure:: /images/editors_python-console_completion.png

The submodules are listed in green. Attributes and methods will be listed
in the same way, with methods being indicated by a trailing ``(``.


Examples
========

bpy.context
-----------

This module gives you access to the current scene,
the currently selected objects, the current object mode, and so on.

.. note::

   For the commands below to show the proper output,
   make sure you have selected object(s) in the 3D Viewport.

.. figure:: /images/editors_python-console_bpy-context.png

Get the current 3D Viewport mode (Object, Edit, Sculpt, etc.)::

   bpy.context.mode

Get the active object::

   bpy.context.object
   bpy.context.active_object

Change the active object's X coordinate to 1::

   bpy.context.object.location.x = 1

Move the active object by 0.5 along the X axis::

   bpy.context.object.location.x += 0.5

Change all three location coordinates in one go::

   bpy.context.object.location = (1, 2, 3)

Change only the X and Y coordinates::

   bpy.context.object.location.xy = (1, 2)

Get the selected objects::

   bpy.context.selected_objects

Get the selected objects excluding the active one::

   [obj for obj in bpy.context.selected_objects if obj != bpy.context.object]


bpy.data
--------

Gives you access to all the data in the blend-file,
regardless of whether it's currently active or selected.

.. figure:: /images/editors_python-console_bpy-data.png


bpy.ops
-------

"Operators" are actions that are normally triggered from a button or menu item
but can also be called programmatically. See the
`bpy.ops <https://docs.blender.org/api/current/bpy.ops.html>`__
API documentation for a list of all operators.
