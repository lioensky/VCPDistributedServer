ID(bpy_struct)
==============

.. currentmodule:: bpy.types

base class --- :class:`bpy_struct`

subclasses --- 
:class:`Action`, :class:`Annotation`, :class:`Armature`, :class:`Brush`, :class:`CacheFile`, :class:`Camera`, :class:`Collection`, :class:`Curve`, :class:`Curves`, :class:`FreestyleLineStyle`, :class:`GreasePencil`, :class:`Image`, :class:`Key`, :class:`Lattice`, :class:`Library`, :class:`Light`, :class:`LightProbe`, :class:`Mask`, :class:`Material`, :class:`Mesh`, :class:`MetaBall`, :class:`MovieClip`, :class:`NodeTree`, :class:`Object`, :class:`PaintCurve`, :class:`Palette`, :class:`ParticleSettings`, :class:`PointCloud`, :class:`Scene`, :class:`Screen`, :class:`Sound`, :class:`Speaker`, :class:`Text`, :class:`Texture`, :class:`VectorFont`, :class:`Volume`, :class:`WindowManager`, :class:`WorkSpace`, :class:`World`

.. class:: ID(bpy_struct)

   Base type for data-blocks, defining a unique name, linking from other libraries and garbage collection

   .. attribute:: asset_data

      Additional data for an asset data-block

      :type: :class:`AssetMetaData` | None

   .. data:: id_type

      Type identifier of this data-block (default ``'ACTION'``, readonly)

      :type: Literal[:ref:`rna_enum_id_type_items`]

   .. data:: is_editable

      This data-block is editable in the user interface. Linked data-blocks are not editable, except if they were loaded as editable assets. (default False, readonly)

      :type: bool

   .. data:: is_embedded_data

      This data-block is not an independent one, but is actually a sub-data of another ID (typical example: root node trees or master collections) (default False, readonly)

      :type: bool

   .. data:: is_evaluated

      Whether this ID is runtime-only, evaluated data-block, or actual data from .blend file (default False, readonly)

      :type: bool

   .. data:: is_library_indirect

      Is this ID block linked indirectly (default False, readonly)

      :type: bool

   .. data:: is_linked_packed

      This data-block is linked and packed into the .blend file (default False, readonly)

      :type: bool

   .. data:: is_missing

      This data-block is a place-holder for missing linked data (i.e. it is [an override of] a linked data that could not be found anymore) (default False, readonly)

      :type: bool

   .. attribute:: is_runtime_data

      This data-block is runtime data, i.e. it won't be saved in .blend file. Note that e.g. evaluated IDs are always runtime, so this value is only editable for data-blocks in Main data-base. (default False)

      :type: bool

   .. data:: library

      Library file the data-block is linked from (readonly)

      :type: :class:`Library` | None

   .. data:: library_weak_reference

      Weak reference to a data-block in another library .blend file (used to re-use already appended data instead of appending new copies) (readonly)

      :type: :class:`LibraryWeakReference` | None

   .. attribute:: name

      Unique data-block ID name (within a same type and library) (default "", never None)

      :type: str

   .. data:: name_full

      Unique data-block ID name, including library one if any (default "", readonly, never None)

      :type: str

   .. data:: original

      Actual data-block from .blend file (Main database) that generated that evaluated one (readonly)

      :type: :class:`ID` | None

   .. data:: override_library

      Library override data (readonly)

      :type: :class:`IDOverrideLibrary` | None

   .. data:: preview

      Preview image and icon of this data-block (always None if not supported for this type of data) (readonly)

      :type: :class:`ImagePreview` | None

   .. data:: session_uid

      A session-wide unique identifier for the data block that remains the same across renames and internal reallocations, unchanged when reloading the file (in [-inf, inf], default 0, readonly)

      :type: int

   .. attribute:: tag

      Tools can use this to tag data for their own purposes (initial state is undefined) (default False)

      :type: bool

   .. attribute:: use_extra_user

      Indicates whether an extra user is set or not (mainly for internal/debug usages) (default False)

      :type: bool

   .. attribute:: use_fake_user

      Save this data-block even if it has no users (default False)

      :type: bool

   .. data:: users

      Number of times this data-block is referenced (in [0, inf], default 0, readonly)

      :type: int

   .. method:: bl_system_properties_get(*, do_create=False)

      DEBUG ONLY. Internal access to runtime-defined RNA data storage, intended solely for testing and debugging purposes. Do not access it in regular scripting work, and in particular, do not assume that it contains writable data

      :param do_create: Ensure that system properties are created if they do not exist yet (optional)
      :type do_create: bool
      :return: The system properties root container, or None if there are no system properties stored in this data yet, and its creation was not requested
      :rtype: :class:`PropertyGroup`

   .. method:: rename(name, *, mode='NEVER')

      More refined handling in case the new name collides with another ID's name

      :param name: New name to rename the ID to, if empty will re-use the current ID name (never None)
      :type name: str
      :param mode: How to handle name collision, in case the requested new name is already used by another ID of the same type (optional)

         - ``NEVER``
           Never Rename -- Never rename an existing ID whose name would conflict, the currently renamed ID will get a numeric suffix appended to its new name.
         - ``ALWAYS``
           Always Rename -- Always rename an existing ID whose name would conflict, ensuring that the currently renamed ID will get requested name.
         - ``SAME_ROOT``
           Rename If Same Root -- Only rename an existing ID whose name would conflict if its name root (everything besides the numerical suffix) is the same as the existing name of the currently renamed ID.
      :type mode: Literal['NEVER', 'ALWAYS', 'SAME_ROOT']
      :return: How did the renaming of the data-block went on

         - ``UNCHANGED``
           Unchanged -- The ID was not renamed, e.g. because it is already named as requested.
         - ``UNCHANGED_COLLISION``
           Unchanged Due to Collision -- The ID was not renamed, because requested name would have collided with another existing ID's name, and the automatically adjusted name was the same as the current ID's name.
         - ``RENAMED_NO_COLLISION``
           Renamed Without Collision -- The ID was renamed as requested, without creating any name collision.
         - ``RENAMED_COLLISION_ADJUSTED``
           Renamed With Collision -- The ID was renamed with adjustment of the requested name, to avoid a name collision.
         - ``RENAMED_COLLISION_FORCED``
           Renamed Enforced With Collision -- The ID was renamed as requested, also renaming another ID to avoid a name collision.
      :rtype: Literal['UNCHANGED', 'UNCHANGED_COLLISION', 'RENAMED_NO_COLLISION', 'RENAMED_COLLISION_ADJUSTED', 'RENAMED_COLLISION_FORCED']

   .. method:: evaluated_get(depsgraph)

      Get corresponding evaluated ID from the given dependency graph. Note that this does not ensure the dependency graph is fully evaluated, it just returns the result of the last evaluation.

      :param depsgraph: Dependency graph to perform lookup in (never None)
      :type depsgraph: :class:`Depsgraph` | None
      :return: New copy of the ID
      :rtype: :class:`ID`

   .. method:: copy()

      Create a copy of this data-block (not supported for all data-blocks). The result is added to the Blend-File Data (Main database), with all references to other data-blocks ensured to be from within the same Blend-File Data.

      :return: New copy of the ID
      :rtype: :class:`ID`

   .. method:: asset_mark()

      Enable easier reuse of the data-block through the Asset Browser, with the help of customizable metadata (like previews, descriptions and tags)


   .. method:: asset_clear()

      Delete all asset metadata and turn the asset data-block back into a normal data-block


   .. method:: asset_generate_preview()

      Generate preview image (might be scheduled in a background thread)


   .. method:: override_create(*, remap_local_usages=False)

      Create an overridden local copy of this linked data-block (not supported for all data-blocks)

      :param remap_local_usages: Whether local usages of the linked ID should be remapped to the new library override of it (optional)
      :type remap_local_usages: bool
      :return: New overridden local copy of the ID
      :rtype: :class:`ID`

   .. method:: override_hierarchy_create(scene, view_layer, *, reference=None, do_fully_editable=False)

      Create an overridden local copy of this linked data-block, and most of its dependencies when it is a Collection or and Object

      :param scene: In which scene the new overrides should be instantiated (never None)
      :type scene: :class:`Scene` | None
      :param view_layer: In which view layer the new overrides should be instantiated (never None)
      :type view_layer: :class:`ViewLayer` | None
      :param reference: Another ID (usually an Object or Collection) used as a hint to decide where to instantiate the new overrides (optional)
      :type reference: :class:`ID` | None
      :param do_fully_editable: Make all library overrides generated by this call fully editable by the user (none will be 'system overrides') (optional)
      :type do_fully_editable: bool
      :return: New overridden local copy of the root ID
      :rtype: :class:`ID`

   .. method:: user_clear()

      Clear the user count of a data-block so its not saved, on reload the data will be removed


      This function is for advanced use only, misuse can crash Blender since the user
      count is used to prevent data being removed when it is used.

      .. literalinclude:: ./examples/bpy.types.ID.user_clear.1.py
         :lines: 6-


   .. method:: user_remap(new_id)

      Replace all usage in the .blend file of this ID by new given one

      :param new_id: New ID to use (never None)
      :type new_id: :class:`ID` | None

   .. method:: make_local(*, clear_proxy=True, clear_liboverride=False, clear_asset_data=True)

      Make this data-block local, return local one (may be a copy of the original, in case it is also indirectly used)

      :param clear_proxy: Deprecated, has no effect (optional)
      :type clear_proxy: bool
      :param clear_liboverride: Remove potential library override data from the newly made local data (optional)
      :type clear_liboverride: bool
      :param clear_asset_data: Remove potential asset metadata so the newly local data-block is not treated as asset data-block and won't show up in asset libraries (optional)
      :type clear_asset_data: bool
      :return: This ID, or the new ID if it was copied
      :rtype: :class:`ID`

   .. method:: user_of_id(id)

      Count the number of times that ID uses/references given one

      :param id: ID to count usages (never None)
      :type id: :class:`ID` | None
      :return: Number of usages/references of given id by current data-block (in [0, inf])
      :rtype: int

   .. method:: animation_data_create()

      Create animation data to this ID, note that not all ID types support this

      :return: New animation data or None
      :rtype: :class:`AnimData`

   .. method:: animation_data_clear()

      Clear animation on this ID


   .. method:: update_tag(*, refresh=set())

      Tag the ID to update its display data, e.g. when calling :class:`bpy.types.Scene.update`

      :param refresh: Type of updates to perform (optional)
      :type refresh: set[Literal['OBJECT', 'DATA', 'TIME']]

   .. method:: preview_ensure()

      Ensure that this ID has preview data (if ID type supports it)

      :return: The existing or created preview
      :rtype: :class:`ImagePreview`

   .. classmethod:: bl_rna_get_subclass(id, default=None, /)
   
      :param id: The RNA type identifier.
      :type id: str
      :param default: The value to return when not found.
      :type default: :class:`bpy.types.Struct` | None
      :return: The RNA type or default when not found.
      :rtype: :class:`bpy.types.Struct`


   .. classmethod:: bl_rna_get_subclass_py(id, default=None, /)
   
      :param id: The RNA type identifier.
      :type id: str
      :param default: The value to return when not found.
      :type default: type | None
      :return: The class or default when not found.
      :rtype: type


