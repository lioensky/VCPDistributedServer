
********
Settings
********

.. reference::

   :Panel:     :menuselection:`Physics --> Fluid --> Settings`
   :Type:      Domain

The domain object contains the entire simulation. Fluid simulations cannot leave the domain,
it will either collide with the edge or disappear, depending on the domain's settings.

Keep in mind that large domains need higher resolutions and longer bake times.
You will want to make it just large enough that the simulation will fit inside it,
but not so large that it takes too long to compute the simulation.

To create a domain, add a cube and transform it until it encloses the area where you want
the simulation to take place. Translation, rotation, and scaling are all allowed.
To turn it into a fluid domain, click *Fluid* in the :menuselection:`Properties --> Physics` tab,
then select *Domain* as the fluid *Type*.

.. note::

   You *can* use other shapes of mesh objects as domain objects,
   but the fluid simulator will use the shape's :term:`Bounding Box` as the domain bounds.
   In other words, the actual shape of the domain will still be rectangular.

.. _bpy.types.FluidDomainSettings.domain_type:

Domain Type
   A fluid domain can control either liquid or gas flows. Liquid domains take all liquid flow objects
   that intersect with the domain into consideration. Gas domains consider all
   intersecting *Smoke*, *Fire*, and *Smoke & Fire* flow objects. It is not possible to change
   the domain type dynamically.

.. _bpy.types.FluidDomainSettings.resolution_max:

Resolution Divisions
   The fluid domain is subdivided into many "cells" called :term:`Voxels <Voxel>`
   which make up "pixels" of fluid. This setting controls the number of subdivisions in the domain.
   Higher numbers of subdivisions are one way of creating higher resolution fluids.

   Since the resolution is defined in terms of "subdivisions",
   larger domains will need more divisions to get an equivalent resolution to a small domain.
   For example, a one meter cube with 64 *Resolution Divisions* will need 128 divisions to match a 2 meter cube.
   The dimension used as the base division is the longest dimension of the objects bounding box.
   To help visualize the voxel size, the *Resolution Divisions* can be previewed with a small cube
   shown in the 3D Viewport, to show the size of these divisions.

.. _bpy.types.FluidDomainSettings.time_scale:

Time Scale
   Controls the speed of the simulation. Low values result in a "slow motion" simulation,
   while higher values can be used to advance the simulation faster
   (good for generating fluids to be used in still renders).

.. _bpy.types.FluidDomainSettings.use_adaptive_timesteps:

Adaptive Time Steps
   Lets the solver automatically decide when to perform multiple simulation steps per frame.
   It takes into account the maximum and minimum number of time steps,
   the current *Frame Rate*, and the *Time Scale*.

.. _bpy.types.FluidDomainSettings.cfl_condition:

CFL Number
   Determines the maximum velocity per grid cell and is measured in grid cells per time step.
   Fluid is only allowed to move up to this velocity in one time step. If this threshold is
   exceeded the solver will subdivide the simulation step.

   In general, greater CFL
   (`Courant–Friedrichs–Lewy <https://en.wikipedia.org/wiki/Courant%E2%80%93Friedrichs%E2%80%93Lewy_condition>`__)
   numbers will minimize the number of simulation steps and the computation time.
   Yet it will yield less physically accurate behavior for fast fluid flows.
   Smaller CFL numbers result in more simulation steps per frame, longer simulation times
   but more accurate behavior at high velocities (e.g. fast fluid flow colliding
   with obstacle).

.. note::

   When lowering the *CFL* number it is recommended to increase the maximum number of time steps.
   Similarly, when increasing the *CFL* number the minimum number of time steps should be adjusted.

.. _bpy.types.FluidDomainSettings.timesteps_max:

Timesteps Maximum
   Maximum number of allowed time steps per frame. If needed, the solver will divide
   a simulation step up to this number of sub-steps.

.. _bpy.types.FluidDomainSettings.timesteps_min:

Timesteps Minimum
   Minimum number of allowed time steps per frame. The solver will always perform at least
   this number of simulation steps per frame.

.. _bpy.types.FluidDomainSettings.gravity:

Gravity
   By default the fluid solver will use the global scene gravity. This behavior can be disabled
   in the scene settings. Disabling the global gravity will enable the fluid gravity options.

.. _bpy.types.FluidDomainSettings.clipping:

Empty Space :guilabel:`Gas Only`
   Voxels with values under this value are considered empty space.
   More empty space optimizes rendering. With OpenVDB caching it also reduces cache sizes.

.. _bpy.types.FluidDomainSettings.delete_in_obstacle:

Delete in Obstacle
   Remover any volume of fluid that intersects with an obstacle inside the domain.


.. _bpy.types.FluidDomainSettings.use_collision_border_front:
.. _bpy.types.FluidDomainSettings.use_collision_border_back:
.. _bpy.types.FluidDomainSettings.use_collision_border_right:
.. _bpy.types.FluidDomainSettings.use_collision_border_left:
.. _bpy.types.FluidDomainSettings.use_collision_border_top:
.. _bpy.types.FluidDomainSettings.use_collision_border_bottom:

