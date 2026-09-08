SoftBodySettings(bpy_struct)
============================

.. currentmodule:: bpy.types

base class --- :class:`bpy_struct`

.. class:: SoftBodySettings(bpy_struct)

   Soft body simulation settings for an object

   .. attribute:: aero

      Make edges 'sail' (in [0, 30000], default 0)

      :type: int

   .. attribute:: aerodynamics_type

      Method of calculating aerodynamic interaction (default ``'SIMPLE'``)

      - ``SIMPLE``
        Simple -- Edges receive a drag force from surrounding media.
      - ``LIFT_FORCE``
        Lift Force -- Edges receive a lift force when passing through surrounding media.

      :type: Literal['SIMPLE', 'LIFT_FORCE']

   .. attribute:: ball_damp

      Blending to inelastic collision (in [0.001, 1], default 0.0)

      :type: float

   .. attribute:: ball_size

      Absolute ball size or factor if not manually adjusted (in [-10, 10], default 0.0)

      :type: float

   .. attribute:: ball_stiff

      Ball inflating pressure (in [0.001, 100], default 0.0)

      :type: float

   .. attribute:: bend

      Bending Stiffness (in [0, 10], default 0.0)

      :type: float

   .. attribute:: choke

      'Viscosity' inside collision target (in [0, 100], default 0)

      :type: int

   .. attribute:: collision_collection

      Limit colliders to this collection

      :type: :class:`Collection` | None

   .. attribute:: collision_type

      Choose Collision Type (default ``'MANUAL'``)

      - ``MANUAL``
        Manual -- Manual adjust.
      - ``AVERAGE``
        Average -- Average Spring length \* Ball Size.
      - ``MINIMAL``
        Minimal -- Minimal Spring length \* Ball Size.
      - ``MAXIMAL``
        Maximal -- Maximal Spring length \* Ball Size.
      - ``MINMAX``
        AvMinMax -- (Min+Max)/2 \* Ball Size.

      :type: Literal['MANUAL', 'AVERAGE', 'MINIMAL', 'MAXIMAL', 'MINMAX']

   .. attribute:: damping

      Edge spring friction (in [0, 50], default 0.0)

      :type: float

   .. data:: effector_weights

      (readonly)

      :type: :class:`EffectorWeights` | None

   .. attribute:: error_threshold

      The Runge-Kutta ODE solver error limit, low value gives more precision, high values speed (in [0.001, 10], default 0.0)

      :type: float

   .. attribute:: friction

      General media friction for point movements (in [0, 50], default 0.0)

      :type: float

   .. attribute:: fuzzy

      Fuzziness while on collision, high values make collision handling faster but less stable (in [1, 100], default 0)

      :type: int

   .. attribute:: goal_default

      Default Goal (vertex target position) value (in [0, 1], default 0.0)

      :type: float

   .. attribute:: goal_friction

      Goal (vertex target position) friction (in [0, 50], default 0.0)

      :type: float

   .. attribute:: goal_max

      Goal maximum, vertex weights are scaled to match this range (in [0, 1], default 0.0)

      :type: float

   .. attribute:: goal_min

      Goal minimum, vertex weights are scaled to match this range (in [0, 1], default 0.0)

      :type: float

   .. attribute:: goal_spring

      Goal (vertex target position) spring stiffness (in [0, 0.999], default 0.0)

      :type: float

   .. attribute:: gravity

      Apply gravitation to point movement (in [-10, 10], default 0.0)

      :type: float

   .. attribute:: location_mass_center

      Location of center of mass (array of 3 items, in [-inf, inf], default (0.0, 0.0, 0.0))

      :type: :class:`mathutils.Vector`

   .. attribute:: mass

      General Mass value (in [0, 50000], default 0.0)

      :type: float

   .. attribute:: plastic

      Permanent deform (in [0, 100], default 0)

      :type: int

   .. attribute:: pull

      Edge spring stiffness when longer than rest length (in [0, 0.999], default 0.0)

      :type: float

   .. attribute:: push

      Edge spring stiffness when shorter than rest length (in [0, 0.999], default 0.0)

      :type: float

   .. attribute:: rotation_estimate

      Estimated rotation matrix (multi-dimensional array of 3 * 3 items, in [-inf, inf], default ((0.0, 0.0, 0.0), (0.0, 0.0, 0.0), (0.0, 0.0, 0.0)))

      :type: :class:`mathutils.Matrix`

   .. attribute:: scale_estimate

      Estimated scale matrix (multi-dimensional array of 3 * 3 items, in [-inf, inf], default ((0.0, 0.0, 0.0), (0.0, 0.0, 0.0), (0.0, 0.0, 0.0)))

      :type: :class:`mathutils.Matrix`

   .. attribute:: shear

      Shear Stiffness (in [0, 1], default 0.0)

      :type: float

   .. attribute:: speed

      Tweak timing for physics to control frequency and speed (in [0.01, 100], default 0.0)

      :type: float

   .. attribute:: spring_length

      Alter spring length to shrink/blow up (unit %) 0 to disable (in [0, 200], default 0)

      :type: int

   .. attribute:: step_max

      Maximal # solver steps/frame (in [0, 30000], default 0)

      :type: int

   .. attribute:: step_min

      Minimal # solver steps/frame (in [0, 30000], default 0)

      :type: int

   .. attribute:: use_auto_step

      Use velocities for automagic step sizes (default False)

      :type: bool

   .. attribute:: use_diagnose

      Turn on SB diagnose console prints (default False)

      :type: bool

   .. attribute:: use_edge_collision

      Edges collide too (default False)

      :type: bool

   .. attribute:: use_edges

      Use Edges as springs (default False)

      :type: bool

   .. attribute:: use_estimate_matrix

      Store the estimated transforms in the soft body settings (default False)

      :type: bool

   .. attribute:: use_face_collision

      Faces collide too, can be very slow (default False)

      :type: bool

   .. attribute:: use_goal

      Define forces for vertices to stick to animated position (default False)

      :type: bool

   .. attribute:: use_self_collision

      Enable naive vertex ball self collision (default False)

      :type: bool

   .. attribute:: use_stiff_quads

      Add diagonal springs on 4-gons (default False)

      :type: bool

   .. attribute:: vertex_group_goal

      Control point weight values (default "", never None)

      :type: str

   .. attribute:: vertex_group_mass

      Control point mass values (default "", never None)

      :type: str

   .. attribute:: vertex_group_spring

      Control point spring strength values (default "", never None)

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

   - :class:`Object.soft_body`
   - :class:`SoftBodyModifier.settings`

