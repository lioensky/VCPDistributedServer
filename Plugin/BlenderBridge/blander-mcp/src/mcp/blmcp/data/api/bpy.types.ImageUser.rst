ImageUser(bpy_struct)
=====================

.. currentmodule:: bpy.types

base class --- :class:`bpy_struct`

.. class:: ImageUser(bpy_struct)

   Parameters defining how an Image data-block is used by another data-block

   .. attribute:: frame_current

      Current frame number in image sequence or movie (in [-1048574, 1048574], default 0)

      :type: int

   .. attribute:: frame_duration

      Number of images of a movie to use (in [0, 1048574], default 0)

      :type: int

   .. attribute:: frame_offset

      Offset the number of the frame to use in the animation (in [-inf, inf], default 0)

      :type: int

   .. attribute:: frame_start

      Global starting frame of the movie/sequence, assuming first picture has a #1 (in [-1048574, 1048574], default 0)

      :type: int

   .. data:: multilayer_layer

      Layer in multilayer image (in [0, 32767], default 0, readonly)

      :type: int

   .. data:: multilayer_pass

      Pass in multilayer image (in [0, 32767], default 0, readonly)

      :type: int

   .. data:: multilayer_view

      View in multilayer image (in [0, 32767], default 0, readonly)

      :type: int

   .. attribute:: tile

      Tile in tiled image (in [0, inf], default 0)

      :type: int

   .. attribute:: use_auto_refresh

      Always refresh image on frame changes (default False)

      :type: bool

   .. attribute:: use_cyclic

      Cycle the images in the movie (default False)

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

   - :class:`CameraBackgroundImage.image_user`
   - :class:`Image.filepath_from_user`
   - :class:`ImageTexture.image_user`
   - :class:`Object.image_user`
   - :class:`RenderSlot.clear`
   - :class:`ShaderNodeTexEnvironment.image_user`
   - :class:`ShaderNodeTexImage.image_user`
   - :class:`SpaceImageEditor.image_user`
   - :class:`TextureNodeImage.image_user`
   - :class:`UILayout.template_image`
   - :class:`UILayout.template_image_layers`

