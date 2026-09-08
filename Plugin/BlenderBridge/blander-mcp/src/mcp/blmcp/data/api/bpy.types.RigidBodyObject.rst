RigidBodyObject(bpy_struct)
===========================

.. currentmodule:: bpy.types

base class --- :class:`bpy_struct`

.. class:: RigidBodyObject(bpy_struct)

   Settings for object participating in Rigid Body Simulation

   .. attribute:: angular_damping

      Amount of angular velocity that is lost over time (in [0, 1], default 0.1)

      :type: float

   .. attribute:: collision_collections

      Collision collections rigid body belongs to (array of 20 items, default (False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False))

      :type: :class:`bpy_prop_array`\ [bool]

   .. attribute:: collision_margin

      Threshold of distance near surface where collisions are still considered (best results when non-zero) (in [0, 1], default 0.04)

      :type: float

   .. attribute:: collision_shape

      Collision Shape of object in Rigid Body Simulations (default ``'BOX'``)

      :type: Literal[:ref:`rna_enum_rigidbody_object_shape_items`]

   .. attribute:: deactivate_angular_velocity

      Angular Velocity below which simulation stops simulating object (in [0, inf], default 0.5)

      :type: float

   .. attribute:: deactivate_linear_velocity

      Linear Velocity below which simulation stops simulating object (in [0, inf], default 0.4)

      :type: float

   .. attribute:: enabled

      Rigid Body actively participates to the simulation (default True)

      :type: bool

   .. attribute:: friction

      Resistance of object to movement (in [0, inf], default 0.5)

      :type: float

   .. attribute:: kinematic

      Allow rigid body to be controlled by the animation system (default False)

      :type: bool

   .. attribute:: linear_damping

      Amount of linear velocity that is lost over time (in [0, 1], default 0.04)

      :type: float

   .. attribute:: mass

      How much the object 'weighs' irrespective of gravity (in [0.001, inf], default 1.0)

      :type: float

   .. attribute:: mesh_source

      Source of the mesh used to create collision shape (default ``'BASE'``)

      - ``BASE``
        Base -- Base mesh.
      - ``DEFORM``
        Deform -- Deformations (shape keys, deform modifiers).
      - ``FINAL``
        Final -- All modifiers.

      :type: Literal['BASE', 'DEFORM', 'FINAL']

   .. attribute:: restitution

      Tendency of object to bounce after colliding with another (0 = stays still, 1 = perfectly elastic) (in [0, inf], default 0.0)

      :type: float

   .. attribute:: type

      Role of object in Rigid Body Simulations (default ``'ACTIVE'``)

      :type: Literal[:ref:`rna_enum_rigidbody_object_type_items`]

   .. attribute:: use_deactivation

      Enable deactivation of resting rigid bodies (increases performance and stability but can cause glitches) (default True)

      :type: bool

   .. attribute:: use_deform

      Rigid body deforms during simulation (default False)

      :type: bool

   .. attribute:: use_margin

      Use custom collision margin (some shapes will have a visible gap around them) (default False)

      :type: bool

   .. attribute:: use_start_deactivated

      Deactivate rigid body at the start of the simulation (default False)

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

   - :class:`Object.rigid_body`

