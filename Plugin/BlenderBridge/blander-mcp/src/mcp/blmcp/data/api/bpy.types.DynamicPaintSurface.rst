DynamicPaintSurface(bpy_struct)
===============================

.. currentmodule:: bpy.types

base class --- :class:`bpy_struct`

.. class:: DynamicPaintSurface(bpy_struct)

   A canvas surface layer

   .. attribute:: brush_collection

      Only use brush objects from this collection

      :type: :class:`Collection` | None

   .. attribute:: brush_influence_scale

      Adjust influence brush objects have on this surface (in [0, 1], default 0.0)

      :type: float

   .. attribute:: brush_radius_scale

      Adjust radius of proximity brushes or particles for this surface (in [0, 10], default 0.0)

      :type: float

   .. attribute:: color_dry_threshold

      The wetness level when colors start to shift to the background (in [0, 1], default 0.0)

      :type: float

   .. attribute:: color_spread_speed

      How fast colors get mixed within wet paint (in [0, 2], default 0.0)

      :type: float

   .. attribute:: depth_clamp

      Maximum level of depth intersection in object space (use 0.0 to disable) (in [0, 50], default 0.0)

      :type: float

   .. attribute:: displace_factor

      Strength of displace when applied to the mesh (in [-50, 50], default 0.0)

      :type: float

   .. attribute:: displace_type

      (default ``'DISPLACE'``)

      :type: Literal['DISPLACE', 'DEPTH']

   .. attribute:: dissolve_speed

      Approximately in how many frames should dissolve happen (in [1, 10000], default 0)

      :type: int

   .. attribute:: drip_acceleration

      How much surface acceleration affects dripping (in [-200, 200], default 0.0)

      :type: float

   .. attribute:: drip_velocity

      How much surface velocity affects dripping (in [-200, 200], default 0.0)

      :type: float

   .. attribute:: dry_speed

      Approximately in how many frames should drying happen (in [1, 10000], default 0)

      :type: int

   .. attribute:: effect_ui

      (default ``'SPREAD'``)

      :type: Literal['SPREAD', 'DRIP', 'SHRINK']

   .. data:: effector_weights

      (readonly)

      :type: :class:`EffectorWeights` | None

   .. attribute:: frame_end

      Simulation end frame (in [1, 1048574], default 0)

      :type: int

   .. attribute:: frame_start

      Simulation start frame (in [1, 1048574], default 0)

      :type: int

   .. attribute:: frame_substeps

      Do extra frames between scene frames to ensure smooth motion (in [0, 20], default 0)

      :type: int

   .. attribute:: image_fileformat

      (default ``'PNG'``)

      :type: Literal['PNG']

   .. attribute:: image_output_path

      Directory to save the textures (default "", never None, blend relative ``//`` prefix supported)

      :type: str

   .. attribute:: image_resolution

      Output image resolution (in [16, 4096], default 0)

      :type: int

   .. attribute:: init_color

      Initial color of the surface (array of 4 items, in [0, inf], default (0.0, 0.0, 0.0, 0.0))

      :type: :class:`bpy_prop_array`\ [float]

   .. attribute:: init_color_type

      (default ``'NONE'``)

      :type: Literal['NONE', 'COLOR', 'TEXTURE', 'VERTEX_COLOR']

   .. attribute:: init_layername

      (default "", never None)

      :type: str

   .. attribute:: init_texture

      :type: :class:`Texture` | None

   .. attribute:: is_active

      Toggle whether surface is processed or ignored (default False)

      :type: bool

   .. data:: is_cache_user

      (default False, readonly)

      :type: bool

   .. attribute:: name

      Surface name (default "", never None)

      :type: str

   .. attribute:: output_name_a

      Name used to save output from this surface (default "", never None)

      :type: str

   .. attribute:: output_name_b

      Name used to save output from this surface (default "", never None)

      :type: str

   .. data:: point_cache

      (readonly, never None)

      :type: :class:`PointCache`

   .. attribute:: shrink_speed

      How fast shrink effect moves on the canvas surface (in [0.001, 10], default 0.0)

      :type: float

   .. attribute:: spread_speed

      How fast spread effect moves on the canvas surface (in [0.001, 10], default 0.0)

      :type: float

   .. attribute:: surface_format

      Surface Format (default ``'VERTEX'``)

      :type: Literal['VERTEX', 'IMAGE']

   .. attribute:: surface_type

      Surface Type (default ``'PAINT'``)

      :type: Literal['PAINT']

   .. attribute:: use_antialiasing

      Use 5× multisampling to smooth paint edges (default False)

      :type: bool

   .. attribute:: use_dissolve

      Enable to make surface changes disappear over time (default False)

      :type: bool

   .. attribute:: use_dissolve_log

      Use logarithmic dissolve (makes high values to fade faster than low values) (default False)

      :type: bool

   .. attribute:: use_drip

      Process drip effect (drip wet paint to gravity direction) (default False)

      :type: bool

   .. attribute:: use_dry_log

      Use logarithmic drying (makes high values to dry faster than low values) (default False)

      :type: bool

   .. attribute:: use_drying

      Enable to make surface wetness dry over time (default False)

      :type: bool

   .. attribute:: use_incremental_displace

      New displace is added cumulatively on top of existing (default False)

      :type: bool

   .. attribute:: use_output_a

      Save this output layer (default False)

      :type: bool

   .. attribute:: use_output_b

      Save this output layer (default False)

      :type: bool

   .. attribute:: use_premultiply

      Multiply color by alpha (recommended for Blender input) (default False)

      :type: bool

   .. attribute:: use_shrink

      Process shrink effect (shrink paint areas) (default False)

      :type: bool

   .. attribute:: use_spread

      Process spread effect (spread wet paint around surface) (default False)

      :type: bool

   .. attribute:: use_wave_open_border

      Pass waves through mesh edges (default False)

      :type: bool

   .. attribute:: uv_layer

      UV map name (default "", never None)

      :type: str

   .. attribute:: wave_damping

      Wave damping factor (in [0, 1], default 0.0)

      :type: float

   .. attribute:: wave_smoothness

      Limit maximum steepness of wave slope between simulation points (use higher values for smoother waves at expense of reduced detail) (in [0, 10], default 0.0)

      :type: float

   .. attribute:: wave_speed

      Wave propagation speed (in [0.01, 5], default 0.0)

      :type: float

   .. attribute:: wave_spring

      Spring force that pulls water level back to zero (in [0, 1], default 0.0)

      :type: float

   .. attribute:: wave_timescale

      Wave time scaling factor (in [0.01, 3], default 0.0)

      :type: float

   .. method:: output_exists(object, index)

      Checks if surface output layer of given name exists

      :param object: (never None)
      :type object: :class:`Object` | None
      :param index: Index, (in [0, 1])
      :type index: int
      :rtype: bool

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

   - :class:`DynamicPaintCanvasSettings.canvas_surfaces`
   - :class:`DynamicPaintSurfaces.active`

