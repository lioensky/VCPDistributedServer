*************
Link & Append
*************

These functions help you reuse objects, materials and other :doc:`data-blocks </files/data_blocks>`
from another blend-file.
You can build libraries of common content and share them across multiple referencing files.

.. tip::

   Instead of using the menu, you can also Link/Append blend-files by dragging and dropping them
   into the Blender window.

.. note::

   It's not possible to Link or Append data from :doc:`much newer blend-files </files/blend/compatibility>`.


.. _bpy.ops.wm.link:

Link
====

.. reference::

   :Editor:    Topbar
   :Mode:      All modes except Edit Mode
   :Menu:      :menuselection:`File --> Link...`

*Link* creates a reference to data in a source file such that changes made there will be
reflected in the current file the next time it is reloaded.
In the :doc:`File Browser </editors/file_browser>`, navigate to the external source blend-file
and select the data-blocks you want to reuse.

Linked data-blocks are indicated with a chain icon in the :doc:`Outliner </editors/outliner/introduction>`.
They're also listed in the Outliner's *Blender File* :ref:`bpy.types.SpaceOutliner.display_mode`,
along with the path of the blend-file they originate from.

Linked data-blocks are initially not editable. This even includes the location/rotation/scale
of linked objects, which are locked to the transformation they have in the source file.
There are ways around this, however:

- If you link a collection with *Instance Collections* enabled or some
  :doc:`object data </scene_layout/object/introduction>` with
  *Instance Object Data* enabled, the collection/object data will be referenced through
  an object created inside the current blend-file, which *can* be transformed.
  (This new object will be created at the :ref:`editors-3dview-3d_cursor`.)
- You can also do some level of editing/animating on linked (and thus normally locked)
  data-blocks using :doc:`Library Overrides </files/linked_libraries/library_overrides>`.

.. warning::

   Since it is not editable, linked data cannot be :ref:`protected with the Fake User option
   <data-system-datablock-fake-user>`. Adding a :doc:`custom property </files/custom_properties>` pointing to an
   otherwise unused linked data-block (e.g. a Text block) is a good way to keep it referenced across saves and
   reloads.

Options
-------

These options are available in the right-hand panel of the File Browser.

Relative Path
   Reference the external blend-file using a
   :ref:`relative path <files-blend-relative_paths>` rather than an absolute one.
Select
   Select the newly added objects.
Active Collection
   When enabled, objects and collections will be added to the active collection of the active
   :doc:`view layer </render/layers/introduction>`.
   Otherwise, they will be added to a new "Linked Data" collection in the active view layer.
Instance Collections
   When enabled, each linked collection will be added to the scene as an
   :doc:`instance collection </scene_layout/object/properties/instancing/collection>`
   (that is, a single object that represents the entire collection).
   You can add more such instances using :menuselection:`Add --> Collection Instance`,
   or replace an instance by the collection contents using :ref:`bpy.ops.object.duplicates_make_real`.

   When disabled, the collections will be added as-is so you can see their content in the
   Outliner and create Library Overrides.
Instance Object Data
   When enabled, an object will be created for each directly linked object data.
   Otherwise, no object will be created and the object data will not be visible in
   the scene until you create one yourself (e.g. by dragging the object data from the
   Outliner into the 3D Viewport).


.. _bpy.ops.wm.append:

Append
======

.. reference::

   :Editor:    Topbar
   :Mode:      All modes except Edit Mode
   :Menu:      :menuselection:`File --> Append...`

*Append* copies data-blocks into your blend-file without keeping any reference to the original ones.
You can make further edits to your local copy of the data,
but changes in the external source file will not be reflected in the current one.

In the :doc:`File Browser </editors/file_browser>`,
navigate to the external source blend-file and select the data-blocks you want to reuse.

.. note::

   Appending data you already have linked will add objects/collections to the scene,
   but will keep them linked (and uneditable).

   This is done so existing relationships with linked data remain intact.


Options
-------

These options are available in the right-hand panel of the File Browser.

Select
   Select the newly added objects.
Active Collection
   When enabled, objects and collections will be added to the active collection of the active
   :doc:`view layer </render/layers/introduction>`.
   Otherwise, they will be added to a new "Appended Data" collection in the active view layer.
