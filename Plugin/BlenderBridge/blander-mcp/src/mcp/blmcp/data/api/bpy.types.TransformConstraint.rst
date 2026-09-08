TransformConstraint(Constraint)
===============================

.. currentmodule:: bpy.types

base classes --- :class:`bpy_struct`, :class:`Constraint`

.. class:: TransformConstraint(Constraint)

   Map transformations of the target to the object

   .. attribute:: from_max_x

      Top range of X axis source motion (in [-inf, inf], default 0.0)

      :type: float

   .. attribute:: from_max_x_rot

      Top range of X axis source motion (in [-inf, inf], default 0.0)

      :type: float

   .. attribute:: from_max_x_scale

      Top range of X axis source motion (in [-inf, inf], default 0.0)

      :type: float

   .. attribute:: from_max_y

      Top range of Y axis source motion (in [-inf, inf], default 0.0)

      :type: float

   .. attribute:: from_max_y_rot

      Top range of Y axis source motion (in [-inf, inf], default 0.0)

      :type: float

   .. attribute:: from_max_y_scale

      Top range of Y axis source motion (in [-inf, inf], default 0.0)

      :type: float

   .. attribute:: from_max_z

      Top range of Z axis source motion (in [-inf, inf], default 0.0)

      :type: float

   .. attribute:: from_max_z_rot

      Top range of Z axis source motion (in [-inf, inf], default 0.0)

      :type: float

   .. attribute:: from_max_z_scale

      Top range of Z axis source motion (in [-inf, inf], default 0.0)

      :type: float

   .. attribute:: from_min_x

      Bottom range of X axis source motion (in [-inf, inf], default 0.0)

      :type: float

   .. attribute:: from_min_x_rot

      Bottom range of X axis source motion (in [-inf, inf], default 0.0)

      :type: float

   .. attribute:: from_min_x_scale

      Bottom range of X axis source motion (in [-inf, inf], default 0.0)

      :type: float

   .. attribute:: from_min_y

      Bottom range of Y axis source motion (in [-inf, inf], default 0.0)

      :type: float

   .. attribute:: from_min_y_rot

      Bottom range of Y axis source motion (in [-inf, inf], default 0.0)

      :type: float

   .. attribute:: from_min_y_scale

      Bottom range of Y axis source motion (in [-inf, inf], default 0.0)

      :type: float

   .. attribute:: from_min_z

      Bottom range of Z axis source motion (in [-inf, inf], default 0.0)

      :type: float

   .. attribute:: from_min_z_rot

      Bottom range of Z axis source motion (in [-inf, inf], default 0.0)

      :type: float

   .. attribute:: from_min_z_scale

      Bottom range of Z axis source motion (in [-inf, inf], default 0.0)

      :type: float

   .. attribute:: from_rotation_mode

      Specify the type of rotation channels to use (default ``'AUTO'``)

      :type: Literal[:ref:`rna_enum_driver_target_rotation_mode_items`]

   .. attribute:: map_from

      The transformation type to use from the target (default ``'LOCATION'``)

      :type: Literal['LOCATION', 'ROTATION', 'SCALE']

   .. attribute:: map_to

      The transformation type to affect on the constrained object (default ``'LOCATION'``)

      :type: Literal['LOCATION', 'ROTATION', 'SCALE']

   .. attribute:: map_to_x_from

      The source axis constrained object's X axis uses (default ``'X'``)

      :type: Literal[:ref:`rna_enum_axis_xyz_items`]

   .. attribute:: map_to_y_from

      The source axis constrained object's Y axis uses (default ``'X'``)

      :type: Literal[:ref:`rna_enum_axis_xyz_items`]

   .. attribute:: map_to_z_from

      The source axis constrained object's Z axis uses (default ``'X'``)

      :type: Literal[:ref:`rna_enum_axis_xyz_items`]

   .. attribute:: mix_mode

      Specify how to combine the new location with original (default ``'ADD'``)

      - ``REPLACE``
        Replace -- Replace component values.
      - ``ADD``
        Add -- Add component values together.

      :type: Literal['REPLACE', 'ADD']

   .. attribute:: mix_mode_rot

      Specify how to combine the new rotation with original (default ``'ADD'``)

      - ``REPLACE``
        Replace -- Replace component values.
      - ``ADD``
        Add -- Add component values together.
      - ``BEFORE``
        Before Original -- Apply new rotation before original, as if it was on a parent.
      - ``AFTER``
        After Original -- Apply new rotation after original, as if it was on a child.

      :type: Literal['REPLACE', 'ADD', 'BEFORE', 'AFTER']

   .. attribute:: mix_mode_scale

      Specify how to combine the new scale with original (default ``'REPLACE'``)

      - ``REPLACE``
        Replace -- Replace component values.
      - ``MULTIPLY``
        Multiply -- Multiply component values together.

      :type: Literal['REPLACE', 'MULTIPLY']

   .. attribute:: subtarget

      Armature bone, mesh or lattice vertex group, ... (default "", never None)

      :type: str

   .. attribute:: target

      Target object

      :type: :class:`Object` | None

   .. attribute:: to_euler_order

      Explicitly specify the output euler rotation order (default ``'AUTO'``)

      - ``AUTO``
        Default -- Euler using the default rotation order.
      - ``XYZ``
        XYZ Euler -- Euler using the XYZ rotation order.
      - ``XZY``
        XZY Euler -- Euler using the XZY rotation order.
      - ``YXZ``
        YXZ Euler -- Euler using the YXZ rotation order.
      - ``YZX``
        YZX Euler -- Euler using the YZX rotation order.
      - ``ZXY``
        ZXY Euler -- Euler using the ZXY rotation order.
      - ``ZYX``
        ZYX Euler -- Euler using the ZYX rotation order.

      :type: Literal['AUTO', 'XYZ', 'XZY', 'YXZ', 'YZX', 'ZXY', 'ZYX']

   .. attribute:: to_max_x

      Top range of X axis destination motion (in [-inf, inf], default 0.0)

      :type: float

   .. attribute:: to_max_x_rot

      Top range of X axis destination motion (in [-inf, inf], default 0.0)

      :type: float

   .. attribute:: to_max_x_scale

      Top range of X axis destination motion (in [-inf, inf], default 0.0)

      :type: float

   .. attribute:: to_max_y

      Top range of Y axis destination motion (in [-inf, inf], default 0.0)

      :type: float

   .. attribute:: to_max_y_rot

      Top range of Y axis destination motion (in [-inf, inf], default 0.0)

      :type: float

   .. attribute:: to_max_y_scale

      Top range of Y axis destination motion (in [-inf, inf], default 0.0)

      :type: float

   .. attribute:: to_max_z

      Top range of Z axis destination motion (in [-inf, inf], default 0.0)

      :type: float

   .. attribute:: to_max_z_rot

      Top range of Z axis destination motion (in [-inf, inf], default 0.0)

      :type: float

   .. attribute:: to_max_z_scale

      Top range of Z axis destination motion (in [-inf, inf], default 0.0)

      :type: float

   .. attribute:: to_min_x

      Bottom range of X axis destination motion (in [-inf, inf], default 0.0)

      :type: float

   .. attribute:: to_min_x_rot

      Bottom range of X axis destination motion (in [-inf, inf], default 0.0)

      :type: float

   .. attribute:: to_min_x_scale

      Bottom range of X axis destination motion (in [-inf, inf], default 0.0)

      :type: float

   .. attribute:: to_min_y

      Bottom range of Y axis destination motion (in [-inf, inf], default 0.0)

      :type: float

   .. attribute:: to_min_y_rot

      Bottom range of Y axis destination motion (in [-inf, inf], default 0.0)

      :type: float

   .. attribute:: to_min_y_scale

      Bottom range of Y axis destination motion (in [-inf, inf], default 0.0)

      :type: float

   .. attribute:: to_min_z

      Bottom range of Z axis destination motion (in [-inf, inf], default 0.0)

      :type: float

   .. attribute:: to_min_z_rot

      Bottom range of Z axis destination motion (in [-inf, inf], default 0.0)

      :type: float

   .. attribute:: to_min_z_scale

      Bottom range of Z axis destination motion (in [-inf, inf], default 0.0)

      :type: float

   .. attribute:: use_motion_extrapolate

      Extrapolate ranges (default False)

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

