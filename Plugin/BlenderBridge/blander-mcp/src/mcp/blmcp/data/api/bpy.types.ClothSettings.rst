ClothSettings(bpy_struct)
=========================

.. currentmodule:: bpy.types

base class --- :class:`bpy_struct`

.. class:: ClothSettings(bpy_struct)

   Cloth simulation settings for an object

   .. attribute:: air_damping

      Air has normally some thickness which slows falling things down (in [0, 10], default 1.0)

      :type: float

   .. attribute:: bending_damping

      Amount of damping in bending behavior (in [0, 1000], default 0.5)

      :type: float

   .. attribute:: bending_model

      Physical model for simulating bending forces (default ``'ANGULAR'``)

      - ``ANGULAR``
        Angular -- Cloth model with angular bending springs.
      - ``LINEAR``
        Linear -- Cloth model with linear bending springs (legacy).

      :type: Literal['ANGULAR', 'LINEAR']

   .. attribute:: bending_stiffness

      How much the material resists bending (in [0, 10000], default 0.5)

      :type: float

   .. attribute:: bending_stiffness_max

      Maximum bending stiffness value (in [0, 10000], default 0.5)

      :type: float

   .. attribute:: collider_friction

      (in [0, 1], default 0.0)

      :type: float

   .. attribute:: compression_damping

      Amount of damping in compression behavior (in [0, 50], default 5.0)

      :type: float

   .. attribute:: compression_stiffness

      How much the material resists compression (in [0, 10000], default 15.0)

      :type: float

   .. attribute:: compression_stiffness_max

      Maximum compression stiffness value (in [0, 10000], default 15.0)

      :type: float

   .. attribute:: density_strength

      Influence of target density on the simulation (in [0, 1], default 0.0)

      :type: float

   .. attribute:: density_target

      Maximum density of hair (in [0, 10000], default 0.0)

      :type: float

   .. data:: effector_weights

      (readonly)

      :type: :class:`EffectorWeights` | None

   .. attribute:: fluid_density

      Density (kg/l) of the fluid contained inside the object, used to create a hydrostatic pressure gradient simulating the weight of the internal fluid, or buoyancy from the surrounding fluid if negative (in [-inf, inf], default 0.0)

      :type: float

   .. attribute:: goal_default

      Default Goal (vertex target position) value, when no Vertex Group used (in [0, 1], default 0.0)

      :type: float

   .. attribute:: goal_friction

      Goal (vertex target position) friction (in [0, 50], default 0.0)

      :type: float

   .. attribute:: goal_max

      Goal maximum, vertex group weights are scaled to match this range (in [0, 1], default 1.0)

      :type: float

   .. attribute:: goal_min

      Goal minimum, vertex group weights are scaled to match this range (in [0, 1], default 0.0)

      :type: float

   .. attribute:: goal_spring

      Goal (vertex target position) spring stiffness (in [0, 0.999], default 1.0)

      :type: float

   .. attribute:: gravity

      Gravity or external force vector (array of 3 items, in [-100, 100], default (0.0, 0.0, -9.81))

      :type: :class:`mathutils.Vector`

   .. attribute:: internal_compression_stiffness

      How much the material resists compression (in [0, 10000], default 15.0)

      :type: float

   .. attribute:: internal_compression_stiffness_max

      Maximum compression stiffness value (in [0, 10000], default 15.0)

      :type: float

   .. attribute:: internal_friction

      (in [0, 1], default 0.0)

      :type: float

   .. attribute:: internal_spring_max_diversion

      How much the rays used to connect the internal points can diverge from the vertex normal (in [0, 0.785398], default 0.785398)

      :type: float

   .. attribute:: internal_spring_max_length

      The maximum length an internal spring can have during creation. If the distance between internal points is greater than this, no internal spring will be created between these points. A length of zero means that there is no length limit. (in [0, 1000], default 0.0)

      :type: float

   .. attribute:: internal_spring_normal_check

      Require the points the internal springs connect to have opposite normal directions (default True)

      :type: bool

   .. attribute:: internal_tension_stiffness

      How much the material resists stretching (in [0, 10000], default 15.0)

      :type: float

   .. attribute:: internal_tension_stiffness_max

      Maximum tension stiffness value (in [0, 10000], default 15.0)

      :type: float

   .. attribute:: mass

      The mass of each vertex on the cloth material (in [0, inf], default 0.3)

      :type: float

   .. attribute:: pin_stiffness

      Pin (vertex target position) spring stiffness (in [0, 50], default 1.0)

      :type: float

   .. attribute:: pressure_factor

      Ambient pressure (kPa) that balances out between the inside and outside of the object when it has the target volume (in [0, 10000], default 1.0)

      :type: float

   .. attribute:: quality

      Quality of the simulation in steps per frame (higher is better quality but slower) (in [1, inf], default 5)

      :type: int

   .. attribute:: rest_shape_key

      Shape key to use the rest spring lengths from

      :type: :class:`ShapeKey` | None

   .. attribute:: sewing_force_max

      Maximum sewing force (in [0, 10000], default 0.0)

      :type: float

   .. attribute:: shear_damping

      Amount of damping in shearing behavior (in [0, 50], default 5.0)

      :type: float

   .. attribute:: shear_stiffness

      How much the material resists shearing (in [0, 10000], default 5.0)

      :type: float

   .. attribute:: shear_stiffness_max

      Maximum shear scaling value (in [0, 10000], default 5.0)

      :type: float

   .. attribute:: shrink_max

      Max amount to shrink cloth by (in [-inf, 1], default 0.0)

      :type: float

   .. attribute:: shrink_min

      Factor by which to shrink cloth (in [-inf, 1], default 0.0)

      :type: float

   .. attribute:: target_volume

      The mesh volume where the inner/outer pressure will be the same. If set to zero the change in volume will not affect pressure. (in [0, 10000], default 0.0)

      :type: float

   .. attribute:: tension_damping

      Amount of damping in stretching behavior (in [0, 50], default 5.0)

      :type: float

   .. attribute:: tension_stiffness

      How much the material resists stretching (in [0, 10000], default 15.0)

      :type: float

   .. attribute:: tension_stiffness_max

      Maximum tension stiffness value (in [0, 10000], default 15.0)

      :type: float

   .. attribute:: time_scale

      Cloth speed is multiplied by this value (in [0, inf], default 1.0)

      :type: float

   .. attribute:: uniform_pressure_force

      The uniform pressure that is constantly applied to the mesh, in units of Pressure Scale. Can be negative. (in [-10000, 10000], default 0.0)

      :type: float

   .. attribute:: use_dynamic_mesh

      Make simulation respect deformations in the base mesh (default False)

      :type: bool

   .. attribute:: use_internal_springs

      Simulate an internal volume structure by creating springs connecting the opposite sides of the mesh (default False)

      :type: bool

   .. attribute:: use_pressure

      Simulate pressure inside a closed cloth mesh (default False)

      :type: bool

   .. attribute:: use_pressure_volume

      Use the Target Volume parameter as the initial volume, instead of calculating it from the mesh itself (default False)

      :type: bool

   .. attribute:: use_sewing_springs

      Pulls loose edges together (default False)

      :type: bool

   .. attribute:: vertex_group_bending

      Vertex group for fine control over bending stiffness (default "", never None)

      :type: str

   .. attribute:: vertex_group_intern

      Vertex group for fine control over the internal spring stiffness (default "", never None)

      :type: str

   .. attribute:: vertex_group_mass

      Vertex Group for pinning of vertices (default "", never None)

      :type: str

   .. attribute:: vertex_group_pressure

      Vertex Group for where to apply pressure. Zero weight means no pressure while a weight of one means full pressure. Faces with a vertex that has zero weight will be excluded from the volume calculation. (default "", never None)

      :type: str

   .. attribute:: vertex_group_shear_stiffness

      Vertex group for fine control over shear stiffness (default "", never None)

      :type: str

   .. attribute:: vertex_group_shrink

      Vertex Group for shrinking cloth (default "", never None)

      :type: str

   .. attribute:: vertex_group_structural_stiffness

      Vertex group for fine control over structural stiffness (default "", never None)

      :type: str

   .. attribute:: voxel_cell_size

      Size of the voxel grid cells for interaction effects (in [0.0001, 10000], default 0.1)

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

   - :class:`ClothModifier.settings`