Instance Collections
   When enabled, each appended collection will be added to the scene as an
   :doc:`instance collection </scene_layout/object/properties/instancing/collection>`
   (that is, a single object that represents the entire collection).
   You can add more such instances using :menuselection:`Add --> Collection Instance`,
   or replace an instance by the collection contents using :ref:`bpy.ops.object.duplicates_make_real`.

   When disabled, the collections will be added as-is so you can see their content in the
   Outliner.
Instance Object Data
   When enabled, an object will be created for each directly appended object data.
   Otherwise, no object will be created and the object data will not be visible in
   the scene until you create one yourself (e.g. by dragging the object data from the
   Outliner into the 3D Viewport).
Fake User
   Marks the appended data-blocks as :ref:`Protected <data-system-datablock-fake-user>`.
Localize All
   Also copy all indirectly linked data, instead of maintaining the links.


.. _bpy.ops.outliner.lib_operation:

Reload Library
==============

.. reference::

   :Editor:    Outliner
   :Menu:      :menuselection:`Context menu --> Reload`

When the Outliner is in the *Blender File* :ref:`bpy.types.SpaceOutliner.display_mode`,
you can right-click a linked blend-file and choose *Reload* to immediately update
the current blend-file with the latest version of the linked data-blocks,
without having to reopen the file.

Relocate Library
================

.. reference::

   :Editor:    Outliner
   :Menu:      :menuselection:`Context menu --> Relocate`

When the Outliner is in the *Blender File* :ref:`bpy.types.SpaceOutliner.display_mode`,
a right-click on a library (a linked blend-file) will show the *Relocate* option.
It allows to replace it by a different file.
This can be used to either fix a broken linked library (e.g. because the file was moved
or renamed), or to switch to a variation of the same data in a different file.


Broken Libraries
----------------

If Blender cannot find a library while loading a blend-file,
it will create placeholder data-blocks to replace missing linked ones.
That way, references to the missing data are not lost, and by relocating the missing library,
the lost data can be automatically restored.


Relocate Linked ID
==================

.. reference::

   :Editor:    Outliner
   :Menu:      :menuselection:`Context menu --> ID Data --> Relocate`

A right-click a linked ID will show the *Relocate* option in the *ID Data* sub-menu. It allows to
relocate a directly linked ID by another one, from the same library or from a different one.
This can be used to either fix a broken linked data-block (e.g. because the ID was renamed),
or to switch to a variation of the same data.

.. note::

   This operation is only available on data-blocks that are directly linked, and are not
   a dependency of any other linked data.


.. _bpy.ops.object.make_local:

Make Local
==========

.. reference::

   :Editor:    3D Viewport
   :Mode:      Object Mode
   :Menu:      :menuselection:`Object --> Relations --> Make Local...`

.. reference::

   :Editor:    Outliner
   :Menu:      :menuselection:`Context menu --> ID Data --> Make Local`

Makes the selected or all external objects local to the current blend-file.
Links to the original library file will be lost,
but the data-blocks will become fully editable, just like the ones directly
created in the current blend-file.


Options
-------

The operation available from the Outliner's context menu has no options
and only affects the selected data-blocks.

The operation available from the 3D Viewport only affects the selected objects,
but it can also make local the objects' dependencies:

Type
   Whether to localize only the objects themselves, or also their data and materials.


Known Limitations
=================

For the most part, linking data will work as expected.
However, there are some limitations to be aware of.


Circular Dependencies
---------------------

In general, dependencies should not go in both directions.
Attempting to link or append data which links back to the current file will likely result in missing links.


Scene-Level Settings
--------------------

Scene-level settings such as the :doc:`/physics/rigid_body/world` will not
be copied when linking objects. As an alternative, you can link the
entire scene and use it as a :ref:`bpy.types.Scene.background_set`.


.. _files-linked_libraries-known_limitations-compression:

Compression & Memory Use
------------------------

Referencing :ref:`compressed <files-blend-compress>` blend-files may need a lot of
memory because they have to be loaded in their entirety, even if you only link/append
a small part of them. Once the data-blocks are loaded, however, memory usage is the same.
