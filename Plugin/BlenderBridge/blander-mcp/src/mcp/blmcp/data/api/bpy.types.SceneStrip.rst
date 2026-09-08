SceneStrip(Strip)
=================

.. currentmodule:: bpy.types

base classes --- :class:`bpy_struct`, :class:`Strip`

.. class:: SceneStrip(Strip)

   Sequence strip using the rendered image of a scene

   .. attribute:: alpha_mode

      Representation of alpha information in the RGBA pixels (default ``'STRAIGHT'``)

      - ``STRAIGHT``
        Straight -- RGB channels in transparent pixels are unaffected by the alpha channel.
      - ``PREMUL``
        Premultiplied -- RGB channels in transparent pixels are multiplied by the alpha channel.

      :type: Literal['STRAIGHT', 'PREMUL']

   .. attribute:: animation_offset_end

      Animation end offset (trim end) (in [0, inf], default 0)

      .. deprecated:: 5.10 removal planned in version 6.0

         Replaced by '.content_trim_end'.

      :type: int

   .. attribute:: animation_offset_start

      Animation start offset (trim start) (in [0, inf], default 0)

      .. deprecated:: 5.10 removal planned in version 6.0

         Replaced by '.content_trim_start'.

      :type: int

   .. attribute:: color_multiply

      (in [0, 20], default 1.0)

      :type: float

   .. attribute:: color_saturation

      Adjust the intensity of the input's color (in [0, 20], default 1.0)

      :type: float

   .. attribute:: content_trim_end

      Number of frames to ignore from the end of the underlying source. The source content is trimmed, and future frames are turned into holds (in [0, inf], default 0)

      :type: int

   .. attribute:: content_trim_start

      Number of frames to ignore from the start of the underlying source. The source content is trimmed, and previous frames are turned into holds (in [0, inf], default 0)

      :type: int

   .. data:: crop

      (readonly)

      :type: :class:`StripCrop` | None

   .. data:: fps

      Frames per second (in [-inf, inf], default 0.0, readonly)

      :type: float

   .. attribute:: multiply_alpha

      Multiply alpha along with color channels (default False)

      :type: bool

   .. data:: proxy

      (readonly)

      :type: :class:`StripProxy` | None

   .. data:: retiming_keys

      (default None, readonly)

      :type: :class:`RetimingKeys`\ [:class:`RetimingKey`]

   .. attribute:: scene

      Scene that this strip uses

      :type: :class:`Scene` | None

   .. attribute:: scene_camera

      Override the scene's active camera

      :type: :class:`Object` | None

   .. attribute:: scene_input

      Input type to use for the Scene strip (default ``'CAMERA'``)

      - ``CAMERA``
        Camera -- Use the Scene's 3D camera as input.
      - ``SEQUENCER``
        Sequencer -- Use the Scene's Sequencer timeline as input.

      :type: Literal['CAMERA', 'SEQUENCER']

   .. attribute:: strobe

      Only display every nth frame (in [1, 30], default 0.0)

      :type: float

   .. data:: transform

      (readonly)

      :type: :class:`StripTransform` | None

   .. attribute:: use_annotations

      Show Annotations in OpenGL previews (default True)

      :type: bool

   .. attribute:: use_deinterlace

      Remove fields from video movies (default False)

      :type: bool

   .. attribute:: use_flip_x

      Flip on the X axis (default False)

      :type: bool

   .. attribute:: use_flip_y

      Flip on the Y axis (default False)

      :type: bool

   .. attribute:: use_float

      Convert input to float data (default False)

      :type: bool

   .. attribute:: use_proxy

      Use a preview proxy and/or time-code index for this strip (default False)

      :type: bool

   .. attribute:: use_reverse_frames

      Reverse frame order (default False)

      :type: bool

   .. attribute:: volume

      Playback volume of the sound (in [0, 100], default 1.0)

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
   - :class:`Strip.name`
   - :class:`Strip.type`
   - :class:`Strip.select`
   - :class:`Strip.select_left_handle`
   - :class:`Strip.select_right_handle`
   - :class:`Strip.mute`
   - :class:`Strip.lock`
   - :class:`Strip.frame_final_duration`
   - :class:`Strip.duration`
   - :class:`Strip.frame_duration`
   - :class:`Strip.content_duration`
   - :class:`Strip.frame_start`
   - :class:`Strip.content_start`
   - :class:`Strip.content_end`
   - :class:`Strip.frame_final_start`
   - :class:`Strip.left_handle`
   - :class:`Strip.frame_final_end`
   - :class:`Strip.right_handle`
   - :class:`Strip.frame_offset_start`
   - :class:`Strip.left_handle_offset`
   - :class:`Strip.frame_offset_end`
   - :class:`Strip.right_handle_offset`
   - :class:`Strip.channel`
   - :class:`Strip.use_linear_modifiers`
   - :class:`Strip.blend_type`
   - :class:`Strip.blend_alpha`
   - :class:`Strip.effect_fader`
   - :class:`Strip.use_default_fade`
   - :class:`Strip.color_tag`
   - :class:`Strip.modifiers`
   - :class:`Strip.show_retiming_keys`

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
   - :class:`Strip.bl_system_properties_get`
   - :class:`Strip.strip_elem_from_frame`
   - :class:`Strip.swap`
   - :class:`Strip.move_to_meta`
   - :class:`Strip.parent_meta`
   - :class:`Strip.invalidate_cache`
   - :class:`Strip.split`
   - :class:`Strip.bl_rna_get_subclass`
   - :class:`Strip.bl_rna_get_subclass_py`

