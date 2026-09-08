FluidDomainSettings(bpy_struct)
===============================

.. currentmodule:: bpy.types

base class --- :class:`bpy_struct`

.. class:: FluidDomainSettings(bpy_struct)

   Fluid domain settings

   .. attribute:: adapt_margin

      Margin added around fluid to minimize boundary interference (in [2, 24], default 4)

      :type: int

   .. attribute:: adapt_threshold

      Minimum amount of fluid grid values (smoke density, fuel and heat) a cell can contain, before it is considered empty (in [0, 1], default 0.002)

      :type: float

   .. attribute:: additional_res

      Maximum number of additional cells (in [0, 512], default 0)

      :type: int

   .. attribute:: alpha

      Buoyant force based on smoke density (higher value results in faster rising smoke) (in [-5, 5], default 1.0)

      :type: float

   .. attribute:: beta

      Buoyant force based on smoke heat (higher value results in faster rising smoke) (in [-5, 5], default 1.0)

      :type: float

   .. attribute:: burning_rate

      Speed of the burning reaction (higher value results in smaller flames) (in [0.01, 4], default 0.75)

      :type: float

   .. attribute:: cache_data_format

      Select the file format to be used for caching volumetric data (default ``'OPENVDB'``)

      - ``UNI``
        Uni Cache -- Uni file format (.uni).
      - ``OPENVDB``
        OpenVDB -- OpenVDB file format (.vdb).
      - ``RAW``
        Raw Cache -- Raw file format (.raw).

      :type: Literal['UNI', 'OPENVDB', 'RAW']

   .. attribute:: cache_directory

      Directory that contains fluid cache files (default "", never None, blend relative ``//`` prefix supported)

      :type: str

   .. attribute:: cache_frame_end

      Frame on which the simulation stops (last frame baked) (in [-1048574, 1048574], default 250)

      :type: int

   .. attribute:: cache_frame_offset

      Frame offset that is used when loading the simulation from the cache. It is not considered when baking the simulation, only when loading it. (in [-1048574, 1048574], default 0)

      :type: int

   .. attribute:: cache_frame_pause_data

      (in [-inf, inf], default 0)

      :type: int

   .. attribute:: cache_frame_pause_guide

      (in [-inf, inf], default 0)

      :type: int

   .. attribute:: cache_frame_pause_mesh

      (in [-inf, inf], default 0)

      :type: int

   .. attribute:: cache_frame_pause_noise

      (in [-inf, inf], default 0)

      :type: int

   .. attribute:: cache_frame_pause_particles

      (in [-inf, inf], default 0)

      :type: int

   .. attribute:: cache_frame_start

      Frame on which the simulation starts (first frame baked) (in [-1048574, 1048574], default 1)

      :type: int

   .. attribute:: cache_mesh_format

      Select the file format to be used for caching surface data (default ``'UNI'``)

      - ``UNI``
        Uni Cache -- Uni file format (.uni).
      - ``OPENVDB``
        OpenVDB -- OpenVDB file format (.vdb).
      - ``RAW``
        Raw Cache -- Raw file format (.raw).

      :type: Literal['UNI', 'OPENVDB', 'RAW']

   .. attribute:: cache_noise_format

      Select the file format to be used for caching noise data (default ``'OPENVDB'``)

      - ``UNI``
        Uni Cache -- Uni file format (.uni).
      - ``OPENVDB``
        OpenVDB -- OpenVDB file format (.vdb).
      - ``RAW``
        Raw Cache -- Raw file format (.raw).

      :type: Literal['UNI', 'OPENVDB', 'RAW']

   .. attribute:: cache_particle_format

      Select the file format to be used for caching particle data (default ``'OPENVDB'``)

      - ``UNI``
        Uni Cache -- Uni file format (.uni).
      - ``OPENVDB``
        OpenVDB -- OpenVDB file format (.vdb).
      - ``RAW``
        Raw Cache -- Raw file format (.raw).

      :type: Literal['UNI', 'OPENVDB', 'RAW']

   .. attribute:: cache_resumable

      Additional data will be saved so that the bake jobs can be resumed after pausing. Because more data will be written to disk it is recommended to avoid enabling this option when baking at high resolutions. (default False)

      :type: bool

   .. attribute:: cache_type

      Change the cache type of the simulation (default ``'REPLAY'``)

      - ``REPLAY``
        Replay -- Use the timeline to bake the scene.
      - ``MODULAR``
        Modular -- Bake every stage of the simulation separately.
      - ``ALL``
        All -- Bake all simulation settings at once.

      :type: Literal['REPLAY', 'MODULAR', 'ALL']

   .. data:: cell_size

      Cell Size (array of 3 items, in [-inf, inf], default (0.0, 0.0, 0.0), readonly)

      :type: :class:`mathutils.Vector`

   .. attribute:: cfl_condition

      Maximal velocity per cell (greater CFL numbers will minimize the number of simulation steps and the computation time.) (in [0, 10], default 2.0)

      :type: float

   .. attribute:: clipping

      Value under which voxels are considered empty space to optimize rendering (in [0, 1], default 1e-06)

      :type: float

   .. data:: color_ramp

      (readonly)

      :type: :class:`ColorRamp` | None

   .. attribute:: color_ramp_field

      Simulation field to color map (default ``'NONE'``)

      :type: Literal['NONE']

   .. attribute:: color_ramp_field_scale

      Multiplier for scaling the selected field to color map (in [0.001, 100000], default 1.0)

      :type: float

   .. attribute:: delete_in_obstacle

      Delete fluid inside obstacles (default False)

      :type: bool

   .. attribute:: display_interpolation

      Interpolation method to use for smoke/fire volumes in solid mode (default ``'LINEAR'``)

      - ``LINEAR``
        Linear -- Good smoothness and speed.
      - ``CUBIC``
        Cubic -- Smoothed high quality interpolation, but slower.
      - ``CLOSEST``
        Closest -- No interpolation.

      :type: Literal['LINEAR', 'CUBIC', 'CLOSEST']

   .. attribute:: display_thickness

      Thickness of smoke display in the viewport (in [0.001, 1000], default 1.0)

      :type: float

   .. attribute:: dissolve_speed

      Determine how quickly the smoke dissolves (lower value makes smoke disappear faster) (in [1, 10000], default 5)

      :type: int

   .. data:: domain_resolution

      Smoke Grid Resolution (array of 3 items, in [-inf, inf], default (0, 0, 0), readonly)

      :type: :class:`bpy_prop_array`\ [int]

   .. attribute:: domain_type

      Change domain type of the simulation (default ``'GAS'``)

      - ``GAS``
        Gas -- Create domain for gases.
      - ``LIQUID``
        Liquid -- Create domain for liquids.

      :type: Literal['GAS', 'LIQUID']

   .. attribute:: effector_group

      Limit effectors to this collection

      :type: :class:`Collection` | None

   .. data:: effector_weights

      (readonly)

      :type: :class:`EffectorWeights` | None

   .. attribute:: export_manta_script

      Generate and export Mantaflow script from current domain settings during bake. This is only needed if you plan to analyze the cache (e.g. view grids, velocity vectors, particles) in Mantaflow directly (outside of Blender) after baking the simulation. (default False)

      :type: bool

   .. attribute:: flame_ignition

      Minimum temperature of the flames (higher value results in faster rising flames) (in [0.5, 5], default 1.5)

      :type: float

   .. attribute:: flame_max_temp

      Maximum temperature of the flames (higher value results in faster rising flames) (in [1, 10], default 3.0)

      :type: float

   .. attribute:: flame_smoke

      Amount of smoke created by burning fuel (in [0, 8], default 1.0)

      :type: float

   .. attribute:: flame_smoke_color

      Color of smoke emitted from burning fuel (array of 3 items, in [0, inf], default (0.7, 0.7, 0.7))

      :type: :class:`mathutils.Color`

   .. attribute:: flame_vorticity

      Additional vorticity for the flames (in [0, 2], default 0.5)

      :type: float

   .. attribute:: flip_ratio

      PIC/FLIP Ratio. A value of 1.0 will result in a completely FLIP based simulation. Use a lower value for simulations which should produce smaller splashes. (in [0, 1], default 0.97)

      :type: float

   .. attribute:: fluid_group

      Limit fluid objects to this collection

      :type: :class:`Collection` | None

   .. attribute:: force_collection

      Limit forces to this collection

      :type: :class:`Collection` | None

   .. attribute:: fractions_distance

      Determines how far apart fluid and obstacle are (higher values will result in fluid being further away from obstacles, smaller values will let fluid move towards the inside of obstacles) (in [-5, 5], default 0.5)

      :type: float

   .. attribute:: fractions_threshold

      Determines how much fluid is allowed in an obstacle cell (higher values will tag a boundary cell as an obstacle easier and reduce the boundary smoothening effect) (in [0.001, 1], default 0.05)

      :type: float

   .. attribute:: gravity

      Gravity in X, Y and Z direction (array of 3 items, in [-1000.1, 1000.1], default (0.0, 0.0, -9.81))

      :type: :class:`mathutils.Vector`

   .. attribute:: gridlines_cell_filter

      Cell type to be highlighted (default ``'NONE'``)

      - ``NONE``
        None -- Highlight the cells regardless of their type.
      - ``FLUID``
        Fluid -- Highlight only the cells of type Fluid.
      - ``OBSTACLE``
        Obstacle -- Highlight only the cells of type Obstacle.
      - ``EMPTY``
        Empty -- Highlight only the cells of type Empty.
      - ``INFLOW``
        Inflow -- Highlight only the cells of type Inflow.
      - ``OUTFLOW``
        Outflow -- Highlight only the cells of type Outflow.

      :type: Literal['NONE', 'FLUID', 'OBSTACLE', 'EMPTY', 'INFLOW', 'OUTFLOW']

   .. attribute:: gridlines_color_field

      Simulation field to color map onto gridlines (default ``'NONE'``)

      - ``NONE``
        None -- None.
      - ``FLAGS``
        Flags -- Flag grid of the fluid domain.
      - ``RANGE``
        Highlight Range -- Highlight the voxels with values of the color mapped field within the range.

      :type: Literal['NONE', 'FLAGS', 'RANGE']

   .. attribute:: gridlines_lower_bound

      Lower bound of the highlighting range (in [-inf, inf], default 0.0)

      :type: float

   .. attribute:: gridlines_range_color

      Color used to highlight the range (array of 4 items, in [0, inf], default (1.0, 0.0, 0.0, 1.0))

      :type: :class:`bpy_prop_array`\ [float]

   .. attribute:: gridlines_upper_bound

      Upper bound of the highlighting range (in [-inf, inf], default 1.0)

      :type: float

   .. attribute:: guide_alpha

      Guiding weight (higher value results in greater lag) (in [1, 100], default 2.0)

      :type: float

   .. attribute:: guide_beta

      Guiding size (higher value results in larger vortices) (in [1, 50], default 5)

      :type: int

   .. attribute:: guide_parent

      Use velocities from this object for the guiding effect (object needs to have fluid modifier and be of type domain))

      :type: :class:`Object` | None

   .. attribute:: guide_source

      Choose where to get guiding velocities from (default ``'DOMAIN'``)

      - ``DOMAIN``
        Domain -- Use a fluid domain for guiding (domain needs to be baked already so that velocities can be extracted). Guiding domain can be of any type (i.e. gas or liquid)..
      - ``EFFECTOR``
        Effector -- Use guiding (effector) objects to create fluid guiding (guiding objects should be animated and baked once set up completely).

      :type: Literal['DOMAIN', 'EFFECTOR']

   .. attribute:: guide_vel_factor

      Guiding velocity factor (higher value results in greater guiding velocities) (in [0, 100], default 2.0)

      :type: float

   .. attribute:: has_cache_baked_any

      (default False)

      :type: bool

   .. attribute:: has_cache_baked_data

      (default False)

      :type: bool

   .. attribute:: has_cache_baked_guide

      (default False)

      :type: bool

   .. attribute:: has_cache_baked_mesh

      (default False)

      :type: bool

   .. attribute:: has_cache_baked_noise

      (default False)

      :type: bool

   .. attribute:: has_cache_baked_particles

      (default False)

      :type: bool

   .. attribute:: highres_sampling

      Method for sampling the high resolution flow (default ``'FULLSAMPLE'``)

      :type: Literal['FULLSAMPLE', 'LINEAR', 'NEAREST']

   .. attribute:: is_cache_baking_any

      (default False)

      :type: bool

   .. attribute:: is_cache_baking_data

      (default False)

      :type: bool

   .. attribute:: is_cache_baking_guide

      (default False)

      :type: bool

   .. attribute:: is_cache_baking_mesh

      (default False)

      :type: bool

   .. attribute:: is_cache_baking_noise

      (default False)

      :type: bool

   .. attribute:: is_cache_baking_particles

      (default False)

      :type: bool

   .. attribute:: mesh_concave_lower

      Lower mesh concavity bound (high values tend to smoothen and fill out concave regions) (in [0, 10], default 0.4)

      :type: float

   .. attribute:: mesh_concave_upper

      Upper mesh concavity bound (high values tend to smoothen and fill out concave regions) (in [0, 10], default 3.5)

      :type: float

   .. attribute:: mesh_generator

      Which particle level set generator to use (default ``'IMPROVED'``)

      - ``IMPROVED``
        Final -- Use improved particle level set (slower but more precise and with mesh smoothening options).
      - ``UNION``
        Preview -- Use union particle level set (faster but lower quality).

      :type: Literal['IMPROVED', 'UNION']

   .. attribute:: mesh_particle_radius

      Particle radius factor (higher value results in larger (meshed) particles). Needs to be adjusted after changing the mesh scale. (in [0, 10], default 2.0)

      :type: float

   .. attribute:: mesh_scale

      The mesh simulation is scaled up by this factor (compared to the base resolution of the domain). For best meshing, it is recommended to adjust the mesh particle radius alongside this value. (in [1, 100], default 2)

      :type: int

   .. attribute:: mesh_smoothen_neg

      Negative mesh smoothening (in [0, 100], default 1)

      :type: int

   .. attribute:: mesh_smoothen_pos

      Positive mesh smoothening (in [0, 100], default 1)

      :type: int

   .. attribute:: noise_pos_scale

      Scale of noise (higher value results in larger vortices) (in [0.0001, 10], default 2.0)

      :type: float

   .. attribute:: noise_scale

      The noise simulation is scaled up by this factor (compared to the base resolution of the domain) (in [1, 100], default 2)

      :type: int

   .. attribute:: noise_strength

      Strength of noise (in [0, 10], default 1.0)

      :type: float

   .. attribute:: noise_time_anim

      Animation time of noise (in [0.0001, 10], default 0.1)

      :type: float

   .. attribute:: openvdb_cache_compress_type

      Compression method to be used (default ``'ZIP'``)

      - ``ZIP``
        Zip -- Effective but slow compression.
      - ``NONE``
        None -- Do not use any compression.

      :type: Literal['ZIP', 'NONE']

   .. attribute:: openvdb_data_depth

      Bit depth for fluid particles and grids (lower bit values reduce file size) (default ``'NONE'``)

      :type: Literal['NONE']

   .. attribute:: particle_band_width

      Particle (narrow) band width (higher value results in thicker band and more particles) (in [0, 1000], default 3.0)

      :type: float

   .. attribute:: particle_max

      Maximum number of particles per cell (ensures that each cell has at most this amount of particles) (in [0, 1000], default 16)

      :type: int

   .. attribute:: particle_min

      Minimum number of particles per cell (ensures that each cell has at least this amount of particles) (in [0, 1000], default 8)

      :type: int

   .. attribute:: particle_number

      Particle number factor (higher value results in more particles) (in [1, 5], default 2)

      :type: int

   .. attribute:: particle_radius

      Particle radius factor. Increase this value if the simulation appears to leak volume, decrease it if the simulation seems to gain volume. (in [0, 10], default 1.0)

      :type: float

   .. attribute:: particle_randomness

      Randomness factor for particle sampling (in [0, 10], default 0.1)

      :type: float

   .. attribute:: particle_scale

      The particle simulation is scaled up by this factor (compared to the base resolution of the domain) (in [1, 100], default 1)

      :type: int

   .. attribute:: resolution_max

      Resolution used for the fluid domain. Value corresponds to the longest domain side (resolution for other domain sides is calculated automatically). (in [6, 10000], default 32)

      :type: int

   .. attribute:: show_gridlines

      Show gridlines (default False)

      :type: bool

   .. attribute:: show_velocity

      Visualize vector fields (default False)

      :type: bool

   .. attribute:: simulation_method

      Change the underlying simulation method (default ``'FLIP'``)

      - ``FLIP``
        FLIP -- Use FLIP as the simulation method (more splashy behavior).
      - ``APIC``
        APIC -- Use APIC as the simulation method (more energetic and stable behavior).

      :type: Literal['FLIP', 'APIC']

   .. attribute:: slice_axis

      (default ``'AUTO'``)

      - ``AUTO``
        Auto -- Adjust slice direction according to the view direction.
      - ``X``
        X -- Slice along the X axis.
      - ``Y``
        Y -- Slice along the Y axis.
      - ``Z``
        Z -- Slice along the Z axis.

      :type: Literal['AUTO', 'X', 'Y', 'Z']

   .. attribute:: slice_depth

      Position of the slice (in [0, 1], default 0.5)

      :type: float

   .. attribute:: slice_per_voxel

      How many slices per voxel should be generated (in [0, 100], default 5.0)

      :type: float

   .. attribute:: sndparticle_boundary

      How particles that left the domain are treated (default ``'DELETE'``)

      - ``DELETE``
        Delete -- Delete secondary particles that are inside obstacles or left the domain.
      - ``PUSHOUT``
        Push Out -- Push secondary particles that left the domain back into the domain.

      :type: Literal['DELETE', 'PUSHOUT']

   .. attribute:: sndparticle_bubble_buoyancy

      Amount of buoyancy force that rises bubbles (high value results in bubble movement mainly upwards) (in [0, 100], default 0.5)

      :type: float

   .. attribute:: sndparticle_bubble_drag

      Amount of drag force that moves bubbles along with the fluid (high value results in bubble movement mainly along with the fluid) (in [0, 100], default 0.6)

      :type: float

   .. attribute:: sndparticle_combined_export

      Determines which particle systems are created from secondary particles (default ``'OFF'``)

      - ``OFF``
        Off -- Create a separate particle system for every secondary particle type.
      - ``SPRAY_FOAM``
        Spray + Foam -- Spray and foam particles are saved in the same particle system.
      - ``SPRAY_BUBBLES``
        Spray + Bubbles -- Spray and bubble particles are saved in the same particle system.
      - ``FOAM_BUBBLES``
        Foam + Bubbles -- Foam and bubbles particles are saved in the same particle system.
      - ``SPRAY_FOAM_BUBBLES``
        Spray + Foam + Bubbles -- Create one particle system that contains all three secondary particle types.

      :type: Literal['OFF', 'SPRAY_FOAM', 'SPRAY_BUBBLES', 'FOAM_BUBBLES', 'SPRAY_FOAM_BUBBLES']

   .. attribute:: sndparticle_life_max

      Highest possible particle lifetime (in [0, 10000], default 25.0)

      :type: float

   .. attribute:: sndparticle_life_min

      Lowest possible particle lifetime (in [0, 10000], default 10.0)

      :type: float

   .. attribute:: sndparticle_potential_max_energy

      Upper clamping threshold that indicates the fluid speed where cells no longer emit more particles (higher value results in generally less particles) (in [0, 1000], default 5.0)

      :type: float

   .. attribute:: sndparticle_potential_max_trappedair

      Upper clamping threshold for marking fluid cells where air is trapped (higher value results in less marked cells) (in [0, 1000], default 20.0)

      :type: float

   .. attribute:: sndparticle_potential_max_wavecrest

      Upper clamping threshold for marking fluid cells as wave crests (higher value results in less marked cells) (in [0, 1000], default 8.0)

      :type: float

   .. attribute:: sndparticle_potential_min_energy

      Lower clamping threshold that indicates the fluid speed where cells start to emit particles (lower values result in generally more particles) (in [0, 1000], default 1.0)

      :type: float

   .. attribute:: sndparticle_potential_min_trappedair

      Lower clamping threshold for marking fluid cells where air is trapped (lower value results in more marked cells) (in [0, 1000], default 5.0)

      :type: float

   .. attribute:: sndparticle_potential_min_wavecrest

      Lower clamping threshold for marking fluid cells as wave crests (lower value results in more marked cells) (in [0, 1000], default 2.0)

      :type: float

   .. attribute:: sndparticle_potential_radius

      Radius to compute potential for each cell (higher values are slower but create smoother potential grids) (in [1, 4], default 2)

      :type: int

   .. attribute:: sndparticle_sampling_trappedair

      Maximum number of particles generated per trapped air cell per frame (in [0, 10000], default 40)

      :type: int

   .. attribute:: sndparticle_sampling_wavecrest

      Maximum number of particles generated per wave crest cell per frame (in [0, 10000], default 200)

      :type: int

   .. attribute:: sndparticle_update_radius

      Radius to compute position update for each particle (higher values are slower but particles move less chaotic) (in [1, 4], default 2)

      :type: int

   .. data:: start_point

      Start point (array of 3 items, in [-inf, inf], default (0.0, 0.0, 0.0), readonly)

      :type: :class:`mathutils.Vector`

   .. attribute:: surface_tension

      Surface tension of liquid (higher value results in greater hydrophobic behavior) (in [0, 100], default 0.0)

      :type: float

   .. attribute:: sys_particle_maximum

      Maximum number of fluid particles that are allowed in this simulation (in [0, inf], default 0)

      :type: int

   .. attribute:: time_scale

      Adjust simulation speed (in [0.0001, 10], default 1.0)

      :type: float

   .. attribute:: timesteps_max

      Maximum number of simulation steps to perform for one frame (in [1, 100], default 4)

      :type: int

   .. attribute:: timesteps_min

      Minimum number of simulation steps to perform for one frame (in [1, 100], default 1)

      :type: int

   .. attribute:: use_adaptive_domain

      Adapt simulation resolution and size to fluid (default False)

      :type: bool

   .. attribute:: use_adaptive_timesteps

      Automatically decide when to perform multiple simulation steps per frame (default True)

      :type: bool

   .. attribute:: use_bubble_particles

      Create bubble particle system (default False)

      :type: bool

   .. attribute:: use_collision_border_back

      Enable collisions with back domain border (default False)

      :type: bool

   .. attribute:: use_collision_border_bottom

      Enable collisions with bottom domain border (default False)

      :type: bool

   .. attribute:: use_collision_border_front

      Enable collisions with front domain border (default False)

      :type: bool

   .. attribute:: use_collision_border_left

      Enable collisions with left domain border (default False)

      :type: bool

   .. attribute:: use_collision_border_right

      Enable collisions with right domain border (default False)

      :type: bool

   .. attribute:: use_collision_border_top

      Enable collisions with top domain border (default False)

      :type: bool

   .. attribute:: use_color_ramp

      Render a simulation field while mapping its voxels values to the colors of a ramp or using a predefined color code (default False)

      :type: bool

   .. attribute:: use_diffusion

      Enable fluid diffusion settings (e.g. viscosity, surface tension) (default False)

      :type: bool

   .. attribute:: use_dissolve_smoke

      Let smoke disappear over time (default False)

      :type: bool

   .. attribute:: use_dissolve_smoke_log

      Dissolve smoke in a logarithmic fashion. Dissolves quickly at first, but lingers longer. (default True)

      :type: bool

   .. attribute:: use_flip_particles

      Create liquid particle system (default False)

      :type: bool

   .. attribute:: use_foam_particles

      Create foam particle system (default False)

      :type: bool

   .. attribute:: use_fractions

      Fractional obstacles improve and smoothen the fluid-obstacle boundary (default False)

      :type: bool

   .. attribute:: use_guide

      Enable fluid guiding (default False)

      :type: bool

   .. attribute:: use_mesh

      Enable fluid mesh (using amplification) (default True)

      :type: bool

   .. attribute:: use_noise

      Enable fluid noise (using amplification) (default False)

      :type: bool

   .. attribute:: use_slice

      Perform a single slice of the domain object (default False)

      :type: bool

   .. attribute:: use_speed_vectors

      Caches velocities of mesh vertices. These will be used (automatically) when rendering with motion blur enabled. (default False)

      :type: bool

   .. attribute:: use_spray_particles

      Create spray particle system (default False)

      :type: bool

   .. attribute:: use_tracer_particles

      Create tracer particle system (default False)

      :type: bool

   .. attribute:: use_viscosity

      Simulate fluids with high viscosity using a special solver (default False)

      :type: bool

   .. attribute:: vector_display_type

      (default ``'NEEDLE'``)

      - ``NEEDLE``
        Needle -- Display vectors as needles.
      - ``STREAMLINE``
        Streamlines -- Display vectors as streamlines.
      - ``MAC``
        MAC Grid -- Display vector field as MAC grid.

      :type: Literal['NEEDLE', 'STREAMLINE', 'MAC']

   .. attribute:: vector_field

      Vector field to be represented by the display vectors (default ``'FLUID_VELOCITY'``)

      - ``FLUID_VELOCITY``
        Fluid Velocity -- Velocity field of the fluid domain.
      - ``GUIDE_VELOCITY``
        Guide Velocity -- Guide velocity field of the fluid domain.
      - ``FORCE``
        Force -- Force field of the fluid domain.

      :type: Literal['FLUID_VELOCITY', 'GUIDE_VELOCITY', 'FORCE']

   .. attribute:: vector_scale

      Multiplier for scaling the vectors (in [0, 1000], default 1.0)

      :type: float

   .. attribute:: vector_scale_with_magnitude

      Scale vectors with their magnitudes (default False)

      :type: bool

   .. attribute:: vector_show_mac_x

      Show X-component of MAC Grid (default True)

      :type: bool

   .. attribute:: vector_show_mac_y

      Show Y-component of MAC Grid (default True)

      :type: bool

   .. attribute:: vector_show_mac_z

      Show Z-component of MAC Grid (default True)

      :type: bool

   .. attribute:: velocity_scale

      Factor to control the amount of motion blur (in [0, inf], default 1.0)

      :type: float

   .. attribute:: viscosity_base

      Viscosity setting: value that is multiplied by 10 to the power of (exponent*-1) (in [0, 10], default 1.0)

      :type: float

   .. attribute:: viscosity_exponent

      Negative exponent for the viscosity value (to simplify entering small values e.g. 5*10^-6) (in [0, 10], default 6)

      :type: int

   .. attribute:: viscosity_value

      Viscosity of liquid (higher values result in more viscous fluids, a value of 0 will still apply some viscosity) (in [0, 10], default 0.05)

      :type: float

   .. attribute:: vorticity

      Amount of turbulence and rotation in smoke (in [0, 4], default 0.0)

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

   - :class:`FluidModifier.domain_settings`

