PreferencesExperimental(bpy_struct)
===================================

.. currentmodule:: bpy.types

base class --- :class:`bpy_struct`

.. class:: PreferencesExperimental(bpy_struct)

   Experimental features

   .. attribute:: no_data_block_packing

      Fall-back to appending instead of packing data-blocks (default False)

      :type: bool

   .. attribute:: override_auto_resync

      Disable library overrides automatic resync detection and process on file load (can be useful to help fixing broken files). Also see the "--disable-liboverride-auto-resync" command line option (default False)

      :type: bool

   .. attribute:: show_asset_debug_info

      Enable some extra fields in the Asset Browser to aid in debugging (default False)

      :type: bool

   .. attribute:: use_all_linked_data_direct

      Forces all linked data to be considered as directly linked. Workaround for current issues/limitations in BAT (Blender studio pipeline tool) (default False)

      :type: bool

   .. attribute:: use_asset_indexing

      Disable the asset indexer, to force every asset library refresh to completely reread assets from disk (default False)

      :type: bool

   .. attribute:: use_cycles_debug

      Enable Cycles debugging options for developers (default False)

      :type: bool

   .. attribute:: use_eevee_debug

      Enable EEVEE debugging options for developers (default False)

      :type: bool

   .. attribute:: use_extended_asset_browser

      Enable Asset Browser editor and operators to manage regular data-blocks as assets, not just poses (default False)

      :type: bool

   .. attribute:: use_extensions_debug

      Extra debugging information & developer support utilities for extensions (default False)

      :type: bool

   .. attribute:: use_geometry_bundle

      Support storing custom bundles in a geometry in Geometry Nodes (default False)

      :type: bool

   .. attribute:: use_geometry_nodes_lists

      Enable new list types and nodes (default False)

      :type: bool

   .. attribute:: use_new_curves_tools

      Enable additional features for the new curves data block (default False)

      :type: bool

   .. attribute:: use_paint_debug

      Enable paint & sculpt debugging options for developers (default False)

      :type: bool

   .. attribute:: use_recompute_usercount_on_save_debug

      Recompute all ID user-counts before saving to a blend-file. Allows to work around invalid user-count handling in code that may lead to loss of data due to wrongly detected unused data-blocks (default False)

      :type: bool

   .. attribute:: use_sculpt_texture_paint

      Use texture painting in Sculpt Mode (default False)

      :type: bool

   .. attribute:: use_shader_node_previews

      Enables previews in the shader node editor (default False)

      :type: bool

   .. attribute:: use_undo_legacy

      Use legacy undo (slower than the new default one, but may be more stable in some cases) (default False)

      :type: bool

   .. attribute:: use_viewport_debug

      Enable viewport debugging options for developers in the overlays pop-over (default False)

      :type: bool

   .. attribute:: write_legacy_blend_file_format

      Use file format used before Blender 5.0. This format is more limited but it may have better compatibility with tools that don't support the new format yet (default False)

      :type: bool

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

   - :class:`Preferences.experimental`

