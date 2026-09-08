ActionConstraint(Constraint)
============================

.. currentmodule:: bpy.types

base classes --- :class:`bpy_struct`, :class:`Constraint`

.. class:: ActionConstraint(Constraint)

   Map an action to the transform axes of a bone

   .. attribute:: action

      The constraining action

      :type: :class:`Action` | None

   .. attribute:: action_slot

      The slot identifies which sub-set of the Action is considered to be for this strip, and its name is used to find the right slot when assigning another Action

      :type: :class:`ActionSlot` | None

   .. attribute:: action_slot_handle

      A number that identifies which sub-set of the Action is considered to be for this Action Constraint (in [-inf, inf], default 0)

      :type: int

   .. data:: action_suitable_slots

      The list of action slots suitable for this NLA strip (default None, readonly)

      :type: :class:`bpy_prop_collection`\ [:class:`ActionSlot`]

   .. attribute:: eval_time

      Interpolates between Action Start and End frames (in [0, 1], default 0.0)

      :type: float

   .. attribute:: frame_end

      Last frame of the Action to use (in [-1048574, 1048574], default 0)

      :type: int

   .. attribute:: frame_start

      First frame of the Action to use (in [-1048574, 1048574], default 0)

      :type: int

   .. attribute:: last_slot_identifier

      The identifier of the most recently assigned action slot. The slot identifies which sub-set of the Action is considered to be for this constraint, and its identifier is used to find the right slot when assigning an Action. (default "", never None)

      :type: str

   .. attribute:: max

      Maximum value for target channel range (in [-1000, 1000], default 0.0)

      :type: float

   .. attribute:: min

      Minimum value for target channel range (in [-1000, 1000], default 0.0)

      :type: float

   .. attribute:: mix_mode

      Specify how existing transformations and the action channels are combined (default ``'AFTER_FULL'``)

      - ``REPLACE``
        Replace -- Replace the original transformation with the action channels.
      - ``BEFORE_FULL``
        Before Original (Full) -- Apply the action channels before the original transformation, as if applied to an imaginary parent in Full Inherit Scale mode. Will create shear when combining rotation and non-uniform scale..
      - ``BEFORE``
        Before Original (Aligned) -- Apply the action channels before the original transformation, as if applied to an imaginary parent in Aligned Inherit Scale mode. This effectively uses Full for location and Split Channels for rotation and scale..
      - ``BEFORE_SPLIT``
        Before Original (Split Channels) -- Apply the action channels before the original transformation, handling location, rotation and scale separately.
      - ``AFTER_FULL``
        After Original (Full) -- Apply the action channels after the original transformation, as if applied to an imaginary child in Full Inherit Scale mode. Will create shear when combining rotation and non-uniform scale..
      - ``AFTER``
        After Original (Aligned) -- Apply the action channels after the original transformation, as if applied to an imaginary child in Aligned Inherit Scale mode. This effectively uses Full for location and Split Channels for rotation and scale..
      - ``AFTER_SPLIT``
        After Original (Split Channels) -- Apply the action channels after the original transformation, handling location, rotation and scale separately.

      :type: Literal['REPLACE', 'BEFORE_FULL', 'BEFORE', 'BEFORE_SPLIT', 'AFTER_FULL', 'AFTER', 'AFTER_SPLIT']

   .. attribute:: subtarget

      Armature bone, mesh or lattice vertex group, ... (default "", never None)

      :type: str

   .. attribute:: target

      Target object

      :type: :class:`Object` | None

   .. attribute:: transform_channel

      Transformation channel from the target that is used to key the Action (default ``'ROTATION_X'``)

      :type: Literal['LOCATION_X', 'LOCATION_Y', 'LOCATION_Z', 'ROTATION_X', 'ROTATION_Y', 'ROTATION_Z', 'SCALE_X', 'SCALE_Y', 'SCALE_Z']

   .. attribute:: use_bone_object_action

      Bones only: apply the object's transformation channels of the action to the constrained bone, instead of bone's channels (default False)

      :type: bool

   .. attribute:: use_eval_time

      Interpolate between Action Start and End frames, with the Evaluation Time slider instead of the Target object/bone (default False)

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

