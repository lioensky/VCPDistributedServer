SPHFluidSettings(bpy_struct)
============================

.. currentmodule:: bpy.types

base class --- :class:`bpy_struct`

.. class:: SPHFluidSettings(bpy_struct)

   Settings for particle fluids physics

   .. attribute:: buoyancy

      Artificial buoyancy force in negative gravity direction based on pressure differences inside the fluid (in [0, 10], default 0.0)

      :type: float

   .. attribute:: fluid_radius

      Fluid interaction radius (in [0, 20], default 0.0)

      :type: float

   .. attribute:: linear_viscosity

      Linear viscosity (in [0, 100], default 0.0)

      :type: float

   .. attribute:: plasticity

      How much the spring rest length can change after the elastic limit is crossed (in [0, 100], default 0.0)

      :type: float

   .. attribute:: repulsion

      How strongly the fluid tries to keep from clustering (factor of stiffness) (in [0, 100], default 0.0)

      :type: float

   .. attribute:: rest_density

      Fluid rest density (in [0, 10000], default 0.0)

      :type: float

   .. attribute:: rest_length

      Spring rest length (factor of particle radius) (in [0, 2], default 0.0)

      :type: float

   .. attribute:: solver

      The code used to calculate internal forces on particles (default ``'DDR'``)

      - ``DDR``
        Double-Density -- An artistic solver with strong surface tension effects (original).
      - ``CLASSICAL``
        Classical -- A more physically-accurate solver.

      :type: Literal['DDR', 'CLASSICAL']

   .. attribute:: spring_force

      Spring force (in [0, 100], default 0.0)

      :type: float

   .. attribute:: spring_frames

      Create springs for this number of frames since particles birth (0 is always) (in [0, 100], default 0)

      :type: int

   .. attribute:: stiff_viscosity

      Creates viscosity for expanding fluid (in [0, 100], default 0.0)

      :type: float

   .. attribute:: stiffness

      How incompressible the fluid is (speed of sound) (in [0, 1000], default 0.0)

      :type: float

   .. attribute:: use_factor_density

      Density is calculated as a factor of default density (depends on particle size) (default False)

      :type: bool

   .. attribute:: use_factor_radius

      Interaction radius is a factor of 4 * particle size (default False)

      :type: bool

   .. attribute:: use_factor_repulsion

      Repulsion is a factor of stiffness (default False)

      :type: bool

   .. attribute:: use_factor_rest_length

      Spring rest length is a factor of 2 * particle size (default False)

      :type: bool

   .. attribute:: use_factor_stiff_viscosity

      Stiff viscosity is a factor of normal viscosity (default False)

      :type: bool

   .. attribute:: use_initial_rest_length

      Use the initial length as spring rest length instead of 2 * particle size (default False)

      :type: bool

   .. attribute:: use_viscoelastic_springs

      Use viscoelastic springs instead of Hooke's springs (default False)

      :type: bool

   .. attribute:: yield_ratio

      How much the spring has to be stretched/compressed in order to change its rest length (in [0, 1], default 0.0)

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

   - :class:`ParticleSettings.fluid`

