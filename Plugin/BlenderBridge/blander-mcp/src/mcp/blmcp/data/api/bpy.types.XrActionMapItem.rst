XrActionMapItem(bpy_struct)
===========================

.. currentmodule:: bpy.types

base class --- :class:`bpy_struct`

.. class:: XrActionMapItem(bpy_struct)


   .. attribute:: bimanual

      The action depends on the states/poses of both user paths (default False)

      :type: bool

   .. data:: bindings

      Bindings for the action map item, mapping the action to an XR input (default None, readonly)

      :type: :class:`XrActionMapBindings`\ [:class:`XrActionMapBinding`]

   .. attribute:: haptic_amplitude

      Intensity of the haptic vibration, ranging from 0.0 to 1.0 (in [0, 1], default 0.0)

      :type: float

   .. attribute:: haptic_duration

      Haptic duration in seconds. 0.0 is the minimum supported duration. (in [0, inf], default 0.0)

      :type: float

   .. attribute:: haptic_frequency

      Frequency of the haptic vibration in hertz. 0.0 specifies the OpenXR runtime's default frequency. (in [0, inf], default 0.0)

      :type: float

   .. attribute:: haptic_match_user_paths

      Apply haptics to the same user paths for the haptic action and this action (default False)

      :type: bool

   .. attribute:: haptic_mode

      Haptic application mode (default ``'PRESS'``)

      - ``PRESS``
        Press -- Apply haptics on button press.
      - ``RELEASE``
        Release -- Apply haptics on button release.
      - ``PRESS_RELEASE``
        Press Release -- Apply haptics on button press and release.
      - ``REPEAT``
        Repeat -- Apply haptics repeatedly for the duration of the button press.

      :type: Literal['PRESS', 'RELEASE', 'PRESS_RELEASE', 'REPEAT']

   .. attribute:: haptic_name

      Name of the haptic action to apply when executing this action (default "", never None)

      :type: str

   .. attribute:: name

      Name of the action map item (default "", never None)

      :type: str

   .. attribute:: op

      Identifier of operator to call on action event (default "", never None)

      :type: str

   .. attribute:: op_mode

      Operator execution mode (default ``'PRESS'``)

      - ``PRESS``
        Press -- Execute operator on button press (non-modal operators only).
      - ``RELEASE``
        Release -- Execute operator on button release (non-modal operators only).
      - ``MODAL``
        Modal -- Use modal execution (modal operators only).

      :type: Literal['PRESS', 'RELEASE', 'MODAL']

   .. data:: op_name

      Name of operator (translated) to call on action event (default "", readonly, never None)

      :type: str

   .. data:: op_properties

      Properties to set when the operator is called (readonly)

      :type: :class:`OperatorProperties` | None

   .. attribute:: pose_is_controller_aim

      The action poses will be used for the VR controller aims (default False)

      :type: bool

   .. attribute:: pose_is_controller_grip

      The action poses will be used for the VR controller grips (default False)

      :type: bool

   .. attribute:: selected_binding

      Currently selected binding (in [-32768, 32767], default 0)

      :type: int

   .. attribute:: type

      Action type (default ``'FLOAT'``)

      - ``FLOAT``
        Float -- Float action, representing either a digital or analog button.
      - ``VECTOR2D``
        Vector2D -- 2D float vector action, representing a thumbstick or trackpad.
      - ``POSE``
        Pose -- 3D pose action, representing a controller's location and rotation.
      - ``VIBRATION``
        Vibration -- Haptic vibration output action, to be applied with a duration, frequency, and amplitude.

      :type: Literal['FLOAT', 'VECTOR2D', 'POSE', 'VIBRATION']

   .. data:: user_paths

      OpenXR user paths (default None, readonly)

      :type: :class:`XrUserPaths`\ [:class:`XrUserPath`]

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

   - :class:`XrActionMap.actionmap_items`
   - :class:`XrActionMapItems.find`
   - :class:`XrActionMapItems.new`
   - :class:`XrActionMapItems.new_from_item`
   - :class:`XrActionMapItems.new_from_item`
   - :class:`XrActionMapItems.remove`
   - :class:`XrSessionState.action_binding_create`
   - :class:`XrSessionState.action_create`

