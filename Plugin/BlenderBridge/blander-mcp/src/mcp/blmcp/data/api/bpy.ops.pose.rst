Pose Operators
==============

.. module:: bpy.ops.pose

.. function:: armature_apply(*, selected=False)

   Apply the current pose as the new rest pose

   :param selected: Selected Only, Only apply the selected bones (with propagation to children) (optional)
   :type selected: bool
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: autoside_names(*, axis='XAXIS')

   Automatically renames the selected bones according to which side of the target axis they fall on

   :param axis: Axis, Axis to tag names with (optional)

      - ``XAXIS``
        X-Axis -- Left/Right.
      - ``YAXIS``
        Y-Axis -- Front/Back.
      - ``ZAXIS``
        Z-Axis -- Top/Bottom.
   :type axis: Literal['XAXIS', 'YAXIS', 'ZAXIS']
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: blend_to_neighbor(*, factor=0.5, prev_frame=0, next_frame=0, channels='ALL', axis_lock='FREE')

   Blend from current position to previous or next keyframe

   :param factor: Factor, Weighting factor for which keyframe is favored more (in [0, 1], optional)
   :type factor: float
   :param prev_frame: Previous Keyframe, Frame number of keyframe immediately before the current frame (in [-1048574, 1048574], optional)
   :type prev_frame: int
   :param next_frame: Next Keyframe, Frame number of keyframe immediately after the current frame (in [-1048574, 1048574], optional)
   :type next_frame: int
   :param channels: Channels, Set of properties that are affected (optional)

      - ``ALL``
        All Properties -- All properties, including transforms, bendy bone shape, and custom properties.
      - ``LOC``
        Location -- Location only.
      - ``ROT``
        Rotation -- Rotation only.
      - ``SIZE``
        Scale -- Scale only.
      - ``BBONE``
        Bendy Bone -- Bendy Bone shape properties.
      - ``CUSTOM``
        Custom Properties -- Custom properties.
   :type channels: Literal['ALL', 'LOC', 'ROT', 'SIZE', 'BBONE', 'CUSTOM']
   :param axis_lock: Axis Lock, Transform axis to restrict effects to (optional)

      - ``FREE``
        Free -- All axes are affected.
      - ``X``
        X -- Only X-axis transforms are affected.
      - ``Y``
        Y -- Only Y-axis transforms are affected.
      - ``Z``
        Z -- Only Z-axis transforms are affected.
   :type axis_lock: Literal['FREE', 'X', 'Y', 'Z']
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: blend_with_rest(*, factor=0.5, prev_frame=0, next_frame=0, channels='ALL', axis_lock='FREE')

   Make the current pose more similar to, or further away from, the rest pose

   :param factor: Factor, Weighting factor for which keyframe is favored more (in [0, 1], optional)
   :type factor: float
   :param prev_frame: Previous Keyframe, Frame number of keyframe immediately before the current frame (in [-1048574, 1048574], optional)
   :type prev_frame: int
   :param next_frame: Next Keyframe, Frame number of keyframe immediately after the current frame (in [-1048574, 1048574], optional)
   :type next_frame: int
   :param channels: Channels, Set of properties that are affected (optional)

      - ``ALL``
        All Properties -- All properties, including transforms, bendy bone shape, and custom properties.
      - ``LOC``
        Location -- Location only.
      - ``ROT``
        Rotation -- Rotation only.
      - ``SIZE``
        Scale -- Scale only.
      - ``BBONE``
        Bendy Bone -- Bendy Bone shape properties.
      - ``CUSTOM``
        Custom Properties -- Custom properties.
   :type channels: Literal['ALL', 'LOC', 'ROT', 'SIZE', 'BBONE', 'CUSTOM']
   :param axis_lock: Axis Lock, Transform axis to restrict effects to (optional)

      - ``FREE``
        Free -- All axes are affected.
      - ``X``
        X -- Only X-axis transforms are affected.
      - ``Y``
        Y -- Only Y-axis transforms are affected.
      - ``Z``
        Z -- Only Z-axis transforms are affected.
   :type axis_lock: Literal['FREE', 'X', 'Y', 'Z']
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: breakdown(*, factor=0.5, prev_frame=0, next_frame=0, channels='ALL', axis_lock='FREE')

   Create a suitable breakdown pose on the current frame

   :param factor: Factor, Weighting factor for which keyframe is favored more (in [0, 1], optional)
   :type factor: float
   :param prev_frame: Previous Keyframe, Frame number of keyframe immediately before the current frame (in [-1048574, 1048574], optional)
   :type prev_frame: int
   :param next_frame: Next Keyframe, Frame number of keyframe immediately after the current frame (in [-1048574, 1048574], optional)
   :type next_frame: int
   :param channels: Channels, Set of properties that are affected (optional)

      - ``ALL``
        All Properties -- All properties, including transforms, bendy bone shape, and custom properties.
      - ``LOC``
        Location -- Location only.
      - ``ROT``
        Rotation -- Rotation only.
      - ``SIZE``
        Scale -- Scale only.
      - ``BBONE``
        Bendy Bone -- Bendy Bone shape properties.
      - ``CUSTOM``
        Custom Properties -- Custom properties.
   :type channels: Literal['ALL', 'LOC', 'ROT', 'SIZE', 'BBONE', 'CUSTOM']
   :param axis_lock: Axis Lock, Transform axis to restrict effects to (optional)

      - ``FREE``
        Free -- All axes are affected.
      - ``X``
        X -- Only X-axis transforms are affected.
      - ``Y``
        Y -- Only Y-axis transforms are affected.
      - ``Z``
        Z -- Only Z-axis transforms are affected.
   :type axis_lock: Literal['FREE', 'X', 'Y', 'Z']
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: constraint_add(*, type='CHILD_OF')

   Add a constraint to the active bone

   :param type: Type, (optional)
   :type type: Literal[:ref:`rna_enum_constraint_type_items`]
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: constraint_add_with_targets(*, type='CHILD_OF')

   Add a constraint to the active bone, with target (where applicable) set to the selected Objects/Bones

   :param type: Type, (optional)
   :type type: Literal[:ref:`rna_enum_constraint_type_items`]
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: constraints_clear()

   Clear all constraints from the selected bones

   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]
