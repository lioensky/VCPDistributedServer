DynamicPaintBrushSettings(bpy_struct)
=====================================

.. currentmodule:: bpy.types

base class --- :class:`bpy_struct`

.. class:: DynamicPaintBrushSettings(bpy_struct)

   Brush settings

   .. attribute:: invert_proximity

      Proximity falloff is applied inside the volume (default False)

      :type: bool

   .. attribute:: paint_alpha

      Paint alpha (in [0, 1], default 0.0)

      :type: float

   .. attribute:: paint_color

      Color of the paint (array of 3 items, in [0, inf], default (0.0, 0.0, 0.0))

      :type: :class:`mathutils.Color`

   .. attribute:: paint_distance

      Maximum distance from brush to mesh surface to affect paint (in [0, 500], default 0.0)

      :type: float

   .. data:: paint_ramp

      Color ramp used to define proximity falloff (readonly)

      :type: :class:`ColorRamp` | None

   .. attribute:: paint_source

      (default ``'VOLUME'``)

      :type: Literal['PARTICLE_SYSTEM', 'POINT', 'DISTANCE', 'VOLUME_DISTANCE', 'VOLUME']

   .. attribute:: paint_wetness

      Paint wetness, visible in wetmap (some effects only affect wet paint) (in [0, 1], default 0.0)

      :type: float

   .. attribute:: particle_system

      The particle system to paint with

      :type: :class:`ParticleSystem` | None

   .. attribute:: proximity_falloff

      Proximity falloff type (default ``'CONSTANT'``)

      :type: Literal['SMOOTH', 'CONSTANT', 'RAMP']

   .. attribute:: ray_direction

      Ray direction to use for projection (if brush object is located in that direction it's painted) (default ``'CANVAS'``)

      :type: Literal['CANVAS', 'BRUSH', 'Z_AXIS']

   .. attribute:: smooth_radius

      Smooth falloff added after solid radius (in [0, 10], default 0.0)

      :type: float

   .. attribute:: smudge_strength

      Smudge effect strength (in [0, 1], default 0.0)

      :type: float

   .. attribute:: solid_radius

      Radius that will be painted solid (in [0.01, 10], default 0.0)

      :type: float

   .. attribute:: use_absolute_alpha

      Only increase alpha value if paint alpha is higher than existing (default False)

      :type: bool

   .. attribute:: use_negative_volume

      Negate influence inside the volume (default False)

      :type: bool

   .. attribute:: use_paint_erase

      Erase / remove paint instead of adding it (default False)

      :type: bool

   .. attribute:: use_particle_radius

      Use radius from particle settings (default False)

      :type: bool

   .. attribute:: use_proximity_project

      Brush is projected to canvas from defined direction within brush proximity (default False)

      :type: bool

   .. attribute:: use_proximity_ramp_alpha

      Only read color ramp alpha (default False)

      :type: bool

   .. attribute:: use_smudge

      Make this brush to smudge existing paint as it moves (default False)

      :type: bool

   .. attribute:: use_velocity_alpha

      Multiply brush influence by velocity color ramp alpha (default False)

      :type: bool

   .. attribute:: use_velocity_color

      Replace brush color by velocity color ramp (default False)

      :type: bool

   .. attribute:: use_velocity_depth

      Multiply brush intersection depth (displace, waves) by velocity ramp alpha (default False)

      :type: bool

   .. attribute:: velocity_max

      Velocity considered as maximum influence (Blender units per frame) (in [0.0001, 10], default 0.0)

      :type: float

   .. data:: velocity_ramp

      Color ramp used to define brush velocity effect (readonly)

      :type: :class:`ColorRamp` | None

   .. attribute:: wave_clamp

      Maximum level of surface intersection used to influence waves (use 0.0 to disable) (in [0, 50], default 0.0)

      :type: float

   .. attribute:: wave_factor

      Multiplier for wave influence of this brush (in [-2, 2], default 0.0)

      :type: float

   .. attribute:: wave_type

      (default ``'DEPTH'``)

      :type: Literal['CHANGE', 'DEPTH', 'FORCE', 'REFLECT']

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

   - :class:`DynamicPaintModifier.brush_settings`

