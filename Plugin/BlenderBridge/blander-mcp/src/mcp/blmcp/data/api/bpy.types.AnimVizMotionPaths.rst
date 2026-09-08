AnimVizMotionPaths(bpy_struct)
==============================

.. currentmodule:: bpy.types

base class --- :class:`bpy_struct`

.. class:: AnimVizMotionPaths(bpy_struct)

   Motion Path settings for animation visualization

   .. attribute:: bake_location

      When calculating Bone Paths, use Head or Tips (default ``'TAILS'``)

      :type: Literal[:ref:`rna_enum_motionpath_bake_location_items`]

   .. attribute:: frame_after

      Number of frames to show after the current frame (only for 'Around Frame' Onion-skinning method) (in [1, 524287], default 0)

      :type: int

   .. attribute:: frame_before

      Number of frames to show before the current frame (only for 'Around Frame' Onion-skinning method) (in [1, 524287], default 0)

      :type: int

   .. attribute:: frame_end

      End frame of range of paths to display/calculate (not for 'Around Frame' Onion-skinning method) (in [-inf, inf], default 0)

      :type: int

   .. attribute:: frame_start

      Starting frame of range of paths to display/calculate (not for 'Around Frame' Onion-skinning method) (in [-inf, inf], default 0)

      :type: int

   .. attribute:: frame_step

      Number of frames between paths shown (not for 'On Keyframes' Onion-skinning method) (in [1, 100], default 0)

      :type: int

   .. data:: has_motion_paths

      Are there any bone paths that will need updating (read-only) (default False, readonly)

      :type: bool

   .. attribute:: range

      Type of range to calculate for Motion Paths (default ``'SCENE'``)

      :type: Literal[:ref:`rna_enum_motionpath_range_items`]

   .. attribute:: show_frame_numbers

      Show frame numbers on Motion Paths (default False)

      :type: bool

   .. attribute:: show_keyframe_action_all

      For bone motion paths, search whole Action for keyframes instead of in group with matching name only (is slower) (default False)

      :type: bool

   .. attribute:: show_keyframe_highlight

      Emphasize position of keyframes on Motion Paths (default False)

      :type: bool

   .. attribute:: show_keyframe_numbers

      Show frame numbers of Keyframes on Motion Paths (default False)

      :type: bool

   .. attribute:: type

      Type of range to show for Motion Paths (default ``'RANGE'``)

      :type: Literal[:ref:`rna_enum_motionpath_display_type_items`]

   .. attribute:: use_camera_space_bake

      Motion path points will be baked into the camera space of the active camera. This means they will only look right when looking through that camera. Switching cameras using markers is not supported. (default False)

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

   - :class:`AnimViz.motion_path`

