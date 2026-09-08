Struct(bpy_struct)
==================

.. currentmodule:: bpy.types

base class --- :class:`bpy_struct`

.. class:: Struct(bpy_struct)

   RNA structure definition

   .. data:: base

      Struct definition this is derived from (readonly)

      :type: :class:`Struct` | None

   .. data:: description

      Description of the Struct's purpose (default "", readonly, never None)

      :type: str

   .. data:: functions

      (default None, readonly)

      :type: :class:`bpy_prop_collection`\ [:class:`Function`]

   .. data:: identifier

      Unique name used in the code and scripting (default "", readonly, never None)

      :type: str

   .. data:: name

      Human readable name (default "", readonly, never None)

      :type: str

   .. data:: name_property

      Property that gives the name of the struct (readonly)

      :type: :class:`StringProperty` | None

   .. data:: nested

      Struct in which this struct is always nested, and to which it logically belongs (readonly)

      :type: :class:`Struct` | None

   .. data:: properties

      Properties in the struct (default None, readonly)

      :type: :class:`bpy_prop_collection`\ [:class:`Property`]

   .. data:: property_tags

      Tags that properties can use to influence behavior (default None, readonly)

      :type: :class:`bpy_prop_collection`\ [:class:`EnumPropertyItem`]

   .. data:: translation_context

      Translation context of the struct's name (default "", readonly, never None)

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

   - :class:`BlenderRNA.structs`
   - :class:`CollectionProperty.fixed_type`
   - :class:`PointerProperty.fixed_type`
   - :class:`Property.srna`
   - :class:`Struct.base`
   - :class:`Struct.nested`

