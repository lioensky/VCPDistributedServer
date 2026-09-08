FluidFlowSettings(bpy_struct)
=============================

.. currentmodule:: bpy.types

base class --- :class:`bpy_struct`

.. class:: FluidFlowSettings(bpy_struct)

   Fluid flow settings

   .. attribute:: density

      (in [0, 10], default 1.0)

      :type: float

   .. attribute:: density_vertex_group

      Name of vertex group which determines surface emission rate (default "", never None)

      :type: str

   .. attribute:: flow_behavior

      Change flow behavior in the simulation (default ``'GEOMETRY'``)

      - ``INFLOW``
        Inflow -- Add fluid to simulation.
      - ``OUTFLOW``
        Outflow -- Delete fluid from simulation.
      - ``GEOMETRY``
        Geometry -- Only use given geometry for fluid.

      :type: Literal['INFLOW', 'OUTFLOW', 'GEOMETRY']

   .. attribute:: flow_source

      Change how fluid is emitted (default ``'NONE'``)

      :type: Literal['NONE']

   .. attribute:: flow_type

      Change type of fluid in the simulation (default ``'SMOKE'``)

      - ``SMOKE``
        Smoke -- Add smoke.
      - ``BOTH``
        Fire + Smoke -- Add fire and smoke.
      - ``FIRE``
        Fire -- Add fire.
      - ``LIQUID``
        Liquid -- Add liquid.

      :type: Literal['SMOKE', 'BOTH', 'FIRE', 'LIQUID']

   .. attribute:: fuel_amount

      (in [0, 10], default 1.0)

      :type: float

   .. attribute:: noise_texture

      Texture that controls emission strength

      :type: :class:`Texture` | None

   .. attribute:: particle_size

      Particle size in simulation cells (in [0.1, inf], default 1.0)

      :type: float

   .. attribute:: particle_system

      Particle systems emitted from the object

      :type: :class:`ParticleSystem` | None

   .. attribute:: smoke_color

      Color of smoke (array of 3 items, in [0, inf], default (0.7, 0.7, 0.7))

      :type: :class:`mathutils.Color`

   .. attribute:: subframes

      Number of additional samples to take between frames to improve quality of fast moving flows (in [0, 200], default 0)

      :type: int

   .. attribute:: surface_distance

      Height (in domain grid units) of fluid emission above the mesh surface. Higher values result in emission further away from the mesh surface. If this value and the emitter size are smaller than the domain grid unit, fluid will not be created (in [0, 10], default 1.0)

      :type: float

   .. attribute:: temperature

      Temperature difference to ambient temperature (in [-10, 10], default 1.0)

      :type: float

   .. attribute:: texture_map_type

      Texture mapping type (default ``'AUTO'``)

      - ``AUTO``
        Generated -- Generated coordinates centered to flow object.
      - ``UV``
        UV -- Use UV layer for texture coordinates.

      :type: Literal['AUTO', 'UV']

   .. attribute:: texture_offset

      Z-offset of texture mapping (in [0, 200], default 0.0)

      :type: float

   .. attribute:: texture_size

      Size of texture mapping (in [0.01, 10], default 1.0)

      :type: float

   .. attribute:: use_absolute

      Only allow given density value in emitter area and will not add up (default True)

      :type: bool

   .. attribute:: use_inflow

      Control when to apply fluid flow (default True)

      :type: bool

   .. attribute:: use_initial_velocity

      Fluid has some initial velocity when it is emitted (default False)

      :type: bool

   .. attribute:: use_particle_size

      Set particle size in simulation cells or use nearest cell (default True)

      :type: bool

   .. attribute:: use_plane_init

      Treat this object as a planar and unclosed mesh. Fluid will only be emitted from the mesh surface and based on the surface emission value. (default False)

      :type: bool

   .. attribute:: use_texture

      Use a texture to control emission strength (default False)

      :type: bool

   .. attribute:: uv_layer

      UV map name (default "", never None)

      :type: str

   .. attribute:: velocity_coord

      Additional initial velocity in X, Y and Z direction (added to source velocity) (array of 3 items, in [-1000.1, 1000.1], default (0.0, 0.0, 0.0))

      :type: :class:`mathutils.Vector`

   .. attribute:: velocity_factor

      Multiplier of source velocity passed to fluid (source velocity is non-zero only if object is moving) (in [-100, 100], default 1.0)

      :type: float

   .. attribute:: velocity_normal

      Amount of normal directional velocity (in [-100, 100], default 0.0)

      :type: float

   .. attribute:: velocity_random

      Amount of random velocity (in [0, 10], default 0.0)

      :type: float

   .. attribute:: volume_density

      Controls fluid emission from within the mesh (higher value results in greater emissions from inside the mesh) (in [0, 1], default 0.0)

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

   - :class:`FluidModifier.flow_settings`

