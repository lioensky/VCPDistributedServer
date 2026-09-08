AssetRepresentation(bpy_struct)
===============================

.. currentmodule:: bpy.types

base class --- :class:`bpy_struct`

.. class:: AssetRepresentation(bpy_struct)

   Information about an entity that makes it possible for the asset system to deal with the entity as asset

   .. data:: full_library_path

      Absolute path to the .blend file containing this asset (default "", readonly, never None)

      :type: str

   .. data:: full_path

      Absolute path to the .blend file containing this asset extended with the path of the asset inside the file (default "", readonly, never None)

      :type: str

   .. data:: id_type

      The type of the data-block, if the asset represents one ('NONE' otherwise) (default ``'ACTION'``, readonly)

      :type: Literal[:ref:`rna_enum_id_type_items`]

   .. data:: local_id

      The local data-block this asset represents; only valid if that is a data-block in this file (readonly)

      :type: :class:`ID` | None

   .. data:: metadata

      Additional information about the asset (readonly)

      :type: :class:`AssetMetaData` | None

   .. data:: name

      (default "", readonly, never None)

      :type: str

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

   - :mod:`bpy.context.asset`
   - :mod:`bpy.context.selected_assets`
   - :class:`AssetShelf.asset_poll`
   - :class:`AssetShelf.draw_context_menu`
   - :class:`Context.asset`

