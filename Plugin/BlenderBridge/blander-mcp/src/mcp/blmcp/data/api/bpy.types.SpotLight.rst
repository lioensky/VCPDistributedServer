SpotLight(Light)
================

.. currentmodule:: bpy.types

base classes --- :class:`bpy_struct`, :class:`ID`, :class:`Light`

.. class:: SpotLight(Light)

   Directional cone Light

   .. attribute:: energy

      The energy this light would emit over its entire area if it wasn't limited by the spot angle, in units of radiant power (W) (in [-inf, inf], default 10.0)

      :type: float

   .. attribute:: shadow_buffer_clip_start

      Shadow map clip start, below which objects will not generate shadows (in [1e-06, inf], default 0.05)

      :type: float

   .. attribute:: shadow_filter_radius

      Blur shadow aliasing using Percentage Closer Filtering (in [0, inf], default 1.0)

      :type: float

   .. attribute:: shadow_jitter_overblur

      Apply shadow tracing to each jittered sample to reduce under-sampling artifacts (in [0, 100], default 10.0)

      :type: float

   .. attribute:: shadow_maximum_resolution

      Minimum size of a shadow map pixel. Higher values use less memory at the cost of shadow quality. (in [0, inf], default 0.001)

      :type: float

   .. attribute:: shadow_soft_size

      Light size for ray shadow sampling (Raytraced shadows) (in [0, inf], default 0.0)

      :type: float

   .. attribute:: show_cone

      Display transparent cone in 3D view to visualize which objects are contained in it (default False)

      :type: bool

   .. attribute:: spot_blend

      The softness of the spotlight edge (in [0, 1], default 0.15)

      :type: float

   .. attribute:: spot_size

      Angular diameter of the spotlight beam (in [0.0174533, 3.14159], default 0.785398)

      :type: float

   .. attribute:: use_absolute_resolution

      Limit the resolution at 1 unit from the light origin instead of relative to the shadowed pixel (default False)

      :type: bool

   .. attribute:: use_shadow_jitter

      Enable jittered soft shadows to increase shadow precision (disabled in viewport unless enabled in the render settings). Has a high performance impact. (default False)

      :type: bool

   .. attribute:: use_soft_falloff

      Apply falloff to avoid sharp edges when the light geometry intersects with other objects (default True)

      :type: bool

   .. attribute:: use_square

      Cast a square spot light shape (default False)

      :type: bool

   .. method:: inline_shader_nodes()

      Get the inlined shader nodes of this light. This preprocesses the node tree
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
   - :class:`Light.type`
   - :class:`Light.use_temperature`
   - :class:`Light.color`
   - :class:`Light.temperature`
   - :class:`Light.temperature_color`
   - :class:`Light.specular_factor`
   - :class:`Light.diffuse_factor`
   - :class:`Light.transmission_factor`
   - :class:`Light.volume_factor`
   - :class:`Light.use_custom_distance`
   - :class:`Light.cutoff_distance`
   - :class:`Light.use_shadow`
   - :class:`Light.exposure`
   - :class:`Light.normalize`
   - :class:`Light.node_tree`
   - :class:`Light.use_nodes`
   - :class:`Light.animation_data`

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
   - :class:`Light.area`
   - :class:`Light.inline_shader_nodes`
   - :class:`Light.bl_rna_get_subclass`
   - :class:`Light.bl_rna_get_subclass_py`

