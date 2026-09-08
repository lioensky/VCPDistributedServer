FileAssetSelectParams(FileSelectParams)
=======================================

.. currentmodule:: bpy.types

base classes --- :class:`bpy_struct`, :class:`FileSelectParams`

.. class:: FileAssetSelectParams(FileSelectParams)

   Settings for the file selection in Asset Browser mode

   .. attribute:: asset_library_reference

      (default ``'ALL'``)

      - ``ALL``
        All Libraries -- Show assets from all of the listed asset libraries.
      - ``LOCAL``
        Current File -- Show the assets currently available in this Blender session.
      - ``ESSENTIALS``
        Essentials -- Show the basic building blocks and utilities coming with Blender.
      - ``CUSTOM``
        Custom -- Show assets from the asset libraries configured in the Preferences.

      :type: Literal['ALL', 'LOCAL', 'ESSENTIALS', 'CUSTOM']

   .. attribute:: catalog_id

      The UUID of the catalog shown in the browser (default "", never None)

      :type: str

   .. data:: filter_asset_id

      Which asset types to show/hide, when browsing an asset library (readonly, never None)

      :type: :class:`FileAssetSelectIDFilter`

   .. attribute:: import_method

      Determine how the asset will be imported (default ``'LINK'``)

      - ``FOLLOW_PREFS``
        Follow Preferences -- Use the import method set in the Preferences for this asset library, don't override it for this Asset Browser.
      - ``LINK``
        Link -- Import the assets as linked data-block.
      - ``APPEND``
        Append -- Import the asset as copied data-block, with no link to the original asset data-block.
      - ``APPEND_REUSE``
        Append (Reuse Data) -- Import the asset as copied data-block while avoiding multiple copies of nested, typically heavy data. For example the textures of a material asset, or the mesh of an object asset, don't have to be copied every time this asset is imported. The instances of the asset share the data instead.
      - ``PACK``
        Pack -- Import the asset as linked data-block, and pack it in the current file (ensures that it remains unchanged in case the library data is modified, is not available anymore, etc.).

      :type: Literal['FOLLOW_PREFS', 'LINK', 'APPEND', 'APPEND_REUSE', 'PACK']

   .. attribute:: instance_collections_on_append

      Create instances for collections when appending, rather than adding them directly to the scene (default False)

      :type: bool

   .. attribute:: instance_collections_on_link

      Create instances for collections when linking, rather than adding them directly to the scene (default False)

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
   - :class:`FileSelectParams.title`
   - :class:`FileSelectParams.directory`
   - :class:`FileSelectParams.filename`
   - :class:`FileSelectParams.use_library_browsing`
   - :class:`FileSelectParams.display_type`
   - :class:`FileSelectParams.recursion_level`
   - :class:`FileSelectParams.show_details_size`
   - :class:`FileSelectParams.show_details_datetime`
   - :class:`FileSelectParams.use_filter`
   - :class:`FileSelectParams.show_hidden`
   - :class:`FileSelectParams.sort_method`
   - :class:`FileSelectParams.use_sort_invert`
   - :class:`FileSelectParams.use_filter_image`
   - :class:`FileSelectParams.use_filter_blender`
   - :class:`FileSelectParams.use_filter_backup`
   - :class:`FileSelectParams.use_filter_movie`
   - :class:`FileSelectParams.use_filter_script`
   - :class:`FileSelectParams.use_filter_font`
   - :class:`FileSelectParams.use_filter_sound`
   - :class:`FileSelectParams.use_filter_text`
   - :class:`FileSelectParams.use_filter_volume`
   - :class:`FileSelectParams.use_filter_folder`
   - :class:`FileSelectParams.use_filter_blendid`
   - :class:`FileSelectParams.use_filter_asset_only`
   - :class:`FileSelectParams.filter_id`
   - :class:`FileSelectParams.filter_glob`
   - :class:`FileSelectParams.filter_search`
   - :class:`FileSelectParams.display_size`
   - :class:`FileSelectParams.display_size_discrete`
   - :class:`FileSelectParams.list_display_size`
   - :class:`FileSelectParams.list_column_size`

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
   - :class:`FileSelectParams.bl_rna_get_subclass`
   - :class:`FileSelectParams.bl_rna_get_subclass_py`