Border Collisions
=================

.. reference::

   :Panel:     :menuselection:`Physics --> Fluid --> Settings --> Border Collisions`
   :Type:      Domain (Gas)

Controls which sides of the domain will allow fluid "pass through" the domain, making it disappear
without influencing the rest of the simulation, and which sides will deflect fluids.


Gas
===

.. reference::

   :Panel:     :menuselection:`Physics --> Fluid --> Gas`
   :Type:      Domain (Gas)

.. _bpy.types.FluidDomainSettings.alpha:

Buoyancy Density
   Buoyant force based on gas density.

   - Values above 0 will cause the gas to rise (simulating gas which is lighter than ambient air).
   - Values below 0 will cause gas to sink (simulating gas which is heavier than ambient air).

.. _bpy.types.FluidDomainSettings.beta:

Buoyancy Heat
   Controls how much gas is affected by temperature.
   The effect this setting has on gas depends on the per flow object
   :ref:`Initial Temperature <bpy.types.FluidFlowSettings.temperature>`:

   - Values above 0 will result in the gas rising when the flow object *Initial Temperature* is
     set to a positive value, and gas sinking when the flow object *Initial Temperature* is
     set to a negative value.
   - Values below 0 will result in the opposite of positive values,
     i.e. gas emitted from flow objects with a positive *Initial Temperature* will sink,
     and gas from flow objects with a negative *Initial Temperature* will rise.

   Note that gas from multiple flow objects with different temperatures will mix and warm up or
   cool down until an equilibrium is reached.

.. _bpy.types.FluidDomainSettings.vorticity:

Vorticity
   Controls the amount of turbulence in the gas. Higher values will make lots of small swirls,
   while lower values make smoother shapes.

   .. list-table:: Comparison of different amounts of vorticity.

      * - .. figure:: /images/physics_fluid_type_domain_settings_vorticity-off.png

             Domain with a vorticity of 0.0.

        - .. figure:: /images/physics_fluid_type_domain_settings_vorticity-on.png

             Domain with a vorticity of 0.2.


.. _bpy.types.FluidDomainSettings.use_dissolve_smoke:

Dissolve
--------

Allow gas to dissipate over time.

.. _bpy.types.FluidDomainSettings.dissolve_speed:

Time
   Speed of gas dissipation in frames.

.. _bpy.types.FluidDomainSettings.use_dissolve_smoke_log:

Slow
   Dissolve gas in a logarithmic fashion. Dissolves quickly at first, but lingers longer.


Fire
====

.. reference::

   :Type:      Domain
   :Panel:     :menuselection:`Physics --> Fluid --> Gas --> Fire`

.. _bpy.types.FluidDomainSettings.burning_rate:

Reaction Speed
   How fast fuel burns. Larger values result in smaller flames (fuel burns before it can go very far),
   smaller values result in larger flames (fuel has time to flow farther before being fully consumed).

.. _bpy.types.FluidDomainSettings.flame_smoke:

Flame Smoke
   Amount of extra smoke created automatically to simulate burnt fuel. This smoke is best visible
   when using a "Fire + Smoke" :ref:`Flow Object <bpy.types.FluidFlowSettings.flow_type>`.

.. _bpy.types.FluidDomainSettings.flame_vorticity:

Vorticity
   Vorticity for flames in addition to the global fluid
   :ref:`Vorticity <bpy.types.FluidDomainSettings.vorticity>`.

.. _bpy.types.FluidDomainSettings.flame_max_temp:

Temperature Maximum
   Maximum temperature of flames. Larger values result in faster rising flames.

.. _bpy.types.FluidDomainSettings.flame_ignition:

Minimum
   Minimum temperature of flames. Larger values result in faster rising flames.

.. _bpy.types.FluidDomainSettings.flame_smoke_color:

Smoke Color
   Color of smoke emitted from burning fuel.


.. _bpy.types.FluidDomainSettings.use_flip_particles:

Liquid
======

.. reference::

   :Type:      Domain
   :Panel:     :menuselection:`Physics --> Fluid --> Liquid`

Liquid settings control the behavior of the particles which the simulation consists of.
Enabling the liquid checkbox will automatically create a particle system for the simulation.
This particle system visualizes the flow of the simulation. Visualizing the liquid particles is optional.
The fluid simulation will make use of all the fields without an attached particle system too.

.. note::

   Disabling the liquid checkbox will delete the attached particle system and its settings.

.. _bpy.types.FluidDomainSettings.simulation_method:

Simulation Method
   Determines the liquid particle simulation method.

   :FLIP:
      (FLuid Implicit Particle)
      Produces a very splashy simulation with lots of particles dispersed in the air.
   :APIC:
      (Affine Particle-In-Cell)
      Produces a very energetic but also more stable simulation.
      Vortices within the liquid will be preserved better than with *FLIP*.

.. _bpy.types.FluidDomainSettings.flip_ratio:

