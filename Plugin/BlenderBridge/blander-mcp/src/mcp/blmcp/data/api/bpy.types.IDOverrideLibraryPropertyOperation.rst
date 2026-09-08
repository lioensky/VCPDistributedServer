IDOverrideLibraryPropertyOperation(bpy_struct)
==============================================

.. currentmodule:: bpy.types

base class --- :class:`bpy_struct`

.. class:: IDOverrideLibraryPropertyOperation(bpy_struct)

   Description of an override operation over an overridden property

   .. data:: flag

      Status flags (default set(), readonly)

      - ``MANDATORY``
        Mandatory -- For templates, prevents the user from removing predefined operation (NOT USED).
      - ``LOCKED``
        Locked -- Prevents the user from modifying that override operation (NOT USED).
      - ``IDPOINTER_MATCH_REFERENCE``
        Match Reference -- The ID pointer overridden by this operation is expected to match the reference hierarchy.
      - ``IDPOINTER_ITEM_USE_ID``
        ID Item Use ID Pointer -- RNA collections of IDs only, the reference to the item also uses the ID pointer itself, not only its name.

      :type: set[Literal['MANDATORY', 'LOCKED', 'IDPOINTER_MATCH_REFERENCE', 'IDPOINTER_ITEM_USE_ID']]

   .. data:: operation

      What override operation is performed (default ``'REPLACE'``, readonly)

      - ``NOOP``
        No-Op -- Does nothing, prevents adding actual overrides (NOT USED).
      - ``REPLACE``
        Replace -- Replace value of reference by overriding one.
      - ``DIFF_ADD``
        Differential -- Stores and apply difference between reference and local value (NOT USED).
      - ``DIFF_SUB``
        Differential -- Stores and apply difference between reference and local value (NOT USED).
      - ``FACT_MULTIPLY``
        Factor -- Stores and apply multiplication factor between reference and local value (NOT USED).
      - ``INSERT_AFTER``
        Insert After -- Insert a new item into collection after the one referenced in subitem_reference_name/_id or _index.
      - ``INSERT_BEFORE``
        Insert Before -- Insert a new item into collection before the one referenced in subitem_reference_name/_id or _index (NOT USED).

      :type: Literal['NOOP', 'REPLACE', 'DIFF_ADD', 'DIFF_SUB', 'FACT_MULTIPLY', 'INSERT_AFTER', 'INSERT_BEFORE']

   .. data:: subitem_local_id

      Collection of IDs only, used to disambiguate between potential IDs with same name from different libraries (readonly)

      :type: :class:`ID` | None

   .. data:: subitem_local_index

      Used to handle changes into collection (in [-1, inf], default -1, readonly)

      :type: int

   .. data:: subitem_local_name

      Used to handle changes into collection (default "", readonly, never None)

      :type: str

   .. data:: subitem_reference_id

      Collection of IDs only, used to disambiguate between potential IDs with same name from different libraries (readonly)

      :type: :class:`ID` | None

   .. data:: subitem_reference_index

      Used to handle changes into collection (in [-1, inf], default -1, readonly)

      :type: int

   .. data:: subitem_reference_name

      Used to handle changes into collection (default "", readonly, never None)

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

   - :class:`IDOverrideLibraryProperty.operations`
   - :class:`IDOverrideLibraryPropertyOperations.add`
   - :class:`IDOverrideLibraryPropertyOperations.remove`

