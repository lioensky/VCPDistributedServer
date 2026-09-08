CollisionSettings(bpy_struct)
=============================

.. currentmodule:: bpy.types

base class --- :class:`bpy_struct`

.. class:: CollisionSettings(bpy_struct)

   Collision settings for object in physics simulation

   .. attribute:: absorption

      How much of effector force gets lost during collision with this object (in percent) (in [0, 1], default 0.0)

      :type: float

   .. attribute:: cloth_friction

      Friction for cloth collisions (in [0, 80], default 0.0)

      :type: float

   .. attribute:: damping

      Amount of damping during collision (in [0, 1], default 0.0)

      :type: float

   .. attribute:: damping_factor

      Amount of damping during particle collision (in [0, 1], default 0.0)

      :type: float

   .. attribute:: damping_random

      Random variation of damping (in [0, 1], default 0.0)

      :type: float

   .. attribute:: friction_factor

      Amount of friction during particle collision (in [0, 1], default 0.0)

      :type: float

   .. attribute:: friction_random

      Random variation of friction (in [0, 1], default 0.0)

      :type: float

   .. attribute:: permeability

      Chance that the particle will pass through the mesh (in [0, 1], default 0.0)

      :type: float

   .. attribute:: stickiness

      Amount of stickiness to surface collision (in [0, 10], default 0.0)

      :type: float

   .. attribute:: thickness_inner

      Inner face thickness (only used by softbodies) (in [0.001, 1], default 0.0)

      :type: float

   .. attribute:: thickness_outer

      Outer face thickness (in [0.001, 1], default 0.0)

      :type: float

   .. attribute:: use

      Enable this object as a collider for physics systems (default False)

      :type: bool

   .. attribute:: use_culling

      Cloth collision acts with respect to the collider normals (improves penetration recovery) (default False)

      :type: bool

   .. attribute:: use_normal

      Cloth collision impulses act in the direction of the collider normals (more reliable in some cases) (default False)

      :type: bool

   .. attribute:: use_particle_kill

      Kill collided particles (default False)

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

   - :class:`CollisionModifier.settings`
   - :class:`Object.collision`

