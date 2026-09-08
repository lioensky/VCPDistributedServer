Texture(ID)
===========

.. currentmodule:: bpy.types

base classes --- :class:`bpy_struct`, :class:`ID`

subclasses --- 
:class:`BlendTexture`, :class:`CloudsTexture`, :class:`DistortedNoiseTexture`, :class:`ImageTexture`, :class:`MagicTexture`, :class:`MarbleTexture`, :class:`MusgraveTexture`, :class:`NoiseTexture`, :class:`StucciTexture`, :class:`VoronoiTexture`, :class:`WoodTexture`

.. class:: Texture(ID)

   Texture data-block used by materials, lights, worlds and brushes

   .. data:: animation_data

      Animation data for this data-block (readonly)

      :type: :class:`AnimData` | None

   .. data:: color_ramp

      (readonly)

      :type: :class:`ColorRamp` | None

   .. attribute:: contrast

      Adjust the contrast of the texture (in [0, 5], default 1.0)

      :type: float

   .. attribute:: factor_blue

      (in [0, 2], default 1.0)

      :type: float

   .. attribute:: factor_green

      (in [0, 2], default 1.0)

      :type: float

   .. attribute:: factor_red

      (in [0, 2], default 1.0)

      :type: float

   .. attribute:: intensity

      Adjust the brightness of the texture (in [0, 2], default 1.0)

      :type: float

   .. data:: node_tree

      Node tree for node-based textures (readonly)

      :type: :class:`NodeTree` | None

   .. attribute:: saturation

      Adjust the saturation of colors in the texture (in [0, 2], default 1.0)

      :type: float

   .. attribute:: type

      (default ``'IMAGE'``)

      :type: Literal[:ref:`rna_enum_texture_type_items`]

   .. attribute:: use_clamp

      Set negative texture RGB and intensity values to zero, for some uses like displacement this option can be disabled to get the full range (default False)

      :type: bool

   .. attribute:: use_color_ramp

      Map the texture intensity to the color ramp. Note that the alpha value is used for image textures, enable "Calculate Alpha" for images without an alpha channel. (default False)

      :type: bool

   .. attribute:: use_nodes

      Make this a node-based texture (default False)

      :type: bool

   .. attribute:: use_preview_alpha

      Show Alpha in Preview Render (default False)

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

   .. method:: evaluate(value)

      Evaluate the texture at the given coordinate and returns the result

      :param value: The coordinates (x,y,z) of the texture, in case of a 3D texture, the z value is the slice of the texture that is evaluated. For 2D textures such as images, the z value is ignored., (array of 3 items, in [-inf, inf])
      :type value: :class:`mathutils.Vector` | Sequence[float]
      :return: The result of the texture where (x,y,z,w) are (red, green, blue, intensity). For grayscale textures, often intensity only will be used., (array of 4 items, in [-inf, inf])
      :rtype: :class:`mathutils.Vector`

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

   - :mod:`bpy.context.texture`
   - :class:`BlendData.textures`
   - :class:`BlendDataTextures.new`
   - :class:`BlendDataTextures.remove`
   - :class:`Brush.mask_texture`
   - :class:`Brush.texture`
   - :class:`DisplaceModifier.texture`
   - :class:`DynamicPaintSurface.init_texture`
   - :class:`FieldSettings.texture`
   - :class:`FluidFlowSettings.noise_texture`
   - :class:`FreestyleLineStyle.active_texture`
   - :class:`NodeSocketTexture.default_value`
   - :class:`NodeTreeInterfaceSocketTexture.default_value`
   - :class:`ParticleSettings.active_texture`
   - :class:`TextureNodeTexture.texture`
   - :class:`TextureSlot.texture`
   - :class:`VertexWeightEditModifier.mask_texture`
   - :class:`VertexWeightMixModifier.mask_texture`
   - :class:`VertexWeightProximityModifier.mask_texture`
   - :class:`VolumeDisplaceModifier.texture`
   - :class:`WarpModifier.texture`
   - :class:`WaveModifier.texture`