FLIP Ratio :guilabel:`Simulation FLIP Only`:
   How much FLIP velocity to use when updating liquid particle velocities. A value of 1.0
   will result in a completely FLIP based simulation. Completely FLIP based simulations
   produce more chaotic splashes and are preferable when simulating greater quantities of liquid.
   When using smaller values the behavior will be less turbulent and splashes are more subtle.
   This is optimal when simulating scenes where the liquid is supposed to be on a small scale.

.. _bpy.types.FluidDomainSettings.sys_particle_maximum:

System Maximum
   Maximum number of fluid particles that are allowed in the simulation. If this field is set to a nonzero value
   the simulation will never contain more than this number of fluid particles. Otherwise, with a value of zero
   the solver will always sample new particles when needed.

.. _bpy.types.FluidDomainSettings.particle_radius:

Particle Radius
   The radius of one liquid particle in grid cells units. This value describes how much area is covered
   by a particle and thus determines how much area around it can be considered as liquid.
   A greater radius will let particles cover more area. This will result in more grids cell being tagged
   as liquid instead of just being empty.

   Whenever the simulation appears to leak or gain volume in an undesired, non physically accurate way it is
   a good idea to adjust this value. That is, when liquid seems to disappear this value needs to be increased.
   The inverse applies when too much liquid is being produced.

.. _bpy.types.FluidDomainSettings.particle_number:

Sampling
   Factor that is used when sampling particles. A higher value will sample more particles.
   Note that particle resampling occurs at every single simulation step.

.. _bpy.types.FluidDomainSettings.particle_randomness:

Randomness
   New particles are sampled with some randomness attached to their position
   which can be controlled by this field. Higher values will sample the liquid particles more
   randomly in inflow regions. With a value of 0.0 all new particles will be sampled uniformly inside
   their corresponding grid cells.

   When trying to create a laminar inflow (with little randomness) or more turbulent flows
   (with greater randomness) this value can be useful.

.. _bpy.types.FluidDomainSettings.particle_max:

Particles Maximum
   The maximum number of liquid particles per grid cell. During a simulation the number of liquid
   particles in a cell can fluctuate: Particles can flow into other cells or can get deleted
   if they move outside the narrow band. Resampling will add new particles considering this maximum.

   This value sets the upper threshold of particles per cell. It is also a good way to estimate how
   many particles there can be in your simulation (one needs to take grid resolution into account too).
   This can be useful before baking and when planning a simulation.

.. _bpy.types.FluidDomainSettings.particle_min:

Minimum
   The minimum number of liquid particles per grid cell. Similarly to the maximum particle threshold,
   this value ensures that there are at least a certain amount of particles per cell.

.. _bpy.types.FluidDomainSettings.particle_band_width:

Narrow Band Width
   Controls the width in grid cell units of the narrow band that liquid particles are allowed to flow in.
   A high value will result in a thicker band and can result in an inflow region completely filled
   with particles. Unless the goal of the simulation is to visualize the liquid particles it is
   recommended to not increase the band width significantly as more particles slow down the simulation.

   In some situations increasing this value can help create volume when the simulation appears to leak.
   In all other cases it is best to keep the narrow band as thin as possible since the liquid surface
   contains most details and simulating particles inside the liquid is not an optimal use of computing resources.

.. seealso::

   The narrow band is an implementation of `Narrow Band FLIP for Liquid Simulations
   <https://www.cs.cit.tum.de/cg/research/publications/2016/narrow-band-flip-for-liquid-simulations/>`__.

.. _bpy.types.FluidDomainSettings.use_fractions:

Fractional Obstacles
   Enables finer resolution in fluid / obstacle regions (second order obstacles).
   This option reduces the "stepping effect" that results when an obstacle lies inclined inside the domain.
   It also makes liquid flow more smoothly over an obstacle.

   .. _bpy.types.FluidDomainSettings.fractions_distance:

   Obstacle Distance
      Determines how far apart fluid and obstacles are. This value can be used to achieve a more fluid motion over
      inclined obstacles: Depending on the slope of the obstacle increasing this value can help liquid particles
      flow better over an obstacle.
      Setting this field to a negative value will let fluid move towards the inside of an obstacle.

   .. _bpy.types.FluidDomainSettings.fractions_threshold:

   Obstacle Threshold
      Value to control the smoothness of the fractional obstacle option. Smaller value reduce
      the "stepping effect" but may result particles sticking to the obstacle.

.. _bpy.ops.fluid.bake_data:
.. _bpy.ops.fluid.free_data:

Bake Data, Free Data
   This option is only available when using the :ref:`Modular <bpy.types.FluidDomainSettings.cache_type>` cache type.
   *Bake Data* simulates and stores the base of the fluid simulation on drive.
   Both gas and liquid simulations can add refinements on top of this
   (e.g. gas simulations can add noise, liquid simulations can add a mesh or secondary particles or both).

   The progress will be displayed in the status bar. Pressing :kbd:`Esc` will pause the simulation.

   Once the simulation has been baked, the cache can be deleted by pressing *Free Data*.
   It is possible to pause or resume a *Bake All* process.
