ShaderNodeTexSky(ShaderNode)
============================

.. currentmodule:: bpy.types

base classes --- :class:`bpy_struct`, :class:`Node`, :class:`NodeInternal`, :class:`ShaderNode`

.. class:: ShaderNodeTexSky(ShaderNode)

   Generate a procedural sky texture

   .. attribute:: aerosol_density

      Density of dust, pollution and water droplets.
      0 means no aerosols, 1 means urban city aerosols
      
      (in [0, 1000], default 1.0)

      :type: float

   .. attribute:: air_density

      Density of air molecules.
      0 means no air, 1 means urban city air
      
      (in [0, 1000], default 1.0)

      :type: float

   .. attribute:: altitude

      Height from sea level (in [0, 100000], default 100.0)

      :type: float

   .. data:: color_mapping

      Color mapping settings (readonly, never None)

      :type: :class:`ColorMapping`

   .. attribute:: ground_albedo

      Ground color that is subtly reflected in the sky (in [0, 1], default 0.0)

      :type: float

   .. attribute:: ozone_density

      Density of ozone layer.
      0 means no ozone, 1 means urban city ozone
      
      (in [0, 1000], default 1.0)

      :type: float

   .. attribute:: sky_type

      Which sky model should be used (default ``'PREETHAM'``)

      - ``SINGLE_SCATTERING``
        Single Scattering -- Single scattering sky model.
      - ``MULTIPLE_SCATTERING``
        Multiple Scattering -- Multiple scattering sky model (more accurate).
      - ``PREETHAM``
        Preetham -- Preetham 1999 (Legacy).
      - ``HOSEK_WILKIE``
        Hosek / Wilkie -- Hosek / Wilkie 2012 (Legacy).

      :type: Literal['SINGLE_SCATTERING', 'MULTIPLE_SCATTERING', 'PREETHAM', 'HOSEK_WILKIE']

   .. attribute:: sun_direction

      Direction from where the sun is shining (array of 3 items, in [-inf, inf], default (0.0, 0.0, 1.0))

      :type: :class:`mathutils.Vector`

   .. attribute:: sun_disc

      Include the sun itself in the output (default True)

      :type: bool

   .. attribute:: sun_elevation

      Sun angle from horizon (in [-inf, inf], default 0.261799)

      :type: float

   .. attribute:: sun_intensity

      Strength of Sun (in [0, 1000], default 1.0)

      :type: float

   .. attribute:: sun_rotation

      Rotation of sun around zenith (in [-inf, inf], default 0.0)

      :type: float

   .. attribute:: sun_size

      Size of sun disc (in [0, 1.5708], default 0.00951204)

      :type: float

   .. data:: texture_mapping

      Texture coordinate mapping settings (readonly, never None)

      :type: :class:`TexMapping`

   .. attribute:: turbidity

      Atmospheric turbidity (in [1, 10], default 0.0)

      :type: float

   .. classmethod:: is_registered_node_type()

      True if a registered node type

      :return: Result
      :rtype: bool

   .. classmethod:: input_template(index)

      Input socket template

      :param index: Index, (in [0, inf])
      :type index: int
      :return: result
      :rtype: :class:`NodeInternalSocketTemplate`

   .. classmethod:: output_template(index)

      Output socket template

      :param index: Index, (in [0, inf])
      :type index: int
      :return: result
      :rtype: :class:`NodeInternalSocketTemplate`

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
   - :class:`Node.type`
   - :class:`Node.location`
   - :class:`Node.location_absolute`
   - :class:`Node.width`
   - :class:`Node.height`
   - :class:`Node.dimensions`
   - :class:`Node.name`
   - :class:`Node.label`
   - :class:`Node.inputs`
   - :class:`Node.outputs`
   - :class:`Node.internal_links`
   - :class:`Node.parent`
   - :class:`Node.warning_propagation`
   - :class:`Node.use_custom_color`
   - :class:`Node.color`
   - :class:`Node.color_tag`
   - :class:`Node.select`
   - :class:`Node.show_options`
   - :class:`Node.show_preview`
   - :class:`Node.hide`
   - :class:`Node.mute`
   - :class:`Node.show_texture`
   - :class:`Node.bl_idname`
   - :class:`Node.bl_label`
   - :class:`Node.bl_description`
   - :class:`Node.bl_icon`
   - :class:`Node.bl_static_type`
   - :class:`Node.bl_width_default`
   - :class:`Node.bl_width_min`
   - :class:`Node.bl_width_max`
   - :class:`Node.bl_height_default`
   - :class:`Node.bl_height_min`
   - :class:`Node.bl_height_max`

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
   - :class:`Node.bl_system_properties_get`
   - :class:`Node.socket_value_update`
   - :class:`Node.is_registered_node_type`
   - :class:`Node.poll`
   - :class:`Node.poll_instance`
   - :class:`Node.update`
   - :class:`Node.insert_link`
   - :class:`Node.init`
   - :class:`Node.copy`
   - :class:`Node.free`
   - :class:`Node.draw_buttons`
   - :class:`Node.draw_buttons_ext`
   - :class:`Node.draw_label`
   - :class:`Node.debug_zone_body_lazy_function_graph`
   - :class:`Node.debug_zone_lazy_function_graph`
   - :class:`Node.poll`
   - :class:`Node.bl_rna_get_subclass`
   - :class:`Node.bl_rna_get_subclass_py`
   - :class:`NodeInternal.poll`
   - :class:`NodeInternal.poll_instance`
   - :class:`NodeInternal.update`
   - :class:`NodeInternal.draw_buttons`
   - :class:`NodeInternal.draw_buttons_ext`
   - :class:`NodeInternal.bl_rna_get_subclass`
   - :class:`NodeInternal.bl_rna_get_subclass_py`
   - :class:`ShaderNode.poll`
   - :class:`ShaderNode.bl_rna_get_subclass`
   - :class:`ShaderNode.bl_rna_get_subclass_py`