.. function:: constraints_copy()

   Copy constraints to other selected bones

   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]
.. function:: copy()

   Copy the current pose of the selected bones to the internal clipboard

   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]
.. function:: flip_names(*, do_strip_numbers=False)

   Flips (and corrects) the axis suffixes of the names of selected bones

   :param do_strip_numbers: Strip Numbers, Try to remove right-most dot-number from flipped names.Warning: May result in incoherent naming in some cases(optional)
   :type do_strip_numbers: bool
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: hide(*, unselected=False)

   Tag selected bones to not be visible in Pose Mode

   :param unselected: Unselected, (optional)
   :type unselected: bool
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: ik_add(*, with_targets=True)

   Add an IK Constraint to the active Bone. The target can be a selected bone or object

   :param with_targets: With Targets, Assign IK Constraint with targets derived from the select bones/objects (optional)
   :type with_targets: bool
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: ik_clear()

   Remove all IK Constraints from selected bones

   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]
.. function:: loc_clear()

   Reset locations of selected bones to their default values

   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]
.. function:: paste(*, flipped=False, selected_mask=False)

   Paste the stored pose on to the current pose

   :param flipped: Flipped on X-Axis, Paste the stored pose flipped on to current pose (optional)
   :type flipped: bool
   :param selected_mask: On Selected Only, Only paste the stored pose on to selected bones in the current pose (optional)
   :type selected_mask: bool
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: paths_calculate(*, display_type='RANGE', range='SCENE', bake_location='HEADS')

   Calculate paths for the selected bones

   :param display_type: Display Type, (optional)
   :type display_type: Literal[:ref:`rna_enum_motionpath_display_type_items`]
   :param range: Computation Range, (optional)
   :type range: Literal[:ref:`rna_enum_motionpath_range_items`]
   :param bake_location: Bake Location, Which point on the bones is used when calculating paths (optional)
   :type bake_location: Literal[:ref:`rna_enum_motionpath_bake_location_items`]
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: paths_clear(*, only_selected=False)

   Undocumented, consider `contributing <https://developer.blender.org/>`__.

   :param only_selected: Only Selected, Only clear motion paths of selected bones (optional)
   :type only_selected: bool
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: paths_range_update()

   Update frame range for motion paths from the Scene's current frame range

   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]
