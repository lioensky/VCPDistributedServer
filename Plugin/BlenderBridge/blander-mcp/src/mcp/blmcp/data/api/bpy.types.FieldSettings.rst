FieldSettings(bpy_struct)
=========================

.. currentmodule:: bpy.types

base class --- :class:`bpy_struct`

.. class:: FieldSettings(bpy_struct)

   Field settings for an object in physics simulation

   .. attribute:: apply_to_location

      Affect particle's location (default False)

      :type: bool

   .. attribute:: apply_to_rotation

      Affect particle's dynamic rotation (default False)

      :type: bool

   .. attribute:: distance_max

      Maximum distance for the field to work (in [0, inf], default 0.0)

      :type: float

   .. attribute:: distance_min

      Minimum distance for the field's falloff (in [0, 1000], default 0.0)

      :type: float

   .. attribute:: falloff_power

      How quickly strength falls off with distance from the force field (in [0, 10], default 0.0)

      :type: float

   .. attribute:: falloff_type

      (default ``'SPHERE'``)

      :type: Literal['CONE', 'SPHERE', 'TUBE']

   .. attribute:: flow

      Convert effector force into air flow velocity (in [-inf, inf], default 0.0)

      :type: float

   .. attribute:: guide_clump_amount

      Amount of clumping (in [-1, 1], default 0.0)

      :type: float

   .. attribute:: guide_clump_shape

      Shape of clumping (in [-0.999, 0.999], default 0.0)

      :type: float

   .. attribute:: guide_free

      Guide-free time from particle life's end (in [0, 0.99], default 0.0)

      :type: float

   .. attribute:: guide_kink_amplitude

      The amplitude of the offset (in [0, 10], default 0.0)

      :type: float

   .. attribute:: guide_kink_axis

      Which axis to use for offset (default ``'X'``)

      :type: Literal[:ref:`rna_enum_axis_xyz_items`]

   .. attribute:: guide_kink_frequency

      The frequency of the offset (1/total length) (in [0, 10], default 0.0)

      :type: float

   .. attribute:: guide_kink_shape

      Adjust the offset to the beginning/end (in [-0.999, 0.999], default 0.0)

      :type: float

   .. attribute:: guide_kink_type

      Type of periodic offset on the curve (default ``'NONE'``)

      :type: Literal['NONE', 'BRAID', 'CURL', 'RADIAL', 'ROLL', 'ROTATION', 'WAVE']

   .. attribute:: guide_minimum

      The distance from which particles are affected fully (in [-inf, inf], default 0.0)

      :type: float

   .. attribute:: harmonic_damping

      Damping of the harmonic force (in [-inf, inf], default 0.0)

      :type: float

   .. attribute:: inflow

      Inwards component of the vortex force (in [-inf, inf], default 0.0)

      :type: float

   .. attribute:: linear_drag

      Drag component proportional to velocity (in [-inf, inf], default 0.0)

      :type: float

   .. attribute:: noise

      Amount of noise for the force strength (in [0, 10], default 0.0)

      :type: float

   .. attribute:: quadratic_drag

      Drag component proportional to the square of velocity (in [-inf, inf], default 0.0)

      :type: float

   .. attribute:: radial_falloff

      Radial falloff power (real gravitational falloff = 2) (in [0, 10], default 0.0)

      :type: float

   .. attribute:: radial_max

      Maximum radial distance for the field to work (in [0, 1000], default 0.0)

      :type: float

   .. attribute:: radial_min

      Minimum radial distance for the field's falloff (in [0, 1000], default 0.0)

      :type: float

   .. attribute:: rest_length

      Rest length of the harmonic force (in [0, inf], default 0.0)

      :type: float

   .. attribute:: seed

      Seed of the noise (in [1, 128], default 0)

      :type: int

   .. attribute:: shape

      Which direction is used to calculate the effector force (default ``'POINT'``)

      - ``POINT``
        Point -- Field originates from the object center.
      - ``LINE``
        Line -- Field originates from the local Z axis of the object.
      - ``PLANE``
        Plane -- Field originates from the local XY plane of the object.
      - ``SURFACE``
        Surface -- Field originates from the surface of the object.
      - ``POINTS``
        Every Point -- Field originates from all of the vertices of the object.

      :type: Literal['POINT', 'LINE', 'PLANE', 'SURFACE', 'POINTS']

   .. attribute:: size

      Size of the turbulence (in [0, inf], default 0.0)

      :type: float

   .. attribute:: source_object

      Select domain object of the smoke simulation

      :type: :class:`Object` | None

   .. attribute:: strength

      Strength of force field (in [-inf, inf], default 0.0)

      :type: float

   .. attribute:: texture

      Texture to use as force

      :type: :class:`Texture` | None

   .. attribute:: texture_mode

      How the texture effect is calculated (RGB and Curl need a RGB texture, else Gradient will be used instead) (default ``'RGB'``)

      :type: Literal['CURL', 'GRADIENT', 'RGB']

   .. attribute:: texture_nabla

      Defines size of derivative offset used for calculating gradient and curl (in [0.0001, 1], default 0.0)

      :type: float

   .. attribute:: type

      Type of field (default ``'NONE'``)

      - ``NONE``
        None.
      - ``BOID``
        Boid -- Create a force that acts as a boid's predators or target.
      - ``CHARGE``
        Charge -- Spherical forcefield based on the charge of particles, only influences other charge force fields.
      - ``GUIDE``
        Curve Guide -- Create a force along a curve object.
      - ``DRAG``
        Drag -- Create a force that dampens motion.
      - ``FLUID_FLOW``
        Fluid Flow -- Create a force based on fluid simulation velocities.
      - ``FORCE``
        Force -- Radial field toward the center of object.
      - ``HARMONIC``
        Harmonic -- The source of this force field is the zero point of a harmonic oscillator.
      - ``LENNARDJ``
        Lennard-Jones -- Forcefield based on the Lennard-Jones potential.
      - ``MAGNET``
        Magnetic -- Forcefield depends on the speed of the particles.
      - ``TEXTURE``
        Texture -- Force field based on a texture.
      - ``TURBULENCE``
        Turbulence -- Create turbulence with a noise field.
      - ``VORTEX``
        Vortex -- Spiraling force that twists the force object's local Z axis.
      - ``WIND``
        Wind -- Constant force along the force object's local Z axis.

      :type: Literal['NONE', 'BOID', 'CHARGE', 'GUIDE', 'DRAG', 'FLUID_FLOW', 'FORCE', 'HARMONIC', 'LENNARDJ', 'MAGNET', 'TEXTURE', 'TURBULENCE', 'VORTEX', 'WIND']

   .. attribute:: use_2d_force

      Apply force only in 2D (default False)

      :type: bool

   .. attribute:: use_absorption

      Force gets absorbed by collision objects (default False)

      :type: bool

   .. attribute:: use_global_coords

      Use effector/global coordinates for turbulence (default False)

      :type: bool

   .. attribute:: use_gravity_falloff

      Multiply force by 1/distance² (default False)

      :type: bool

   .. attribute:: use_guide_path_add

      Based on distance/falloff it adds a portion of the entire path (default False)

      :type: bool

   .. attribute:: use_guide_path_weight

      Use curve weights to influence the particle influence along the curve (default False)

      :type: bool

   .. attribute:: use_max_distance

      Use a maximum distance for the field to work (default False)

      :type: bool

   .. attribute:: use_min_distance

      Use a minimum distance for the field's falloff (default False)

      :type: bool

   .. attribute:: use_multiple_springs

      Every point is affected by multiple springs (default False)

      :type: bool

   .. attribute:: use_object_coords

      Use object/global coordinates for texture (default False)

      :type: bool

   .. attribute:: use_radial_max

      Use a maximum radial distance for the field to work (default False)

      :type: bool

   .. attribute:: use_radial_min

      Use a minimum radial distance for the field's falloff (default False)

      :type: bool

   .. attribute:: use_root_coords

      Texture coordinates from root particle locations (default False)

      :type: bool

   .. attribute:: use_smoke_density

      Adjust force strength based on smoke density (default False)

      :type: bool

   .. attribute:: wind_factor

      How much the force is reduced when acting parallel to a surface, e.g. cloth (in [0, 1], default 0.0)

      :type: float

   .. attribute:: z_direction

      Effect in full or only positive/negative Z direction (default ``'BOTH'``)

      :type: Literal['POSITIVE', 'NEGATIVE', 'BOTH']

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

   - :class:`Object.field`
   - :class:`ParticleSettings.force_field_1`
   - :class:`ParticleSettings.force_field_2`

