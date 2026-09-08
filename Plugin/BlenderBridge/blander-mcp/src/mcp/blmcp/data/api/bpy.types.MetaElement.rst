MetaElement(bpy_struct)
=======================

.. currentmodule:: bpy.types

base class --- :class:`bpy_struct`

.. class:: MetaElement(bpy_struct)

   Blobby element in a metaball data-block

   .. attribute:: co

      (array of 3 items, in [-inf, inf], default (0.0, 0.0, 0.0))

      :type: :class:`mathutils.Vector`

   .. attribute:: hide

      Hide element (default False)

      :type: bool

   .. attribute:: radius

      (in [0, inf], default 0.0)

      :type: float

   .. attribute:: rotation

      Normalized quaternion rotation (array of 4 items, in [-inf, inf], default (0.0, 0.0, 0.0, 0.0))

      :type: :class:`mathutils.Quaternion`

   .. attribute:: select

      Select element (default False)

      :type: bool

   .. attribute:: size_x

      Size of element, use of components depends on element type (in [0, 20], default 0.0)

      :type: float

   .. attribute:: size_y

      Size of element, use of components depends on element type (in [0, 20], default 0.0)

      :type: float

   .. attribute:: size_z

      Size of element, use of components depends on element type (in [0, 20], default 0.0)

      :type: float

   .. attribute:: stiffness

      Stiffness defines how much of the element to fill (in [0, 10], default 0.0)

      :type: float

   .. attribute:: type

      Metaball type (default ``'BALL'``)

      :type: Literal[:ref:`rna_enum_metaelem_type_items`]

   .. attribute:: use_negative

      Set metaball as negative one (default False)

      :type: bool

   .. attribute:: use_scale_stiffness

      Scale stiffness instead of radius (default True)

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

   - :class:`MetaBall.elements`
   - :class:`MetaBallElements.active`
   - :class:`MetaBallElements.new`
   - :class:`MetaBallElements.remove`

