
*********
Interface
*********

Header
======

.. _bpy.types.SpaceOutliner.display_mode:

Display Mode
------------

This header dropdown lets you choose what the Outliner should show.

:Scenes:
   Shows the :doc:`view layers </render/layers/introduction>`,
   :doc:`collections </scene_layout/collections/introduction>`,
   and objects across all scenes.
:View Layer:
   Shows the collections and objects in the current view layer of the current scene.
:Video Sequencer:
   Shows the images and videos that are used in the :doc:`Video Sequencer </video_editing/index>`.

.. _outliner-blender-file-mode:

:Blender File:
   Lists all data in the current blend-file. On the right side of the list, a shield icon shows the number
   of users -- clicking it adds or removes a :ref:`fake user <data-system-datablock-fake-user>`.
:Data API:
   Lists every :doc:`data-block </files/data_blocks>` in the file along with any properties that it might have.
:Library Overrides:
   Shows the :doc:`library overrides </files/linked_libraries/library_overrides>`.
   Separated further into two view modes:

   .. _bpy.types.SpaceOutliner.lib_override_view_mode:

   :Properties:
      Shows the data-blocks that have overridden properties in a list grouped by type.
      You can expand each data-block to see and change these properties.
   :Hierarchies:
      Shows the overridden data-blocks in a tree that visualizes their hierarchy.
      This includes parent data-blocks that were overridden implicitly.
      For example, if you created an override for a material,
      this tree would show the hierarchy object > mesh > material.

      .. _bpy.ops.ed.lib_id_override_editable_toggle:

      This view also shows a column of icons on the right that let you toggle whether
      each override is editable.
:Unused Data:
   Lists the data-blocks that are unused or only have a :ref:`fake user <data-system-datablock-fake-user>`.
   You can add/remove a fake user by clicking the shield icon on the right.

   Unused data-blocks are automatically deleted when saving and reloading the file.
   You can also delete them manually by clicking *Purge* in the header.

.. _bpy.types.SpaceOutliner.filter_text:

Search
------

The textbox lets you filter the tree by typing a substring. You can focus it using :kbd:`Ctrl-F`
or clear it using :kbd:`Alt-F`.


.. _editors-outliner-interface-filter:

Filter
------

The funnel icon in the header offers further control over what is displayed in the editor.
Depending on the *Display Mode*, some options are not available.

.. _bpy.types.SpaceOutliner.show_restrict_column:

Restriction Toggles
   Set which `Restriction Toggles`_ should be visible.

.. _bpy.types.SpaceOutliner.use_sort_alpha:

Sort Alphabetically
   Sort the entries alphabetically.

.. _bpy.types.SpaceOutliner.use_sync_select:

Sync Selection
   Whether to synchronize the Outliner selection to and from the
   :doc:`3D Viewport </editors/3dview/index>` and
   :doc:`Video Sequencer </video_editing/index>` editors.

.. _bpy.types.SpaceOutliner.show_mode_column:

Show Mode Column
   Show the column for toggling the :doc:`object interaction mode </editors/3dview/modes>`.


.. rubric:: Search

.. _bpy.types.SpaceOutliner.use_filter_complete:

Exact Match
   Only show the items whose name fully matches the :ref:`search text <bpy.types.SpaceOutliner.filter_text>`
   rather than only containing it as a substring.

.. _bpy.types.SpaceOutliner.use_filter_case_sensitive:

Case Sensitive
   Take lower/upper case into account when comparing the search text to the item names.


.. rubric:: Filter

.. _bpy.types.SpaceOutliner.use_filter_view_layers:

All View Layers
   Show all the :doc:`view layers </render/layers/index>` in the scene instead of only the active one.
   Combined with disabling the *Objects* filter, this gives a compact overview of all the collections in relation
   to the view layers.

.. _bpy.types.SpaceOutliner.use_filter_collection:

Collections
   Show the collections in the scene hierarchy. Only the collections themselves are hidden when this option
   is disabled; the objects within them remain visible.

.. _bpy.types.SpaceOutliner.use_filter_object:

