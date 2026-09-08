ImageTexture(Texture)
=====================

.. currentmodule:: bpy.types

base classes --- :class:`bpy_struct`, :class:`ID`, :class:`Texture`

.. class:: ImageTexture(Texture)


   .. attribute:: checker_distance

      Distance between checker tiles (in [0, 0.99], default 0.0)

      :type: float

   .. attribute:: crop_max_x

      Maximum X value to crop the image (in [-10, 10], default 1.0)

      :type: float

   .. attribute:: crop_max_y

      Maximum Y value to crop the image (in [-10, 10], default 1.0)

      :type: float

   .. attribute:: crop_min_x

      Minimum X value to crop the image (in [-10, 10], default 0.0)

      :type: float

   .. attribute:: crop_min_y

      Minimum Y value to crop the image (in [-10, 10], default 0.0)

      :type: float

   .. attribute:: extension

      How the image is extrapolated past its original bounds (default ``'REPEAT'``)

      - ``EXTEND``
        Extend -- Extend by repeating edge pixels of the image.
      - ``CLIP``
        Clip -- Clip to image size and set exterior pixels as transparent.
      - ``CLIP_CUBE``
        Clip Cube -- Clip to cubic-shaped area around the image and set exterior pixels as transparent.
      - ``REPEAT``
        Repeat -- Cause the image to repeat horizontally and vertically.
      - ``CHECKER``
        Checker -- Cause the image to repeat in checker board pattern.

      :type: Literal['EXTEND', 'CLIP', 'CLIP_CUBE', 'REPEAT', 'CHECKER']

   .. attribute:: filter_size

      Multiply the filter size used by interpolation (in [0.1, 50], default 1.0)

      :type: float

   .. attribute:: image

      :type: :class:`Image` | None

   .. data:: image_user

      Parameters defining which layer, pass and frame of the image is displayed (readonly)

      :type: :class:`ImageUser` | None

   .. attribute:: invert_alpha

      Invert all the alpha values in the image (default False)

      :type: bool

   .. attribute:: repeat_x

      Repetition multiplier in the X direction (in [1, 512], default 1)

      :type: int

   .. attribute:: repeat_y

      Repetition multiplier in the Y direction (in [1, 512], default 1)

      :type: int

   .. attribute:: use_alpha

      Use the alpha channel information in the image (default True)

      :type: bool

   .. attribute:: use_calculate_alpha

      Calculate an alpha channel based on RGB values in the image (default False)

      :type: bool

   .. attribute:: use_checker_even

      Even checker tiles (default False)

      :type: bool

   .. attribute:: use_checker_odd

      Odd checker tiles (default True)

      :type: bool

   .. attribute:: use_flip_axis

      Flip the texture's X and Y axis (default False)

      :type: bool

   .. attribute:: use_interpolation

      Interpolate pixels using selected filter (default True)

      :type: bool

   .. attribute:: use_mirror_x

      Mirror the image repetition on the X direction (default False)

      :type: bool

   .. attribute:: use_mirror_y

      Mirror the image repetition on the Y direction (default False)

      :type: bool

   .. attribute:: use_normal_map

      Use image RGB values for normal mapping (default False)

      :type: bool

   .. data:: users_material

      Materials that use this texture
      
      :type: tuple[:class:`Material`, ...]
      
      .. note:: Takes ``O(len(bpy.data.materials) * len(material.texture_slots))`` time.

      (readonly)

   .. data:: users_object_modifier

      Object modifiers that use this texture
      
      :type: tuple[:class:`Object`, ...]
      
      .. note:: Takes ``O(len(bpy.data.objects) * len(obj.modifiers))`` time.

      (readonly)

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
   - :class:`Texture.type`
   - :class:`Texture.use_clamp`
   - :class:`Texture.use_color_ramp`
   - :class:`Texture.color_ramp`
   - :class:`Texture.intensity`
   - :class:`Texture.contrast`
   - :class:`Texture.saturation`
   - :class:`Texture.factor_red`
   - :class:`Texture.factor_green`
   - :class:`Texture.factor_blue`
   - :class:`Texture.use_preview_alpha`
   - :class:`Texture.use_nodes`
   - :class:`Texture.node_tree`
   - :class:`Texture.animation_data`
   - :class:`Texture.users_material`
   - :class:`Texture.users_object_modifier`

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
   - :class:`Texture.evaluate`
   - :class:`Texture.bl_rna_get_subclass`
   - :class:`Texture.bl_rna_get_subclass_py`

