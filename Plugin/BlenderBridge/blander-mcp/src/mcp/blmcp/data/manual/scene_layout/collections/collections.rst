.. _bpy.types.Collection:
.. _bpy.ops.collection:

***********
Collections
***********

There can be many objects in a scene: A typical stage scene consists of furniture, props,
lights, and backdrops.
Blender helps you keep everything organized by allowing you to group like objects together.
Objects can be grouped together without any kind of transformation relationship (unlike parenting).
Collections are used to just logically organize your scene,
or to facilitate one-step appending or linking between files or across scenes.


.. _scene-layout_collections_collections_tab:

Collections Tab
===============

.. reference::

   :Menu:      :menuselection:`Properties --> Collection Properties`

Collection properties tab allows convenient access to properties for the active collection.

.. figure:: /images/scene-layout_collections_property_panel.png

   Collection properties.


Visibility
----------

.. _bpy.types.Collection.hide_select:

Selectable
   Toggles the ability to select the objects of this collection in the 3D Viewport.

   This is useful for if you have placed something in the scene and
   do not want to accidentally select it when working on something else for example references images.

.. _bpy.types.Collection.hide_render:

Show In -- Renders
   Enables/disables visibility of the collection in renders.


.. _bpy.types.LayerCollection:

View Layer
^^^^^^^^^^

Each collection in a scene can be configured per :doc:`View Layer </render/layers/index>`
to control how its contents appear in the render.
These settings allow for flexible render setups by including or excluding specific collections,
masking objects, or limiting their contribution to indirect effects.

.. _bpy.types.LayerCollection.exclude:

Include
   Includes this collection in the active View Layer.
   When disabled, all objects in the collection will be excluded from the render, the 3D Viewport, and the Outliner
   for the current view layer.

   This is useful for rendering alternate versions of a scene or isolating elements for compositing.

.. _bpy.types.LayerCollection.holdout:

Holdout
   Marks all objects in this collection as holdouts in the active view layer.

   Holdouts render as transparent regions in the final image, effectively masking out anything behind them. This is
   typically used in compositing workflows to create cutouts or to separate foreground and background elements.

   .. seealso::

      :doc:`Holdout Shader Node </render/shader_nodes/shader/holdout>`

.. _bpy.types.LayerCollection.indirect_only:

Indirect Only :guilabel:`Cycles Only`
   Objects in this collection will not appear directly in the rendered image,
   but they will still contribute indirectly through lighting, shadows, and reflections.

   This is useful for rendering clean product shots while preserving realistic environmental lighting or reflections.


Instancing
----------

.. _bpy.types.Collection.instance_offset:

Instance Offset X, Y Z
   Applies a spatial offset of the instanced collections from the original object's origin.


.. _collections-exporters:

Exporters
---------

Each collection can be exported to a number of various file formats.
These exporters are available globally, see :doc:`/files/import_export/index`,
however, this panel streamlines the process of re-exporting the same asset(s) repeatedly.
For example when creating glTF assets for a game and iterating on the look,
or when using Blender in a studio pipeline to create USD assets.

The following file formats are supported, see each for the documentation of export parameters:

- :doc:`/files/import_export/alembic`
- :doc:`/files/import_export/usd`
- :doc:`/files/import_export/obj`
- :doc:`/files/import_export/ply`
- :doc:`/addons/import_export/scene_fbx`
- :doc:`/addons/import_export/scene_gltf2`

.. _bpy.types.Collection.active_exporter_index:

Exporter List
   A :ref:`list view <ui-list-view>` of all the enabled exporters for the active collection.
   The selecting an exporter from the list will show it's options in a sub panel below.

.. _bpy.ops.collection.exporter_add:

:bl-icon:`add` (Add Exporter)
   Opens a menu to choose an exporter to add.

.. _bpy.ops.collection.exporter_remove:

:bl-icon:`remove` (Remove Exporter)
   Removes the selected exporter.

.. _bpy.ops.collection.export_all:

Export All
   Exports all exports for the active collection.

.. tip::

   Use :menuselection:`File --> Export All Collections` to export all exporters for all collections.


.. _scene_layout-collections-line-art:

Line Art
--------

.. _bpy.types.Collection.lineart_usage:

Usage
   How the collection is loaded into Line Art.
   Child objects of the collection can override this setting
   if they wish in :ref:`Object Properties <bpy.types.ObjectLineArt.usage>`.

   :Include: Generate feature lines for this collection.
   :Occlusion Only:
      Objects in the collection will only cause occlusion to existing feature lines
      and their geometry stay invisible.
   :Exclude:
      Objects in this collection will not be loaded into Line Art at all.
   :Intersection Only:
      Objects in the collection will only produce intersection lines in
      the scene and their own geometry stay invisible.
   :No Intersection: Include this collection but do not generate intersection lines.
   :Force Intersection: Generate intersection lines even with objects that disabled intersection.

