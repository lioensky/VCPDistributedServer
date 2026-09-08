Bone(bpy_struct)
================

.. currentmodule:: bpy.types

base class --- :class:`bpy_struct`

.. class:: Bone(bpy_struct)

   Bone in an Armature data-block

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

   .. attribute:: bbone_custom_handle_end

      Bone that serves as the end handle for the B-Bone curve

      :type: :class:`Bone` | None

   .. attribute:: bbone_custom_handle_start

      Bone that serves as the start handle for the B-Bone curve

      :type: :class:`Bone` | None

   .. attribute:: bbone_easein

      Length of first Bézier Handle (for B-Bones only) (in [-inf, inf], default 1.0)

      :type: float

   .. attribute:: bbone_easeout

      Length of second Bézier Handle (for B-Bones only) (in [-inf, inf], default 1.0)

      :type: float

   .. attribute:: bbone_handle_type_end

      Selects how the end handle of the B-Bone is computed (default ``'AUTO'``)

      - ``AUTO``
        Automatic -- Use connected parent and children to compute the handle.
      - ``ABSOLUTE``
        Absolute -- Use the position of the specified bone to compute the handle.
      - ``RELATIVE``
        Relative -- Use the offset of the specified bone from rest pose to compute the handle.
      - ``TANGENT``
        Tangent -- Use the orientation of the specified bone to compute the handle, ignoring the location.

      :type: Literal['AUTO', 'ABSOLUTE', 'RELATIVE', 'TANGENT']

   .. attribute:: bbone_handle_type_start

      Selects how the start handle of the B-Bone is computed (default ``'AUTO'``)

      - ``AUTO``
        Automatic -- Use connected parent and children to compute the handle.
      - ``ABSOLUTE``
        Absolute -- Use the position of the specified bone to compute the handle.
      - ``RELATIVE``
        Relative -- Use the offset of the specified bone from rest pose to compute the handle.
      - ``TANGENT``
        Tangent -- Use the orientation of the specified bone to compute the handle, ignoring the location.

      :type: Literal['AUTO', 'ABSOLUTE', 'RELATIVE', 'TANGENT']

   .. attribute:: bbone_handle_use_ease_end

      Multiply the B-Bone Ease Out channel by the local Y scale value of the end handle. This is done after the Scale Easing option and isn't affected by it. (default False)

      :type: bool

   .. attribute:: bbone_handle_use_ease_start

      Multiply the B-Bone Ease In channel by the local Y scale value of the start handle. This is done after the Scale Easing option and isn't affected by it. (default False)

      :type: bool

   .. attribute:: bbone_handle_use_scale_end

      Multiply B-Bone Scale Out channels by the local scale values of the end handle. This is done after the Scale Easing option and isn't affected by it. (array of 3 items, default (False, False, False))

      :type: :class:`bpy_prop_array`\ [bool]

   .. attribute:: bbone_handle_use_scale_start

      Multiply B-Bone Scale In channels by the local scale values of the start handle. This is done after the Scale Easing option and isn't affected by it. (array of 3 items, default (False, False, False))

      :type: :class:`bpy_prop_array`\ [bool]

   .. attribute:: bbone_mapping_mode

      Selects how the vertices are mapped to B-Bone segments based on their position (default ``'STRAIGHT'``)

      - ``STRAIGHT``
        Straight -- Fast mapping that is good for most situations, but ignores the rest pose curvature of the B-Bone.
      - ``CURVED``
        Curved -- Slower mapping that gives better deformation for B-Bones that are sharply curved in rest pose.

      :type: Literal['STRAIGHT', 'CURVED']

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

   .. attribute:: bbone_segments

      Number of subdivisions of bone (for B-Bones only) (in [1, 32], default 0)

      :type: int

   .. attribute:: bbone_x

      B-Bone X size (in [-inf, inf], default 0.0)

      :type: float

   .. attribute:: bbone_z

      B-Bone Z size (in [-inf, inf], default 0.0)

      :type: float

   .. data:: children

      Bones which are children of this bone (default None, readonly)

      :type: :class:`bpy_prop_collection`\ [:class:`Bone`]

   .. data:: collections

      Bone Collections that contain this bone (default None, readonly)

      :type: :class:`BoneCollectionMemberships`\ [:class:`BoneCollection`]

   .. data:: color

      (readonly)

      :type: :class:`BoneColor` | None

   .. attribute:: display_type

      (default ``'OCTAHEDRAL'``)

      - ``ARMATURE_DEFINED``
        Armature Defined -- Use display mode from armature (default).
      - ``OCTAHEDRAL``
        Octahedral -- Display bones as octahedral shape.
      - ``STICK``
        Stick -- Display bones as simple 2D lines with dots.
      - ``BBONE``
        B-Bone -- Display bones as boxes, showing subdivision and B-Splines.
      - ``ENVELOPE``
        Envelope -- Display bones as extruded spheres, showing deformation influence volume.
      - ``WIRE``
        Wire -- Display bones as thin wires, showing subdivision and B-Splines.

      :type: Literal['ARMATURE_DEFINED', 'OCTAHEDRAL', 'STICK', 'BBONE', 'ENVELOPE', 'WIRE']

   .. attribute:: envelope_distance

      Bone deformation distance (for Envelope deform only) (in [0, 1000], default 0.0)

      :type: float

   .. attribute:: envelope_weight

      Bone deformation weight (for Envelope deform only) (in [0, 1000], default 0.0)

      :type: float

   .. data:: head

      Location of head end of the bone relative to its parent (array of 3 items, in [-inf, inf], default (0.0, 0.0, 0.0), readonly)

      :type: :class:`mathutils.Vector`

   .. data:: head_local

      Location of head end of the bone relative to armature (array of 3 items, in [-inf, inf], default (0.0, 0.0, 0.0), readonly)

      :type: :class:`mathutils.Vector`

   .. attribute:: head_radius

      Radius of head of bone (for Envelope deform only) (in [-inf, inf], default 0.0)

      :type: float

   .. attribute:: hide

      Bone is not visible when it is in Edit Mode (default False)

      :type: bool

   .. attribute:: hide_select

      Bone is able to be selected (default False)

      :type: bool

   .. attribute:: inherit_scale

      Specifies how the bone inherits scaling from the parent bone (default ``'FULL'``)

      - ``FULL``
        Full -- Inherit all effects of parent scaling.
      - ``FIX_SHEAR``
        Fix Shear -- Inherit scaling, but remove shearing of the child in the rest orientation.
      - ``ALIGNED``
        Aligned -- Rotate non-uniform parent scaling to align with the child, applying parent X scale to child X axis, and so forth.
      - ``AVERAGE``
        Average -- Inherit uniform scaling representing the overall change in the volume of the parent.
      - ``NONE``
        None -- Completely ignore parent scaling.
      - ``NONE_LEGACY``
        None (Legacy) -- Ignore parent scaling without compensating for parent shear. Replicates the effect of disabling the original Inherit Scale checkbox..

      :type: Literal['FULL', 'FIX_SHEAR', 'ALIGNED', 'AVERAGE', 'NONE', 'NONE_LEGACY']

   .. data:: length

      Length of the bone (in [-inf, inf], default 0.0, readonly)

      :type: float

   .. data:: matrix

      3×3 bone matrix (multi-dimensional array of 3 * 3 items, in [-inf, inf], default ((0.0, 0.0, 0.0), (0.0, 0.0, 0.0), (0.0, 0.0, 0.0)), readonly)

      :type: :class:`mathutils.Matrix`

   .. data:: matrix_local

      4×4 bone matrix relative to armature (multi-dimensional array of 4 * 4 items, in [-inf, inf], default ((0.0, 0.0, 0.0, 0.0), (0.0, 0.0, 0.0, 0.0), (0.0, 0.0, 0.0, 0.0), (0.0, 0.0, 0.0, 0.0)), readonly)

      :type: :class:`mathutils.Matrix`

   .. attribute:: name

      (default "", never None)

      :type: str

   .. data:: parent

      Parent bone (in same Armature) (readonly)

      :type: :class:`Bone` | None

   .. attribute:: show_wire

      Bone is always displayed in wireframe regardless of viewport shading mode (useful for non-obstructive custom bone shapes) (default False)

      :type: bool

   .. data:: tail

      Location of tail end of the bone relative to its parent (array of 3 items, in [-inf, inf], default (0.0, 0.0, 0.0), readonly)

      :type: :class:`mathutils.Vector`

   .. data:: tail_local

      Location of tail end of the bone relative to armature (array of 3 items, in [-inf, inf], default (0.0, 0.0, 0.0), readonly)

      :type: :class:`mathutils.Vector`

   .. attribute:: tail_radius

      Radius of tail of bone (for Envelope deform only) (in [-inf, inf], default 0.0)

      :type: float

   .. data:: use_connect

      When bone has a parent, bone's head is stuck to the parent's tail (default False, readonly)

      :type: bool

   .. attribute:: use_cyclic_offset

      When bone does not have a parent, it receives cyclic offset effects (Deprecated) (default True)

      :type: bool

   .. attribute:: use_deform

      Enable Bone to deform geometry (default True)

      :type: bool

   .. attribute:: use_endroll_as_inroll

      Add Roll Out of the Start Handle bone to the Roll In value (default False)

      :type: bool

   .. attribute:: use_envelope_multiply

      When deforming bone, multiply effects of Vertex Group weights with Envelope influence (default False)

      :type: bool

   .. attribute:: use_inherit_rotation

      Bone inherits rotation or scale from parent bone (default True)

      :type: bool

   .. attribute:: use_local_location

      Bone location is set in local space (default True)

      :type: bool

   .. attribute:: use_relative_parent

      Object children will use relative transform, like deform (default False)

      :type: bool

   .. attribute:: use_scale_easing

      Multiply the final easing values by the Scale In/Out Y factors (default False)

      :type: bool

   .. data:: basename

      The name of this bone before any ``.`` character.

      (readonly)

   .. data:: center

      The midpoint between the head and the tail.

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

   .. method:: convert_local_to_pose(matrix, matrix_local, *, parent_matrix=((0.0, 0.0, 0.0, 0.0), (0.0, 0.0, 0.0, 0.0), (0.0, 0.0, 0.0, 0.0), (0.0, 0.0, 0.0, 0.0)), parent_matrix_local=((0.0, 0.0, 0.0, 0.0), (0.0, 0.0, 0.0, 0.0), (0.0, 0.0, 0.0, 0.0), (0.0, 0.0, 0.0, 0.0)), invert=False)

      Transform a matrix from Local to Pose space (or back), taking into account options like Inherit Scale and Local Location. Unlike Object.convert_space, this uses custom rest and pose matrices provided by the caller. If the parent matrices are omitted, the bone is assumed to have no parent.

      :param matrix: The matrix to transform (multi-dimensional array of 4 * 4 items, in [-inf, inf])
      :type matrix: :class:`mathutils.Matrix` | Sequence[Sequence[float]]
      :param matrix_local: The custom rest matrix of this bone (Bone.matrix_local) (multi-dimensional array of 4 * 4 items, in [-inf, inf])
      :type matrix_local: :class:`mathutils.Matrix` | Sequence[Sequence[float]]
      :param parent_matrix: The custom pose matrix of the parent bone (PoseBone.matrix) (multi-dimensional array of 4 * 4 items, in [-inf, inf], optional)
      :type parent_matrix: :class:`mathutils.Matrix` | Sequence[Sequence[float]]
      :param parent_matrix_local: The custom rest matrix of the parent bone (Bone.matrix_local) (multi-dimensional array of 4 * 4 items, in [-inf, inf], optional)
      :type parent_matrix_local: :class:`mathutils.Matrix` | Sequence[Sequence[float]]
      :param invert: Convert from Pose to Local space (optional)
      :type invert: bool
      :return: The transformed matrix (multi-dimensional array of 4 * 4 items, in [-inf, inf])
      :rtype: :class:`mathutils.Matrix`

      This method enables conversions between Local and Pose space for bones in
      the middle of updating the armature without having to update dependencies
      after each change, by manually carrying updated matrices in a recursive walk.

      .. literalinclude:: ./examples/bpy.types.Bone.convert_local_to_pose.0.py
         :lines: 8-


   .. classmethod:: MatrixFromAxisRoll(axis, roll)

      Convert the axis + roll representation to a matrix

      :param axis: The main axis of the bone (tail - head) (array of 3 items, in [-inf, inf], never None)
      :type axis: :class:`mathutils.Vector` | Sequence[float]
      :param roll: The roll of the bone (in [-inf, inf])
      :type roll: float
      :return: The resulting orientation matrix (multi-dimensional array of 3 * 3 items, in [-inf, inf])
      :rtype: :class:`mathutils.Matrix`

   .. classmethod:: AxisRollFromMatrix(matrix, *, axis=(0.0, 0.0, 0.0))

      Convert a rotational matrix to the axis + roll representation. Note that the resulting value of the roll may not be as expected if the matrix has shear or negative determinant.

      :param matrix: The orientation matrix of the bone (multi-dimensional array of 3 * 3 items, in [-inf, inf], never None)
      :type matrix: :class:`mathutils.Matrix` | Sequence[Sequence[float]]
      :param axis: The optional override for the axis (finds closest approximation for the matrix) (array of 3 items, in [-inf, inf], optional)
      :type axis: Sequence[float]
      :return:
         ``result_axis``, The main axis of the bone, :class:`mathutils.Vector`

         ``result_roll``, The roll of the bone, float

      :rtype: tuple[:class:`mathutils.Vector`, float]

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

   - :mod:`bpy.context.active_bone`
   - :mod:`bpy.context.bone`
   - :class:`Armature.bones`
   - :class:`ArmatureBones.active`
   - :class:`Bone.bbone_custom_handle_end`
   - :class:`Bone.bbone_custom_handle_start`
   - :class:`Bone.children`
   - :class:`Bone.parent`
   - :class:`BoneCollection.bones`
   - :class:`PoseBone.bone`

