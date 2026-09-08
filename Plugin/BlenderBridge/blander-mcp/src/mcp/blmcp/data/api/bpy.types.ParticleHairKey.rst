ParticleHairKey(bpy_struct)
===========================

.. currentmodule:: bpy.types

base class --- :class:`bpy_struct`

.. class:: ParticleHairKey(bpy_struct)

   Particle key for hair particle system

   .. attribute:: co

      Location of the hair key in object space (array of 3 items, in [-inf, inf], default (0.0, 0.0, 0.0))

      :type: :class:`mathutils.Vector`

   .. attribute:: co_local

      Location of the hair key in its local coordinate system, relative to the emitting face (array of 3 items, in [-inf, inf], default (0.0, 0.0, 0.0))

      :type: :class:`mathutils.Vector`

   .. attribute:: time

      Relative time of key over hair length (in [0, inf], default 0.0)

      :type: float

   .. attribute:: weight

      Weight for cloth simulation (in [0, 1], default 0.0)

      :type: float

   .. method:: co_object(object, modifier, particle)

      Obtain hairkey location with particle and modifier data

      :param object: Object (never None)
      :type object: :class:`Object` | None
      :param modifier: Particle modifier (never None)
      :type modifier: :class:`ParticleSystemModifier` | None
      :param particle: hair particle (never None)
      :type particle: :class:`Particle` | None
      :return: Co, Exported hairkey location (array of 3 items, in [-inf, inf])
      :rtype: :class:`mathutils.Vector`

   .. method:: co_object_set(object, modifier, particle, co)

      Set hairkey location with particle and modifier data

      :param object: Object (never None)
      :type object: :class:`Object` | None
      :param modifier: Particle modifier (never None)
      :type modifier: :class:`ParticleSystemModifier` | None
      :param particle: hair particle (never None)
      :type particle: :class:`Particle` | None
      :param co: Co, Specified hairkey location (array of 3 items, in [-inf, inf])
      :type co: :class:`mathutils.Vector` | Sequence[float]

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

   - :class:`Particle.hair_keys`