.. function:: paths_update()

   Recalculate paths for bones that already have them

   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]
.. function:: propagate(*, mode='NEXT_KEY', end_frame=250.0)

   Copy selected aspects of the current pose to subsequent poses already keyframed

   :param mode: Terminate Mode, Method used to determine when to stop propagating pose to keyframes (optional)

      - ``NEXT_KEY``
        To Next Keyframe -- Propagate pose to first keyframe following the current frame only.
      - ``LAST_KEY``
        To Last Keyframe -- Propagate pose to the last keyframe only (i.e. making action cyclic).
      - ``BEFORE_FRAME``
        Before Frame -- Propagate pose to all keyframes between current frame and 'Frame' property.
      - ``BEFORE_END``
        Before Last Keyframe -- Propagate pose to all keyframes from current frame until no more are found.
      - ``SELECTED_KEYS``
        On Selected Keyframes -- Propagate pose to all selected keyframes.
      - ``SELECTED_MARKERS``
        On Selected Markers -- Propagate pose to all keyframes occurring on frames with Scene Markers after the current frame.
   :type mode: Literal['NEXT_KEY', 'LAST_KEY', 'BEFORE_FRAME', 'BEFORE_END', 'SELECTED_KEYS', 'SELECTED_MARKERS']
   :param end_frame: End Frame, Frame to stop propagating frames to (for 'Before Frame' mode) (in [1.17549e-38, inf], optional)
   :type end_frame: float
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: push(*, factor=0.5, prev_frame=0, next_frame=0, channels='ALL', axis_lock='FREE')

   Exaggerate the current pose in regards to the breakdown pose

   :param factor: Factor, Weighting factor for which keyframe is favored more (in [0, 1], optional)
   :type factor: float
   :param prev_frame: Previous Keyframe, Frame number of keyframe immediately before the current frame (in [-1048574, 1048574], optional)
   :type prev_frame: int
   :param next_frame: Next Keyframe, Frame number of keyframe immediately after the current frame (in [-1048574, 1048574], optional)
   :type next_frame: int
   :param channels: Channels, Set of properties that are affected (optional)

      - ``ALL``
        All Properties -- All properties, including transforms, bendy bone shape, and custom properties.
      - ``LOC``
        Location -- Location only.
      - ``ROT``
        Rotation -- Rotation only.
      - ``SIZE``
        Scale -- Scale only.
      - ``BBONE``
        Bendy Bone -- Bendy Bone shape properties.
      - ``CUSTOM``
        Custom Properties -- Custom properties.
   :type channels: Literal['ALL', 'LOC', 'ROT', 'SIZE', 'BBONE', 'CUSTOM']
   :param axis_lock: Axis Lock, Transform axis to restrict effects to (optional)

      - ``FREE``
        Free -- All axes are affected.
      - ``X``
        X -- Only X-axis transforms are affected.
      - ``Y``
        Y -- Only Y-axis transforms are affected.
      - ``Z``
        Z -- Only Z-axis transforms are affected.
   :type axis_lock: Literal['FREE', 'X', 'Y', 'Z']
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: quaternions_flip()

   Flip quaternion values to achieve desired rotations, while maintaining the same orientations

   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]
