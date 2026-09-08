.. _bpy.types.TextStrip:

**********
Text Strip
**********

The Text strip allows you to directly display text in the Sequence editor.
The strip will display the text inserted in its text field on the final sequence.

.. figure:: /images/video-editing_sequencer_strips_text_example.png

   Text effect.

.. tip::

   All Text strips in a video sequence can be :ref:`exported <bpy.ops.sequencer.export_subtitles>`
   as a `SubRip <https://en.wikipedia.org/wiki/SubRip>`__ file.
   This is useful when using Text strips as subtitles.


Options
=======

Text
   The actual text displayed.
   Text is limited to 512 characters.

Wrap Width
   Wraps the text by the percentage of the frame width,
   setting this to zero disables word wrapping.


Style
-----

Font
   :ref:`ui-data-block` to choose which font-file is used to render the text.

   :bl-icon:`bold` (Bold)
      Use a bold font face with a strong/thick visual appearance.
   :bl-icon:`italic` (Italic)
      Use an italicized font face with a slanted visual appearance.
Size
   Size of the text.
Color
   The text color.


Outline
^^^^^^^

Creates a line enclosing the shape of the text.

Color
   The color and opacity of the outline.
Width
   The thickness of the outline.


Shadow
^^^^^^

Creates a shadow under the text.

Color
   The color and opacity of the shadow.
Angle
   Defines the position of the shadow as an angle, 0° being to the right and 90° being below.
Offset
   Amount to shift the shadow compared to the normal text.
Blur
   Amount to blur the shadow.


Box
^^^

Creates a background for the text to improve the readability and clarity of text in some situations.

Color
   The color and opacity of the box.
Margin
   The distance the box boundaries extends from the boundaries of the font glyphs.
   The distance is measured as a factor of the image's width.
Roundness
   Rounds the corners of the box, defined as a factor of box height.


Layout
------

Location X, Y
   Positions the text on the X, Y axis.
Alignment X, Y
   Controls the horizontal positioning of text within the text strip.
   The text content can be aligned to the left, center, or right.
Anchor X, Y
   Horizontal (X) or vertical (Y) "origin" of the text relative to the location.


.. _bpy.ops.sequencer.text_edit_mode_toggle:

Text Editing in Preview
=======================

Text strips can be edited directly in the **Preview** window, providing a more intuitive workflow.

- **Enable Editing**: Press :kbd:`Tab` to enter edit mode. A boundary box and cursor will appear.
- **Disable Editing**: Press :kbd:`Tab` again to exit edit mode.


Editing
-------

.. reference::

   :View Type:   Preview
   :Menu:        :menuselection:`Strip --> Text`

Copy Text :kbd:`Ctrl-C`
   Copy the selected text.
Paste Text :kbd:`Ctrl-V`
   Uses the system clipboard, allowing text from external applications to be pasted.
Cut Text :kbd:`Ctrl-X`
   Cut the selected text.
Delete Character :kbd:`Backspace`
   Delete the character before the cursor.
Insert Line Break :kbd:`Return`
   Insert a new line.
Select All :kbd:`Ctrl-A`
   Select all the text.
Deselect All :kbd:`Esc`
   Deselect the text.


Navigation
----------

- :kbd:`Left` -- Move the cursor one character left.
- :kbd:`Right` -- Move the cursor one character right.
- :kbd:`Up` -- Move the cursor one line up**.
- :kbd:`Down` -- Move the cursor one line down**.
- :kbd:`Home` -- Move the cursor to the beginning of the current line.
- :kbd:`End` -- Move the cursor to the end of the current line.
- :kbd:`Ctrl-Left` -- Move the cursor one word left.
- :kbd:`Ctrl-Right` -- Move the cursor one word right.
- :kbd:`PageUp` -- Move the cursor to the start of the text.
- :kbd:`PageDown` -- Move the cursor to the end of the text.


Text Selection
--------------

Holding :kbd:`Shift` while pressing a navigation key enables text selection.

- :kbd:`Shift-Left` -- Select the previous character.
- :kbd:`Shift-Right` -- Select the next character.
- :kbd:`Shift-Up` -- Select the previous line.
- :kbd:`Shift-Down` -- Select the next line.
- :kbd:`Shift-Home` -- Select from the cursor to the beginning of the line.
- :kbd:`Shift-End` -- Select from the cursor to the end of the line.
- :kbd:`Shift-Ctrl-Left` -- Select the previous word.
- :kbd:`Shift-Ctrl-Right` -- Select the next word.
- :kbd:`Shift-PageUp` -- Select from the cursor to the start of the text.
- :kbd:`Shift-PageDown` -- Select from the cursor to the end of the text.
