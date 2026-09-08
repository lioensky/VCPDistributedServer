.. _pack-unpack-data:

***********
Packed Data
***********

Blender has the ability to encapsulate (incorporate)
various kinds of data within the blend-file that is normally saved outside of the blend-file.
For example, an image texture that is an external image file can be put "inside" the blend-file.
This allows sharing a full project as a single file,
instead of e.g. an archive containing the blend-file and all its dependencies.

You know that a data is packed when you see a little "gift box" icon displayed next to its path.

.. warning:: Not all external files can be packed

   Some typically heavy external files, like videos from the :doc:`Sequence Editor </video_editing/introduction>`
   or :doc:`Movie Clips </editors/clip/introduction>`, cannot be packed in a blend-file.


Pack Data
=========

.. _bpy.ops.file.pack_all:

Pack Resources
--------------

.. reference::

   :Panel:     :menuselection:`File --> External Data --> Pack Resources`

Mark all eligible external resource files used by the blend-file as packed.
Actual packing will happen on the next save of the blend-file.


.. _bpy.ops.file.autopack_toggle:

Automatically Pack Resources
----------------------------

.. reference::

   :Panel:     :menuselection:`File --> External Data --> Automatically Pack Resources`

When enabled, this option will ensure that all eligible external resource files, existing or added later,
are systematically marked as packed.
As with *Pack Resources*, the blend-file must be saved to the drive for this to have an effect.

Disabling that option won't unpack anything, but future external files
won't be automatically marked as packed anymore.


Selective Packing
-----------------

A single file can be packed by clicking on the little "gift box" icon to the left of its file-path UI widget.


Unpack Data
===========

.. _bpy.ops.file.unpack_all:

Unpack Resources
----------------

.. reference::

   :Panel:     :menuselection:`File --> External Data --> Unpack Resources`

Unpack all external resource files stored into a blend-file.


Options
^^^^^^^

Use files in current directory (create when necessary)
   Unpacks all files in the same directory ``//`` as the blend-file,
   grouping them in proper folders (like ''textures'' for instance).
   However, if the final file exists already, it will use that file, instead of unpacking it.
Write files to current directory (overwrite existing files)
   As with previous option, but if the final file exists already, it will overwrite it.
Use files in original location (create when necessary)
   Unpacks all files in their original location.
   However, if the final file exists already, it will use that file, instead of unpacking it.
Write files to original location (overwrite existing files)
   As with previous option, but if the final file exists already, it will overwrite it.
Disable AutoPack, keep all packed files
   Only deactivates the *Automatically Pack Resources* option.


Selective Unpacking
-------------------

A single file can be unpacked by clicking on the little "gift box" icon to the left of its file-path UI widget.


Options
^^^^^^^

Remove Pack
   Just mark the file as unpacked, without actually writing it or reloading it from the drive.
Create <local file path>
   Unpack the file at the proposed path, which is local to the current blend-file.
Use <original file path> (differs)|(identical)
   If the original file path still exists, mark it as unpacked.
   Note that it won't be automatically reloaded from the drive.
   *(differs)* or *(identical)* show difference status between the packed version
   and the one on-drive.
Overwrite <original file path>
   If the original file path still exists but differs from the packed version,
   mark it as unpacked and overwrite the on-drive file with the packed version.
Create <original file path>
   If the original file path does not exist, mark it as unpacked and write it to drive.


.. _bpy.ops.file.pack_libraries:

Pack Linked Libraries
=====================

.. reference::

   :Panel:     :menuselection:`File --> External Data --> Pack Linked Libraries`

Mark all linked library files in the current blend-file as packed.
Actual packing will happen on the next save of the blend-file.


.. _bpy.ops.file.unpack_libraries:

Unpack Linked Libraries
=======================

.. reference::

   :Panel:     :menuselection:`File --> External Data --> Unpack Linked Libraries`

Unpack all used linked library files from this blend-file.
