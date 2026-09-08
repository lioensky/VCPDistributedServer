Material(ID)
============

.. currentmodule:: bpy.types

base classes --- :class:`bpy_struct`, :class:`ID`

.. class:: Material(ID)

   Material data-block to define the appearance of geometric objects for rendering

   .. attribute:: alpha_threshold

      A pixel is rendered only if its alpha value is above this threshold (in [0, 1], default 0.5)

      :type: float

   .. data:: animation_data

      Animation data for this data-block (readonly)

      :type: :class:`AnimData` | None

   .. attribute:: blend_method

      Blend Mode for Transparent Faces (Deprecated: use 'surface_render_method') (default ``'OPAQUE'``)

      - ``OPAQUE``
        Opaque -- Render surface without transparency.
      - ``CLIP``
        Alpha Clip -- Use the alpha threshold to clip the visibility (binary visibility).
      - ``HASHED``
        Alpha Hashed -- Use noise to dither the binary visibility (works well with multi-samples).
      - ``BLEND``
        Alpha Blend -- Render polygon transparent, depending on alpha channel of the texture.

      :type: Literal['OPAQUE', 'CLIP', 'HASHED', 'BLEND']

   .. attribute:: diffuse_color

      Diffuse color of the material (array of 4 items, in [0, inf], default (0.8, 0.8, 0.8, 1.0))

      :type: :class:`bpy_prop_array`\ [float]

   .. attribute:: displacement_method

      Method to use for the displacement (default ``'BUMP'``)

      - ``BUMP``
        Bump Only -- Bump mapping to simulate the appearance of displacement.
      - ``DISPLACEMENT``
        Displacement Only -- Use true displacement of surface only, requires fine subdivision.
      - ``BOTH``
        Displacement and Bump -- Combination of true displacement and bump mapping for finer detail.

      :type: Literal['BUMP', 'DISPLACEMENT', 'BOTH']

   .. data:: grease_pencil

      Grease Pencil color settings for material (readonly)

      :type: :class:`MaterialGPencilStyle` | None

   .. data:: is_grease_pencil

      True if this material has Grease Pencil data (default False, readonly)

      :type: bool

   .. attribute:: line_color

      Line color used for Freestyle line rendering (array of 4 items, in [0, inf], default (0.0, 0.0, 0.0, 0.0))

      :type: :class:`bpy_prop_array`\ [float]

   .. attribute:: line_priority

      The line color of a higher priority is used at material boundaries (in [0, 32767], default 0)

      :type: int

   .. data:: lineart

      Line Art settings for material (readonly)

      :type: :class:`MaterialLineArt` | None

   .. attribute:: max_vertex_displacement

      The max distance a vertex can be displaced. Displacements over this threshold may cause visibility issues. (in [0, inf], default 0.0)

      :type: float

   .. attribute:: metallic

      Amount of mirror reflection for raytrace (in [0, 1], default 0.0)

      :type: float

   .. data:: node_tree

      Node tree for node based materials (readonly)

      :type: :class:`NodeTree` | None

   .. attribute:: paint_active_slot

      Index of active texture paint slot (in [0, 32767], default 0)

      :type: int

   .. attribute:: paint_clone_slot

      Index of clone texture paint slot (in [0, 32767], default 0)

      :type: int

   .. attribute:: pass_index

      Index number for the "Material Index" render pass (in [0, 32767], default 0)

      :type: int

   .. attribute:: preview_render_type

      Type of preview render (default ``'SPHERE'``)

      - ``FLAT``
        Flat -- Flat XY plane.
      - ``SPHERE``
        Sphere -- Sphere.
      - ``CUBE``
        Cube -- Cube.
      - ``HAIR``
        Hair -- Hair strands.
      - ``SHADERBALL``
        Shader Ball -- Shader ball.
      - ``CLOTH``
        Cloth -- Cloth.
      - ``FLUID``
        Fluid -- Fluid.

      :type: Literal['FLAT', 'SPHERE', 'CUBE', 'HAIR', 'SHADERBALL', 'CLOTH', 'FLUID']

   .. attribute:: refraction_depth

      Approximate the thickness of the object to compute two refraction events (0 is disabled) (Deprecated) (in [0, inf], default 0.0)

      :type: float

   .. attribute:: roughness

      Roughness of the material (in [0, 1], default 0.4)

      :type: float

   .. attribute:: show_transparent_back

      Render multiple transparent layers (may introduce transparency sorting problems) (Deprecated: use 'use_tranparency_overlap') (default True)

      :type: bool

   .. attribute:: specular_color

      Specular color of the material (array of 3 items, in [0, inf], default (1.0, 1.0, 1.0))

      :type: :class:`mathutils.Color`

   .. attribute:: specular_intensity

      How intense (bright) the specular reflection is (in [0, 1], default 0.5)

      :type: float

   .. attribute:: surface_render_method

      Controls the blending and the compatibility with certain features (default ``'DITHERED'``)

      - ``DITHERED``
        Dithered -- Allows for grayscale hashed transparency, and compatible with render passes and raytracing. Also known as deferred rendering..
      - ``BLENDED``
        Blended -- Allows for colored transparency, but incompatible with render passes and raytracing. Also known as forward rendering..

      :type: Literal['DITHERED', 'BLENDED']

   .. data:: texture_paint_images

      Texture images used for texture painting (default None, readonly)

      :type: :class:`bpy_prop_collection`\ [:class:`Image`]

   .. data:: texture_paint_slots

      Texture slots defining the mapping and influence of textures (default None, readonly)

      :type: :class:`bpy_prop_collection`\ [:class:`TexPaintSlot`]

   .. attribute:: thickness_mode

      Approximation used to model the light interactions inside the object (default ``'SPHERE'``)

      - ``SPHERE``
        Sphere -- Approximate the object as a sphere whose diameter is equal to the thickness defined by the node tree.
      - ``SLAB``
        Slab -- Approximate the object as an infinite slab of thickness defined by the node tree.

      :type: Literal['SPHERE', 'SLAB']

   .. attribute:: use_backface_culling

      Use back face culling to hide the back side of faces (default False)

      :type: bool

   .. attribute:: use_backface_culling_lightprobe_volume

      Consider material single sided for light probe volume capture. Additionally helps rejecting probes inside the object to avoid light leaks. (default True)

      :type: bool

   .. attribute:: use_backface_culling_shadow

      Use back face culling when casting shadows (default False)

      :type: bool

   .. attribute:: use_nodes

      Use shader nodes to render the material (default False)

      .. deprecated:: 5.0 removal planned in version 6.0

         Unused but kept for compatibility reasons. Setting the property has no effect, and getting it always returns True.

      :type: bool

   .. attribute:: use_preview_world

      Use the current world background to light the preview render (default False)

      :type: bool

   .. attribute:: use_raytrace_refraction

      Use raytracing to determine transmitted color instead of using only light probes. This prevents the surface from contributing to the lighting of surfaces not using this setting. (default False)

      :type: bool

   .. attribute:: use_screen_refraction

      Use raytracing to determine transmitted color instead of using only light probes. This prevents the surface from contributing to the lighting of surfaces not using this setting. Deprecated: use 'use_raytrace_refraction'. (default False)

      :type: bool

   .. attribute:: use_sss_translucency

      Add translucency effect to subsurface (Deprecated) (default False)

      :type: bool

   .. attribute:: use_thickness_from_shadow

      Use the shadow maps from shadow casting lights to refine the thickness defined by the material node tree (default False)

      :type: bool

   .. attribute:: use_transparency_overlap

      Render multiple transparent layers (may introduce transparency sorting problems) (default True)

      :type: bool

   .. attribute:: use_transparent_shadow

      Use transparent shadows for this material if it contains a Transparent BSDF, disabling will render faster but not give accurate shadows (default True)

      :type: bool

   .. attribute:: volume_intersection_method

      Determines which inner part of the mesh will produce volumetric effect (default ``'FAST'``)

      - ``FAST``
        Fast -- Each face is considered as a medium interface. Gives correct results for manifold geometry that contains no inner parts..
      - ``ACCURATE``
        Accurate -- Faces are considered as medium interface only when they have different consecutive facing. Gives correct results as long as the max ray depth is not exceeded. Have significant memory overhead compared to the fast method..

      :type: Literal['FAST', 'ACCURATE']

   .. method:: inline_shader_nodes()

      Get the inlined shader nodes of this material. This preprocesses the node tree
      to remove nested groups, repeat zones and more.
      
      :return: The inlined shader nodes.
      :rtype: :class:`bpy.types.InlineShaderNodes`

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

   - :mod:`bpy.context.material`
   - :class:`BlendData.materials`
   - :class:`BlendDataMaterials.create_gpencil_data`
   - :class:`BlendDataMaterials.new`
   - :class:`BlendDataMaterials.remove`
   - :class:`BlendDataMaterials.remove_gpencil_data`
   - :class:`BrushGpencilSettings.material`
   - :class:`BrushGpencilSettings.material_alt`
   - :class:`Curve.materials`
   - :class:`Curves.materials`
   - :class:`GeometryNodeInputMaterial.material`
   - :class:`GreasePencil.materials`
   - :class:`GreasePencilArrayModifier.material_filter`
   - :class:`GreasePencilBuildModifier.material_filter`
   - :class:`GreasePencilColorModifier.material_filter`
   - :class:`GreasePencilDashModifierData.material_filter`
   - :class:`GreasePencilEnvelopeModifier.material_filter`
   - :class:`GreasePencilHookModifier.material_filter`
   - :class:`GreasePencilLatticeModifier.material_filter`
   - :class:`GreasePencilLengthModifier.material_filter`
   - :class:`GreasePencilLineartModifier.target_material`
   - :class:`GreasePencilMirrorModifier.material_filter`
   - :class:`GreasePencilMultiplyModifier.material_filter`
   - :class:`GreasePencilNoiseModifier.material_filter`
   - :class:`GreasePencilOffsetModifier.material_filter`
   - :class:`GreasePencilOpacityModifier.material_filter`
   - :class:`GreasePencilOutlineModifier.material_filter`
   - :class:`GreasePencilOutlineModifier.outline_material`
   - :class:`GreasePencilShrinkwrapModifier.material_filter`
   - :class:`GreasePencilSimplifyModifier.material_filter`
   - :class:`GreasePencilSmoothModifier.material_filter`
   - :class:`GreasePencilSubdivModifier.material_filter`
   - :class:`GreasePencilTextureModifier.material_filter`
   - :class:`GreasePencilThickModifierData.material_filter`
   - :class:`GreasePencilTintModifier.material_filter`
   - :class:`GreasePencilWeightAngleModifier.material_filter`
   - :class:`GreasePencilWeightProximityModifier.material_filter`
   - :class:`IDMaterials.append`
   - :class:`IDMaterials.pop`
   - :class:`MaterialSlot.material`
   - :class:`Mesh.materials`
   - :class:`MetaBall.materials`
   - :class:`NodeSocketMaterial.default_value`
   - :class:`NodeTreeInterfaceSocketMaterial.default_value`
   - :class:`Object.active_material`
   - :class:`PointCloud.materials`
   - :class:`ViewLayer.material_override`
   - :class:`Volume.materials`