Inherited Properties
--------------------

.. hlist::
   :columns: 2

   - :class:`bpy_struct.id_data`

Inherited Functions
-------------------

.. hlist::
   :columns: 2

   - :class:`bpy_struct.as_pointer`
   - :class:`bpy_struct.driver_add`
   - :class:`bpy_struct.driver_remove`
   - :class:`bpy_struct.get`
   - :class:`bpy_struct.id_properties_clear`
   - :class:`bpy_struct.id_properties_ensure`
   - :class:`bpy_struct.id_properties_ui`
   - :class:`bpy_struct.is_property_hidden`
   - :class:`bpy_struct.is_property_overridable_library`
   - :class:`bpy_struct.is_property_readonly`
   - :class:`bpy_struct.is_property_set`
   - :class:`bpy_struct.items`
   - :class:`bpy_struct.keyframe_delete`
   - :class:`bpy_struct.keyframe_insert`
   - :class:`bpy_struct.keys`
   - :class:`bpy_struct.path_from_id`
   - :class:`bpy_struct.path_from_module`
   - :class:`bpy_struct.path_resolve`
   - :class:`bpy_struct.pop`
   - :class:`bpy_struct.property_overridable_library_set`
   - :class:`bpy_struct.property_unset`
   - :class:`bpy_struct.rna_ancestors`
   - :class:`bpy_struct.type_recast`
   - :class:`bpy_struct.values`

