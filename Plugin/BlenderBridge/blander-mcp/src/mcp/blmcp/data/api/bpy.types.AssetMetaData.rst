AssetMetaData(bpy_struct)
=========================

.. currentmodule:: bpy.types

base class --- :class:`bpy_struct`

.. class:: AssetMetaData(bpy_struct)

   Additional data stored for an asset data-block

   .. attribute:: active_tag

      Index of the tag set for editing (in [-32768, 32767], default 0)

      :type: int

   .. attribute:: author

      Name of the creator of the asset (default "", never None)

      :type: str

   .. attribute:: catalog_id

      Identifier for the asset's catalog, used by Blender to look up the asset's catalog path. Must be a UUID according to RFC4122. (default "", never None)

      :type: str

   .. data:: catalog_simple_name

      Simple name of the asset's catalog, for debugging and data recovery purposes (default "", readonly, never None)

      :type: str

   .. attribute:: copyright

      Copyright notice for this asset. An empty copyright notice does not necessarily indicate that this is copyright-free. Contact the author if any clarification is needed. (default "", never None)

      :type: str

   .. attribute:: description

      A description of the asset to be displayed for the user (default "", never None)

      :type: str

   .. attribute:: license

      The type of license this asset is distributed under. An empty license name does not necessarily indicate that this is free of licensing terms. Contact the author if any clarification is needed. (default "", never None)

      :type: str

   .. data:: tags

      Custom tags (name tokens) for the asset, used for filtering and general asset management (default None, readonly)

      :type: :class:`AssetTags`\ [:class:`AssetTag`]

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

   - :class:`AssetRepresentation.metadata`
   - :class:`FileSelectEntry.asset_data`
   - :class:`ID.asset_data`

