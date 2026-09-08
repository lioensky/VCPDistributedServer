Action(ID)
==========

.. currentmodule:: bpy.types

base classes --- :class:`bpy_struct`, :class:`ID`

.. class:: Action(ID)

   A collection of F-Curves for animation

   .. data:: curve_frame_range

      The combined frame range of all F-Curves within this action (array of 2 items, in [-inf, inf], default (0.0, 0.0), readonly)

      :type: :class:`mathutils.Vector`

   .. attribute:: frame_end

      The end frame of the manually set intended playback range (in [-1.04857e+06, 1.04857e+06], default 0.0)

      :type: float

   .. attribute:: frame_range

      The intended playback frame range of this action, using the manually set range if available, or the combined frame range of all F-Curves within this action if not (assigning sets the manual frame range) (array of 2 items, in [-inf, inf], default (0.0, 0.0))

      :type: :class:`mathutils.Vector`

   .. attribute:: frame_start

      The start frame of the manually set intended playback range (in [-1.04857e+06, 1.04857e+06], default 0.0)

      :type: float

   .. data:: is_action_layered

      Return whether this is a layered Action. At this point all actions are layered through versioning and this function will always return true (default False, readonly)

      :type: bool

   .. data:: is_action_legacy

      Return whether this is a legacy Action. Legacy Actions have no layers or slots. Since Blender 4.4 actions are automatically updated to layered actions. This will only return true on empty actions (default False, readonly)

      :type: bool

   .. data:: is_empty

      False when there is any Layer, Slot, or legacy F-Curve (default False, readonly)

      :type: bool

   .. data:: layers

      The list of layers that make up this Action (default None, readonly)

      :type: :class:`ActionLayers`\ [:class:`ActionLayer`]

   .. data:: pose_markers

      Markers specific to this action, for labeling poses (default None, readonly)

      :type: :class:`ActionPoseMarkers`\ [:class:`TimelineMarker`]

   .. data:: slots

      The list of slots in this Action (default None, readonly)

      :type: :class:`ActionSlots`\ [:class:`ActionSlot`]

   .. attribute:: use_cyclic

      The action is intended to be used as a cycle looping over its manually set playback frame range (enabling this does not automatically make it loop) (default False)

      :type: bool

   .. attribute:: use_frame_range

      Manually specify the intended playback frame range for the action (this range is used by some tools, but does not affect animation evaluation) (default False)

      :type: bool

   .. method:: deselect_keys()

      Deselects all keys of the Action. The selection status of F-Curves is unchanged.


   .. method:: fcurve_ensure_for_datablock(datablock, data_path, *, index=0, group_name="")

      Ensure that an F-Curve exists, with the given data path and array index, for the given data-block. This action must already be assigned to the data-block. This function will also create the layer, keyframe strip, and action slot if necessary, and take care of assigning the action slot too

      :param datablock: The data-block animated by this action, for which to ensure the F-Curve exists. This action must already be assigned to the data-block (never None)
      :type datablock: :class:`ID` | None
      :param data_path: Data Path, F-Curve data path (never None)
      :type data_path: str
      :param index: Index, Array index (in [0, inf], optional)
      :type index: int
      :param group_name: Group Name, Name of the group for this F-Curve, if any. If the F-Curve already exists, this parameter is ignored (optional, never None)
      :type group_name: str
      :return: The found or created F-Curve
      :rtype: :class:`FCurve`

   .. method:: flip_with_pose(object)

      Flip the action around the X axis using a pose

      :param object: The reference armature object to use when flipping (never None)
      :type object: :class:`Object` | None

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
   - :class:`ID.name`
   - :class:`ID.name_full`
   - :class:`ID.id_type`
   - :class:`ID.session_uid`
   - :class:`ID.is_evaluated`
   - :class:`ID.original`
   - :class:`ID.users`
   - :class:`ID.use_fake_user`
   - :class:`ID.use_extra_user`
   - :class:`ID.is_embedded_data`
   - :class:`ID.is_linked_packed`
   - :class:`ID.is_missing`
   - :class:`ID.is_runtime_data`
   - :class:`ID.is_editable`
   - :class:`ID.tag`
   - :class:`ID.is_library_indirect`
   - :class:`ID.library`
   - :class:`ID.library_weak_reference`
   - :class:`ID.asset_data`
   - :class:`ID.override_library`
   - :class:`ID.preview`

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
   - :class:`ID.bl_system_properties_get`
   - :class:`ID.rename`
   - :class:`ID.evaluated_get`
   - :class:`ID.copy`
   - :class:`ID.asset_mark`
   - :class:`ID.asset_clear`
   - :class:`ID.asset_generate_preview`
   - :class:`ID.override_create`
   - :class:`ID.override_hierarchy_create`
   - :class:`ID.user_clear`
   - :class:`ID.user_remap`
   - :class:`ID.make_local`
   - :class:`ID.user_of_id`
   - :class:`ID.animation_data_create`
   - :class:`ID.animation_data_clear`
   - :class:`ID.update_tag`
   - :class:`ID.preview_ensure`
   - :class:`ID.bl_rna_get_subclass`
   - :class:`ID.bl_rna_get_subclass_py`

References
----------

.. hlist::
   :columns: 2

   - :mod:`bpy.context.active_action`
   - :mod:`bpy.context.selected_editable_actions`
   - :mod:`bpy.context.selected_visible_actions`
   - :class:`ActionConstraint.action`
   - :class:`AnimData.action`
   - :class:`AnimData.action_tweak_storage`
   - :class:`BlendData.actions`
   - :class:`BlendDataActions.new`
   - :class:`BlendDataActions.remove`
   - :class:`GLTF2_filter_action.action`
   - :class:`NlaStrip.action`
   - :class:`NlaStrips.new`
   - :class:`Pose.apply_pose_from_action`
   - :class:`Pose.backup_create`
   - :class:`Pose.blend_pose_from_action`
   - :class:`WindowManager.poselib_previous_action`

