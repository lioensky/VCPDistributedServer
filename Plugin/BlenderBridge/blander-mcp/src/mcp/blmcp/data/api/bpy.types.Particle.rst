Particle(bpy_struct)
====================

.. currentmodule:: bpy.types

base class --- :class:`bpy_struct`

.. class:: Particle(bpy_struct)

   Particle in a particle system

   .. attribute:: alive_state

      (default ``'DEAD'``)

      :type: Literal['DEAD', 'UNBORN', 'ALIVE', 'DYING']

   .. attribute:: angular_velocity

      (array of 3 items, in [-inf, inf], default (0.0, 0.0, 0.0))

      :type: :class:`mathutils.Vector`

   .. attribute:: birth_time

      (in [-inf, inf], default 0.0)

      :type: float

   .. attribute:: die_time

      (in [-inf, inf], default 0.0)

      :type: float

   .. data:: hair_keys

      (default None, readonly)

      :type: :class:`bpy_prop_collection`\ [:class:`ParticleHairKey`]

   .. data:: is_exist

      (default True, readonly)

      :type: bool

   .. data:: is_visible

      (default True, readonly)

      :type: bool

   .. attribute:: lifetime

      (in [-inf, inf], default 0.0)

      :type: float

   .. attribute:: location

      (array of 3 items, in [-inf, inf], default (0.0, 0.0, 0.0))

      :type: :class:`mathutils.Vector`

   .. data:: particle_keys

      (default None, readonly)

      :type: :class:`bpy_prop_collection`\ [:class:`ParticleKey`]

   .. attribute:: prev_angular_velocity

      (array of 3 items, in [-inf, inf], default (0.0, 0.0, 0.0))

      :type: :class:`mathutils.Vector`

   .. attribute:: prev_location

      (array of 3 items, in [-inf, inf], default (0.0, 0.0, 0.0))

      :type: :class:`mathutils.Vector`

   .. attribute:: prev_rotation

      (array of 4 items, in [-inf, inf], default (0.0, 0.0, 0.0, 0.0))

      :type: :class:`mathutils.Quaternion`

   .. attribute:: prev_velocity

      (array of 3 items, in [-inf, inf], default (0.0, 0.0, 0.0))

      :type: :class:`mathutils.Vector`

   .. attribute:: rotation

      (array of 4 items, in [-inf, inf], default (0.0, 0.0, 0.0, 0.0))

      :type: :class:`mathutils.Quaternion`

   .. attribute:: size

      (in [-inf, inf], default 0.0)

      :type: float

   .. attribute:: velocity

      (array of 3 items, in [-inf, inf], default (0.0, 0.0, 0.0))

      :type: :class:`mathutils.Vector`

   .. method:: uv_on_emitter(modifier)

      Obtain UV coordinates for a particle on an evaluated mesh.

      :param modifier: Particle modifier from an evaluated object (never None)
      :type modifier: :class:`ParticleSystemModifier` | None
      :return: uv, (array of 2 items, in [-inf, inf])
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

   - :class:`ParticleHairKey.co_object`
   - :class:`ParticleHairKey.co_object_set`
   - :class:`ParticleSystem.mcol_on_emitter`
   - :class:`ParticleSystem.particles`
   - :class:`ParticleSystem.uv_on_emitter`