.. function:: relax(*, factor=0.5, prev_frame=0, next_frame=0, channels='ALL', axis_lock='FREE')

   Make the current pose more similar to its breakdown pose

   :param factor: Factor, Weighting factor for which keyframe is favored more (in [0, 1], optional)
   :type factor: float
   :param prev_frame: Previous Keyframe, Frame number of keyframe immediately before the current frame (in [-1048574, 1048574], optional)
   :type prev_frame: int
   :param next_frame: Next Keyframe, Frame number of keyframe immediately after the current frame (in [-1048574, 1048574], optional)
   :type next_frame: int
   :param channels: Channels, Set of properties that are affected (optional)

      - ``ALL``
        All Properties -- All properties, including transforms, bendy bone shape, and custom properties.
      - ``LOC``
        Location -- Location only.
      - ``ROT``
        Rotation -- Rotation only.
      - ``SIZE``
        Scale -- Scale only.
      - ``BBONE``
        Bendy Bone -- Bendy Bone shape properties.
      - ``CUSTOM``
        Custom Properties -- Custom properties.
   :type channels: Literal['ALL', 'LOC', 'ROT', 'SIZE', 'BBONE', 'CUSTOM']
   :param axis_lock: Axis Lock, Transform axis to restrict effects to (optional)

      - ``FREE``
        Free -- All axes are affected.
      - ``X``
        X -- Only X-axis transforms are affected.
      - ``Y``
        Y -- Only Y-axis transforms are affected.
      - ``Z``
        Z -- Only Z-axis transforms are affected.
   :type axis_lock: Literal['FREE', 'X', 'Y', 'Z']
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: reveal(*, select=True)

   Reveal all bones hidden in Pose Mode

   :param select: Select, (optional)
   :type select: bool
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: rot_clear()

   Reset rotations of selected bones to their default values

   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]
.. function:: rotation_mode_set(*, type='QUATERNION')

   Set the rotation representation used by selected bones

   :param type: Rotation Mode, (optional)
   :type type: Literal[:ref:`rna_enum_object_rotation_mode_items`]
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: scale_clear()

   Reset scaling of selected bones to their default values

   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]
.. function:: select_all(*, action='TOGGLE')

   Toggle selection status of all bones

   :param action: Action, Selection action to execute (optional)

      - ``TOGGLE``
        Toggle -- Toggle selection for all elements.
      - ``SELECT``
        Select -- Select all elements.
      - ``DESELECT``
        Deselect -- Deselect all elements.
      - ``INVERT``
        Invert -- Invert selection of all elements.
   :type action: Literal['TOGGLE', 'SELECT', 'DESELECT', 'INVERT']
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: select_constraint_target()

   Select bones used as targets for the currently selected bones

   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]
.. function:: select_grouped(*, extend=False, type='COLLECTION')

   Select all visible bones grouped by similar properties

   :param extend: Extend, Extend selection instead of deselecting everything first (optional)
   :type extend: bool
   :param type: Type, (optional)

      - ``COLLECTION``
        Collection -- Same collections as the active bone.
      - ``COLOR``
        Color -- Same color as the active bone.
      - ``KEYINGSET``
        Keying Set -- All bones affected by active Keying Set.
      - ``CHILDREN``
        Children -- Select all children of currently selected bones.
      - ``CHILDREN_IMMEDIATE``
        Immediate Children -- Select direct children of currently selected bones.
      - ``PARENT``
        Parents -- Select the parents of currently selected bones.
      - ``SIBLINGS``
        Siblings -- Select all bones that have the same parent as currently selected bones.
   :type type: Literal['COLLECTION', 'COLOR', 'KEYINGSET', 'CHILDREN', 'CHILDREN_IMMEDIATE', 'PARENT', 'SIBLINGS']
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: select_hierarchy(*, direction='PARENT', extend=False)

   Select immediate parent/children of selected bones

   :param direction: Direction, (optional)
   :type direction: Literal['PARENT', 'CHILD']
   :param extend: Extend, Extend the selection (optional)
   :type extend: bool
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: select_linked()

   Select all bones linked by connected parent/child relationships from the current selection

   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]
.. function:: select_linked_pick(*, extend=False)

   Select bones linked by connected parent/child relationships under the mouse cursor

   :param extend: Extend, Extend selection instead of deselecting everything first (optional)
   :type extend: bool
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: select_mirror(*, only_active=False, extend=False)

   Mirror the bone selection

   :param only_active: Active Only, Only operate on the active bone (optional)
   :type only_active: bool
   :param extend: Extend, Extend the selection (optional)
   :type extend: bool
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: select_parent()

   Select bones that are parents of the currently selected bones

   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]
.. function:: selection_set_add()

   Create a new empty Selection Set

   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]
   :File: `startup/bl_operators/bone_selection_sets.py\:147 <https://projects.blender.org/blender/blender/src/branch/main/scripts/startup/bl_operators/bone_selection_sets.py#L147>`__

