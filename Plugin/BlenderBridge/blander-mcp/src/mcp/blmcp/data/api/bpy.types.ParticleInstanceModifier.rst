ParticleInstanceModifier(Modifier)
==================================

.. currentmodule:: bpy.types

base classes --- :class:`bpy_struct`, :class:`Modifier`

.. class:: ParticleInstanceModifier(Modifier)

   Particle system instancing modifier

   .. attribute:: axis

      Pole axis for rotation (default ``'Z'``)

      :type: Literal[:ref:`rna_enum_axis_xyz_items`]

   .. attribute:: index_layer_name

      Custom data layer name for the index (default "", never None)

      :type: str

   .. attribute:: object

      Object that has the particle system

      :type: :class:`Object` | None

   .. attribute:: particle_amount

      Amount of particles to use for instancing (in [0, 1], default 1.0)

      :type: float

   .. attribute:: particle_offset

      Relative offset of particles to use for instancing, to avoid overlap of multiple instances (in [0, 1], default 0.0)

      :type: float

   .. attribute:: particle_system

      :type: :class:`ParticleSystem` | None

   .. attribute:: particle_system_index

      (in [1, 32767], default 1)

      :type: int

   .. attribute:: position

      Position along path (in [0, 1], default 1.0)

      :type: float

   .. attribute:: random_position

      Randomize position along path (in [0, 1], default 0.0)

      :type: float

   .. attribute:: random_rotation

      Randomize rotation around path (in [0, 1], default 0.0)

      :type: float

   .. attribute:: rotation

      Rotation around path (in [0, 1], default 0.0)

      :type: float

   .. attribute:: show_alive

      Show instances when particles are alive (default True)

      :type: bool

   .. attribute:: show_dead

      Show instances when particles are dead (default True)

      :type: bool

   .. attribute:: show_unborn

      Show instances when particles are unborn (default True)

      :type: bool

   .. attribute:: space

      Space to use for copying mesh data (default ``'WORLD'``)

      - ``LOCAL``
        Local -- Use offset from the particle object in the instance object.
      - ``WORLD``
        World -- Use world space offset in the instance object.

      :type: Literal['LOCAL', 'WORLD']

   .. attribute:: use_children

      Create instances from child particles (default False)

      :type: bool

   .. attribute:: use_normal

      Create instances from normal particles (default True)

      :type: bool

   .. attribute:: use_path

      Create instances along particle paths (default False)

      :type: bool

   .. attribute:: use_preserve_shape

      Don't stretch the object (default False)

      :type: bool

   .. attribute:: use_size

      Use particle size to scale the instances (default False)

      :type: bool

   .. attribute:: value_layer_name

      Custom data layer name for the randomized value (default "", never None)

      :type: str

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