Objects
   Show the objects in the scene hierarchy. Disabling this gives you an overview of just the collections.

.. _bpy.types.SpaceOutliner.filter_invert:
.. _bpy.types.SpaceOutliner.filter_state:

Object State
   List the objects based on their state or restrictions.
   The results can be inverted using the *Invert* toggle button.

   :All:
      Show all objects.
   :Visible:
      Only show the objects that are visible in the 3D Viewport.
      This takes both the *Hide in Viewports* and *Disable in Viewports* settings into account;
      see :ref:`editors-outliner-interface-restriction_columns`.
   :Selected:
      Only show the object(s) that are currently :doc:`selected </scene_layout/object/selecting>`
      in the 3D Viewport.
   :Active:
      Only show the active object (typically the one that was selected last).
   :Selectable:
      Only show the objects that can be selected in the 3D Viewport;
      see :ref:`editors-outliner-interface-restriction_columns`.

.. _bpy.types.SpaceOutliner.use_filter_object_content:

Object Contents
   List relevant materials, modifiers, mesh data and so on as children of each object.

.. _bpy.types.SpaceOutliner.use_filter_children:

Object Children
   Show :doc:`child objects </scene_layout/object/editing/parent>` as child nodes in the Outliner tree.
   When disabled, child objects are shown as sibling nodes instead (unless they're in a different collection
   than their parent, in which case they're not shown in the parent's collection at all).

.. _bpy.types.SpaceOutliner.use_filter_object_mesh:
.. _bpy.types.SpaceOutliner.use_filter_object_light:
.. _bpy.types.SpaceOutliner.use_filter_object_camera:
.. _bpy.types.SpaceOutliner.use_filter_object_grease_pencil:
.. _bpy.types.SpaceOutliner.use_filter_object_empty:
.. _bpy.types.SpaceOutliner.use_filter_object_others:

Meshes/Lights/...
   Lets you filter out objects by type.

.. _bpy.types.SpaceOutliner.use_filter_lib_override_system:

System Overrides
   Shows the data-block properties that are defined/controlled automatically (e.g. to make data-blocks
   point to overridden data instead of the original). Only available in the *Library Overrides*
   `Display Mode`_.


Miscellaneous
-------------

Some options in the header will only show if compatible with the active `Display Mode`_.

New Collection :guilabel:`View Layer`
   Add a new collection inside the selected one.
Filter by Type :guilabel:`Blender File` :guilabel:`Unused Data`
   Restrict the type of the data-blocks shown in the Outliner.
Keying Sets (Data API) :guilabel:`Data API`
   Add/Remove the selected property to/from the active :doc:`Keying Set </animation/keyframes/keying_sets>`.
Drivers
   Add/Remove :doc:`Drivers </animation/drivers/index>` to the selected item.

.. _bpy.ops.outliner.orphans_purge:

Purge (Orphan Data) :guilabel:`Unused Data`
   Opens a dialog to remove unused data-blocks from both the current blend-file or any
   :doc:`Linked Data </files/linked_libraries/link_append>` (cannot be undone).

   Local Data-Blocks
      Removes unused data-blocks from the current blend-file.
   Linked Data-Blocks
      Removes unused data-blocks from :doc:`Linked Data </files/linked_libraries/link_append>`.
   Recursive Delete
      Removes data-blocks only used by unused data-blocks,
      ensuring that no orphaned data-blocks remain after execution.


Main Region
===========

Object Interaction Mode
-----------------------

.. figure:: /images/editors_outliner_interface_mode-icons.png

   Mode icons. Two objects are currently in Edit Mode; a third could be added.

If a selected object is in an :doc:`interaction mode </editors/3dview/modes>`
other than the default Object Mode, the Outliner shows an icon representing
this mode on the left.

If the active object has such an icon, the Outliner also shows a dot next to
objects of the same type. You can click such a dot to switch over to a different
object while staying in the same mode.

If the mode supports :ref:`3dview-multi-object-mode`, you can also click a
dot with :kbd:`Ctrl-LMB` to *add* an object to the mode.

