
*********************
Editing Outliner Data
*********************

.. _editors-outliner-editing-context_menu:

Context Menu
============

Show the context menu for a data-block with :kbd:`RMB` on the icon or name.
Depending on the type of the selected data-block(s), you will have all or part of the following options:

Copy/Paste
   Copies/pastes the selected data-blocks.

.. _bpy.ops.outliner.delete:

Delete :kbd:`X`, :kbd:`Delete`
   Removes all usages of the selected data-blocks. Objects are removed from all scenes,
   materials are removed from all meshes, and so on.

.. note::
   Pressing these shortcuts while hovering over the 3D Viewport will instead *Unlink* the selected objects,
   removing them only from the current scene.

Delete Hierarchy
   As above, but also affects child collections/objects. Note that if you run this on a collection,
   child objects that (also) belong to another collection will not be deleted.

Select
   Adds the items that are selected in the Outliner to the selection in the 3D Viewport. This is only
   useful when :ref:`Sync Selection <bpy.types.SpaceOutliner.use_sync_select>` is disabled,
   as when it's enabled (which is the default), the Outliner selection is synchronized to the
   3D Viewport automatically.

Select Hierarchy
   Adds the children of the selected items to the selection in the Outliner. If *Sync Selection* is enabled,
   this also adds them to the selection in the 3D Viewport.

Deselect
   Removes the items that are selected in the Outliner from the selection in the 3D Viewport.

Unlink
   Removes the current usage of the data-block while keeping any others. Objects are only removed
   from the current scene, materials are only removed from the current mesh, and so on.

.. _editors-outliner-editing-collections:

Collections
-----------

:doc:`Collections </scene_layout/collections/index>` let you organize the content of a scene.
They can contain objects as well as other collections.

.. _bpy.ops.outliner.collection_new:

New
   Creates a new collection.

.. _bpy.ops.outliner.collection_duplicate:

Duplicate Collections
   Recursively duplicates the collection including all child collections, objects, and object data.

.. _bpy.ops.outliner.collection_duplicate_linked:

Duplicate Linked
   Recursively duplicates the collection including child collections and objects,
   but reuses object data.

.. _bpy.ops.outliner.collection_instance:

Instance to Scene
   Creates a new :doc:`collection instance </scene_layout/object/properties/instancing/collection>`.

Visibility
^^^^^^^^^^

Controls the collection's visibility in the 3D Viewport and the final render.

.. _bpy.ops.outliner.collection_isolate:

Isolate
   Shows the selected collection (as well as its child and parent collections)
   and hides all the others.

.. _bpy.ops.outliner.collection_show:
.. _bpy.ops.outliner.collection_hide:

Show/Hide
   Changes the :ref:`Hide in Viewports <bpy.types.LayerCollection.hide_viewport>` setting
   for the selected collections.

.. _bpy.ops.outliner.collection_show_inside:
.. _bpy.ops.outliner.collection_hide_inside:

Show/Hide Inside
   Changes the :ref:`Hide in Viewports <bpy.types.LayerCollection.hide_viewport>` setting
   for the selected collections and all their children.

.. _bpy.ops.outliner.collection_enable:
.. _bpy.ops.outliner.collection_disable:

Enable/Disable in Viewports
   Changes the :ref:`Disable in Viewports <bpy.types.Collection.hide_viewport>` setting
   for the selected collections.

.. _bpy.ops.outliner.collection_enable_render:
.. _bpy.ops.outliner.collection_disable_render:

Enable/Disable in Renders
   Changes the :ref:`Disable in Renders <bpy.types.Collection.hide_render>` setting
   for the selected collections.


View Layer
^^^^^^^^^^

Controls the collection's interactions with the :doc:`View Layer </render/layers/introduction>`.

.. figure:: /images/render_layers_introduction_viewlayer-collection.png

   Collection/View layer settings.

.. _bpy.ops.outliner.collection_exclude_clear:

Disable from View Layer
   Remove this collection from the active view layer.
   Objects that are only in this collection will not be rendered for the active view layer.
   This is useful to sometimes leave out some object influence for a particular view layer.

.. _bpy.ops.outliner.collection_exclude_set:

Enable in View Layer
   Add this collection to the active view layer.
   Objects inside the collection will be rendered with the active view layer.

.. _bpy.ops.outliner.collection_holdout_set:

Set Holdout
   Enables the :ref:`Holdout <bpy.types.LayerCollection.holdout>` property for the selected collections.
   Objects inside this collection will generate a holdout/mask in the active view layer.

.. _bpy.ops.outliner.collection_holdout_clear:

Clear Holdout
   Disables the *Holdout* property for the selected collections.

.. _bpy.ops.outliner.collection_indirect_only_set:

Set Indirect Only :guilabel:`Cycles Only`
   Enables the :ref:`Indirect Only <bpy.types.LayerCollection.indirect_only>` property for the selected collections.
   Objects inside this collection will only contribute to the final image indirectly through shadows and reflections.

.. _bpy.ops.outliner.collection_indirect_only_clear:

Clear Indirect Only :guilabel:`Cycles Only`
   Disables the *Indirect Only* property for the selected collections.

-----

.. _bpy.ops.outliner.collection_color_tag_set:

Set Color Tag
   Assigns or clears a collection's :ref:`color tag <scene_layout-collections-color-tagging>`
   for the selected collection.


.. _bpy.ops.outliner.id_operation:

ID Data
-------

Unlink
   Removes the current usage of the data-block while keeping any others
   (e.g. removing a material from only the current mesh).
Make Local
   Turns an :doc:`externally linked </files/linked_libraries/link_append>` data-block into a local one.
Make Single User
   This menu item is not currently functional. You can use the *User Count* button in the
   :doc:`/interface/controls/templates/data_block` instead.
Delete
   Deletes the selected data-block.
Remap Users
   Replaces all usages of the selected data-block by a different one. For example,
   you could use this to globally replace a material by another.
Copy/Paste
   Copies/pastes selected data-blocks.
Add/Clear Fake User
   Adds/removes a :ref:`fake user <data-system-datablock-fake-user>`, which prevents unused data-blocks
   from getting automatically deleted when saving and reloading the blend-file.
Rename :kbd:`F2`
   Renames the selected data-block.
Select Linked
   Selects the data-blocks that use the currently selected one (e.g. selecting all the objects that use the
   selected material). See :ref:`bpy.ops.object.select_linked`.


Mark as Asset
-------------

See :ref:`bpy.ops.asset.mark`.


Clear Asset
-----------

See :ref:`bpy.ops.asset.clear`.


Clear Asset (Set Fake User)
---------------------------

See :ref:`assets-clear-set-fake-user`.


Library Override
----------------

See :doc:`/files/linked_libraries/library_overrides`.


View
----

.. _bpy.ops.outliner.show_active:

Show Active :kbd:`Period`
   Centers the tree view to the active item.

.. _bpy.ops.outliner.expanded_toggle:

Expand/Collapse All :kbd:`Shift-A`
   Expands/collapses every single item in the tree.

.. _bpy.ops.outliner.show_hierarchy:

Show Object Hierarchy :kbd:`Home`
   Expands all objects that have child objects, and collapses all objects that don't.

.. _bpy.ops.outliner.show_one_level:

Show/Hide One Level :kbd:`NumpadPlus`/ :kbd:`NumpadMinus`
   Expands/collapses a level down/up the tree across all items.
