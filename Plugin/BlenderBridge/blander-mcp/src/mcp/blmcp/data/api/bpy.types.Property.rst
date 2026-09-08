Property(bpy_struct)
====================

.. currentmodule:: bpy.types

base class --- :class:`bpy_struct`

subclasses --- 
:class:`BoolProperty`, :class:`CollectionProperty`, :class:`EnumProperty`, :class:`FloatProperty`, :class:`IntProperty`, :class:`PointerProperty`, :class:`StringProperty`

.. class:: Property(bpy_struct)

   RNA property definition

   .. data:: deprecated_note

      A note regarding deprecation (default "", readonly, never None)

      :type: str

   .. data:: deprecated_removal_version

      The Blender version this is expected to be removed (array of 3 items, in [-inf, inf], default (0, 0, 0), readonly)

      :type: :class:`bpy_prop_array`\ [int]

   .. data:: deprecated_version

      The Blender version this was deprecated (array of 3 items, in [-inf, inf], default (0, 0, 0), readonly)

      :type: :class:`bpy_prop_array`\ [int]

   .. data:: description

      Description of the property for tooltips (default "", readonly, never None)

      :type: str

   .. data:: icon

      Icon of the item (default ``'NONE'``, readonly)

      :type: Literal[:ref:`rna_enum_icon_items`]

   .. data:: identifier

      Unique name used in the code and scripting (default "", readonly, never None)

      :type: str

   .. data:: is_animatable

      Property is animatable through RNA (default False, readonly)

      :type: bool

   .. data:: is_argument_optional

      True when the property is optional in a Python function implementing an RNA function (default False, readonly)

      :type: bool

   .. data:: is_deprecated

      The property is deprecated (default False, readonly)

      :type: bool

   .. data:: is_enum_flag

      True when multiple enums (default False, readonly)

      :type: bool

   .. data:: is_hidden

      True when the property is hidden (default False, readonly)

      :type: bool

   .. data:: is_library_editable

      Property is editable from linked instances (changes not saved) (default False, readonly)

      :type: bool

   .. data:: is_never_none

      True when this value cannot be set to None (default False, readonly)

      :type: bool

   .. data:: is_output

      True when this property is an output value from an RNA function (default False, readonly)

      :type: bool

   .. data:: is_overridable

      Property is overridable through RNA (default False, readonly)

      :type: bool

   .. data:: is_path_output

      Property is a filename, filepath or directory output (default False, readonly)

      :type: bool

   .. data:: is_path_supports_blend_relative

      Property is a path which supports the "//" prefix, signifying the location as relative to the ".blend" file's directory (default False, readonly)

      :type: bool

   .. data:: is_path_supports_templates

      Property is a path which supports the "{variable_name}" variable expression syntax, which substitutes the value of the referenced variable in place of the expression (default False, readonly)

      :type: bool

   .. data:: is_readonly

      Property is editable through RNA (default False, readonly)

      :type: bool

   .. data:: is_registered

      Property is registered as part of type registration (default False, readonly)

      :type: bool

   .. data:: is_registered_optional

      Property is optionally registered as part of type registration (default False, readonly)

      :type: bool

   .. data:: is_required

      False when this property is an optional argument in an RNA function (default False, readonly)

      :type: bool

   .. data:: is_runtime

      Property has been dynamically created at runtime (default False, readonly)

      :type: bool

   .. data:: is_skip_preset

      True when the property is not saved in presets (default False, readonly)

      :type: bool

   .. data:: is_skip_save

      True when the property uses ghost values (default False, readonly)

      :type: bool

   .. data:: name

      Human readable name (default "", readonly, never None)

      :type: str

   .. data:: srna

      Struct definition used for properties assigned to this item (readonly)

      :type: :class:`Struct` | None

   .. data:: subtype

      Semantic interpretation of the property (default ``'NONE'``, readonly)

      :type: Literal[:ref:`rna_enum_property_subtype_items`]

   .. data:: tags

      Subset of tags (defined in parent struct) that are set for this property (default set(), readonly)

      :type: set[str]

   .. data:: translation_context

      Translation context of the property's name (default "", readonly, never None)

      :type: str

   .. data:: type

      Data type of the property (default ``'BOOLEAN'``, readonly)

      :type: Literal[:ref:`rna_enum_property_type_items`]

   .. data:: unit

      Type of units for this property (default ``'NONE'``, readonly)

      :type: Literal[:ref:`rna_enum_property_unit_items`]

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

   - :mod:`bpy.context.texture_user_property`
   - :class:`Function.parameters`
   - :class:`Struct.properties`