.. function:: selection_set_add_and_assign()

   Create a new Selection Set with the currently selected bones

   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]
   :File: `startup/bl_operators/bone_selection_sets.py\:278 <https://projects.blender.org/blender/blender/src/branch/main/scripts/startup/bl_operators/bone_selection_sets.py#L278>`__

.. function:: selection_set_assign()

   Add selected bones to Selection Set

   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]
   :File: `startup/bl_operators/bone_selection_sets.py\:194 <https://projects.blender.org/blender/blender/src/branch/main/scripts/startup/bl_operators/bone_selection_sets.py#L194>`__

.. function:: selection_set_copy()

   Copy the selected Selection Set(s) to the clipboard

   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]
   :File: `startup/bl_operators/bone_selection_sets.py\:290 <https://projects.blender.org/blender/blender/src/branch/main/scripts/startup/bl_operators/bone_selection_sets.py#L290>`__

.. function:: selection_set_delete_all()

   Remove all Selection Sets from this Armature

   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]
   :File: `startup/bl_operators/bone_selection_sets.py\:77 <https://projects.blender.org/blender/blender/src/branch/main/scripts/startup/bl_operators/bone_selection_sets.py#L77>`__

.. function:: selection_set_deselect()

   Remove Selection Set bones from current selection

   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]
   :File: `startup/bl_operators/bone_selection_sets.py\:261 <https://projects.blender.org/blender/blender/src/branch/main/scripts/startup/bl_operators/bone_selection_sets.py#L261>`__

.. function:: selection_set_move(*, direction='UP')

   Move the active Selection Set up/down the list of sets

   :param direction: Move Direction, Direction to move the active Selection Set: UP (default) or DOWN (optional)
   :type direction: Literal['UP', 'DOWN']
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]
   :File: `startup/bl_operators/bone_selection_sets.py\:126 <https://projects.blender.org/blender/blender/src/branch/main/scripts/startup/bl_operators/bone_selection_sets.py#L126>`__


.. function:: selection_set_paste()

   Add new Selection Set(s) from the clipboard

   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]
   :File: `startup/bl_operators/bone_selection_sets.py\:302 <https://projects.blender.org/blender/blender/src/branch/main/scripts/startup/bl_operators/bone_selection_sets.py#L302>`__

.. function:: selection_set_remove()

   Remove a Selection Set from this Armature

   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]
   :File: `startup/bl_operators/bone_selection_sets.py\:165 <https://projects.blender.org/blender/blender/src/branch/main/scripts/startup/bl_operators/bone_selection_sets.py#L165>`__

.. function:: selection_set_remove_bones()

   Remove the selected bones from all Selection Sets

   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]
   :File: `startup/bl_operators/bone_selection_sets.py\:89 <https://projects.blender.org/blender/blender/src/branch/main/scripts/startup/bl_operators/bone_selection_sets.py#L89>`__

.. function:: selection_set_select(*, selection_set_index=-1)

   Select the bones from this Selection Set

   :param selection_set_index: Selection Set Index, Which Selection Set to select; -1 uses the active Selection Set (in [-inf, inf], optional)
   :type selection_set_index: int
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]
   :File: `startup/bl_operators/bone_selection_sets.py\:239 <https://projects.blender.org/blender/blender/src/branch/main/scripts/startup/bl_operators/bone_selection_sets.py#L239>`__


.. function:: selection_set_unassign()

   Remove selected bones from Selection Set

   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]
   :File: `startup/bl_operators/bone_selection_sets.py\:213 <https://projects.blender.org/blender/blender/src/branch/main/scripts/startup/bl_operators/bone_selection_sets.py#L213>`__

.. function:: transforms_clear()

   Reset location, rotation, and scaling of selected bones to their default values

   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]
.. function:: user_transforms_clear(*, only_selected=True)

   Reset pose bone transforms to keyframed state

   :param only_selected: Only Selected, Only visible/selected bones (optional)
   :type only_selected: bool
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: visual_transform_apply()

   Apply final constrained position of pose bones to their transform

   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]
