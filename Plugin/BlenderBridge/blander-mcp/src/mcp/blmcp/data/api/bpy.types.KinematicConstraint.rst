KinematicConstraint(Constraint)
===============================

.. currentmodule:: bpy.types

base classes --- :class:`bpy_struct`, :class:`Constraint`

.. class:: KinematicConstraint(Constraint)

   Inverse Kinematics

   .. attribute:: chain_count

      How many bones are included in the IK effect - 0 uses all bones (in [0, 255], default 0)

      :type: int

   .. attribute:: distance

      Radius of limiting sphere (in [0, 100], default 0.0)

      :type: float

   .. attribute:: ik_type

      (default ``'COPY_POSE'``)

      :type: Literal['COPY_POSE', 'DISTANCE']

   .. attribute:: iterations

      Maximum number of solving iterations (in [0, 10000], default 0)

      :type: int

   .. attribute:: limit_mode

      Distances in relation to sphere of influence to allow (default ``'LIMITDIST_INSIDE'``)

      - ``LIMITDIST_INSIDE``
        Inside -- The object is constrained inside a virtual sphere around the target object, with a radius defined by the limit distance.
      - ``LIMITDIST_OUTSIDE``
        Outside -- The object is constrained outside a virtual sphere around the target object, with a radius defined by the limit distance.
      - ``LIMITDIST_ONSURFACE``
        On Surface -- The object is constrained on the surface of a virtual sphere around the target object, with a radius defined by the limit distance.

      :type: Literal['LIMITDIST_INSIDE', 'LIMITDIST_OUTSIDE', 'LIMITDIST_ONSURFACE']

   .. attribute:: lock_location_x

      Constraint position along X axis (default True)

      :type: bool

   .. attribute:: lock_location_y

      Constraint position along Y axis (default True)

      :type: bool

   .. attribute:: lock_location_z

      Constraint position along Z axis (default True)

      :type: bool

   .. attribute:: lock_rotation_x

      Constraint rotation along X axis (default True)

      :type: bool

   .. attribute:: lock_rotation_y

      Constraint rotation along Y axis (default True)

      :type: bool

   .. attribute:: lock_rotation_z

      Constraint rotation along Z axis (default True)

      :type: bool

   .. attribute:: orient_weight

      For Tree-IK: Weight of orientation control for this target (in [0.01, 1], default 0.0)

      :type: float

   .. attribute:: pole_angle

      Pole rotation offset (in [-3.14159, 3.14159], default 0.0)

      :type: float

   .. attribute:: pole_subtarget

      (default "", never None)

      :type: str

   .. attribute:: pole_target

      Object for pole rotation

      :type: :class:`Object` | None

   .. attribute:: reference_axis

      Constraint axis Lock options relative to Bone or Target reference (default ``'BONE'``)

      :type: Literal['BONE', 'TARGET']

   .. attribute:: subtarget

      Armature bone, mesh or lattice vertex group, ... (default "", never None)

      :type: str

   .. attribute:: target

      Target object

      :type: :class:`Object` | None

   .. attribute:: use_location

      Chain follows position of target (default False)

      :type: bool

   .. attribute:: use_rotation

      Chain follows rotation of target (default False)

      :type: bool

   .. attribute:: use_stretch

      Enable IK Stretching (default False)

      :type: bool

   .. attribute:: use_tail

      Include bone's tail as last element in chain (default False)

      :type: bool

   .. attribute:: weight

      For Tree-IK: Weight of position control for this target (in [0.01, 1], default 0.0)

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