You can click the mode icon of the active object to switch it (and any other objects
in case of Multi-Object Editing) back to Object Mode. You can also :kbd:`Ctrl-LMB`
the mode icon of a selected -- but not active -- object to switch only that object
back to Object Mode.


.. _editors-outliner-interface-restriction_columns:

Restriction Toggles
-------------------

.. figure:: /images/editors_outliner_interface_restriction-toggles.png
   :align: right

   Restriction toggles.

The right side of the Outliner shows a series of toggle icons for every collection,
object, bone, modifier, and constraint. These can be used to make the item invisible,
unselectable, and so on.

.. note::
   Only a few icons are shown by default. You can use the `Filter`_ pop-over to
   show additional ones.

Clicking an icon with :kbd:`Shift-LMB` toggles it for the item and all its children.

Clicking a collection's icon with :kbd:`Ctrl-LMB` enables it for the collection (and its
parent/child collections) and disables it for all others. Clicking again enables it for the others again.

:bl-icon:`checkbox_hlt` Exclude from View Layer :guilabel:`Collections`
   Toggles the collection's inclusion in the current :doc:`View Layer </render/layers/index>`.
   When excluded, contents will be hidden in the 3D Viewport, the render, and the Outliner.
   See :ref:`bpy.types.LayerCollection.exclude` for more information.

.. _bpy.types.ObjectBase.select:

:bl-icon:`restrict_select_off` Disable Selection
   Toggles whether the object or collection can be selected in the 3D Viewport.
   This can be useful for, say, reference images that you only want to display and never select/move.

   See more information for:

   - :ref:`Collections <bpy.types.Collection.hide_select>`
   - :ref:`Objects <bpy.types.Object.hide_select>`

.. _bpy.types.ObjectBase.hide_viewport:
.. _bpy.types.LayerCollection.hide_viewport:

:bl-icon:`hide_off` Hide in Viewports
   Toggles the visibility of the object or collection in (only) the 3D Viewport, for the current view layer.
   The render is not affected.

   As an alternative to clicking this icon, you can press :kbd:`H` while hovering over the
   3D Viewport to hide the selected objects, or :kbd:`Alt-H` to unhide all objects.

   This setting only applies within the current blend-file: when you
   :doc:`Link or Append </files/linked_libraries/link_append>` it to another
   blend-file, all collections and objects will be visible there.

   Objects hidden this way are still part of the view layer,
   so they still get evaluated and affect playback performance.

   .. seealso::

      Collections can be hidden for individual 3D Viewports;
      see :ref:`Local Collections <bpy.types.SpaceView3D.use_local_collections>` in the Sidebar.

.. _bpy.types.Collection.hide_viewport:

:bl-icon:`restrict_view_off` Disable in Viewports
   Toggles the visibility of the object or collection in (only) the 3D Viewport, for all view layers.
   The render is not affected.

   This setting is separate from *Hide in Viewports*. An object needs to have both settings
   enabled to be visible. You can use this one for "long-term invisibility,"
   keeping an object invisible even after pressing :kbd:`Alt-H`.

   This setting carries over to other blend-files when linking or appending.

   Objects hidden this way are no longer part of the view layer,
   so they no longer get evaluated and don't affect playback performance.

:bl-icon:`restrict_render_off` Disable in Renders
   Toggles the visibility of the object or collection in (only) the render,
   for all view layers. The 3D Viewport is not affected.

   This is typically used for supporting objects that help modeling and animation
   yet don't belong in the final image.

:bl-icon:`holdout_off` Holdout :guilabel:`Collections`
   Toggles the collection's :ref:`Holdout <bpy.types.LayerCollection.holdout>` property,
   which makes the objects in the collection cut a fully transparent hole into the render output of the view layer.

:bl-icon:`indirect_only_off` Indirect Only :guilabel:`Collections` :guilabel:`Cycles`
   Toggles the collection's :ref:`Indirect Only <bpy.types.LayerCollection.indirect_only>` property.
   Objects inside this collection will only contribute to the final image indirectly through shadows and reflections.
