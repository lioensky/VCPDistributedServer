BlendImportContextItem(bpy_struct)
==================================

.. currentmodule:: bpy.types

base class --- :class:`bpy_struct`

.. class:: BlendImportContextItem(bpy_struct)

   An item (representing a data-block) in a BlendImportContext data. Currently only exposed as read-only data for the pre/post linking handlers

   .. data:: append_action

      How this item has been handled by the append operation. Only set if the data has been appended (default ``'UNSET'``, readonly)

      - ``UNSET``
        Not yet defined.
      - ``KEEP_LINKED``
        ID has been kept linked.
      - ``REUSE_LOCAL``
        An existing matching local ID has been re-used.
      - ``MAKE_LOCAL``
        The newly linked ID has been made local.
      - ``COPY_LOCAL``
        The linked ID had other unrelated usages, so it has been duplicated into a local copy.

      :type: Literal['UNSET', 'KEEP_LINKED', 'REUSE_LOCAL', 'MAKE_LOCAL', 'COPY_LOCAL']

   .. data:: id

      The imported ID. None until it has been linked or appended. May be the same as ``reusable_local_id`` when appended (readonly)

      :type: :class:`ID` | None

   .. data:: id_type

      ID type of the item (default ``'ACTION'``, readonly)

      :type: Literal[:ref:`rna_enum_id_type_items`]

   .. data:: import_info

      Various status info about an item after it has been imported (default set(), readonly)

      - ``INDIRECT_USAGE``
        That item was added for an indirectly imported ID, as a dependency of another data-block.
      - ``LIBOVERRIDE_DEPENDENCY``
        That item represents an ID also used as liboverride dependency (either directly, as a liboverride reference, or indirectly, as data used by a liboverride reference). It should never be directly made local. Mutually exclusive with \`LIBOVERRIDE_DEPENDENCY_ONLY\`.
      - ``LIBOVERRIDE_DEPENDENCY_ONLY``
        That item represents an ID only used as liboverride dependency (either directly or indirectly, see \`LIBOVERRIDE_DEPENDENCY\` for precisions). It should not be considered during the 'make local' (append) process, and remain purely linked data. Mutually exclusive with \`LIBOVERRIDE_DEPENDENCY\`.

      :type: set[Literal['INDIRECT_USAGE', 'LIBOVERRIDE_DEPENDENCY', 'LIBOVERRIDE_DEPENDENCY_ONLY']]

   .. data:: library_override_id

      The library override of the linked ID. None until it has been created (readonly)

      :type: :class:`ID` | None

   .. data:: name

      ID name of the item (default "", readonly, never None)

      :type: str

   .. data:: reusable_local_id

      The already existing local ID that may be reused in append & reuse case. None until it has been found (readonly)

      :type: :class:`ID` | None

   .. data:: source_libraries

      List of libraries to search and import that ID from. The ID will be imported from the first file in that list that contains it (default None, readonly)

      :type: :class:`BlendImportContextLibraries`\ [:class:`BlendImportContextLibrary`]

   .. data:: source_library

      Library ID representing the blendfile from which the ID was imported. None until the ID has been linked or appended (readonly)

      :type: :class:`Library` | None

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

   - :class:`BlendImportContext.import_items`

