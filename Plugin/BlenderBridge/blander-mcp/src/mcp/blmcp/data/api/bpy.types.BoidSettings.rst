BoidSettings(bpy_struct)
========================

.. currentmodule:: bpy.types

base class --- :class:`bpy_struct`

.. class:: BoidSettings(bpy_struct)

   Settings for boid physics

   .. attribute:: accuracy

      Accuracy of attack (in [0, 1], default 0.0)

      :type: float

   .. data:: active_boid_state

      (readonly)

      :type: :class:`BoidRule` | None

   .. attribute:: active_boid_state_index

      (in [0, inf], default 0)

      :type: int

   .. attribute:: aggression

      Boid will fight this times stronger enemy (in [0, 100], default 0.0)

      :type: float

   .. attribute:: air_acc_max

      Maximum acceleration in air (relative to maximum speed) (in [0, 1], default 0.0)

      :type: float

   .. attribute:: air_ave_max

      Maximum angular velocity in air (relative to 180 degrees) (in [0, 1], default 0.0)

      :type: float

   .. attribute:: air_personal_space

      Radius of boids personal space in air (% of particle size) (in [0, 10], default 0.0)

      :type: float

   .. attribute:: air_speed_max

      Maximum speed in air (in [0, 100], default 0.0)

      :type: float

   .. attribute:: air_speed_min

      Minimum speed in air (relative to maximum speed) (in [0, 1], default 0.0)

      :type: float

   .. attribute:: bank

      Amount of rotation around velocity vector on turns (in [0, 2], default 0.0)

      :type: float

   .. attribute:: health

      Initial boid health when born (in [0, 100], default 0.0)

      :type: float

   .. attribute:: height

      Boid height relative to particle size (in [0, 2], default 0.0)

      :type: float

   .. attribute:: land_acc_max

      Maximum acceleration on land (relative to maximum speed) (in [0, 1], default 0.0)

      :type: float

   .. attribute:: land_ave_max

      Maximum angular velocity on land (relative to 180 degrees) (in [0, 1], default 0.0)

      :type: float

   .. attribute:: land_jump_speed

      Maximum speed for jumping (in [0, 100], default 0.0)

      :type: float

   .. attribute:: land_personal_space

      Radius of boids personal space on land (% of particle size) (in [0, 10], default 0.0)

      :type: float

   .. attribute:: land_smooth

      How smoothly the boids land (in [0, 10], default 0.0)

      :type: float

   .. attribute:: land_speed_max

      Maximum speed on land (in [0, 100], default 0.0)

      :type: float

   .. attribute:: land_stick_force

      How strong a force must be to start effecting a boid on land (in [0, 1000], default 0.0)

      :type: float

   .. attribute:: pitch

      Amount of rotation around side vector (in [0, 2], default 0.0)

      :type: float

   .. attribute:: range

      Maximum distance from which a boid can attack (in [0, 100], default 0.0)

      :type: float

   .. data:: states

      (default None, readonly)

      :type: :class:`bpy_prop_collection`\ [:class:`BoidState`]

   .. attribute:: strength

      Maximum caused damage on attack per second (in [0, 100], default 0.0)

      :type: float

   .. attribute:: use_climb

      Allow boids to climb goal objects (default False)

      :type: bool

   .. attribute:: use_flight

      Allow boids to move in air (default False)

      :type: bool

   .. attribute:: use_land

      Allow boids to move on land (default False)

      :type: bool

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

   - :class:`ParticleSettings.boids`

