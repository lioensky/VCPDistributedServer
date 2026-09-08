FollowPathConstraint(Constraint)
================================

.. currentmodule:: bpy.types

base classes --- :class:`bpy_struct`, :class:`Constraint`

.. class:: FollowPathConstraint(Constraint)

   Lock motion to the target path

   .. attribute:: forward_axis

      Axis that points forward along the path (default ``'FORWARD_X'``)

      :type: Literal['FORWARD_X', 'FORWARD_Y', 'FORWARD_Z', 'TRACK_NEGATIVE_X', 'TRACK_NEGATIVE_Y', 'TRACK_NEGATIVE_Z']

   .. attribute:: offset

      Offset from the position corresponding to the time frame (in [-1.04857e+06, 1.04857e+06], default 0.0)

      :type: float

   .. attribute:: offset_factor

      Percentage value defining target position along length of curve (in [-inf, inf], default 0.0)

      :type: float

   .. attribute:: target

      Target Curve object

      :type: :class:`Object` | None

   .. attribute:: up_axis

      Axis that points upward (default ``'UP_X'``)

      :type: Literal['UP_X', 'UP_Y', 'UP_Z']

   .. attribute:: use_curve_follow

      Object will follow the heading and banking of the curve (default False)

      :type: bool

   .. attribute:: use_curve_radius

      Object is scaled by the curve radius (default False)

      :type: bool

   .. attribute:: use_fixed_location

      Object will stay locked to a single point somewhere along the length of the curve regardless of time (default False)

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
   - :class:`Constraint.name`
   - :class:`Constraint.type`
   - :class:`Constraint.is_override_data`
   - :class:`Constraint.owner_space`
   - :class:`Constraint.target_space`
   - :class:`Constraint.space_object`
   - :class:`Constraint.space_subtarget`
   - :class:`Constraint.mute`
   - :class:`Constraint.enabled`
   - :class:`Constraint.show_expanded`
   - :class:`Constraint.is_valid`
   - :class:`Constraint.active`
   - :class:`Constraint.influence`
   - :class:`Constraint.error_location`
   - :class:`Constraint.error_rotation`

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
   - :class:`Constraint.bl_rna_get_subclass`
   - :class:`Constraint.bl_rna_get_subclass_py`

