Light(ID)
=========

.. currentmodule:: bpy.types

base classes --- :class:`bpy_struct`, :class:`ID`

subclasses --- 
:class:`AreaLight`, :class:`PointLight`, :class:`SpotLight`, :class:`SunLight`

.. class:: Light(ID)

   Light data-block for lighting a scene

   .. data:: animation_data

      Animation data for this data-block (readonly)

      :type: :class:`AnimData` | None

   .. attribute:: color

      Light color (array of 3 items, in [0, inf], default (1.0, 1.0, 1.0))

      :type: :class:`mathutils.Color`

   .. attribute:: cutoff_distance

      Distance at which the light influence will be set to 0 (in [0, inf], default 40.0)

      :type: float

   .. attribute:: diffuse_factor

      Diffuse reflection multiplier (in [0, inf], default 1.0)

      :type: float

   .. attribute:: exposure

      Scales the power of the light exponentially, multiplying the intensity by 2^exposure (in [-32, 32], default 0.0)

      :type: float

   .. data:: node_tree

      Node tree for node based lights (readonly)

      :type: :class:`NodeTree` | None

   .. attribute:: normalize

      Normalize intensity by light area, for consistent total light output regardless of size and shape (default True)

      :type: bool

   .. attribute:: specular_factor

      Specular reflection multiplier (in [0, inf], default 1.0)

      :type: float

   .. attribute:: temperature

      Light color temperature in Kelvin (in [800, 20000], default 6500.0)

      :type: float

   .. data:: temperature_color

      Color from Temperature (array of 3 items, in [0, inf], default (0.0, 0.0, 0.0), readonly)

      :type: :class:`mathutils.Color`

   .. attribute:: transmission_factor

      Transmission light multiplier (in [0, inf], default 1.0)

      :type: float

   .. attribute:: type

      Type of light (default ``'POINT'``)

      :type: Literal[:ref:`rna_enum_light_type_items`]

   .. attribute:: use_custom_distance

      Use custom attenuation distance instead of global light threshold (default False)

      :type: bool

   .. attribute:: use_nodes

      Use shader nodes to render the light (default False)

      .. deprecated:: 5.10 removal planned in version 6.0

         Unused but kept for compatibility reasons. Setting the property has no effect, and getting it always returns True.

      :type: bool

   .. attribute:: use_shadow

      (default True)

      :type: bool

   .. attribute:: use_temperature

      Use blackbody temperature to define a natural light color (default False)

      :type: bool

   .. attribute:: volume_factor

      Volume light multiplier (in [0, inf], default 1.0)

      :type: float

   .. method:: area(*, matrix_world=((0.0, 0.0, 0.0, 0.0), (0.0, 0.0, 0.0, 0.0), (0.0, 0.0, 0.0, 0.0), (0.0, 0.0, 0.0, 0.0)))

      Compute light area based on type and shape. The normalize option divides light intensity by this area

      :param matrix_world: Object to world space transformation matrix (multi-dimensional array of 4 * 4 items, in [-inf, inf], optional)
      :type matrix_world: :class:`mathutils.Matrix` | Sequence[Sequence[float]]
      :return: area, (in [-inf, inf])
      :rtype: float

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

   - :mod:`bpy.context.light`
   - :class:`BlendData.lights`
   - :class:`BlendDataLights.new`
   - :class:`BlendDataLights.remove`

