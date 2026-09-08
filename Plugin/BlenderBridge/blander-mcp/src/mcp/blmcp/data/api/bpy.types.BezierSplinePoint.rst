BezierSplinePoint(bpy_struct)
=============================

.. currentmodule:: bpy.types

base class --- :class:`bpy_struct`

.. class:: BezierSplinePoint(bpy_struct)

   Bézier curve point with two handles

   .. attribute:: co

      Coordinates of the control point (array of 3 items, in [-inf, inf], default (0.0, 0.0, 0.0))

      :type: :class:`mathutils.Vector`

   .. attribute:: handle_left

      Coordinates of the first handle (array of 3 items, in [-inf, inf], default (0.0, 0.0, 0.0))

      :type: :class:`mathutils.Vector`

   .. attribute:: handle_left_type

      Handle types (default ``'FREE'``)

      :type: Literal['FREE', 'VECTOR', 'ALIGNED', 'AUTO']

   .. attribute:: handle_right

      Coordinates of the second handle (array of 3 items, in [-inf, inf], default (0.0, 0.0, 0.0))

      :type: :class:`mathutils.Vector`

   .. attribute:: handle_right_type

      Handle types (default ``'FREE'``)

      :type: Literal['FREE', 'VECTOR', 'ALIGNED', 'AUTO']

   .. attribute:: hide

      Visibility status (default False)

      :type: bool

   .. attribute:: radius

      Radius for beveling (in [0, inf], default 0.0)

      :type: float

   .. attribute:: select_control_point

      Control point selection status (default False)

      :type: bool

   .. attribute:: select_left_handle

      Handle 1 selection status (default False)

      :type: bool

   .. attribute:: select_right_handle

      Handle 2 selection status (default False)

      :type: bool

   .. attribute:: tilt

      Tilt in 3D View (in [-376.991, 376.991], default 0.0)

      :type: float

   .. attribute:: weight_softbody

      Softbody goal weight (in [0.01, 100], default 0.0)

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

   - :class:`Spline.bezier_points`

