RigidBodyWorld(bpy_struct)
==========================

.. currentmodule:: bpy.types

base class --- :class:`bpy_struct`

.. class:: RigidBodyWorld(bpy_struct)

   Self-contained rigid body simulation environment and settings

   .. attribute:: collection

      Collection containing objects participating in this simulation

      :type: :class:`Collection` | None

   .. attribute:: constraints

      Collection containing rigid body constraint objects

      :type: :class:`Collection` | None

   .. data:: effector_weights

      (readonly)

      :type: :class:`EffectorWeights` | None

   .. attribute:: enabled

      Simulation will be evaluated (default True)

      :type: bool

   .. data:: point_cache

      (readonly, never None)

      :type: :class:`PointCache`

   .. attribute:: solver_iterations

      Number of constraint solver iterations made per simulation step (higher values are more accurate but slower) (in [1, 1000], default 10)

      :type: int

   .. attribute:: substeps_per_frame

      Number of simulation steps taken per frame (higher values are more accurate but slower) (in [1, 32767], default 10)

      :type: int

   .. attribute:: time_scale

      Change the speed of the simulation (in [0, 100], default 1.0)

      :type: float

   .. attribute:: use_split_impulse

      Reduce extra velocity that can build up when objects collide (lowers simulation stability a little so use only when necessary) (default False)

      :type: bool

   .. method:: convex_sweep_test(object, start, end)

      Sweep test convex rigidbody against the current rigidbody world

      :param object: Rigidbody object with a convex collision shape (never None)
      :type object: :class:`Object` | None
      :param start: (array of 3 items, in [-inf, inf])
      :type start: :class:`mathutils.Vector` | Sequence[float]
      :param end: (array of 3 items, in [-inf, inf])
      :type end: :class:`mathutils.Vector` | Sequence[float]
      :return:
         ``object_location``, The hit location of this sweep test, :class:`mathutils.Vector`

         ``hitpoint``, The hit location of this sweep test, :class:`mathutils.Vector`

         ``normal``, The face normal at the sweep test hit location, :class:`mathutils.Vector`

         ``has_hit``, If the function has found collision point, value is 1, otherwise 0, int

      :rtype: tuple[:class:`mathutils.Vector`, :class:`mathutils.Vector`, :class:`mathutils.Vector`, int]

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

   - :class:`Scene.rigidbody_world`

