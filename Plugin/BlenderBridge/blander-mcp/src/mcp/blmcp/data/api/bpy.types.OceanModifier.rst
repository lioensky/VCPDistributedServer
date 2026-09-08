OceanModifier(Modifier)
=======================

.. currentmodule:: bpy.types

base classes --- :class:`bpy_struct`, :class:`Modifier`

.. class:: OceanModifier(Modifier)

   Simulate an ocean surface

   .. attribute:: bake_foam_fade

      How much foam accumulates over time (baked ocean only) (in [0, inf], default 0.98)

      :type: float

   .. attribute:: choppiness

      Choppiness of the wave's crest (adds some horizontal component to the displacement) (in [0, inf], default 1.0)

      :type: float

   .. attribute:: damping

      Damp reflected waves going in opposite direction to the wind (in [0, 1], default 0.5)

      :type: float

   .. attribute:: depth

      Depth of the solid ground below the water surface (in [-inf, inf], default 200.0)

      :type: float

   .. attribute:: fetch_jonswap

      This is the distance from a lee shore, called the fetch, or the distance over which the wind blows with constant velocity. Used by 'JONSWAP' and 'TMA' models. (in [0, inf], default 120.0)

      :type: float

   .. attribute:: filepath

      Path to a folder to store external baked images (default "", never None, blend relative ``//`` prefix supported)

      :type: str

   .. attribute:: foam_coverage

      Amount of generated foam (in [-inf, inf], default 0.0)

      :type: float

   .. attribute:: foam_layer_name

      Name of the vertex color layer used for foam (default "", never None)

      :type: str

   .. attribute:: frame_end

      End frame of the ocean baking (in [-inf, inf], default 250)

      :type: int

   .. attribute:: frame_start

      Start frame of the ocean baking (in [-inf, inf], default 1)

      :type: int

   .. attribute:: geometry_mode

      Method of modifying geometry (default ``'GENERATE'``)

      - ``GENERATE``
        Generate -- Generate ocean surface geometry at the specified resolution.
      - ``DISPLACE``
        Displace -- Displace existing geometry according to simulation.

      :type: Literal['GENERATE', 'DISPLACE']

   .. attribute:: invert_spray

      Invert the spray direction map (default False)

      :type: bool

   .. data:: is_cached

      Whether the ocean is using cached data or simulating (default False, readonly)

      :type: bool

   .. attribute:: random_seed

      Seed of the random generator (in [0, inf], default 0)

      :type: int

   .. attribute:: repeat_x

      Repetitions of the generated surface in X (in [1, 1024], default 1)

      :type: int

   .. attribute:: repeat_y

      Repetitions of the generated surface in Y (in [1, 1024], default 1)

      :type: int

   .. attribute:: resolution

      Resolution of the generated surface for rendering and baking (in [1, 1024], default 7)

      :type: int

   .. attribute:: sharpen_peak_jonswap

      Peak sharpening for 'JONSWAP' and 'TMA' models (in [0, 1], default 0.0)

      :type: float

   .. attribute:: size

      Surface scale factor (does not affect the height of the waves) (in [0, inf], default 1.0)

      :type: float

   .. attribute:: spatial_size

      Size of the simulation domain (in meters), and of the generated geometry (in BU) (in [-inf, inf], default 50)

      :type: int

   .. attribute:: spectrum

      Spectrum to use (default ``'PHILLIPS'``)

      - ``PHILLIPS``
        Turbulent Ocean -- Use for turbulent seas with foam.
      - ``PIERSON_MOSKOWITZ``
        Established Ocean -- Use for a large area, established ocean (Pierson-Moskowitz method).
      - ``JONSWAP``
        Established Ocean (Sharp Peaks) -- Use for established oceans ('JONSWAP', Pierson-Moskowitz method) with peak sharpening.
      - ``TEXEL_MARSEN_ARSLOE``
        Shallow Water -- Use for shallow water ('JONSWAP', 'TMA' - Texel-Marsen-Arsloe method).

      :type: Literal['PHILLIPS', 'PIERSON_MOSKOWITZ', 'JONSWAP', 'TEXEL_MARSEN_ARSLOE']

   .. attribute:: spray_layer_name

      Name of the vertex color layer used for the spray direction map (default "", never None)

      :type: str

   .. attribute:: time

      Current time of the simulation (in [0, inf], default 1.0)

      :type: float

   .. attribute:: use_foam

      Generate foam mask as a vertex color channel (default False)

      :type: bool

   .. attribute:: use_normals

      Output normals for bump mapping - disabling can speed up performance if it's not needed (default False)

      :type: bool

   .. attribute:: use_spray

      Generate map of spray direction as a vertex color channel (default False)

      :type: bool

   .. attribute:: viewport_resolution

      Viewport resolution of the generated surface (in [1, 1024], default 7)

      :type: int

   .. attribute:: wave_alignment

      How much the waves are aligned to each other (in [0, 1], default 0.0)

      :type: float

   .. attribute:: wave_direction

      Main direction of the waves when they are (partially) aligned (in [-inf, inf], default 0.0)

      :type: float

   .. attribute:: wave_scale

      Scale of the displacement effect (in [0, inf], default 1.0)

      :type: float

   .. attribute:: wave_scale_min

      Shortest allowed wavelength (in [0, inf], default 0.01)

      :type: float

   .. attribute:: wind_velocity

      Wind speed (in [-inf, inf], default 30.0)

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
   - :class:`Modifier.name`
   - :class:`Modifier.type`
   - :class:`Modifier.show_viewport`
   - :class:`Modifier.show_render`
   - :class:`Modifier.show_in_editmode`
   - :class:`Modifier.show_on_cage`
   - :class:`Modifier.show_expanded`
   - :class:`Modifier.is_active`
   - :class:`Modifier.use_pin_to_last`
   - :class:`Modifier.is_override_data`
   - :class:`Modifier.use_apply_on_spline`
   - :class:`Modifier.execution_time`
   - :class:`Modifier.persistent_uid`

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
   - :class:`Modifier.bl_rna_get_subclass`
   - :class:`Modifier.bl_rna_get_subclass_py`

