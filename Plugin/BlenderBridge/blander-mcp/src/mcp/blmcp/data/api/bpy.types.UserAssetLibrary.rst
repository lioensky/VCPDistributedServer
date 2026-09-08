UserAssetLibrary(bpy_struct)
============================

.. currentmodule:: bpy.types

base class --- :class:`bpy_struct`

.. class:: UserAssetLibrary(bpy_struct)

   Settings to define a reusable library for Asset Browsers to use

   .. attribute:: enabled

      Enable the asset library (default True)

      :type: bool

   .. attribute:: import_method

      Determine how the asset will be imported, unless overridden by the Asset Browser (default ``'PACK'``)

      - ``LINK``
        Link -- Import the assets as linked data-block.
      - ``APPEND``
        Append -- Import the assets as copied data-block, with no link to the original asset data-block.
      - ``APPEND_REUSE``
        Append (Reuse Data) -- Import the assets as copied data-block while avoiding multiple copies of nested, typically heavy data. For example the textures of a material asset, or the mesh of an object asset, don't have to be copied every time this asset is imported. The instances of the asset share the data instead..
      - ``PACK``
        Pack -- Import the asset as linked data-block, and pack it in the current file (ensures that it remains unchanged in case the library data is modified, is not available anymore, etc.).

      :type: Literal['LINK', 'APPEND', 'APPEND_REUSE', 'PACK']

   .. attribute:: name

      Identifier (not necessarily unique) for the asset library (default "", never None)

      :type: str

   .. attribute:: path

      Path to a directory with .blend files to use as an asset library (default "", never None)

      :type: str

   .. attribute:: use_relative_path

      Use relative path when linking assets from this asset library (default True)

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

   - :class:`AssetLibraryCollection.new`
   - :class:`AssetLibraryCollection.remove`
   - :class:`PreferencesFilePaths.asset_libraries`

