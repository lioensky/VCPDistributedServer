**************
Editing Images
**************

.. _bpy.ops.image.new:

New
===

.. reference::

   :Mode:      All Modes
   :Menu:      :menuselection:`Image --> New`
   :Shortcut:  :kbd:`Alt-N`

Create a new :ref:`image-generated` Image.


.. _bpy.ops.image.open:

Open
====

.. reference::

   :Mode:      All Modes
   :Menu:      :menuselection:`Image --> Open`
   :Shortcut:  :kbd:`Alt-O`

Opens a file browser to select an image for loading into the editor.
Images can also be opened by dragging and dropping them directly into the editor.

When opening an image, the following options are available:

Relative Path
   Sets the file path to be relative to the currently opened blend-file.

   See :ref:`files-blend-relative_paths`.
Detect Sequences
   Automatically looks for image sequences in the selected images (based on the file name).
   Disable this when you do want to get single images that are part of a sequence.
   See :ref:`image-formats-open-sequence` for more information.
Detect UDIMs
   Automatically looks for :doc:`UDIM </modeling/meshes/uv/workflows/udims>`
   tiles in the directory of the selected image; if matches are found they are loaded into Blender as UDIMs.
   This works by detecting if the filename has a ``.xxxx`` (four digit number) before the file extension.


.. _bpy.ops.image.read_viewlayers:

Open Cached Render
==================

.. reference::

   :Mode:      All Modes
   :Menu:      :menuselection:`Image --> Open Cached Render`
   :Shortcut:  :kbd:`Ctrl-R`

Find the render cache file for the current scene and load it into the
Render Result. This way, you can restore the last render from a previous
Blender session and continue working in the Compositor without having to
render the scene again.

Note that Blender doesn't create these cache files by default. You
have to enable :ref:`Cache Result <bpy.types.RenderSettings.use_render_cache>`
in the scene's Output options and then render it at least once.


.. _bpy.ops.image.replace:

Replace
=======

.. reference::

   :Mode:      All Modes
   :Menu:      :menuselection:`Image --> Replace`

Replace the current image by another.


.. _bpy.ops.image.reload:

Reload
======

.. reference::

   :Mode:      All Modes
   :Menu:      :menuselection:`Image --> Reload`
   :Shortcut:  :kbd:`Alt-R`

Reload the image from the file on drive.


.. _bpy.ops.image.external_edit:

Edit Externally
===============

.. reference::

   :Mode:      All Modes
   :Menu:      :menuselection:`Image --> Edit Externally`

Open the image in the *Image Editor* program specified in the
:doc:`File Paths Preferences </editors/preferences/file_paths>`.


.. _bpy.ops.image.clipboard:

Copy/Paste
==========

.. reference::

   :Mode:      All Modes
   :Menu:      :menuselection:`Image --> Copy/Paste`

Allows copying and pasting images between Blender and the operating system's clipboard.

Note, only PNG files are supported for direct clipboard copying and pasting.

Platform specific behavior:

- Windows: Supports pasting images by copying the image's file path. This method allows all supported image formats.
- Linux: Requires Wayland for clipboard image support.


.. _bpy.ops.image.save:

Save
====

.. reference::

   :Mode:      All Modes
   :Menu:      :menuselection:`Image --> Save`
   :Shortcut:  :kbd:`Alt-S`

Save the image to its current path.

.. important::

   While animation renders are automatically saved, still renders are not.
   These have to be saved manually.


.. _bpy.ops.image.save_as:

Save As
=======

.. reference::

   :Mode:      All Modes
   :Menu:      :menuselection:`Image --> Save As`
   :Shortcut:  :kbd:`Shift-Alt-S`

Save the image to a separate file of any type.
The image output settings can be configured and are the same as the
:doc:`Render Output Properties </render/output/properties/output>`.


Save a Copy
===========

.. reference::

   :Mode:      All Modes
   :Menu:      :menuselection:`Image --> Save a Copy`

Save the file under a specified name,
but keep the old one open in the Image editor.


.. _bpy.ops.image.save_all_modified:

Save All Images
===============

.. reference::

   :Mode:      All Modes
   :Menu:      :menuselection:`Image --> Save All Images`

Save all modified images. Packed images will be repacked.


.. _bpy.ops.image.invert:

Invert
======

.. reference::

   :Mode:      All Modes
   :Menu:      :menuselection:`Image --> Invert`

Invert Image Colors
   Invert the colors of an image.
Invert Red/Green/Blue/Alpha Channel
   Invert a single color channel.


.. _bpy.ops.image.resize:

Resize
======

.. reference::

   :Mode:      All Modes
   :Menu:      :menuselection:`Image --> Resize`

Adjusts the image dimensions by scaling its pixel resolution. This is useful for various tasks, such as:

- Reducing texture resolution to optimize performance and memory usage.
- Increasing image resolution for more detailed painting or editing.

Size X, Y
   Defines the new width and height of the image in pixels.

All UDIM Tiles
   Applies the resizing operation to all UDIM tiles in the image.


Transform
=========

.. _bpy.ops.image.flip:

Flip Horizontally
   Mirrors the image so the left side becomes the right side.
Flip Vertically
   Mirrors the image so the top becomes the bottom.

.. _bpy.ops.image.rotate_orthogonal:

Rotate 90° Clockwise
   Rotates the image clockwise 90°.
Rotate 90° Counter-Clockwise
   Rotates the image counter-clockwise 90°.
Rotate 180°
   Rotates the image 180°.


.. _bpy.ops.image.pack:

Pack
====

.. reference::

   :Mode:      All Modes
   :Menu:      :menuselection:`Image --> Pack`

Pack the image into the blend-file.
See :ref:`pack-unpack-data`.


.. _bpy.ops.image.unpack:

Unpack
======

.. reference::

   :Mode:      All Modes
   :Menu:      :menuselection:`Image --> Unpack`

Unpack the image to a drive.


.. _bpy.ops.palette.extract_from_image:

Extract Palette
===============

.. reference::

   :Mode:      All Modes
   :Menu:      :menuselection:`Image --> Extract Palette`

Extract a :ref:`Color Palette <bpy.types.PaletteColor>` from the image for use by painting tools.
