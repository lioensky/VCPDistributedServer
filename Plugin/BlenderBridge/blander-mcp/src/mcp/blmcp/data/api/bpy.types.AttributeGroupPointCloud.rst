AttributeGroupPointCloud(bpy_prop_collection)
=============================================

.. currentmodule:: bpy.types

base classes --- :class:`bpy_prop`, :class:`bpy_prop_collection`

.. class:: AttributeGroupPointCloud(bpy_prop_collection)

   Group of geometry attributes

   .. attribute:: active

      Active attribute

      :type: :class:`Attribute` | None

   .. attribute:: active_index

      Active attribute index or -1 when none are active (in [-1, inf], default 0)

      :type: int

   .. method:: new(name, type, domain)

      Add attribute to geometry

      :param name: Name, Name of geometry attribute (never None)
      :type name: str
      :param type: Type, Attribute type
      :type type: Literal[:ref:`rna_enum_attribute_type_items`]
      :param domain: Domain, Type of element that attribute is stored on
      :type domain: Literal[:ref:`rna_enum_attribute_domain_items`]
      :return: New geometry attribute
      :rtype: :class:`Attribute`

   .. method:: remove(attribute)

      Remove attribute from geometry

      :param attribute: Geometry Attribute (never None)
      :type attribute: :class:`Attribute` | None

   .. method:: domain_size(domain)

      Get the size of a given domain

      :param domain: Domain, Type of element that attribute is stored on
      :type domain: Literal[:ref:`rna_enum_attribute_domain_items`]
      :return: Size, Size of the domain (in [0, inf])
      :rtype: int

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

   - :class:`PointCloud.attributes`
   - :class:`PointCloud.color_attributes`

