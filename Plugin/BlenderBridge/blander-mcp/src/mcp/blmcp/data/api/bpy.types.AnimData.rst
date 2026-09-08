AnimData(bpy_struct)
====================

.. currentmodule:: bpy.types

base class --- :class:`bpy_struct`

.. class:: AnimData(bpy_struct)

   Animation data for data-block

   .. attribute:: action

      Active Action for this data-block

      :type: :class:`Action` | None

   .. attribute:: action_blend_type

      Method used for combining Active Action's result with result of NLA stack (default ``'REPLACE'``)

      - ``REPLACE``
        Replace -- The strip values replace the accumulated results by amount specified by influence.
      - ``COMBINE``
        Combine -- The strip values are combined with accumulated results by appropriately using addition, multiplication, or quaternion math, based on channel type.
      - ``ADD``
        Add -- Weighted result of strip is added to the accumulated results.
      - ``SUBTRACT``
        Subtract -- Weighted result of strip is removed from the accumulated results.
      - ``MULTIPLY``
        Multiply -- Weighted result of strip is multiplied with the accumulated results.

      :type: Literal['REPLACE', 'COMBINE', 'ADD', 'SUBTRACT', 'MULTIPLY']

   .. attribute:: action_extrapolation

      Action to take for gaps past the Active Action's range (when evaluating with NLA) (default ``'HOLD'``)

      - ``NOTHING``
        Nothing -- Strip has no influence past its extents.
      - ``HOLD``
        Hold -- Hold the first frame if no previous strips in track, and always hold last frame.
      - ``HOLD_FORWARD``
        Hold Forward -- Only hold last frame.

      :type: Literal['NOTHING', 'HOLD', 'HOLD_FORWARD']

   .. attribute:: action_influence

      Amount the Active Action contributes to the result of the NLA stack (in [0, 1], default 1.0)

      :type: float

   .. attribute:: action_slot

      The slot identifies which sub-set of the Action is considered to be for this data-block, and its name is used to find the right slot when assigning an Action

      :type: :class:`ActionSlot` | None

   .. attribute:: action_slot_handle

      A number that identifies which sub-set of the Action is considered to be for this data-block (in [-inf, inf], default 0)

      :type: int

   .. attribute:: action_slot_handle_tweak_storage

      Storage to temporarily hold the main action slot while in tweak mode (in [-inf, inf], default 0)

      :type: int

   .. data:: action_suitable_slots

      The list of slots in this animation data-block (default None, readonly)

      :type: :class:`bpy_prop_collection`\ [:class:`ActionSlot`]

   .. attribute:: action_tweak_storage

      Storage to temporarily hold the main action while in tweak mode

      :type: :class:`Action` | None

   .. data:: drivers

      The Drivers/Expressions for this data-block (default None, readonly)

      :type: :class:`AnimDataDrivers`\ [:class:`FCurve`]

   .. attribute:: last_slot_identifier

      The identifier of the most recently assigned action slot. The slot identifies which sub-set of the Action is considered to be for this data-block, and its identifier is used to find the right slot when assigning an Action. (default "", never None)

      :type: str

   .. data:: nla_tracks

      NLA Tracks (i.e. Animation Layers) (default None, readonly)

      :type: :class:`NlaTracks`\ [:class:`NlaTrack`]

   .. attribute:: use_nla

      NLA stack is evaluated when evaluating this block (default True)

      :type: bool

   .. attribute:: use_pin

      (default False)

      :type: bool

   .. attribute:: use_tweak_mode

      Whether to enable or disable tweak mode in NLA (default False)

      :type: bool

   .. method:: nla_tweak_strip_time_to_scene(frame, *, invert=False)

      Convert a time value from the local time of the tweaked strip to scene time, exactly as done by built-in key editing tools. Returns the input time unchanged if not tweaking.

      :param frame: Input time (in [-1.04857e+06, 1.04857e+06])
      :type frame: float
      :param invert: Invert, Convert scene time to action time (optional)
      :type invert: bool
      :return: Converted time (in [-1.04857e+06, 1.04857e+06])
      :rtype: float

   .. method:: fix_paths_rename_all(*, prefix="", old_name="", new_name="")

      Rename the property paths in the animation system, since properties are animated via string paths, it's needed to keep them valid after properties has been renamed

      :param prefix: Prefix, Name prefix (optional, never None)
      :type prefix: str
      :param old_name: Old Name, Old name (optional, never None)
      :type old_name: str
      :param new_name: New Name, New name (optional, never None)
      :type new_name: str

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

   - :class:`Annotation.animation_data`
   - :class:`Armature.animation_data`
   - :class:`CacheFile.animation_data`
   - :class:`Camera.animation_data`
   - :class:`Curve.animation_data`
   - :class:`Curves.animation_data`
   - :class:`FreestyleLineStyle.animation_data`
   - :class:`GreasePencil.animation_data`
   - :class:`ID.animation_data_create`
   - :class:`Key.animation_data`
   - :class:`Lattice.animation_data`
   - :class:`Light.animation_data`
   - :class:`LightProbe.animation_data`
   - :class:`Mask.animation_data`
   - :class:`Material.animation_data`
   - :class:`Mesh.animation_data`
   - :class:`MetaBall.animation_data`
   - :class:`MovieClip.animation_data`
   - :class:`NodeTree.animation_data`
   - :class:`Object.animation_data`
   - :class:`ParticleSettings.animation_data`
   - :class:`PointCloud.animation_data`
   - :class:`Scene.animation_data`
   - :class:`Speaker.animation_data`
   - :class:`Texture.animation_data`
   - :class:`Volume.animation_data`
   - :class:`World.animation_data`

