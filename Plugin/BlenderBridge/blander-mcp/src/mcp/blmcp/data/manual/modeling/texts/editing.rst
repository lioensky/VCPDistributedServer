.. |atilde| unicode:: U+000E3
.. |aacute| unicode:: U+000E1
.. |agrave| unicode:: U+000E0
.. |acircumflex| unicode:: U+000E2
.. |aring|  unicode:: U+000E5
.. |ash|  unicode:: U+000E6
.. |aordinal|  unicode:: U+000AA
.. |euml|   unicode:: U+000EB
.. |oslash| unicode:: U+000F8
.. |ccedilla| unicode:: U+000E7
.. |cent| unicode:: U+000A2
.. |dagger| unicode:: U+02020
.. |doubledagger| unicode:: U+02021
.. |section| unicode:: U+000A7
.. |copyright| unicode:: U+000A9
.. |registered| unicode:: U+000AE
.. |trademark| unicode:: U+02122
.. |half| unicode:: U+000BD
.. |division| unicode:: U+000F7
.. |plusminus| unicode:: U+000B1

********************
Editing Text Objects
********************

Editing text is quite different from other object types in Blender, and happens mainly in two areas.
First, the 3D Viewport, where you type your text, and have a few shortcuts, e.g. for applying
styles (see :ref:`modeling-text-character`) -- note however, that most Blender shortcuts you know
in Edit Mode do not exist for texts. The second place is the Properties, especially the *Font* tab.

Editing text objects is similar to using a standard text editor but is not as
full-featured and has some differences.
The menu of the 3D Viewport header offers few options. You have no transform nor mirror tools, and so on.
To leave Edit Mode use :kbd:`Tab` as it does not insert a tab character in the text,
but rather enters and exits Edit Mode, as with other object types.


.. _bpy.ops.font.text_cut:

Cut
===

.. reference::

   :Editor:    3D Viewport
   :Mode:      Edit Mode
   :Menu:      :menuselection:`Header --> Text --> Cut`
   :Shortcut:  :kbd:`Ctrl-X`

To cut and copy text to the buffer, use the shortcut or the matching entry in the *Edit* menu.


.. _bpy.ops.font.text_copy:

Copy
====

.. reference::

   :Editor:    3D Viewport
   :Mode:      Edit Mode
   :Menu:      :menuselection:`Header --> Text --> Copy`
   :Shortcut:  :kbd:`Ctrl-C`

To copy text to the buffer, use the shortcut or the matching entry in the *Edit* menu.


.. _bpy.ops.font.text_paste:

Paste
=====

.. reference::

   :Editor:    3D Viewport
   :Mode:      Edit Mode
   :Menu:      :menuselection:`Header --> Text --> Paste`
   :Shortcut:  :kbd:`Ctrl-V`

To paste text from the buffer, use the shortcut or the matching entry in the *Edit* menu.


.. _bpy.ops.font.text_paste_from_file:

Paste File
==========

.. reference::

   :Editor:    3D Viewport
   :Mode:      Edit Mode
   :Menu:      :menuselection:`Header --> Text --> Paste File`

Inserts text from and external text file.
This will bring up a :doc:`File Browser </editors/file_browser>` for navigating to a valid UTF-8 file.
As usual, be careful that the file does not have too many characters,
as interactive response will slow down.


.. _bpy.ops.font.case_set:

To Uppercase
============

.. reference::

   :Editor:    3D Viewport
   :Mode:      Edit Mode
   :Menu:      :menuselection:`Header --> Text --> To Uppercase`

Changes the case of the selected text to uppercase.


To Lowercase
============

.. reference::

   :Editor:    3D Viewport
   :Mode:      Edit Mode
   :Menu:      :menuselection:`Header --> Text --> To Lowercase`

Changes the case of the selected text to lowercase.


.. _bpy.ops.font.text_insert_unicode:

Insert Unicode
==============

.. reference::

   :Editor:    3D Viewport
   :Mode:      Edit Mode
   :Menu:      :menuselection:`Header --> Text --> Insert Unicode`

Opens a dialog box to input the entry of any Unicode character by entering its hexadecimal code point value.

See Wikipedia for a `List of Unicode characters <https://en.wikipedia.org/wiki/List_of_Unicode_characters>`__
which list there respective hexadecimal code point values.


.. _bpy.ops.font.text_insert:

Special Characters
==================

.. reference::

   :Editor:    3D Viewport
   :Mode:      Edit Mode
   :Menu:      :menuselection:`Header --> Text --> Special Characters`

This is a limited character map to insert characters which aren't available from the keyboard.
Many other special characters can be "composed", see `Accent Characters`_.
If you need others, you will have to copy-paste them from an external editor or character map program.

.. note::

   The text buffer is in sync with the desktop clipboard.
   But if it is used within Blender the text formatting will be copied as well.
   For other ways of inserting a text, see `Inserting Text`_.


