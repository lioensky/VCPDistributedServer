
****
Flow
****

Fluid *Flow* types are used to add or remove fluid to a domain object. Flow objects should be
contained within the domain's :term:`Bounding Box` in order to work.

To define any mesh object as a *Flow* object, add Fluid physics by clicking *Fluid* in
:menuselection:`Properties --> Physics`. Then select *Flow* as the fluid *Type*. Now you should have
a default fluid flow source object.


.. _bpy.types.FluidFlowSettings:

Settings
========

.. reference::

   :Panel:     :menuselection:`Physics --> Fluid --> Settings`
   :Type:      Flow

.. _bpy.types.FluidFlowSettings.flow_type:

Flow Type
   :Smoke: Emit only smoke.
   :Fire + Smoke: Emit both fire and smoke.
   :Fire:
      Emit only fire.
      Note that the domain will automatically create some smoke to simulate smoke left by burnt fuel.
   :Liquid: Emit liquid.

.. _bpy.types.FluidFlowSettings.flow_behavior:

Flow Behavior
   Controls if the Flow object either adds (*Inflow*), removes (*Outflow*),
   or turns the mesh itself into fluid (*Geometry*).

   :Inflow:
      This object will emit fluid into the simulation, like a water tap or base of a fire.
   :Outflow:
      Any fluid that enters the :term:`Bounding Box` of this object will be removed from
      the domain (think of a drain or a black hole). This can be useful in combination with
      an inflow to prevent the whole domain from filling up. Outflow objects can be animated
      and the area where the fluid disappears will follow the object as it moves around.
   :Geometry:
      All regions of this object that are inside the domain bounding box will be used as
      actual fluid in the simulation. You can place more than one fluid object inside the domain.
      Also make sure that the surface normals are pointing outwards or else they will not simulate
      properly. In contrast to domain objects, the actual mesh geometry is used for fluid objects.

.. _bpy.types.FluidFlowSettings.use_inflow:

Use Flow :guilabel:`Inflow` :guilabel:`Outflow`
   Enables or disables the flow of fluid, this property is useful for animations to selectively enable and
   disable when fluid is being added to or removed from the domain.

.. _bpy.types.FluidFlowSettings.subframes:

Sampling Substeps
   Number of sub-steps used to reduce gaps in emission of fluid from fast-moving sources.

   .. list-table:: Comparison of smoke inflow quickly rising upwards at different sub-step rates.

      * - .. figure:: /images/physics_fluid_type_flow_substep-off.png

             Sampling sub-steps: 0.

        - .. figure:: /images/physics_fluid_type_flow_substep-on.png

             Sampling sub-steps: 3.

   .. note::

      Sub-Steps occur at every simulation step and not per frame.
      The simulation step count is controlled by the adaptive time stepping.

.. _bpy.types.FluidFlowSettings.smoke_color:

Smoke Color
   The color of emitted smoke. When smoke of different colors are mixed they will blend together,
   eventually settling into a new combined color.

.. _bpy.types.FluidFlowSettings.use_absolute:

Absolute Density
   If this checkbox is enabled, the emitter will only produce more smoke or fire if there is space for
   it in the emitter region. Otherwise smoke or fire will always be produced and add up.

.. _bpy.types.FluidFlowSettings.temperature:

Initial Temperature
   Difference between the temperature of emitted smoke and the domain's ambient temperature.
   This setting's effect on smoke depends on the domain's :ref:`Heat Buoyancy <bpy.types.FluidDomainSettings.beta>`.

.. _bpy.types.FluidFlowSettings.density:

Density
   Amount of smoke to emit at once. Larger values result in more density being produced.

.. _bpy.types.FluidFlowSettings.fuel_amount:

Fuel
   Amount of "fuel" being burned per second. Larger values result in larger flames,
   smaller values result in smaller flames:

   .. list-table:: Comparison of flames with varying fuel rates.

      * - .. figure:: /images/physics_fluid_type_flow_fuelrate-0-5.png

             Fuel: 0.5.

        - .. figure:: /images/physics_fluid_type_flow_fuelrate-1-0.png

             Fuel: 1.0.

