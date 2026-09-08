IDOverrideLibrary(bpy_struct)
=============================

.. currentmodule:: bpy.types

base class --- :class:`bpy_struct`

.. class:: IDOverrideLibrary(bpy_struct)

   Struct gathering all data needed by overridden linked IDs

   .. data:: hierarchy_root

      Library override ID used as root of the override hierarchy this ID is a member of (readonly)

      :type: :class:`ID` | None

   .. attribute:: is_in_hierarchy

      Whether this library override is defined as part of a library hierarchy, or as a single, isolated and autonomous override (default True)

      :type: bool

   .. attribute:: is_system_override

      Whether this library override exists only for the override hierarchy, or if it is actually editable by the user (default False)

      :type: bool

   .. data:: properties

      List of overridden properties (default None, readonly)

      :type: :class:`IDOverrideLibraryProperties`\ [:class:`IDOverrideLibraryProperty`]

   .. data:: reference

      Linked ID used as reference by this override (readonly)

      :type: :class:`ID` | None

   .. method:: operations_update()

      Update the library override operations based on the differences between this override ID and its reference


   .. method:: reset(*, do_hierarchy=True, set_system_override=False)

      Reset this override to match again its linked reference ID

      :param do_hierarchy: Also reset all the dependencies of this override to match their reference linked IDs (optional)
      :type do_hierarchy: bool
      :param set_system_override: Reset all user-editable overrides as (non-editable) system overrides (optional)
      :type set_system_override: bool

   .. method:: destroy(*, do_hierarchy=True)

      Delete this override ID and remap its usages to its linked reference ID instead

      :param do_hierarchy: Also delete all the dependencies of this override and remap their usages to their reference linked IDs (optional)
      :type do_hierarchy: bool

   .. method:: resync(scene, *, view_layer=None, residual_storage=None, do_hierarchy_enforce=False, do_whole_hierarchy=False)

      Resync the data-block and its sub-hierarchy, or the whole hierarchy if requested

      :param scene: The scene to operate in (for contextual things like keeping active object active, ensuring all overridden objects remain instantiated, etc.) (never None)
      :type scene: :class:`Scene` | None
      :param view_layer: The view layer to operate in (same usage as the ``scene`` data, in case it is not provided the scene's collection will be used instead) (optional)
      :type view_layer: :class:`ViewLayer` | None
      :param residual_storage: Collection where to store objects that are instantiated in any other collection anymore (garbage collection, will be created if needed and none is provided) (optional)
      :type residual_storage: :class:`Collection` | None
      :param do_hierarchy_enforce: Enforce restoring the dependency hierarchy between data-blocks to match the one from the reference linked hierarchy (WARNING: if some ID pointers have been purposely overridden, these will be reset to their default value) (optional)
      :type do_hierarchy_enforce: bool
      :param do_whole_hierarchy: Resync the whole hierarchy this data-block belongs to, not only its own sub-hierarchy (optional)
      :type do_whole_hierarchy: bool
      :return: Success, Whether the resync process was successful or not
      :rtype: bool

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

   - :class:`ID.override_library`