References
----------

.. hlist::
   :columns: 2

   - :mod:`bpy.context.annotation_data_owner`
   - :mod:`bpy.context.id`
   - :mod:`bpy.context.selected_ids`
   - :mod:`bpy.context.texture_user`
   - :class:`Action.fcurve_ensure_for_datablock`
   - :class:`ActionSlot.users`
   - :class:`AssetRepresentation.local_id`
   - :class:`BlendData.pack_linked_ids_hierarchy`
   - :class:`BlendData.pack_linked_ids_hierarchy`
   - :class:`BlendDataObjects.new`
   - :class:`BlendImportContextItem.id`
   - :class:`BlendImportContextItem.library_override_id`
   - :class:`BlendImportContextItem.reusable_local_id`
   - :class:`Depsgraph.id_eval_get`
   - :class:`Depsgraph.id_eval_get`
   - :class:`Depsgraph.ids`
   - :class:`DepsgraphUpdate.id`
   - :class:`DopeSheet.source`
   - :class:`DriverTarget.id`
   - :class:`ID.copy`
   - :class:`ID.evaluated_get`
   - :class:`ID.make_local`
   - :class:`ID.original`
   - :class:`ID.override_create`
   - :class:`ID.override_hierarchy_create`
   - :class:`ID.override_hierarchy_create`
   - :class:`ID.user_of_id`
   - :class:`ID.user_remap`
   - :class:`IDOverrideLibrary.hierarchy_root`
   - :class:`IDOverrideLibrary.reference`
   - :class:`IDOverrideLibraryPropertyOperation.subitem_local_id`
   - :class:`IDOverrideLibraryPropertyOperation.subitem_reference_id`
   - :class:`IDOverrideLibraryPropertyOperations.add`
   - :class:`IDOverrideLibraryPropertyOperations.add`
   - :class:`IDViewerPathElem.id`
   - :class:`Key.user`
   - :class:`KeyingSetPath.id`
   - :class:`KeyingSetPaths.add`
   - :class:`MaskParent.id`
   - :class:`NodeTree.get_from_context`
   - :class:`NodeTree.get_from_context`
   - :class:`NodesModifierDataBlock.id`
   - :class:`Object.data`
   - :class:`PropertyGroupItem.id`
   - :class:`SpaceFileBrowser.activate_asset_by_id`
   - :class:`SpaceNodeEditor.id`
   - :class:`SpaceNodeEditor.id_from`
   - :class:`SpaceProperties.pin_id`
   - :class:`UILayout.template_action`
   - :class:`UILayout.template_path_builder`
   - :class:`UILayout.template_preview`
   - :class:`UILayout.template_preview`

