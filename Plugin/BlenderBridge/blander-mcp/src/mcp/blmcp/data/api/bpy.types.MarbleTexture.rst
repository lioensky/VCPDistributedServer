MarbleTexture(Texture)
======================

.. currentmodule:: bpy.types

base classes --- :class:`bpy_struct`, :class:`ID`, :class:`Texture`

.. class:: MarbleTexture(Texture)

   Procedural noise texture

   .. attribute:: marble_type

      (default ``'SOFT'``)

      - ``SOFT``
        Soft -- Use soft marble.
      - ``SHARP``
        Sharp -- Use more clearly defined marble.
      - ``SHARPER``
        Sharper -- Use very clearly defined marble.

      :type: Literal['SOFT', 'SHARP', 'SHARPER']

   .. attribute:: nabla

      Size of derivative offset used for calculating normal (in [0.001, 0.1], default 0.025)

      :type: float

   .. attribute:: noise_basis

      Noise basis used for turbulence (default ``'BLENDER_ORIGINAL'``)

      - ``BLENDER_ORIGINAL``
        Blender Original -- Noise algorithm - Blender original: Smooth interpolated noise.
      - ``ORIGINAL_PERLIN``
        Original Perlin -- Noise algorithm - Original Perlin: Smooth interpolated noise.
      - ``IMPROVED_PERLIN``
        Improved Perlin -- Noise algorithm - Improved Perlin: Smooth interpolated noise.
      - ``VORONOI_F1``
        Voronoi F1 -- Noise algorithm - Voronoi F1: Returns distance to the closest feature point.
      - ``VORONOI_F2``
        Voronoi F2 -- Noise algorithm - Voronoi F2: Returns distance to the 2nd closest feature point.
      - ``VORONOI_F3``
        Voronoi F3 -- Noise algorithm - Voronoi F3: Returns distance to the 3rd closest feature point.
      - ``VORONOI_F4``
        Voronoi F4 -- Noise algorithm - Voronoi F4: Returns distance to the 4th closest feature point.
      - ``VORONOI_F2_F1``
        Voronoi F2-F1 -- Noise algorithm - Voronoi F1-F2.
      - ``VORONOI_CRACKLE``
        Voronoi Crackle -- Noise algorithm - Voronoi Crackle: Voronoi tessellation with sharp edges.
      - ``CELL_NOISE``
        Cell Noise -- Noise algorithm - Cell Noise: Square cell tessellation.

      :type: Literal['BLENDER_ORIGINAL', 'ORIGINAL_PERLIN', 'IMPROVED_PERLIN', 'VORONOI_F1', 'VORONOI_F2', 'VORONOI_F3', 'VORONOI_F4', 'VORONOI_F2_F1', 'VORONOI_CRACKLE', 'CELL_NOISE']

   .. attribute:: noise_basis_2

      (default ``'SIN'``)

      - ``SIN``
        Sin -- Use a sine wave to produce bands.
      - ``SAW``
        Saw -- Use a saw wave to produce bands.
      - ``TRI``
        Tri -- Use a triangle wave to produce bands.

      :type: Literal['SIN', 'SAW', 'TRI']

   .. attribute:: noise_depth

      Depth of the cloud calculation (in [0, 30], default 2)

      :type: int

   .. attribute:: noise_scale

      Scaling for noise input (in [0.0001, inf], default 0.25)

      :type: float

   .. attribute:: noise_type

      (default ``'SOFT_NOISE'``)

      - ``SOFT_NOISE``
        Soft -- Generate soft noise (smooth transitions).
      - ``HARD_NOISE``
        Hard -- Generate hard noise (sharp transitions).

      :type: Literal['SOFT_NOISE', 'HARD_NOISE']

   .. attribute:: turbulence

      Turbulence of the bandnoise and ringnoise types (in [0.0001, inf], default 5.0)

      :type: float

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

