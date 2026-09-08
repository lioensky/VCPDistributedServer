PoseBone(bpy_struct)
====================

.. currentmodule:: bpy.types

base class --- :class:`bpy_struct`

.. class:: PoseBone(bpy_struct)

   Channel defining pose data for a bone in a Pose

   .. attribute:: bbone_curveinx

      X-axis handle offset for start of the B-Bone's curve, adjusts curvature (in [-inf, inf], default 0.0)

      :type: float

   .. attribute:: bbone_curveinz

      Z-axis handle offset for start of the B-Bone's curve, adjusts curvature (in [-inf, inf], default 0.0)

      :type: float

   .. attribute:: bbone_curveoutx

      X-axis handle offset for end of the B-Bone's curve, adjusts curvature (in [-inf, inf], default 0.0)

      :type: float

   .. attribute:: bbone_curveoutz

      Z-axis handle offset for end of the B-Bone's curve, adjusts curvature (in [-inf, inf], default 0.0)

      :type: float

   .. data:: bbone_custom_handle_end

      Bone that serves as the end handle for the B-Bone curve (readonly)

      :type: :class:`PoseBone` | None

   .. data:: bbone_custom_handle_start

      Bone that serves as the start handle for the B-Bone curve (readonly)

      :type: :class:`PoseBone` | None

   .. attribute:: bbone_easein

      Length of first Bézier Handle (for B-Bones only) (in [-inf, inf], default 0.0)

      :type: float

   .. attribute:: bbone_easeout

      Length of second Bézier Handle (for B-Bones only) (in [-inf, inf], default 0.0)

      :type: float

   .. attribute:: bbone_rollin

      Roll offset for the start of the B-Bone, adjusts twist (in [-inf, inf], default 0.0)

      :type: float

   .. attribute:: bbone_rollout

      Roll offset for the end of the B-Bone, adjusts twist (in [-inf, inf], default 0.0)

      :type: float

   .. attribute:: bbone_scalein

      Scale factors for the start of the B-Bone, adjusts thickness (for tapering effects) (array of 3 items, in [-inf, inf], default (1.0, 1.0, 1.0))

      :type: :class:`mathutils.Vector`

   .. attribute:: bbone_scaleout

      Scale factors for the end of the B-Bone, adjusts thickness (for tapering effects) (array of 3 items, in [-inf, inf], default (1.0, 1.0, 1.0))

      :type: :class:`mathutils.Vector`

   .. data:: bone

      Bone associated with this PoseBone (readonly, never None)

      :type: :class:`Bone`

   .. data:: child

      Child of this pose bone (readonly)

      :type: :class:`PoseBone` | None

   .. data:: color

      (readonly)

      :type: :class:`BoneColor` | None

   .. data:: constraints

      Constraints that act on this pose channel (default None, readonly)

      :type: :class:`PoseBoneConstraints`\ [:class:`Constraint`]

   .. attribute:: custom_shape

      Object that defines custom display shape for this bone

      :type: :class:`Object` | None

   .. attribute:: custom_shape_rotation_euler

      Adjust the rotation of the custom shape (array of 3 items, in [-inf, inf], default (0.0, 0.0, 0.0))

      :type: :class:`mathutils.Euler`

   .. attribute:: custom_shape_scale_xyz

      Adjust the size of the custom shape (array of 3 items, in [-inf, inf], default (1.0, 1.0, 1.0))

      :type: :class:`mathutils.Vector`

   .. attribute:: custom_shape_transform

      Bone that defines the display transform of this custom shape

      :type: :class:`PoseBone` | None

   .. attribute:: custom_shape_translation

      Adjust the location of the custom shape (array of 3 items, in [-inf, inf], default (0.0, 0.0, 0.0))

      :type: :class:`mathutils.Vector`

   .. attribute:: custom_shape_wire_width

      Adjust the line thickness of custom shapes (in [1, 16], default 0.0)

      :type: float

   .. data:: head

      Location of head of the channel's bone (array of 3 items, in [-inf, inf], default (0.0, 0.0, 0.0), readonly)

      :type: :class:`mathutils.Vector`

   .. attribute:: hide

      Bone is not visible except for Edit Mode (default False)

      :type: bool

   .. attribute:: ik_linear_weight

      Weight of scale constraint for IK (in [0, 1], default 0.0)

      :type: float

   .. attribute:: ik_max_x

      Maximum angles for IK Limit (in [0, 3.14159], default 0.0)

      :type: float

   .. attribute:: ik_max_y

      Maximum angles for IK Limit (in [0, 3.14159], default 0.0)

      :type: float

   .. attribute:: ik_max_z

      Maximum angles for IK Limit (in [0, 3.14159], default 0.0)

      :type: float

   .. attribute:: ik_min_x

      Minimum angles for IK Limit (in [-3.14159, 0], default 0.0)

      :type: float

   .. attribute:: ik_min_y

      Minimum angles for IK Limit (in [-3.14159, 0], default 0.0)

      :type: float

   .. attribute:: ik_min_z

      Minimum angles for IK Limit (in [-3.14159, 0], default 0.0)

      :type: float

   .. attribute:: ik_rotation_weight

      Weight of rotation constraint for IK (in [0, 1], default 0.0)

      :type: float

   .. attribute:: ik_stiffness_x

      IK stiffness around the X axis (in [0, 0.99], default 0.0)

      :type: float

   .. attribute:: ik_stiffness_y

      IK stiffness around the Y axis (in [0, 0.99], default 0.0)

      :type: float

   .. attribute:: ik_stiffness_z

      IK stiffness around the Z axis (in [0, 0.99], default 0.0)

      :type: float

   .. attribute:: ik_stretch

      Allow scaling of the bone for IK (in [0, 1], default 0.0)

      :type: float

   .. data:: is_in_ik_chain

      Is part of an IK chain (default False, readonly)

      :type: bool

   .. data:: length

      Length of the bone (in [-inf, inf], default 0.0, readonly)

      :type: float

   .. attribute:: location

      (array of 3 items, in [-inf, inf], default (0.0, 0.0, 0.0))

      :type: :class:`mathutils.Vector`

   .. attribute:: lock_ik_x

      Disallow movement around the X axis (default False)

      :type: bool

   .. attribute:: lock_ik_y

      Disallow movement around the Y axis (default False)

      :type: bool

   .. attribute:: lock_ik_z

      Disallow movement around the Z axis (default False)

      :type: bool

   .. attribute:: lock_location

      Lock editing of location when transforming (array of 3 items, default (False, False, False))

      :type: :class:`bpy_prop_array`\ [bool]

   .. attribute:: lock_rotation

      Lock editing of rotation when transforming (array of 3 items, default (False, False, False))

      :type: :class:`bpy_prop_array`\ [bool]

   .. attribute:: lock_rotation_w

      Lock editing of 'angle' component of four-component rotations when transforming (default False)

      :type: bool

   .. attribute:: lock_rotations_4d

      Lock editing of four component rotations by components (instead of as Eulers) (default False)

      :type: bool

   .. attribute:: lock_scale

      Lock editing of scale when transforming (array of 3 items, default (False, False, False))

      :type: :class:`bpy_prop_array`\ [bool]

   .. attribute:: matrix

      Final 4×4 matrix after constraints and drivers are applied, in the armature object space (multi-dimensional array of 4 * 4 items, in [-inf, inf], default ((0.0, 0.0, 0.0, 0.0), (0.0, 0.0, 0.0, 0.0), (0.0, 0.0, 0.0, 0.0), (0.0, 0.0, 0.0, 0.0)))

      :type: :class:`mathutils.Matrix`

   .. attribute:: matrix_basis

      Alternative access to location/scale/rotation relative to the parent and own rest bone (multi-dimensional array of 4 * 4 items, in [-inf, inf], default ((0.0, 0.0, 0.0, 0.0), (0.0, 0.0, 0.0, 0.0), (0.0, 0.0, 0.0, 0.0), (0.0, 0.0, 0.0, 0.0)))

      :type: :class:`mathutils.Matrix`

   .. data:: matrix_channel

      4×4 matrix of the bone's location/rotation/scale channels (including animation and drivers) and the effect of bone constraints (multi-dimensional array of 4 * 4 items, in [-inf, inf], default ((0.0, 0.0, 0.0, 0.0), (0.0, 0.0, 0.0, 0.0), (0.0, 0.0, 0.0, 0.0), (0.0, 0.0, 0.0, 0.0)), readonly)

      :type: :class:`mathutils.Matrix`

   .. data:: motion_path

      Motion Path for this element (readonly)

      :type: :class:`MotionPath` | None

   .. attribute:: name

      (default "", never None)

      :type: str

   .. data:: parent

      Parent of this pose bone (readonly)

      :type: :class:`PoseBone` | None

   .. attribute:: rotation_axis_angle

      Angle of Rotation for Axis-Angle rotation representation (array of 4 items, in [-inf, inf], default (0.0, 0.0, 1.0, 0.0))

      :type: :class:`bpy_prop_array`\ [float]

   .. attribute:: rotation_euler

      Rotation in Eulers (array of 3 items, in [-inf, inf], default (0.0, 0.0, 0.0))

      :type: :class:`mathutils.Euler`

   .. attribute:: rotation_mode

      The kind of rotation to apply, values from other rotation modes are not used (default ``'QUATERNION'``)

      :type: Literal[:ref:`rna_enum_object_rotation_mode_items`]

   .. attribute:: rotation_quaternion

      Rotation in Quaternions (array of 4 items, in [-inf, inf], default (1.0, 0.0, 0.0, 0.0))

      :type: :class:`mathutils.Quaternion`

   .. attribute:: scale

      (array of 3 items, in [-inf, inf], default (1.0, 1.0, 1.0))

      :type: :class:`mathutils.Vector`

   .. attribute:: select

      Bone is selected in Pose Mode (default False)

      :type: bool

   .. data:: tail

      Location of tail of the channel's bone (array of 3 items, in [-inf, inf], default (0.0, 0.0, 0.0), readonly)

      :type: :class:`mathutils.Vector`

   .. attribute:: use_custom_shape_bone_size

      Scale the custom object by the bone length (default True)

      :type: bool

   .. attribute:: use_ik_limit_x

      Limit movement around the X axis (default False)

      :type: bool

   .. attribute:: use_ik_limit_y

      Limit movement around the Y axis (default False)

      :type: bool

   .. attribute:: use_ik_limit_z

      Limit movement around the Z axis (default False)

      :type: bool

   .. attribute:: use_ik_linear_control

      Apply channel size as IK constraint if stretching is enabled (default False)

      :type: bool

   .. attribute:: use_ik_rotation_control

      Apply channel rotation as IK constraint (default False)

      :type: bool

   .. attribute:: use_transform_around_custom_shape

      Transform the bone as if it was a child of the Custom Shape Transform bone. This can be useful when combining shape-key and armature deformations. (default False)

      :type: bool

   .. attribute:: use_transform_at_custom_shape

      The location and orientation of the Custom Shape Transform bone will be used for transform gizmos and for other transform operators in the 3D Viewport. When disabled, the 3D Viewport will still use the actual bone transform for these, even when the custom bone shape transform is overridden. (default False)

      :type: bool

   .. data:: basename

      The name of this bone before any ``.`` character.

      (readonly)

   .. data:: center

      The midpoint between the head and the tail.

      (readonly)

   .. data:: children


      (readonly)

   .. data:: children_recursive

      A list of all children from this bone.
      
      .. note:: Takes ``O(len(bones)**2)`` time.

      (readonly)

   .. data:: children_recursive_basename

      Returns a chain of children with the same base name as this bone.
      Only direct chains are supported, forks caused by multiple children
      with matching base names will terminate the function
      and not be returned.
      
      .. note:: Takes ``O(len(bones)**2)`` time.

      (readonly)

   .. data:: parent_recursive

      A list of parents, starting with the immediate parent.

      (readonly)

   .. data:: vector

      The direction this bone is pointing.
      Utility function for (tail - head)

      (readonly)

   .. data:: x_axis

      Vector pointing down the x-axis of the bone.

      (readonly)

   .. data:: y_axis

      Vector pointing down the y-axis of the bone.

      (readonly)

   .. data:: z_axis

      Vector pointing down the z-axis of the bone.

      (readonly)

   .. method:: bl_system_properties_get(*, do_create=False)

      DEBUG ONLY. Internal access to runtime-defined RNA data storage, intended solely for testing and debugging purposes. Do not access it in regular scripting work, and in particular, do not assume that it contains writable data

      :param do_create: Ensure that system properties are created if they do not exist yet (optional)
      :type do_create: bool
      :return: The system properties root container, or None if there are no system properties stored in this data yet, and its creation was not requested
      :rtype: :class:`PropertyGroup`

   .. method:: evaluate_envelope(point)

      Calculate bone envelope at given point

      :param point: Point, Position in 3d space to evaluate (array of 3 items, in [-inf, inf])
      :type point: :class:`mathutils.Vector` | Sequence[float]
      :return: Factor, Envelope factor (in [-inf, inf])
      :rtype: float

   .. method:: bbone_segment_index(point)

      Retrieve the index and blend factor of the B-Bone segments based on vertex position

      :param point: Point, Vertex position in armature pose space (array of 3 items, in [-inf, inf])
      :type point: :class:`mathutils.Vector` | Sequence[float]
      :return:
         ``index``, The index of the first segment joint affecting the point, int

         ``blend_next``, The blend factor between the given and the following joint, float

      :rtype: tuple[int, float]

   .. method:: bbone_segment_matrix(index, *, rest=False)

      Retrieve the matrix of the joint between B-Bone segments if available

      :param index: Index of the segment endpoint (in [0, inf])
      :type index: int
      :param rest: Return the rest pose matrix (optional)
      :type rest: bool
      :return: The resulting matrix in bone local space (multi-dimensional array of 4 * 4 items, in [-inf, inf])
      :rtype: :class:`mathutils.Matrix`

      This example shows how to use B-Bone segment matrices to emulate deformation
      produced by the Armature modifier or constraint when assigned to the given bone
      (without Preserve Volume). The coordinates are processed in armature Pose space:

      .. literalinclude:: ./examples/bpy.types.PoseBone.bbone_segment_matrix.0.py
         :lines: 6-


   .. method:: compute_bbone_handles(*, rest=False, ease=False, offsets=False)

      Retrieve the vectors and rolls coming from B-Bone custom handles

      :param rest: Return the rest pose state (optional)
      :type rest: bool
      :param ease: Apply scale from ease values (optional)
      :type ease: bool
      :param offsets: Apply roll and curve offsets from bone properties (optional)
      :type offsets: bool
      :return:
         ``handle1``, The direction vector of the start handle in bone local space, :class:`mathutils.Vector`

         ``roll1``, Roll of the start handle, float

         ``handle2``, The direction vector of the end handle in bone local space, :class:`mathutils.Vector`

         ``roll2``, Roll of the end handle, float

      :rtype: tuple[:class:`mathutils.Vector`, float, :class:`mathutils.Vector`, float]

   .. method:: parent_index(parent_test)

      The same as 'bone in other_bone.parent_recursive'
      but saved generating a list.

   .. method:: translate(vec)

      Utility function to add *vec* to the head and tail of this bone.

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

   - :mod:`bpy.context.active_pose_bone`
   - :mod:`bpy.context.pose_bone`
   - :mod:`bpy.context.selected_pose_bones`
   - :mod:`bpy.context.selected_pose_bones_from_active_object`
   - :mod:`bpy.context.visible_pose_bones`
   - :class:`Object.convert_space`
   - :class:`Pose.bones`
   - :class:`PoseBone.bbone_custom_handle_end`
   - :class:`PoseBone.bbone_custom_handle_start`
   - :class:`PoseBone.child`
   - :class:`PoseBone.custom_shape_transform`
   - :class:`PoseBone.parent`