.. _bpy.ops.font.style_toggle:

Toggle Bold, Italics, Underline, Small Caps
===========================================

.. reference::

   :Editor:    3D Viewport
   :Mode:      Edit Mode
   :Menu:      :menuselection:`Header --> Text --> Toggle Bold/Italics/Underline/Small Caps`

To apply the *Bold*, *Italics*, *Underline* or *Small Caps* attribute to a set of characters,
you either turn on the related setting prior to typing characters,
or select existing text, and then toggle desired style from the menu.

.. warning::

   Blender's *Bold* and *Italic* buttons do not work the same way as in other applications,
   as they also serve as placeholders for you to load up other fonts manually.


.. _bpy.ops.font.change_spacing:

Kerning
=======

.. reference::

   :Editor:    3D Viewport
   :Mode:      Edit Mode
   :Menu:      :menuselection:`Header --> Text --> Kerning`

Font kerning is the space between individual characters.

Decrease Kerning :kbd:`Alt-Left`
   Decreases the spacing between the characters on either side of the cursor.
Increase Kerning :kbd:`Alt-Right`
   Increase the spacing between the characters on either side of the cursor.
Reset Kerning
   Sets the spacing between the characters on either side of the cursor to their initial value.


.. _bpy.ops.font.delete:

Delete
======

.. reference::

   :Editor:    3D Viewport
   :Mode:      Edit Mode
   :Menu:      :menuselection:`Header --> Text --> Delete`

Previous/Next Character
   Deletes the character before or after the cursor.
Previous/Next Word
   Deletes the word before or after the cursor.


Inserting Text
==============

You can insert text in two ways: from the internal text buffer or from a text file.

Using an existing text data-block, you can convert it to an object from the Text editor's header,
select :menuselection:`Edit --> Text to 3D Object`,
*One Object* or *One Object per Line* depending on your needs.

It is also possible to paste from the clipboard or a file, while editing 3D text.


Accent Characters
-----------------

Many special characters (such as accented chars, which are not directly available on your keyboard)
can be "composed" using a combination of two other characters. To do so,
type the main char, press :kbd:`Alt-Backspace`,
and then press the desired "modifier" to produce the special character.
Some examples are given below:

.. hlist::
   :columns: 2

   - |atilde|: ``A``, :kbd:`Alt-Backspace`, ``~``
   - |aacute|: ``A``, :kbd:`Alt-Backspace`, ``'``
   - |agrave|: ``A``, :kbd:`Alt-Backspace`, ``\``
   - |acircumflex|: ``A``, :kbd:`Alt-Backspace`, ``^``
   - |aring|: ``A``, :kbd:`Alt-Backspace`, ``O``
   - |ash|: ``A``, :kbd:`Alt-Backspace`, ``E``
   - |aordinal|: ``A``, :kbd:`Alt-Backspace`, ``-``
   - |euml|: ``E``, :kbd:`Alt-Backspace`, ``"``
   - |ccedilla|: ``C``, :kbd:`Alt-Backspace`, ``,``
   - |cent|: ``C``, :kbd:`Alt-Backspace`, ``|``
   - |oslash|: ``O``, :kbd:`Alt-Backspace`, ``/``

   - |section|: ``S``, :kbd:`Alt-Backspace`, ``S``
   - |dagger|: ``|``, :kbd:`Alt-Backspace`, ``-``
   - |doubledagger|: ``|``, :kbd:`Alt-Backspace`, ``=``
   - |copyright|: ``O``, :kbd:`Alt-Backspace`, ``C``
   - |registered|: ``O``, :kbd:`Alt-Backspace`, ``R``
   - |trademark|: ``T``, :kbd:`Alt-Backspace`, ``M``

   - |half|: ``1``, :kbd:`Alt-Backspace`, ``2``
   - |division|: ``-``, :kbd:`Alt-Backspace`, ``:``
   - |plusminus|: ``-``, :kbd:`Alt-Backspace`, ``+``


Converting to a Mesh or Curve
=============================

In Object Mode, it is possible to convert a text object to a mesh or curve one, see :ref:`object-convert-to`.

.. tip::

   The topology of the result is usually a bit messy,
   so it may be useful to use a *Limited Dissolve* deletion,
   or apply a :doc:`Remesh modifier </modeling/modifiers/generate/remesh>`
   at a low threshold, to clean up your mesh.


Assigning Materials
===================

.. reference::

   :Mode:      Edit
   :Panel:     :menuselection:`Properties --> Materials`

Each character can have a different *Material index* in order to have different materials
on different characters.

You can assign indices either as you type, or after by selecting blocks of text and
clicking on the *Assign* button in the *Materials* panel.

.. figure:: /images/modeling_texts_editing_material-index-example.png

   Red Green Blue text example.
