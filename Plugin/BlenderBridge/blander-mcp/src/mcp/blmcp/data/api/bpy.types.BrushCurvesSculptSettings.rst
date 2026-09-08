BrushCurvesSculptSettings(bpy_struct)
=====================================

.. currentmodule:: bpy.types

base class --- :class:`bpy_struct`

.. class:: BrushCurvesSculptSettings(bpy_struct)


   .. attribute:: add_amount

      Number of curves added by the Add brush (in [1, inf], default 0)

      :type: int

   .. attribute:: curve_length

      Length of newly added curves when it is not interpolated from other curves (in [0, inf], default 0.0)

      :type: float

   .. data:: curve_parameter_falloff

      Falloff that is applied from the tip to the root of each curve (readonly)

      :type: :class:`CurveMapping` | None

   .. attribute:: curve_radius

      Radius of newly added curves when it is not interpolated from other curves (in [0, inf], default 0.01)

      :type: float

   .. attribute:: density_add_attempts

      How many times the Density brush tries to add a new curve (in [0, inf], default 0)

      :type: int

   .. attribute:: density_mode

      Determines whether the brush adds or removes curves (default ``'AUTO'``)

      - ``AUTO``
        Auto -- Either add or remove curves depending on the minimum distance of the curves under the cursor.
      - ``ADD``
        Add -- Add new curves between existing curves, taking the minimum distance into account.
      - ``REMOVE``
        Remove -- Remove curves whose root points are too close.

      :type: Literal['AUTO', 'ADD', 'REMOVE']

   .. attribute:: minimum_distance

      Goal distance between curve roots for the Density brush (in [0, inf], default 0.0)

      :type: float

   .. attribute:: minimum_length

      Avoid shrinking curves shorter than this length (in [0, inf], default 0.0)

      :type: float

   .. attribute:: points_per_curve

      Number of control points in a newly added curve (in [2, inf], default 0)

      :type: int

   .. attribute:: use_length_interpolate

      Use length of the curves in close proximity (default False)

      :type: bool

   .. attribute:: use_point_count_interpolate

      Use the number of points from the curves in close proximity (default False)

      :type: bool

   .. attribute:: use_radius_interpolate

      Use radius of the curves in close proximity (default True)

      :type: bool

   .. attribute:: use_shape_interpolate

      Use shape of the curves in close proximity (default False)

      :type: bool

   .. attribute:: use_uniform_scale

      Grow or shrink curves by changing their size uniformly instead of using trimming or extrapolation (default False)

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

   - :class:`Brush.curves_sculpt_settings`