.. _bpy.types.FluidFlowSettings.density_vertex_group:

Vertex Group
   When set, use the specified :doc:`Vertex Group </modeling/meshes/properties/vertex_groups/vertex_groups>`
   to control where smoke is emitted.


.. _bpy.types.FluidFlowSettings.use_particle_size:

Flow Source
-----------

.. _bpy.types.FluidFlowSettings.flow_source:

Flow Source
   This setting defines the method used to emit fluid.

   :Mesh: Emit fluid directly from the object's mesh.

      .. _bpy.types.FluidFlowSettings.use_plane_init:

      Is Planar
         Defines the effector as either a single dimension object i.e. a plane or the mesh is :term:`Non-manifold`.
         This ensures that the fluid simulator will give the most accurate results for these types of meshes.

      .. _bpy.types.FluidFlowSettings.surface_distance:

      Surface Emission
         Maximum distance in :term:`Voxels <Voxel>` from the surface of the mesh in which fluid is emitted.
         Since this setting uses voxels to determine the distance,
         results will vary depending on the domain's resolution.

      .. _bpy.types.FluidFlowSettings.volume_density:

      Volume Emission :guilabel:`Fire or Smoke Only`:
         Amount of fluid to emit inside the emitter mesh, where 0 is none and 1 is the full amount.
         Note that emitting fluid based on volume can have unpredictable results
         if your mesh is :term:`Non-manifold`.

   :Particle System:
      :guilabel:`Fire or Smoke Only`:
      Create smoke or fire from a particle system on the flow object.

      .. _bpy.types.FluidFlowSettings.particle_system:

      The particle system can be selected with a :ref:`ui-data-id`.

      Note that only *Emitter* type particle systems can add smoke.
      See :doc:`Particles </physics/particles/introduction>` for information on
      how to create a particle system.

      Set Size
         When this setting is enabled, it allows the *Size* setting to define the maximum distance in voxels
         at which particles can emit smoke, similar to the *Surface Emission* setting for mesh sources.

         When disabled, particles will fill the nearest :term:`Voxel` with smoke.


.. _bpy.types.FluidFlowSettings.use_initial_velocity:

Initial Velocity
----------------

When enabled, the fluid will inherit the momentum of the flow source.

.. _bpy.types.FluidFlowSettings.velocity_factor:

Source
   Factor for the inherited velocity. A value of 1 will emit fluid moving at the same speed as the source.

.. _bpy.types.FluidFlowSettings.velocity_normal:

Normal
   This option controls how much velocity fluid is given along a face :term:`Normal`.
   Note that, initial velocities will always be applied along all face normals.
   Thus with a closed flow source mesh, fluid will always be emitted in more than one direction.
   To set initial velocities along only one direction all normals need to point in the same direction.
   This is can be achieved when using a plane as the flow object.

.. _bpy.types.FluidFlowSettings.velocity_coord:

Initial X, Y, Z
   Initial velocity along X, Y, Z coordinates in world space.
   This can be used in addition to the initial velocity along
   the :ref:`Normal <bpy.types.FluidFlowSettings.velocity_normal>`.


.. _bpy.types.FluidFlowSettings.use_texture:

Texture
-------

.. reference::

   :Type:      Flow
   :Panel:     :menuselection:`Physics --> Fluid --> Settings --> Texture`

When enabled, use the specified texture and settings to control where on
the mesh smoke or fire can be emitted from. These settings have no effect on *Outflow Flow Behavior*.

.. _bpy.types.FluidFlowSettings.noise_texture:

Texture
   A :ref:`ui-data-id` selector to choose the :doc:`Texture </render/materials/legacy_textures/index>`.

.. _bpy.types.FluidFlowSettings.texture_map_type:

Mapping
   Controls whether to use :ref:`Generated UVs <properties-texture-space>` or manual UV mapping.

.. _bpy.types.FluidFlowSettings.texture_size:

Size
   Overall texture scale.

.. _bpy.types.FluidFlowSettings.texture_offset:

Offset
   Translates the texture along the Z axis.