.. _bpy.types.Collection.lineart_use_intersection_mask:

Collection Mask
   Use custom intersection mask for faces in this collection.
   Intersection masks can be used by the Line Art modifier to filter lines.
   See :ref:`Collection Masks <bpy.types.GreasePencilLineartModifier.use_intersection_mask>` for more information.

.. _bpy.types.Collection.lineart_intersection_mask:

Mask
   Intersections generated by this collection will have this mask value.

.. _bpy.types.Collection.use_lineart_intersection_priority:
.. _bpy.types.Collection.lineart_intersection_priority:

Intersection Priority
   Assigns an intersection priority value for this collection.
   The intersection line will be included into the object with the higher intersection priority value.


Custom Properties
-----------------

Create and manage your own properties to store data in the collection's data block.
See the :ref:`Custom Properties <files-data_blocks-custom-properties>` page for more information.


Collections Menu
================

.. reference::

   :Mode:      Object Mode
   :Menu:      :menuselection:`Object --> Collection`

The *Collections* menu provides tools for organizing and managing objects within collections.
Collections are used to group objects for easier scene organization,
visibility control, and rendering management.
Objects can belong to one or multiple collections, allowing flexible structuring of complex scenes.

.. _bpy.ops.object.move_to_collection:

Move to Collection :kbd:`M`
   Moves the selected objects to a different collection.
   The menu allows choosing an existing collection, creating a new one,
   or moving the objects to the *Scene Collection* (the root level of the scene).
   Once moved, the objects are removed from their previous collection unless they are also linked elsewhere.

.. _bpy.ops.object.link_to_collection:

Link to Collection :kbd:`Shift-M`
   Links the selected objects to an additional collection without removing them from their existing collections.
   This allows the same object to appear in multiple collections simultaneously,
   useful for managing shared elements across different scene layers or views.
   A new collection can also be created from the menu.
Create New Collection :kbd:`Ctrl-G`
   Creates a new collection and adds the selected object(s) to it.
   The name of the new collection can be specified in
   the *Create New Collection* :ref:`bpy.ops.screen.redo_last` panel.
   This collection is not linked to the active scene.
Remove from Collection :kbd:`Ctrl-Alt-G`
   Remove the selected objects from a collection. If the object belongs to more than one collection,
   a pop-up lets you select the collection and an option to remove it from all collections.
Remove from All Collections :kbd:`Shift-Ctrl-Alt-G`
   Remove the selected objects from all collections.
Add Selected to Active Objects Collection :kbd:`Shift-Ctrl-G`
   Adds the selected objects to one of the collections active object belongs to.
   Optionally add to \"All Collections\"
   to ensure selected objects are included in the same collections as the active object.
Remove Selected from Active Collection :kbd:`Shift-Alt-G`
   Causes the selected objects to be removed from the collections to which the active object belongs.
Hide Other Collections :kbd:`Ctrl-H`
   Hides collections which were not selected.

.. _scene-layout_collections_collections_panel:

Collections Panel
=================

.. reference::

   :Mode:      Object Mode
   :Panel:     :menuselection:`Object tab --> Collections`

.. figure:: /images/scene-layout_collections_collections_panel.png

   Collections panel.

All collections that an object has been assigned to are listed in the Properties
:menuselection:`Object tab --> Collections panel`.

Add to Collection
   Adds the selected object to a collection.
   A pop-up lets you specify the collection to add to.
:bl-icon:`add` (Add to Collection)
   Creates a new collection and adds the selected object to it.

Name
   To rename a collection, simply click in the collections name field.
:bl-icon:`x` (Remove Collection)
   Removes the object from the specified collection.
:bl-icon:`downarrow_hlt` (Collection Specials)
   Unlink Collection, Select Objects in Collection, Set Offset from Cursor
X, Y, Z
   Applies a spatial offset of the instanced collections from the original object's origin.

.. seealso:: Appending or Linking Collections

   To append a collection from another blend-file,
   consult :doc:`this page </files/linked_libraries/index>`.
   In summary, :menuselection:`File --> Link/Append Link`, Select a blend-file, and then the collection.

.. tip:: Selecting Collections

   Collections can be selected, see :ref:`Select Grouped <bpy.ops.object.select_grouped>` for more information.
