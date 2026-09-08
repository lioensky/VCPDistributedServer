Itasc(IKParam)
==============

.. currentmodule:: bpy.types

base classes --- :class:`bpy_struct`, :class:`IKParam`

.. class:: Itasc(IKParam)

   Parameters for the iTaSC IK solver

   .. attribute:: damping_epsilon

      Singular value under which damping is progressively applied (higher values produce results with more stability, less reactivity) (in [0, 1], default 0.0)

      :type: float

   .. attribute:: damping_max

      Maximum damping coefficient when singular value is nearly 0 (higher values produce results with more stability, less reactivity) (in [0, 1], default 0.0)

      :type: float

   .. attribute:: feedback

      Feedback coefficient for error correction, average response time is 1/feedback (in [0, 100], default 0.0)

      :type: float

   .. attribute:: iterations

      Maximum number of iterations for convergence in case of reiteration (in [0, 1000], default 0)

      :type: int

   .. attribute:: mode

      (default ``'ANIMATION'``)

      - ``ANIMATION``
        Animation -- Stateless solver computing pose starting from current action and non-IK constraints.
      - ``SIMULATION``
        Simulation -- State-full solver running in real-time context and ignoring actions and non-IK constraints.

      :type: Literal['ANIMATION', 'SIMULATION']

   .. attribute:: precision

      Precision of convergence in case of reiteration (in [0, 0.1], default 0.0)

      :type: float

   .. attribute:: reiteration_method

      Defines if the solver is allowed to reiterate (converge until precision is met) on none, first or all frames (default ``'NEVER'``)

      - ``NEVER``
        Never -- The solver does not reiterate, not even on first frame (starts from rest pose).
      - ``INITIAL``
        Initial -- The solver reiterates (converges) on the first frame but not on subsequent frame.
      - ``ALWAYS``
        Always -- The solver reiterates (converges) on all frames.

      :type: Literal['NEVER', 'INITIAL', 'ALWAYS']

   .. attribute:: solver

      Solving method selection: automatic damping or manual damping (default ``'SDLS'``)

      - ``SDLS``
        SDLS -- Selective Damped Least Square.
      - ``DLS``
        DLS -- Damped Least Square with Numerical Filtering.

      :type: Literal['SDLS', 'DLS']

   .. attribute:: step_count

      Divide the frame interval into this many steps (in [1, 50], default 0)

      :type: int

   .. attribute:: step_max

      Higher bound for timestep in second in case of automatic substeps (in [0, 1], default 0.0)

      :type: float

   .. attribute:: step_min

      Lower bound for timestep in second in case of automatic substeps (in [0, 0.1], default 0.0)

      :type: float

   .. attribute:: translate_root_bones

      Translate root (i.e. parentless) bones to the armature origin (default False)

      :type: bool

   .. attribute:: use_auto_step

      Automatically determine the optimal number of steps for best performance/accuracy trade off (default False)

      :type: bool

   .. attribute:: velocity_max

      Maximum joint velocity in radians/second (in [0, 100], default 0.0)

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
   - :class:`IKParam.ik_solver`

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
   - :class:`IKParam.bl_rna_get_subclass`
   - :class:`IKParam.bl_rna_get_subclass_py`

