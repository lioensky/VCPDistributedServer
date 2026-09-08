MaskSplinePoint(bpy_struct)
===========================

.. currentmodule:: bpy.types

base class --- :class:`bpy_struct`

.. class:: MaskSplinePoint(bpy_struct)

   Single point in spline used for defining mask

   .. attribute:: co

      Coordinates of the control point (array of 2 items, in [-inf, inf], default (0.0, 0.0))

      :type: :class:`mathutils.Vector`

   .. data:: feather_points

      Points defining feather (default None, readonly)

      :type: :class:`bpy_prop_collection`\ [:class:`MaskSplinePointUW`]

   .. attribute:: handle_left

      Coordinates of the first handle (array of 2 items, in [-inf, inf], default (0.0, 0.0))

      :type: :class:`mathutils.Vector`

   .. attribute:: handle_left_type

      Handle type (default ``'FREE'``)

      :type: Literal['AUTO', 'VECTOR', 'ALIGNED', 'ALIGNED_DOUBLESIDE', 'FREE']

   .. attribute:: handle_right

      Coordinates of the second handle (array of 2 items, in [-inf, inf], default (0.0, 0.0))

      :type: :class:`mathutils.Vector`

   .. attribute:: handle_right_type

      Handle type (default ``'FREE'``)

      :type: Literal['AUTO', 'VECTOR', 'ALIGNED', 'ALIGNED_DOUBLESIDE', 'FREE']

   .. attribute:: handle_type

      Handle type (default ``'FREE'``)

      :type: Literal['AUTO', 'VECTOR', 'ALIGNED', 'ALIGNED_DOUBLESIDE', 'FREE']

   .. data:: parent

      (readonly)

      :type: :class:`MaskParent` | None

   .. attribute:: select

      Selection status of the control point. (Deprecated: use Select Control Point instead) (default False)

      :type: bool

   .. attribute:: select_control_point

      Selection status of the control point (default False)

      :type: bool

   .. attribute:: select_left_handle

      Selection status of the left handle (default False)

      :type: bool

   .. attribute:: select_right_handle

      Selection status of the right handle (default False)

      :type: bool

   .. attribute:: select_single_handle

      Selection status of the Aligned Single handle (default False)

      :type: bool

   .. attribute:: weight

      Weight of the point (in [0, 1], default 0.0)

      :type: float

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

   - :class:`MaskSpline.points`
   - :class:`MaskSplinePoints.remove`
   - :class:`MaskSplines.active_point`

