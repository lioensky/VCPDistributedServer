Keyframe(bpy_struct)
====================

.. currentmodule:: bpy.types

base class --- :class:`bpy_struct`

.. class:: Keyframe(bpy_struct)

   Bézier curve point with two handles defining a Keyframe on an F-Curve

   .. attribute:: amplitude

      Amount to boost elastic bounces for 'elastic' easing (in [0, inf], default 0.0)

      :type: float

   .. attribute:: back

      Amount of overshoot for 'back' easing (in [-inf, inf], default 0.0)

      :type: float

   .. attribute:: co

      Coordinates of the control point (array of 2 items, in [-inf, inf], default (0.0, 0.0))

      :type: :class:`mathutils.Vector`

   .. attribute:: co_ui

      Coordinates of the control point. Note: Changing this value also updates the handles similar to using the graph editor transform operator (array of 2 items, in [-inf, inf], default (0.0, 0.0))

      :type: :class:`mathutils.Vector`

   .. attribute:: easing

      Which ends of the segment between this and the next keyframe easing interpolation is applied to (default ``'AUTO'``)

      :type: Literal[:ref:`rna_enum_beztriple_interpolation_easing_items`]

   .. attribute:: handle_left

      Coordinates of the left handle (before the control point) (array of 2 items, in [-inf, inf], default (0.0, 0.0))

      :type: :class:`mathutils.Vector`

   .. attribute:: handle_left_type

      Handle types (default ``'FREE'``)

      :type: Literal[:ref:`rna_enum_keyframe_handle_type_items`]

   .. attribute:: handle_right

      Coordinates of the right handle (after the control point) (array of 2 items, in [-inf, inf], default (0.0, 0.0))

      :type: :class:`mathutils.Vector`

   .. attribute:: handle_right_type

      Handle types (default ``'FREE'``)

      :type: Literal[:ref:`rna_enum_keyframe_handle_type_items`]

   .. attribute:: interpolation

      Interpolation method to use for segment of the F-Curve from this Keyframe until the next Keyframe (default ``'CONSTANT'``)

      :type: Literal[:ref:`rna_enum_beztriple_interpolation_mode_items`]

   .. attribute:: period

      Time between bounces for elastic easing (in [-inf, inf], default 0.0)

      :type: float

   .. attribute:: select_control_point

      Control point selection status (default False)

      :type: bool

   .. attribute:: select_left_handle

      Left handle selection status (default False)

      :type: bool

   .. attribute:: select_right_handle

      Right handle selection status (default False)

      :type: bool

   .. attribute:: type

      Type of keyframe (for visual purposes only) (default ``'KEYFRAME'``)

      :type: Literal[:ref:`rna_enum_beztriple_keyframe_type_items`]

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

   - :mod:`bpy.context.selected_editable_keyframes`
   - :class:`FCurve.keyframe_points`
   - :class:`FCurveKeyframePoints.insert`
   - :class:`FCurveKeyframePoints.remove`

