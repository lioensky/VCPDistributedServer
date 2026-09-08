
***************
Developer Tools
***************

These preferences are reserved for features that aid Blender and add-on development.
This category is hidden by default and is visible enabling
:ref:`Developer Extras <bpy.types.PreferencesView.show_developer_ui>`.


Debug
=====

.. _bpy.types.PreferencesExperimental.use_undo_legacy:

Undo Legacy
   Use legacy undo (slower than the new default one, but may be more stable in some cases).

.. _bpy.types.PreferencesExperimental.override_auto_resync:

No Override Auto Resync
   Disables library overrides automatic resync detection and process on file load.
   Enable when dealing with older blend-files that need manual Resync (Enforce) handling.

.. _bpy.types.PreferencesExperimental.use_cycles_debug:

Cycles Debug
   Show the Cycles rendering debug panel.

.. _bpy.types.PreferencesExperimental.show_asset_debug_info:

Asset Debug Info
   Enable some extra fields in the Asset Browser to aid debugging.

.. _bpy.types.PreferencesExperimental.use_asset_indexing:

Asset Indexing
   Disabling the asset indexer forces every asset library refresh to completely reread assets from disk.

.. _bpy.types.PreferencesExperimental.use_viewport_debug:

Viewport Debug
   Enable viewport debugging options for developers in the overlays pop-over.

.. _bpy.types.PreferencesExperimental.use_eevee_debug:

EEVEE Debug
   Enable EEVEE debugging options for developers.
