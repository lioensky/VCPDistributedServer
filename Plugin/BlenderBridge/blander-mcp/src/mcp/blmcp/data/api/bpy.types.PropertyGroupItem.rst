PropertyGroupItem(bpy_struct)
=============================

.. currentmodule:: bpy.types

base class --- :class:`bpy_struct`

.. class:: PropertyGroupItem(bpy_struct)

   Property that stores arbitrary, user defined properties

   .. attribute:: bool

      (default False)

      :type: bool

   .. attribute:: bool_array

      (array of 1 items, default (False,))

      :type: :class:`bpy_prop_array`\ [bool]

   .. data:: collection

      (default None, readonly)

      :type: :class:`bpy_prop_collection`\ [:class:`PropertyGroup`]

   .. attribute:: double

      (in [-inf, inf], default 0.0)

      :type: float

   .. attribute:: double_array

      (array of 1 items, in [-inf, inf], default (0.0,))

      :type: :class:`bpy_prop_array`\ [float]

   .. attribute:: enum

      (default ``'DEFAULT'``)

      :type: Literal['DEFAULT']

   .. attribute:: float

      (in [-inf, inf], default 0.0)

      :type: float

   .. attribute:: float_array

      (array of 1 items, in [-inf, inf], default (0.0,))

      :type: :class:`bpy_prop_array`\ [float]

   .. data:: group

      (readonly)

      :type: :class:`PropertyGroup` | None

   .. attribute:: id

      :type: :class:`ID` | None

   .. data:: idp_array

      (default None, readonly)

      :type: :class:`bpy_prop_collection`\ [:class:`PropertyGroup`]

   .. attribute:: int

      (in [-inf, inf], default 0)

      :type: int

   .. attribute:: int_array

      (array of 1 items, in [-inf, inf], default (0,))

      :type: :class:`bpy_prop_array`\ [int]

   .. attribute:: string

      (default "", never None)

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

